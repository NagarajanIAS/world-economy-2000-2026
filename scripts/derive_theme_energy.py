"""Derived figures and series for chapters/theme-energy.html.
Output: data/clean/derived/theme_energy.json and data/js/derived/en_cmo.js (World Bank Pink Sheet monthly price indices,
2010 = 100, and Brent $/bbl), en_co2.js (fossil CO2 emissions, Gt, and per person, t; Global Carbon Budget 2026 via OWID),
en_temp.js (NASA GISTEMP v4 global temperature anomaly), en_elec.js (shares of electricity by source; Ember and Energy
Institute via OWID).
    .venv/bin/python scripts/derive_theme_energy.py
"""
import csv, json, statistics
from collections import defaultdict
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
RAW = ROOT / "data/raw"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


# ---- World Bank Pink Sheet (CMO historical data, monthly, updated 3 Nov 2026)
wb = openpyxl.load_workbook(RAW / "wb_cmo/CMO-Historical-Data-Monthly.xlsx", read_only=True)
pr = list(wb["Monthly Prices"].iter_rows(values_only=True))
hdr = pr[4]
col = {h: i for i, h in enumerate(hdr) if h}
brent = {r[0]: num(r[col["Crude oil, Brent"]]) for r in pr[6:] if r[0] and num(r[col["Crude oil, Brent"]]) is not None}
gas_eu = {r[0]: num(r[col["Natural gas, Europe"]]) for r in pr[6:] if r[0] and num(r[col["Natural gas, Europe"]]) is not None}
ix = list(wb["Monthly Indices"].iter_rows(values_only=True))
IDX = {"ENERGY": 2, "FOOD": 6, "FERT": 13, "METALS": 14}
idx = {k: {r[0]: num(r[c]) for r in ix[9:] if r[0] and num(r[c]) is not None} for k, c in IDX.items()}
m = lambda s: f"{s[:4]}-{s[5:7]}"   # 2008M07 -> 2008-07
def peak(series, a, b):
    k = max((p for p in series if a <= p <= b), key=lambda p: series[p]); return k, series[k]
def trough(series, a, b):
    k = min((p for p in series if a <= p <= b), key=lambda p: series[p]); return k, series[k]
put("brent_2000_01", brent["2000M01"], "Brent, US$/bbl, Jan 2000 (World Bank Pink Sheet)")
k, v = peak(brent, "2008M01", "2008M12"); put("brent_pk2008", v, f"Brent monthly peak 2008 ({k}), $/bbl"); out["brent_pk2008_m"] = {"value": k, "how": ""}
k, v = trough(brent, "2008M07", "2009M06"); put("brent_tr2008", v, f"Brent monthly low after 2008 peak ({k}), $/bbl")
k, v = peak(brent, "2011M01", "2014M08"); put("brent_pk2014", v, f"Brent monthly high 2011-mid 2014 ({k}), $/bbl")
put("brent_2014_06", brent["2014M06"], "Brent, $/bbl, June 2014")
k, v = trough(brent, "2014M07", "2017M12"); put("brent_tr2016", v, f"Brent monthly low 2014-17 ({k}), $/bbl"); out["brent_tr2016_m"] = {"value": k, "how": ""}
put("brent_2020_04", brent["2020M04"], "Brent, $/bbl, April 2020 (monthly average)")
k, v = peak(brent, "2022M01", "2022M12"); put("brent_pk2022", v, f"Brent monthly peak 2022 ({k}), $/bbl"); out["brent_pk2022_m"] = {"value": k, "how": ""}
put("brent_2025_12", brent["2025M12"], "Brent, $/bbl, Dec 2025")
last = max(brent); put("brent_last", brent[last], f"Brent, $/bbl, latest month ({last})"); out["brent_last_m"] = {"value": last, "how": ""}
k, v = peak(brent, "2026M01", last); put("brent_pk2026", v, f"Brent monthly high 2026 ({k}), $/bbl"); out["brent_pk2026_m"] = {"value": k, "how": ""}
put("brent_2020_04_wti", num(pr[[r[0] for r in pr].index("2020M04")][col["Crude oil, WTI"]]), "WTI, $/bbl, April 2020 (monthly average)")
k, v = peak(gas_eu, "2022M01", "2022M12"); put("gaseu_pk2022", v, f"Natural gas, Europe, $/mmbtu, monthly peak 2022 ({k})"); out["gaseu_pk2022_m"] = {"value": k, "how": ""}
gy = defaultdict(list)
for p, v in gas_eu.items(): gy[p[:4]].append(v)
put("gaseu_2019", statistics.fmean(gy["2019"]), "Natural gas, Europe, $/mmbtu, 2019 average")
for K in ("ENERGY", "METALS", "FOOD", "FERT"):
    s = idx[K]
    put(f"ix_{K}_2002", statistics.fmean([s[p] for p in s if p.startswith("2002")]), f"Pink Sheet {K} index (2010 = 100), 2002 average")
    k, v = peak(s, "2007M01", "2008M12"); put(f"ix_{K}_pk2008", v, f"Pink Sheet {K} index, peak 2007-08 ({k})")
    k, v = peak(s, "2021M01", "2022M12"); put(f"ix_{K}_pk2022", v, f"Pink Sheet {K} index, peak 2021-22 ({k})"); out[f"ix_{K}_pk2022_m"] = {"value": k, "how": ""}
    put(f"ix_{K}_2016", statistics.fmean([s[p] for p in s if p.startswith("2016")]), f"Pink Sheet {K} index, 2016 average")
    put(f"ix_{K}_last", s[max(s)], f"Pink Sheet {K} index, {max(s)}")
