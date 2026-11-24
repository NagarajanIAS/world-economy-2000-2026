"""Derived figures and series for chapters/theme-demography.html.
Output: data/clean/derived/theme_demography.json and data/js/derived/dl_tfr.js (total fertility rate), dl_old.js (share
of population aged 65+), dl_wa.js (share aged 15-64), dl_pop.js (population, billions): UN World Population Prospects
2024, estimates to 2023 and medium-variant projections from 2024 to 2050. dl_tight.js: US job openings per unemployed
person (BLS JOLTS and CPS via FRED).
    .venv/bin/python scripts/derive_theme_demography.py
"""
import csv, gzip, json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
RAW = ROOT / "data/raw"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:30s} {round(v, nd):>12}  {how}")


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def S(path):
    return json.loads((C / f"{path}.json").read_text())["data"]


def A(series, area):
    return {int(str(t)[:4]) if len(str(t)) == 4 else t: v for t, v in series[area] if v is not None}


# ---- UN World Population Prospects 2024
WPP = "https://population.un.org/wpp/"
NAMES = {"World": "WLD", "China": "CHN", "India": "IND", "Japan": "JPN", "United States of America": "USA",
         "Republic of Korea": "KOR", "Germany": "DEU", "Italy": "ITA", "Nigeria": "NGA", "Sub-Saharan Africa": "SSF",
         "Europe": "EUR", "Brazil": "BRA"}
