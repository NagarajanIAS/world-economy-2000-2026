"""Derived figures and series for chapters/theme-development.html.
Output: data/clean/derived/theme_development.json, data/js/derived/dv_poor.js (people in extreme poverty, millions:
Sub-Saharan Africa and the rest of the world, from WDI poverty rates x population).
    .venv/bin/python scripts/derive_theme_development.py
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:26s} {round(v, nd):>12}  {how}")


W = lambda i: {a: dict(v) for a, v in json.loads((C / f"wdi/{i}.json").read_text())["data"].items()}
pv, pv42, pv83 = W("SI.POV.DDAY"), W("SI.POV.LMIC"), W("SI.POV.UMIC")
pop, u5, le, mmr = W("SP.POP.TOTL"), W("SH.DYN.MORT"), W("SP.DYN.LE00.IN"), W("SH.STA.MMRT")
cmp_, lpv, gini, gdp = W("SE.PRM.CMPT.ZS"), W("SE.LPV.PRIM"), W("SI.POV.GINI"), W("NY.GDP.PCAP.PP.KD")
oda, stnt = W("DT.ODA.ODAT.CD"), W("SH.STA.STNT.ZS")

# ---- extreme poverty ($3.00 a day, 2021 PPP)
for a in ("WLD", "SSF", "SAS", "EAS", "MEA", "LCN", "LMY"):
    for y in (1990, 2000, 2010, 2015, 2018, 2019, 2020, 2022, 2024):
        if y in pv.get(a, {}):
            put(f"pv_{a}_{y}", pv[a][y], f"poverty headcount at $3.00/day (2021 PPP), % of population, {a} {y}")
            if y in pop.get(a, {}):
                put(f"np_{a}_{y}", pv[a][y] * pop[a][y] / 1e8, f"people below $3.00/day, millions, {a} {y} (rate x population)", 0)
for a in ("WLD", "SSF", "LMY"):
    for y in (2000, 2010, 2019, 2024):
        if y in pv42.get(a, {}):
            put(f"pv42_{a}_{y}", pv42[a][y], f"poverty headcount at $4.20/day, % {a} {y}")
        if y in pv83.get(a, {}):
            put(f"pv83_{a}_{y}", pv83[a][y], f"poverty headcount at $8.30/day, % {a} {y}")
yrs = [y for y in range(1990, 2025) if y in pv["WLD"] and y in pv["SSF"] and y in pop["WLD"] and y in pop["SSF"]]
nW = {y: pv["WLD"][y] * pop["WLD"][y] / 1e8 for y in yrs}
nS = {y: pv["SSF"][y] * pop["SSF"][y] / 1e8 for y in yrs}
for y in (1990, 2000, 2010, 2015, 2024):
    put(f"sh_SSF_{y}", 100 * nS[y] / nW[y], f"Sub-Saharan Africa share of the world's extreme poor, % {y}", 0)
    put(f"np_rest_{y}", nW[y] - nS[y], f"people below $3.00/day outside Sub-Saharan Africa, millions, {y}", 0)
put("np_WLD_2015_2024", nW[2024] - nW[2015], "change in number of extreme poor 2015-2024, millions", 0)
put("np_WLD_2000_2015", nW[2015] - nW[2000], "change in number of extreme poor 2000-2015, millions", 0)
put("np_WLD_2018_2020", nW[2020] - nW[2018], "change in number of extreme poor 2018-2020, millions (no 2019 world estimate in WDI)", 0)
obj = {"id": "derived/dv_poor", "source": "World Bank, World Development Indicators (Poverty and Inequality Platform)",
       "code": "WDI SI.POV.DDAY x SP.POP.TOTL", "label": "People living below $3.00 a day (2021 PPP), millions",
       "unit": "millions", "freq": "A", "url": "https://data.worldbank.org/indicator/SI.POV.DDAY", "retrieved": "2026-11-23",
       "notes": "Poverty rate times population for the World Bank's world and Sub-Saharan Africa aggregates; rest of world = world minus Sub-Saharan Africa. Recent years are partly nowcasts.",
       "data": {"SSF": [[str(y), round(nS[y], 1)] for y in yrs], "REST": [[str(y), round(nW[y] - nS[y], 1)] for y in yrs]}}
(ROOT / "data/js/derived/dv_poor.js").write_text(f'WE.register("derived/dv_poor",{json.dumps(obj, separators=(",", ":"))});\n')

# ---- health
for a in ("WLD", "SSF", "SAS", "EAS", "IND", "CHN", "BGD", "PAK", "NGA", "LMY"):
    for y in (1990, 2000, 2015, 2019, 2024):
        if y in u5.get(a, {}):
            put(f"u5_{a}_{y}", u5[a][y], f"under-5 mortality per 1,000 live births, {a} {y}", 0 if a != "WLD" else 1)
    if 2000 in u5.get(a, {}) and 2024 in u5[a]:
        put(f"u5fall_{a}", 100 * (1 - u5[a][2024] / u5[a][2000]), f"% fall in under-5 mortality 2000-2024, {a}", 0)
for a in ("WLD", "SSF", "SAS", "IND", "CHN", "USA", "NGA", "LMY"):
    for y in (2000, 2019, 2020, 2021, 2022, 2024):
        if y in le.get(a, {}):
            put(f"le_{a}_{y}", le[a][y], f"life expectancy at birth, years, {a} {y}")
put("le_WLD_drop", le["WLD"][2021] - le["WLD"][2019], "change in world life expectancy 2019-2021, years")
put("le_IND_drop", le["IND"][2021] - le["IND"][2019], "change in India life expectancy 2019-2021, years")
for a in ("WLD", "SSF", "SAS", "IND"):
    for y in (2000, 2015, 2023):
        if y in mmr.get(a, {}):
            put(f"mmr_{a}_{y}", mmr[a][y], f"maternal deaths per 100,000 live births (modelled), {a} {y}", 0)

# ---- education
for a in ("WLD", "SSF", "LMY", "IND"):
    for y in (2000, 2010, 2015, 2019, 2024):
        if y in cmp_.get(a, {}):
            put(f"cmp_{a}_{y}", cmp_[a][y], f"primary completion rate, % of relevant age group, {a} {y}", 0)
for a in ("WLD", "SSF", "SAS", "IND", "LMY"):
    for y in sorted(lpv.get(a, {})):
        put(f"lpv_{a}_{y}", lpv[a][y], f"learning poverty (share of 10-year-olds unable to read a simple text, adjusted for out-of-school), % {a} {y}", 0)

# ---- inequality (Gini, survey years vary)
for a in ("BRA", "ZAF", "USA", "CHN", "IND", "IDN", "NGA", "DEU"):
    s = gini.get(a, {})
    if s:
        f, l = min(s), max(s)
        put(f"gini_{a}_first", s[f], f"Gini index, {a}, first year {f}"); out[f"gini_{a}_first_yr"] = {"value": f, "how": ""}
        put(f"gini_{a}_last", s[l], f"Gini index, {a}, latest year {l}"); out[f"gini_{a}_last_yr"] = {"value": l, "how": ""}
        if 2000 in s or 2001 in s:
            y0 = 2000 if 2000 in s else 2001; put(f"gini_{a}_{y0}", s[y0], f"Gini index {a} {y0}")

# ---- aid received (net ODA, current US$)
for a in ("WLD", "SSF", "IND"):
    for y in (2000, 2010, 2019, 2022, 2023):
        if y in oda.get(a, {}):
            put(f"oda_{a}_{y}", oda[a][y] / 1e9, f"net ODA received, US$ billion (current), {a} {y}")

# ---- India
for y in sorted(pv["IND"]):
    put(f"pv_IND_{y}", pv["IND"][y], f"India poverty at $3.00/day, % {y} (survey year)")
    put(f"pv42_IND_{y}", pv42["IND"][y], f"India poverty at $4.20/day, % {y}")
    put(f"pv83_IND_{y}", pv83["IND"][y], f"India poverty at $8.30/day, % {y}")
    put(f"np_IND_{y}", pv["IND"][y] * pop["IND"][y] / 1e8, f"India people below $3.00/day, millions, {y}", 0)
for y in sorted(gini["IND"]):
    put(f"gini_IND_{y}", gini["IND"][y], f"India Gini index (consumption), {y}")
for y in (2000, 2010, 2024, 2025):
    put(f"gdppc_IND_{y}", gdp["IND"][y], f"India GDP per capita, PPP constant 2021 $, {y}", 0)
put("gdppc_IND_x", gdp["IND"][2024] / gdp["IND"][2000], "India GDP per capita PPP 2024 / 2000", 1)
for y in sorted(stnt.get("IND", {})):
    put(f"stnt_IND_{y}", stnt["IND"][y], f"India stunting, % of children under 5, {y}")

# ---- aid given: OECD DAC1, DAC countries, net ODA disbursements (measure 1010, flow 1140), constant 2024 US$ and current
import csv
odaq, odav, gni = {}, {}, {}
for row in csv.DictReader(open(ROOT / "data/raw/oecd/dac1.csv")):
    m = row["MEASURE: Measure"].split(":")[0]; ft = row["FLOW_TYPE: Flow type"][:4]; pb = row["PRICE_BASE: Price base"][0]
    y = int(row["TIME_PERIOD: Time period"]); v = float(row["OBS_VALUE"])
    if m == "1010" and ft == "1140":
        (odaq if pb == "Q" else odav)[y] = v
    if m == "1" and ft == "1140" and pb == "V":
        gni[y] = v
for y in (2000, 2005, 2010, 2015, 2020, 2022, 2023, 2024, 2025):
    put(f"dac_{y}", odaq[y] / 1e3, f"DAC net ODA, US$ billion at constant 2024 prices, {y} (OECD DAC1 measure 1010)")
    put(f"dacgni_{y}", 100 * odav[y] / gni[y], f"DAC net ODA as % of DAC GNI, current prices, {y}", 2)
put("dac_x_2000_2023", odaq[2023] / odaq[2000], "DAC real net ODA 2023 / 2000")
put("dac_fall_2025", 100 * (odaq[2025] / odaq[2024] - 1), "% change in DAC real net ODA, 2025 on 2024")
put("dac_fall_2023_2025", 100 * (odaq[2025] / odaq[2023] - 1), "% change in DAC real net ODA, 2025 on 2023")
yb = min(y for y in odaq if y > 2005 and odaq[y] <= odaq[2025] * 1.0001) if any(y > 2005 and odaq[y] <= odaq[2025] for y in odaq) else None
obj = {"id": "derived/dv_oda", "source": "OECD Development Assistance Committee, DAC1 table (OECD data API)",
       "code": "OECD.DCD.FSD DSD_DAC1@DF_DAC1, donor DAC, measure 1010 (ODA), flow 1140 (net disbursements), constant 2024 prices",
       "label": "Official development assistance from DAC donors, net disbursements, US$ billion at 2024 prices",
       "unit": "US$ bn (2024 prices)", "freq": "A", "url": "https://sdmx.oecd.org/public/rest/data/OECD.DCD.FSD,DSD_DAC1@DF_DAC1,/DAC._Z.......?startPeriod=2000",
       "retrieved": "2026-11-23", "notes": "Net disbursements in constant 2024 US dollars. Since 2018 the OECD's headline measure is the grant equivalent, which differs slightly; 2025 figures are preliminary.",
       "data": {"DAC": [[str(y), round(odaq[y] / 1e3, 1)] for y in sorted(odaq)]}}
(ROOT / "data/js/derived/dv_oda.js").write_text(f'WE.register("derived/dv_oda",{json.dumps(obj, separators=(",", ":"))});\n')

(C / "derived/theme_development.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
