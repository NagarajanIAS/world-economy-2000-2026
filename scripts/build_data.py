"""Turn data/raw/* into tidy data/clean/*.json and loadable data/js/**/*.js.

Every output series carries its provenance:
  {id, source, code, label, unit, freq, vintage, retrieved, url, notes,
   last_actual (WEO only), data: {area: [[period, value], ...]}}

Pages load series on demand with WE.load(["weo/NGDP_RPCH", "fred/WALCL"]).
Run: .venv/bin/python scripts/build_data.py
"""
import csv, io, json, re, statistics, sys, zipfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW, CLEAN, JS = ROOT / "data/raw", ROOT / "data/clean", ROOT / "data/js"
sys.path.insert(0, str(Path(__file__).parent))
import registry as R

LOG = {}
with (RAW / "fetch_log.csv").open() as fh:
    for row in csv.DictReader(fh):
        LOG[(row["source"], row["id"])] = row  # last write wins


def prov(source, sid):
    r = LOG.get((source, sid), {})
    return {"url": r.get("url", ""), "retrieved": r.get("retrieved_utc", "")[:10]}


def num(x):
    try:
        v = float(x)
        return None if v != v else v
    except (TypeError, ValueError):
        return None


def rnd(v, nd=3):
    return None if v is None else round(v, nd)


def write(folder, sid, obj):
    (CLEAN / folder).mkdir(parents=True, exist_ok=True)
    (JS / folder).mkdir(parents=True, exist_ok=True)
    s = json.dumps(obj, separators=(",", ":"), ensure_ascii=False)
    (CLEAN / folder / f"{sid}.json").write_text(s)
    (JS / folder / f"{sid}.js").write_text(f"WE.register({json.dumps(folder + '/' + sid)},{s});\n")


# ---------------------------------------------------------------- WEO
def weo_names():
    t = (RAW / "imf_weo/_structure.xml").read_text()
    out = {}
    for cl in ("CL_WEO_COUNTRY", "CL_WEO_INDICATOR"):
        b = re.search(rf'<str:Codelist [^>]*id="{cl}"(.*?)</str:Codelist>', t, re.S).group(1)
        out[cl] = {i: n for i, n in re.findall(
            r'<str:Code id="([^"]+)"[^>]*>.*?<com:Name xml:lang="en">([^<]+)</com:Name>', b, re.S)}
    return out


UNITS = {"PT": "%", "PT_GDP": "% of GDP", "USD": "US$", "IX": "index", "USD_BBL": "US$ per barrel",
         "USD_MMBTU": "US$ per MMBtu", "PS": "persons", "XDC": "national currency"}
SCALE_WORD = {"0": "", "3": "thousand", "6": "million", "9": "billion", "12": "trillion"}