put("ix_ENERGY_x_02_08", out["ix_ENERGY_pk2008"]["value"] / out["ix_ENERGY_2002"]["value"], "energy index 2008 peak / 2002 average")
put("ix_METALS_x_02_08", out["ix_METALS_pk2008"]["value"] / out["ix_METALS_2002"]["value"], "metals index 2007-08 peak / 2002 average")
reg("en_cmo", {"id": "derived/en_cmo", "source": "World Bank, Commodity Price Data (the Pink Sheet), monthly historical data, updated 3 November 2026",
    "code": "CMO-Historical-Data-Monthly.xlsx: Monthly Indices (Energy, Metals & Minerals, Food, Fertilizers; nominal US$, 2010 = 100) and Monthly Prices (Crude oil, Brent)",
    "label": "Commodity price indices (2010 = 100) and Brent crude ($/bbl)", "unit": "index, 2010 = 100; $/bbl", "freq": "M",
    "url": "https://www.worldbank.org/en/research/commodity-markets", "retrieved": "2026-11-23",
    "notes": "Monthly averages in nominal US dollars.",
    "data": {**{K: [[m(p), v] for p, v in sorted(idx[K].items()) if p >= "1990"] for K in IDX},
             "BRENT": [[m(p), v] for p, v in sorted(brent.items()) if p >= "1990"]}})

# ---- CO2 (Global Carbon Budget 2026, via OWID co2-data)
co2, pc, cum, pop = defaultdict(dict), defaultdict(dict), defaultdict(dict), defaultdict(dict)
for r in csv.DictReader(open(RAW / "owid/owid-co2-data.csv")):
    y = int(r["year"])
    if y < 1990: continue
    c = r["country"]
    if num(r["co2"]) is not None: co2[c][y] = num(r["co2"])
    if num(r["co2_per_capita"]) is not None: pc[c][y] = num(r["co2_per_capita"])
    if num(r["cumulative_co2"]) is not None: cum[c][y] = num(r["cumulative_co2"])
NM = {"World": "WLD", "China": "CHN", "United States": "USA", "European Union (27)": "EU27", "India": "IND", "Japan": "JPN", "Russia": "RUS"}
for c, a in NM.items():
    for y in (2000, 2005, 2010, 2015, 2019, 2020, 2023, 2024, 2025):
        if y in co2[c]: put(f"co2_{a}_{y}", co2[c][y] / 1000, f"CO2 emissions (fossil fuels and industry, excl. land use), Gt, {a} {y}", 1 if co2[c][y] > 1000 else 2)
        if y in pc[c]: put(f"co2pc_{a}_{y}", pc[c][y], f"CO2 per person, tonnes, {a} {y}", 1)
    if 2025 in co2[c]:
        put(f"co2sh_{a}_2025", 100 * co2[c][2025] / co2["World"][2025], f"share of world CO2, % {a} 2025", 0)
        put(f"co2sh_{a}_2000", 100 * co2[c][2000] / co2["World"][2000], f"share of world CO2, % {a} 2000", 0)
    if 2025 in cum[c]:
        put(f"cumsh_{a}", 100 * cum[c][2025] / cum["World"][2025], f"share of cumulative CO2 since 1750, % {a}, to 2025", 0)