ind = defaultdict(dict)   # (area, var) -> {year: value}
with gzip.open(RAW / "wpp/WPP2024_Demographic_Indicators_Medium.csv.gz", "rt", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        a = NAMES.get(r["Location"])
        if not a or r["LocTypeName"] == "" and a not in ("WLD", "SSF", "EUR"):
            continue
        y = int(r["Time"])
        if y > 2100:
            continue
        for v in ("TFR", "TPopulation1July", "MedianAgePop", "LEx", "NetMigrations"):
            x = num(r[v])
            if x is not None:
                ind[(a, v)][y] = x
age = defaultdict(dict)
with open(RAW / "wpp/wpp2024_agepct_extract.csv", newline="") as f:
    for r in csv.DictReader(f):
        a = NAMES.get(r["Region, subregion, country or area *"])
        if not a:
            continue
        y = int(float(r["Year"]))
        for g in ("65+", "15-64", "0-14"):
            x = num(r[g])
            if x is not None:
                age[(a, g)][y] = x

LAST = 2023
proj = {"last_actual_default": LAST, "proj_label": "UN projections",
        "proj_note": "Values from {from} onward (shaded) are UN medium-variant projections."}
base = {"source": "United Nations, Department of Economic and Social Affairs, Population Division, World Population Prospects 2024",
        "url": WPP, "retrieved": "2026-11-23", "freq": "A"}
AREAS = ["WLD", "CHN", "IND", "JPN", "USA", "KOR", "DEU", "ITA", "NGA", "SSF", "EUR", "BRA"]


def ser(d, a, y0=1990, y1=2050, f=lambda v: v, nd=2):
    return [[str(y), round(f(d[(a)][y]), nd)] for y in range(y0, y1 + 1) if y in d[a]]


reg("dl_tfr", {**base, **proj, "id": "derived/dl_tfr", "code": "WPP2024 TFR (Demographic Indicators, medium variant)",
               "label": "Total fertility rate (live births per woman)", "unit": "births per woman",
               "data": {a: ser(ind, (a, "TFR")) for a in AREAS}})
reg("dl_old", {**base, **proj, "id": "derived/dl_old", "code": "WPP2024 POP/F06-1, age 65+",
               "label": "Population aged 65 and over, % of total", "unit": "%",
               "data": {a: ser(age, (a, "65+"), nd=1) for a in AREAS}})
reg("dl_wa", {**base, **proj, "id": "derived/dl_wa", "code": "WPP2024 POP/F06-1, age 15-64",
              "label": "Population aged 15-64, % of total", "unit": "%",
              "data": {a: ser(age, (a, "15-64"), nd=1) for a in AREAS}})
reg("dl_pop", {**base, **proj, "id": "derived/dl_pop", "code": "WPP2024 TPopulation1July",
               "label": "Population on 1 July, billions", "unit": "billion",
               "data": {a: ser(ind, (a, "TPopulation1July"), f=lambda v: v / 1e6, nd=3) for a in ["WLD", "CHN", "IND", "SSF", "EUR"]}})

for a in AREAS:
    t = ind[(a, "TFR")]
    for y in (1990, 2000, 2010, 2015, 2023, 2050):
        put(f"tfr_{a}_{y}", t[y], f"WPP2024 TFR, {a}, {y}", 2)
    o = age[(a, "65+")]
    for y in (2000, 2023, 2050):
        put(f"old_{a}_{y}", o[y], f"WPP2024 share 65+, {a}, {y}")
    w = age[(a, "15-64")]
    for y in (2000, 2023, 2050):
        put(f"wa_{a}_{y}", w[y], f"WPP2024 share 15-64, {a}, {y}")
    put(f"wa_{a}_peak", max(w, key=lambda y: w[y] if y <= 2100 else -1), f"WPP2024 year of peak share 15-64, {a}", 0)
    p = ind[(a, "TPopulation1July")]
    for y in (2000, 2023, 2026, 2050):
        put(f"pop_{a}_{y}", p[y] / 1e3, f"WPP2024 population, million, {a}, {y}", 0)
    put(f"pop_{a}_peak", max(p, key=lambda y: p[y]), f"WPP2024 year of peak population (to 2100), {a}", 0)
    put(f"pop_{a}_peakval", max(p.values()) / 1e3, f"WPP2024 peak population, million, {a}", 0)
    m = ind[(a, "MedianAgePop")]
    for y in (2000, 2023):
        put(f"medage_{a}_{y}", m[y], f"WPP2024 median age, {a}, {y}")
# year India's population overtook China's
cross = min(y for y in range(1990, 2101) if ind[("IND", "TPopulation1July")][y] > ind[("CHN", "TPopulation1July")][y])
put("ind_over_chn", cross, "WPP2024 first year India's 1 July population exceeds China's", 0)
put("chn_decline_2023_2050", (ind[("CHN", "TPopulation1July")][2050] / ind[("CHN", "TPopulation1July")][2023] - 1) * 100,
    "WPP2024 change in China's population 2023-2050, %", 0)
# share of world population growth 2023-2050 in Sub-Saharan Africa
gw = ind[("WLD", "TPopulation1July")][2050] - ind[("WLD", "TPopulation1July")][2023]
gs = ind[("SSF", "TPopulation1July")][2050] - ind[("SSF", "TPopulation1July")][2023]
put("ssf_share_growth_2023_2050", gs / gw * 100, "WPP2024 Sub-Saharan Africa share of world population increase 2023-2050, %", 0)
put("wld_growth_2023_2050", gw / 1e6, "WPP2024 world population increase 2023-2050, billion", 2)

# ---- WDI labour (ILO modelled estimates)
fe = S("wdi/SL.TLF.CACT.FE.ZS"); ma = S("wdi/SL.TLF.CACT.MA.ZS"); un = S("wdi/SL.UEM.TOTL.ZS"); yu = S("wdi/SL.UEM.1524.ZS")
ag = S("wdi/SL.AGR.EMPL.ZS"); rm = S("wdi/BX.TRF.PWKR.CD.DT"); rmg = S("wdi/BX.TRF.PWKR.DT.GD.ZS")
LAB = ["WLD", "IND", "CHN", "USA", "EMU", "JPN", "BRA", "SSF", "BGD", "SAS", "MEA", "KOR", "ESP", "GRC", "ZAF"]
for a in LAB:
    for y in (2000, 2010, 2019, 2025):
        for nm, d in (("lfpf", fe), ("lfpm", ma), ("un", un), ("yun", yu), ("agr", ag)):
            if a in d:
                v = A(d, a).get(y)
                if v is not None:
                    put(f"{nm}_{a}_{y}", v, f"WDI {nm} {a} {y}")
for a in ("USA", "EMU", "ESP", "GRC", "ZAF", "WLD"):
    s = A(un, a)
    pk = max((y for y in s if 2008 <= y <= 2016), key=lambda y: s[y])
    put(f"un_{a}_pk0816", s[pk], f"WDI unemployment peak 2008-16, {a} ({pk})")
    put(f"un_{a}_pk0816_y", pk, f"year of that peak, {a}", 0)
    s2 = A(yu, a)
    pk2 = max((y for y in s2 if 2008 <= y <= 2016), key=lambda y: s2[y])
    put(f"yun_{a}_pk0816", s2[pk2], f"WDI youth unemployment peak 2008-16, {a} ({pk2})")
for a in ("IND", "MEX", "CHN", "PHL", "PAK", "EGY", "BGD", "FRA", "NGA", "LMY", "WLD"):
    s = A(rm, a)
    yy = max(y for y in s)
    put(f"rem_{a}_last", s[yy] / 1e9, f"WDI remittances received, US$ bn, {a}, {yy}")
    put(f"rem_{a}_last_y", yy, f"latest year, {a}", 0)
    if 2000 in s:
        put(f"rem_{a}_2000", s[2000] / 1e9, f"WDI remittances received, US$ bn, {a}, 2000")
s = A(rmg, "IND")
put("remgdp_IND_last", s[max(s)], f"WDI remittances % GDP, India, {max(s)}")

# ---- US labour market (FRED)
def F(code):
    return {t: v for t, v in S(f"fred/{code}")["USA"] if v is not None} if "USA" in S(f"fred/{code}") else None


def fr(code):
    d = S(f"fred/{code}")
    k = list(d.keys())[0]
    return {t: v for t, v in d[k] if v is not None}


jol, une = fr("JTSJOL"), fr("UNEMPLOY")
tight = {t: round(jol[t] / une[t], 3) for t in jol if t in une}
reg("dl_tight", {"id": "derived/dl_tight", "source": "US Bureau of Labor Statistics (JOLTS job openings; CPS unemployment level), via FRED",
                 "code": "FRED JTSJOL / UNEMPLOY", "label": "US job openings per unemployed person", "unit": "ratio",
                 "freq": "M", "url": "https://fred.stlouisfed.org/series/JTSJOL", "retrieved": "2026-11-23",
                 "notes": "Computed for this book: job openings at the end of the month divided by the number of unemployed people.",
                 "data": {"USA": [[t[:7], v] for t, v in sorted(tight.items())]}})
pk = max(tight, key=tight.get)
put("tight_pk", tight[pk], f"US job openings per unemployed, peak ({pk})", 2)
put("tight_pk_y", int(pk[:4]), "year of that peak", 0)
low = min((t for t in tight if t >= "2009"), key=tight.get)
put("tight_low09", tight[low], f"US job openings per unemployed, low after 2009 ({low})", 2)
lt = max(tight)
put("tight_last", tight[lt], f"US job openings per unemployed, latest ({lt})", 2)
q = fr("JTSQUR"); qp = max(q, key=q.get)
put("quits_pk", q[qp], f"US quits rate, peak ({qp})")
put("quits_2019", sum(v for t, v in q.items() if t.startswith("2019")) / 12, "US quits rate, 2019 average")
cp = fr("LNS11300060")
put("prime_2000", sum(v for t, v in cp.items() if t.startswith("2000")) / 12, "US prime-age (25-54) participation, 2000 average")
put("prime_low", min(v for t, v in cp.items() if "2010" <= t < "2016"), "US prime-age participation, 2010-15 low")
put("prime_last", cp[max(cp)], f"US prime-age participation, latest ({max(cp)})")
ls = fr("PRS85006173")
lsy = defaultdict(list)
for t, v in ls.items():
    lsy[t[:4]].append(v)
for y in ("2000", "2014", "2025"):
    if y in lsy:
        put(f"lshare_{y}", sum(lsy[y]) / len(lsy[y]), f"US nonfarm business labour share index (2017=100), {y} average")
ur = fr("UNRATE")
put("us_un_pk2009", max(v for t, v in ur.items() if "2009" <= t < "2011"), "US unemployment peak 2009-10")
put("us_un_pk2020", max(v for t, v in ur.items() if "2020" <= t < "2021"), "US unemployment peak 2020 (April)")
put("us_un_last", ur[max(ur)], f"US unemployment, latest ({max(ur)})")

(C / "derived/theme_demography.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