def build_weo():
    names = weo_names()
    countries = names["CL_WEO_COUNTRY"]
    used = {}
    for ind in R.WEO_INDICATORS:
        f = RAW / "imf_weo" / f"{ind}.csv"
        if not f.exists():
            continue
        rows = list(csv.DictReader(f.open()))
        data, last = defaultdict(list), {}
        unit, scale, pub, sname = "", "0", "", ""
        for r in rows:
            v = num(r["OBS_VALUE"])
            if v is None:
                continue
            c = r["COUNTRY"]
            sc = int(r["SCALE"] or 0)
            data[c].append([int(r["TIME_PERIOD"]), rnd(v / 10 ** sc if sc else v)])  # values arrive in units; SCALE gives display unit
            if r.get("LATEST_ACTUAL_ANNUAL_DATA"):
                m = re.search(r"\d{2,4}", r["LATEST_ACTUAL_ANNUAL_DATA"])  # e.g. "2025" or "FY25"
                if m:
                    y = int(m.group()); last[c] = y + 2000 if y < 100 else y
            unit, scale, pub, sname = r["UNIT"], r["SCALE"], r["PUBLICATION_DATE"][:10], r["SERIES_NAME"]
            used[c] = countries.get(c, c)
        for c in data:
            data[c].sort()
        u = UNITS.get(unit, unit)
        if SCALE_WORD.get(scale):
            u = f"{u} {SCALE_WORD[scale]}".strip()
        write("weo", ind, {
            "id": f"weo/{ind}", "source": "IMF, World Economic Outlook database, October 2026",
            "code": f"IMF.RES,WEO {ind}", "label": sname or names["CL_WEO_INDICATOR"].get(ind, ind),
            "unit": u, "freq": "A", "vintage": f"WEO Oct 2026 (published {pub})",
            **prov("imf_weo", ind),
            # Aggregates carry no latest-actual flag; Oct 2026 WEO treats 2025 as the last full year of data.
            "last_actual": last, "last_actual_default": 2025,
            "notes": "Years after last_actual are IMF staff estimates or projections.",
            "data": dict(data)})
    # Vintages (for forecast-revision charts)
    for v in R.WEO_VINTAGES:
        for ind in R.WEO_VINTAGE_INDICATORS:
            f = RAW / "imf_weo_vintage" / f"{v}__{ind}.csv"
            if not f.exists():
                continue
            data = defaultdict(list)
            for r in csv.DictReader(f.open()):
                val = num(r["OBS_VALUE"])
                if val is not None:
                    data[r["COUNTRY"]].append([int(r["TIME_PERIOD"]), rnd(val)])
            for c in data:
                data[c].sort()
            write("weo_vintage", f"{v}__{ind}", {
                "id": f"weo_vintage/{v}__{ind}", "source": f"IMF, World Economic Outlook database, {v.replace('_VINTAGE','').replace('WEO_','').replace('_',' ')} vintage",
                "code": f"IMF.RES,{v} {ind}", "label": names["CL_WEO_INDICATOR"].get(ind, ind), "unit": "%",
                "freq": "A", "vintage": v, **prov("imf_weo_vintage", f"{v}__{ind}"), "data": dict(data)})
    (CLEAN / "weo").mkdir(parents=True, exist_ok=True)
    meta = {"countries": dict(sorted(used.items()))}
    write("meta", "weo_countries", meta)


# ---------------------------------------------------------------- WDI
def build_wdi():
    cj = json.loads((RAW / "wdi/_countries.json").read_text())[1]
    info = {c["id"]: {"name": c["name"], "region": c["region"]["value"], "income": c["incomeLevel"]["value"],
                      "aggregate": c["region"]["value"] == "Aggregates", "iso2": c["iso2Code"]} for c in cj}
    write("meta", "wdi_countries", info)
    for ind in R.WDI_INDICATORS:
        f = RAW / "wdi" / f"{ind}.json"
        if not f.exists():
            continue
        js = json.loads(f.read_text())
        data, label = defaultdict(list), ind
        for r in js[1] or []:
            v = num(r["value"])
            label = r["indicator"]["value"]
            if v is None or not r["countryiso3code"]:
                continue
            data[r["countryiso3code"]].append([int(r["date"]), rnd(v, 4)])
        for c in data:
            data[c].sort()
        unit = "%" if "%" in label else ("current US$" if "current US$" in label else ("constant 2015 US$" if "constant 2015 US$" in label else ""))
        write("wdi", ind, {"id": f"wdi/{ind}", "source": "World Bank, World Development Indicators",
                           "code": f"WDI {ind}", "label": label, "unit": unit, "freq": "A",
                           "vintage": f"WDI, last updated {js[0].get('lastupdated','')}",
                           **prov("wdi", ind), "data": dict(data)})


# ---------------------------------------------------------------- FRED
def to_monthly(points):
    """points: [(YYYY-MM-DD, v)] daily/weekly -> monthly averages [(YYYY-MM, v)]."""
    b = defaultdict(list)
    for d, v in points:
        b[d[:7]].append(v)
    return [[k, rnd(statistics.fmean(vs), 4)] for k, vs in sorted(b.items())]