put("co2_WLD_x_2000_2025", 100 * (co2["World"][2025] / co2["World"][2000] - 1), "world CO2 2025 vs 2000, % change", 0)
put("co2_CHN_x_2000_2025", co2["China"][2025] / co2["China"][2000], "China CO2 2025 / 2000", 1)
put("co2_USA_ch_2005_2025", 100 * (co2["United States"][2025] / co2["United States"][2005] - 1), "US CO2 2025 vs 2005, % change", 0)
put("co2_EU27_ch_2000_2025", 100 * (co2["European Union (27)"][2025] / co2["European Union (27)"][2000] - 1), "EU27 CO2 2025 vs 2000, % change", 0)
put("co2_IND_x_2000_2025", co2["India"][2025] / co2["India"][2000], "India CO2 2025 / 2000", 1)
row = {c: {y: v / 1000 for y, v in co2[c].items()} for c in NM}
rest = {y: row["World"][y] - sum(row[c][y] for c in ("China", "United States", "European Union (27)", "India")) for y in row["World"] if all(y in row[c] for c in NM if c not in ("Japan", "Russia"))}
put("co2_REST_2025", rest[2025], "CO2 outside China, US, EU27 and India, Gt 2025")
reg("en_co2", {"id": "derived/en_co2", "source": "Global Carbon Budget 2026 (Global Carbon Project), via Our World in Data co2-data",
    "code": "OWID co2-data: co2 (MtCO2, fossil fuels and industry, excluding land-use change) and co2_per_capita",
    "label": "CO2 emissions from fossil fuels and industry: Gt a year (areas) and tonnes per person (areas suffixed _PC)", "unit": "Gt CO2; t CO2 per person", "freq": "A",
    "url": "https://github.com/owid/co2-data", "retrieved": "2026-11-23", "notes": "Excludes emissions from land-use change. Territorial (production-based) emissions.",
    "data": {**{NM[c]: [[str(y), round(v, 3)] for y, v in sorted(row[c].items())] for c in NM},
             "REST": [[str(y), round(v, 3)] for y, v in sorted(rest.items())],
             **{NM[c] + "_PC": [[str(y), round(v, 2)] for y, v in sorted(pc[c].items())] for c in NM}}})

# ---- temperature: NASA GISTEMP v4, annual mean (J-D), anomaly vs 1951-1980
tmp = {}
for r in list(csv.reader(open(RAW / "nasa/GLB.Ts+dSST.csv")))[2:]:
    if r and r[0].isdigit() and num(r[13]) is not None:
        tmp[int(r[0])] = num(r[13])
for y in (2000, 2010, 2015, 2016, 2020, 2023, 2024, 2025):
    put(f"temp_{y}", tmp[y], f"global surface temperature anomaly vs 1951-80, degrees C, {y} (GISTEMP v4)", 2)
top = sorted(tmp, key=lambda y: -tmp[y])[:3]
out["temp_warmest"] = {"value": top[0], "how": "warmest year in GISTEMP"}; out["temp_2nd"] = {"value": top[1], "how": ""}
print("warmest", top)
put("temp_8090", statistics.fmean([tmp[y] for y in range(1980, 1990)]), "mean anomaly 1980-89, C", 2)
put("temp_1625", statistics.fmean([tmp[y] for y in range(2016, 2026)]), "mean anomaly 2016-25, C", 2)
reg("en_temp", {"id": "derived/en_temp", "source": "NASA Goddard Institute for Space Studies, GISTEMP v4 (GLB.Ts+dSST)",
    "code": "Land-ocean temperature index, annual mean (J-D)", "label": "Global surface temperature, difference from the 1951-1980 average, °C",
    "unit": "°C vs 1951–80", "freq": "A", "url": "https://data.giss.nasa.gov/gistemp/", "retrieved": "2026-11-23",
    "notes": "The 1951–1980 base is NASA's; it is not the pre-industrial base (1850–1900) used for the 1.5°C and 2°C goals.",
    "data": {"WLD": [[str(y), v] for y, v in sorted(tmp.items()) if y >= 1950]}})