def build_fred():
    for s in R.FRED_SERIES:
        f = RAW / "fred" / f"{s}.csv"
        if not f.exists():
            continue
        rows = list(csv.reader(f.open()))[1:]
        pts = [(d, num(v)) for d, v in rows if num(v) is not None]
        meta = json.loads((RAW / "fred" / f"{s}__meta.json").read_text())
        dates = [d for d, _ in pts]
        gaps = sorted({(int(b[:4]) - int(a[:4])) * 12 + int(b[5:7]) - int(a[5:7]) for a, b in zip(dates[-60:], dates[-59:])}) if len(dates) > 60 else [1]
        if gaps and gaps[0] == 0:          # daily or weekly -> monthly average
            data, freq, note = to_monthly(pts), "M", "Monthly average of daily or weekly observations (computed)."
        elif gaps and gaps[0] == 3:
            data, freq, note = [[d[:7], rnd(v, 4)] for d, v in pts], "Q", "Quarterly; period shown as first month of quarter."
        else:
            data, freq, note = [[d[:7], rnd(v, 4)] for d, v in pts], "M", ""
        title = re.sub(r"\s*\([A-Z0-9]+\)\s*$", "", meta.get("title", s))
        write("fred", s, {"id": f"fred/{s}", "source": "Federal Reserve Bank of St. Louis, FRED",
                          "code": f"FRED {s}", "label": title, "unit": meta.get("units", ""), "freq": freq,
                          "vintage": f"retrieved {prov('fred', s)['retrieved']}", **prov("fred", s),
                          "notes": note, "data": {"US": data} if True else {}})


# ---------------------------------------------------------------- OECD
def build_oecd():
    f = RAW / "oecd" / "QNA_GDP.csv"
    if not f.exists():
        return
    keymap = {"EA20": "EA"}
    data = defaultdict(list)
    for r in csv.DictReader(f.open(encoding="utf-8-sig")):
        if r.get("ADJUSTMENT") != "Y" or r.get("PRICE_BASE") != "LR":
            continue
        y, q = r["TIME_PERIOD"].split("-Q")
        v = num(r["OBS_VALUE"])
        if v is not None:
            data[keymap.get(r["REF_AREA"], r["REF_AREA"])].append([f"{y}-{(int(q) - 1) * 3 + 1:02d}", rnd(v, 1)])
    for k in data:
        data[k] = sorted({p: [p, v] for p, v in data[k]}.values())
    write("oecd", "QNA_GDP", {"id": "oecd/QNA_GDP", "source": "OECD, Quarterly National Accounts",
          "code": "OECD DF_QNA B1GQ, LR, seasonally adjusted (T0102)",
          "label": "Real gross domestic product, chain-linked volume, seasonally adjusted",
          "unit": "National currency, chain-linked volume", "freq": "Q",
          "vintage": f"retrieved {prov('oecd', 'QNA_GDP')['retrieved']}", **prov("oecd", "QNA_GDP"),
          "notes": "Quarterly; period shown as first month of quarter.", "data": dict(data)})


# ---------------------------------------------------------------- ECB
def build_ecb():
    for name, (flow, key) in R.ECB_SERIES.items():
        f = RAW / "ecb" / f"{name}.csv"
        if not f.exists():
            continue
        rows = list(csv.DictReader(f.open()))
        title = rows[0].get("TITLE", "") or rows[0].get("TITLE_COMPL", "")
        unit = rows[0].get("UNIT", "") or rows[0].get("UNIT_MEASURE", "")
        pts = [(r["TIME_PERIOD"], num(r["OBS_VALUE"])) for r in rows if num(r["OBS_VALUE"]) is not None]
        if len(pts[0][0]) == 10:
            # Daily business series (e.g. DFR): keep change points as monthly end-of-month level
            b = {}
            for d, v in pts:
                b[d[:7]] = v
            data, note = [[k, v] for k, v in sorted(b.items())], "End-of-month level (computed from daily)."
        else:
            data, note = [[d[:7], rnd(v, 4)] for d, v in pts], ""
        write("ecb", name, {"id": f"ecb/{name}", "source": "European Central Bank, ECB Data Portal",
                            "code": f"ECB {flow}.{key}", "label": title, "unit": unit, "freq": "M",
                            "vintage": f"retrieved {prov('ecb', name)['retrieved']}", **prov("ecb", name),
                            "notes": note, "data": {"EA": data}})


# ---------------------------------------------------------------- BIS
def bis_rows(ds):
    z = zipfile.ZipFile(RAW / "bis" / f"{ds}.zip")
    with z.open(z.namelist()[0]) as fh:
        rd = csv.reader(io.TextIOWrapper(fh, encoding="utf-8"))
        hdr = [h.split(":")[0] for h in next(rd)]
        for row in rd:
            yield dict(zip(hdr, row))


def code(x):
    return x.split(":")[0].strip()


def build_bis():
    # Policy rates, monthly
    data = defaultdict(list)
    for r in bis_rows("WS_CBPOL"):
        if code(r["FREQ"]) == "M" and num(r["OBS_VALUE"]) is not None:
            data[code(r["REF_AREA"])].append([r["TIME_PERIOD"], num(r["OBS_VALUE"])])
    for c in data:
        data[c].sort()
    write("bis", "CBPOL", {"id": "bis/CBPOL", "source": "Bank for International Settlements, central bank policy rates",
                           "code": "BIS WS_CBPOL M.{area}", "label": "Central bank policy rate", "unit": "% per year",
                           "freq": "M", "vintage": f"retrieved {prov('bis','WS_CBPOL')['retrieved']}",
                           **prov("bis", "WS_CBPOL"), "notes": "Monthly series, end of period.",
                           "data": dict(data)})
    # Total credit, % GDP, adjusted for breaks; sectors P (private non-fin), H (households), N (non-fin corps), G (government)
    out = defaultdict(lambda: defaultdict(list))
    for r in bis_rows("WS_TC"):
        if (code(r["FREQ"]) == "Q" and code(r["TC_LENDERS"]) == "A" and code(r["UNIT_TYPE"]) == "770"
                and code(r["TC_ADJUST"]) == "A" and num(r["OBS_VALUE"]) is not None):
            sec = code(r["TC_BORROWERS"])
            val = code(r["VALUATION"])
            if sec in "PHNG" and val in ("M", "N"):
                if sec == "G" and val != "N":   # government: nominal value; others: market value
                    continue
                y, q = r["TIME_PERIOD"].split("-Q")
                out[sec][code(r["BORROWERS_CTY"])].append([f"{y}-{(int(q)-1)*3+1:02d}", num(r["OBS_VALUE"])])
    labels = {"P": "Credit to the private non-financial sector, from all sectors",
              "H": "Credit to households and NPISHs, from all sectors",
              "N": "Credit to non-financial corporations, from all sectors",
              "G": "Credit to general government (nominal value)"}
    for sec, d in out.items():
        for c in d:
            d[c].sort()
        write("bis", f"TC_{sec}", {"id": f"bis/TC_{sec}", "source": "Bank for International Settlements, total credit statistics",
                                   "code": f"BIS WS_TC Q.{{area}}.{sec}.A.{'N' if sec=='G' else 'M'}.770.A",
                                   "label": labels[sec], "unit": "% of GDP", "freq": "Q",
                                   "vintage": f"retrieved {prov('bis','WS_TC')['retrieved']}", **prov("bis", "WS_TC"),
                                   "notes": "Quarterly, adjusted for breaks; period shown as first month of quarter.",
                                   "data": dict(d)})
    # Effective exchange rates: broad, nominal and real, monthly
    eer = {"N": defaultdict(list), "R": defaultdict(list)}
    for r in bis_rows("WS_EER"):
        if code(r["FREQ"]) == "M" and code(r["EER_BASKET"]) == "B" and num(r["OBS_VALUE"]) is not None:
            t = code(r["EER_TYPE"])
            if t in eer:
                eer[t][code(r["REF_AREA"])].append([r["TIME_PERIOD"], num(r["OBS_VALUE"])])
    for t, d in eer.items():
        for c in d:
            d[c].sort()
        write("bis", f"EER_{t}", {"id": f"bis/EER_{t}", "source": "Bank for International Settlements, effective exchange rates",
                                  "code": f"BIS WS_EER M.{t}.B.{{area}}", "label": f"{'Nominal' if t=='N' else 'Real'} effective exchange rate, broad basket",
                                  "unit": "index, 2020 = 100", "freq": "M", "vintage": f"retrieved {prov('bis','WS_EER')['retrieved']}",
                                  **prov("bis", "WS_EER"), "notes": "Higher = stronger currency.", "data": dict(d)})