# ---- electricity mix (OWID energy-data: Ember and Energy Institute)
el = defaultdict(lambda: defaultdict(dict))
F = ["coal_share_elec", "gas_share_elec", "oil_share_elec", "nuclear_share_elec", "hydro_share_elec", "solar_share_elec", "wind_share_elec", "renewables_share_elec", "fossil_share_elec"]
for r in csv.DictReader(open(RAW / "owid/owid-energy-data.csv")):
    if r["country"] in ("World", "China", "India", "United States", "European Union (27)") and int(r["year"]) >= 2000:
        for f in F:
            if num(r[f]) is not None: el[r["country"]][f][int(r["year"])] = num(r[f])
EN = {"World": "WLD", "China": "CHN", "India": "IND", "United States": "USA", "European Union (27)": "EU27"}
sw = {c: {y: el[c]["solar_share_elec"][y] + el[c]["wind_share_elec"][y] for y in el[c]["solar_share_elec"] if y in el[c]["wind_share_elec"]} for c in EN}
for c, a in EN.items():
    for y in (2000, 2010, 2015, 2020, 2024, 2025):
        if y in sw[c]: put(f"sw_{a}_{y}", sw[c][y], f"solar + wind share of electricity, % {a} {y}", 1)
        if y in el[c]["coal_share_elec"]: put(f"coal_{a}_{y}", el[c]["coal_share_elec"][y], f"coal share of electricity, % {a} {y}", 0)
        if y in el[c]["fossil_share_elec"]: put(f"fos_{a}_{y}", el[c]["fossil_share_elec"][y], f"fossil share of electricity, % {a} {y}", 0)
for y in (2015, 2020, 2025):
    for f in ("solar_share_elec", "wind_share_elec", "hydro_share_elec", "nuclear_share_elec"):
        if y in el["India"][f]: put(f"{f[:5]}_IND_{y}", el["India"][f][y], f"India {f}, % {y}", 1)
reg("en_elec", {"id": "derived/en_elec", "source": "Ember (Yearly Electricity Data) and Energy Institute (Statistical Review of World Energy), via Our World in Data energy-data",
    "code": "OWID energy-data: *_share_elec", "label": "Share of electricity generation by source, %", "unit": "% of electricity", "freq": "A",
    "url": "https://github.com/owid/energy-data", "retrieved": "2026-11-23", "notes": "Solar plus wind for the SW series; IND_COAL etc. give India's mix.",
    "data": {**{EN[c] + "_SW": [[str(y), round(v, 2)] for y, v in sorted(sw[c].items())] for c in EN},
             **{"IND_" + f.split("_")[0].upper(): [[str(y), round(v, 2)] for y, v in sorted(el["India"][f].items())] for f in F[:7]}}})

# ---- India oil
oi = dict(json.loads((C / "india/oil_imports.json").read_text())["data"]["IND"])
ims = dict(json.loads((C / "india/enr_crude_import_share.json").read_text())["data"]["IND"])
for y in (2000, 2003, 2008, 2011, 2013, 2015, 2016, 2020, 2022, 2024, 2025):
    if y in oi: put(f"oil_IND_{y}", oi[y], f"India oil imports, US$ bn, FY{y}-{str(y+1)[2:]}", 0)
for y in (2001, 2010, 2015, 2020, 2024):
    if y in ims: put(f"cris_IND_{y}", ims[y], f"India crude imports, % of crude supply, FY{y}-{str(y+1)[2:]}", 0)
ngdp = json.loads((C / "weo/NGDPD.json").read_text())["data"]["IND"]; ngdp = dict(ngdp)
for y in (2008, 2011, 2013, 2015, 2022, 2024, 2025):
    if y in oi and y in ngdp: put(f"oilgdp_IND_{y}", 100 * oi[y] / ngdp[y], f"India oil imports, % of GDP (WEO US$ GDP, fiscal year), FY{y}", 1)
ei = {a: dict(v) for a, v in json.loads((C / "wdi/EG.EGY.PRIM.PP.KD.json").read_text())["data"].items()}
for a in ("WLD", "IND", "CHN", "USA"):
    put(f"eint_{a}_ch", 100 * (ei[a][2021] / ei[a][2000] - 1), f"energy intensity of GDP, % change 2000-2021, {a} (WDI)", 0)
(C / "derived/theme_energy.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