# ---------------------------------------------------------------- Shiller
def build_shiller():
    import pandas as pd
    df = pd.read_excel(RAW / "shiller/ie_data.xls", sheet_name="Data", header=7)
    df = df[pd.to_numeric(df["Date"], errors="coerce").notna()]
    price, cape = [], []
    for _, r in df.iterrows():
        y = int(r["Date"]); m = int(round((float(r["Date"]) - y) * 100)) or 10
        p = f"{y}-{m:02d}"
        if num(r["P"]) is not None:
            price.append([p, rnd(num(r["P"]), 2)])
        cp = num(r.get("CAPE"))
        if cp is not None:
            cape.append([p, rnd(cp, 2)])
    base = {"source": "Robert J. Shiller, U.S. stock markets 1871–present and CAPE ratio (Yale)", "freq": "M",
            **prov("shiller", "ie_data"), "vintage": f"retrieved {prov('shiller','ie_data')['retrieved']}"}
    write("shiller", "SP_PRICE", {"id": "shiller/SP_PRICE", "code": "Shiller ie_data.xls, column P",
                                  "label": "S&P Composite stock price index (monthly average of daily closes)",
                                  "unit": "index", "notes": "Monthly average of daily closing prices.",
                                  "data": {"US": price}, **base})
    # Shiller's file ends in 2023; extend with FRED SP500 (monthly average of daily closes, same definition).
    fred = json.loads((CLEAN / "fred/SP500.json").read_text())["data"]["US"] if (CLEAN / "fred/SP500.json").exists() else []
    sh = dict(price); fr = dict(fred)
    overlap = [k for k in sh if k in fr]
    ratio = statistics.fmean(sh[k] / fr[k] for k in overlap[-24:]) if overlap else None
    long = [[k, v] for k, v in price] + [[k, v] for k, v in fred if k > price[-1][0]]
    write("shiller", "SP_LONG", {"id": "shiller/SP_LONG", "code": "Shiller ie_data.xls col P to " + price[-1][0] + "; FRED SP500 after",
                                 "label": "S&P 500 / S&P Composite, monthly average of daily closes",
                                 "unit": "index", "data": {"US": long},
                                 "notes": f"Spliced: Shiller to {price[-1][0]}, FRED SP500 monthly average thereafter. Mean ratio Shiller/FRED over last 24 overlapping months = {ratio:.4f}." if ratio else "Shiller only.",
                                 **base})
    write("shiller", "CAPE", {"id": "shiller/CAPE", "code": "Shiller ie_data.xls, column CAPE",
                              "label": "Cyclically adjusted price-earnings ratio (CAPE)", "unit": "ratio",
                              "notes": "Real price ÷ 10-year average of real earnings. Recent months use estimated earnings.",
                              "data": {"US": cape}, **base})


# ---------------------------------------------------------------- Recessions (computed)
def build_recessions():
    w = json.loads((CLEAN / "wdi/NY.GDP.PCAP.KD.json").read_text())["data"]["WLD"]
    world = [[f"{y}-01", f"{y}-12"] for (py, pv), (y, v) in zip(w, w[1:]) if v < pv]
    us, start, prev = [], None, None
    for p, v in json.loads((CLEAN / "fred/USREC.json").read_text())["data"]["US"]:
        if v == 1 and start is None: start = p
        if v == 0 and start is not None: us.append([start, prev]); start = None
        prev = p
    if start: us.append([start, prev])
    write("meta", "recessions", {"id": "meta/recessions",
        "source": "World: years in which World real GDP per capita (WDI NY.GDP.PCAP.KD, constant US$) fell; US: NBER-based recession months (FRED USREC).",
        "data": {"world": world, "us": [x for x in us if x[0] >= "1990"]}})


# ---------------------------------------------------------------- Geo
def build_geo():
    g = json.loads((RAW / "geo/ne_110m_admin_0_countries.geojson").read_text())
    feats = []
    for f in g["features"]:
        p = f["properties"]
        iso = p.get("ISO_A3") if p.get("ISO_A3") not in (None, "-99") else p.get("ADM0_A3")
        feats.append({"type": "Feature", "properties": {"name": iso, "label": p.get("NAME")}, "geometry": f["geometry"]})
    s = json.dumps({"type": "FeatureCollection", "features": feats}, separators=(",", ":"))
    (ROOT / "assets/geo").mkdir(parents=True, exist_ok=True)
    (ROOT / "assets/geo/world-110m.js").write_text("window.WE_WORLD_GEO=" + s + ";\n")


# ---------------------------------------------------------------- Eurostat / ONS headline inflation
def build_infl():
    f = RAW / "eurostat" / "EA_HICP_ANR.json"
    if f.exists():
        d = json.loads(f.read_text()); t = d["dimension"]["time"]["category"]["index"]; v = d["value"]
        data = [[k, v[str(i)]] for k, i in sorted(t.items(), key=lambda x: x[1]) if str(i) in v]
        write("eurostat", "EA_HICP_ANR", {"id": "eurostat/EA_HICP_ANR", "source": "Eurostat",
              "code": "prc_hicp_minr, geo EA, coicop18 TOTAL, unit RCH_A", "label": d.get("label", "HICP, annual rate of change"),
              "unit": "% change on a year earlier", "freq": "M", "vintage": f"Eurostat update {d.get('updated', '')[:10]}; retrieved {prov('eurostat', 'EA_HICP_ANR')['retrieved']}",
              **prov("eurostat", "EA_HICP_ANR"), "notes": "Euro area HICP, ECOICOP ver. 2 dataset that replaced prc_hicp_manr in 2026.", "data": {"EA": data}})
    f = RAW / "ons" / "UK_CPI_D7G7.csv"
    if f.exists():
        mon = {m: i for i, m in enumerate(["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"], 1)}
        data = []
        for r in csv.reader(f.open(encoding="utf-8-sig")):
            if len(r) == 2 and len(r[0].split()) == 2 and r[0].split()[1] in mon and num(r[1]) is not None:
                y, m = r[0].split(); data.append([f"{y}-{mon[m]:02d}", num(r[1])])
        write("ons", "UK_CPI_D7G7", {"id": "ons/UK_CPI_D7G7", "source": "Office for National Statistics",
              "code": "ONS D7G7 (MM23)", "label": "CPI annual rate, all items (2015=100)", "unit": "% change on a year earlier", "freq": "M",
              "vintage": f"retrieved {prov('ons', 'UK_CPI_D7G7')['retrieved']}", **prov("ons", "UK_CPI_D7G7"), "notes": "", "data": {"GBR": sorted(data)}})


if __name__ == "__main__":
    for fn in (build_weo, build_wdi, build_fred, build_oecd, build_ecb, build_bis, build_shiller, build_recessions, build_geo, build_infl):
        try:
            fn(); print("ok", fn.__name__)
        except Exception as e:
            import traceback; traceback.print_exc(); print("FAIL", fn.__name__, e)
