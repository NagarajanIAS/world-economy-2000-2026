"""Derived figures and series for chapters/theme-debt.html.
Output: data/clean/derived/theme_debt.json, data/js/derived/td_int.js (net interest as % of general government
revenue, WEO), data/js/derived/td_rg.js (US 10-year Treasury yield and nominal GDP growth, annual).
    .venv/bin/python scripts/derive_theme_debt.py
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>10}  {how}")


def lab(k, v, how=""):
    out[k] = {"value": v, "how": how}
    print(f"{k:28s} {v!s:>10}  {how}")


J = lambda p: json.loads((C / p).read_text())
W = lambda ind: {a: dict(v) for a, v in J(f"weo/{ind}.json")["data"].items()}
debt, bal, pb, rev = W("GGXWDG_NGDP"), W("GGXCNL_NGDP"), W("GGXONLB_NGDP"), W("GGR_NGDP")
avg = lambda d, a, b: sum(d[y] for y in range(a, b + 1)) / (b - a + 1)

# ---- gross debt
for a in ("G110", "G200", "G119", "G163", "G603", "USA", "JPN", "CHN", "ITA", "GRC", "GBR", "DEU", "FRA", "IND", "BRA", "ZAF", "CAN", "ZMB", "GHA", "LKA"):
    for y in (2000, 2001, 2007, 2008, 2009, 2012, 2019, 2020, 2021, 2022, 2024, 2025, 2026, 2031):
        if y in debt.get(a, {}):
            put(f"d_{a}_{y}", debt[a][y], f"general government gross debt, % of GDP, {a} {y} (WEO Oct 2026)", 0 if a not in ("G110", "G200", "USA", "CHN", "IND") else 1)
for a in ("G110", "G200", "USA", "CHN", "JPN", "GRC", "ZMB"):
    pk = max(debt[a], key=lambda y: debt[a][y] if y <= 2031 else -1)
    put(f"dpk_{a}", debt[a][pk], f"peak gross debt {a} to 2031", 0); lab(f"dpk_{a}_yr", pk, f"year of peak gross debt {a}")
put("d_G110_2007_2012", debt["G110"][2012] - debt["G110"][2007], "rise in AE debt ratio 2007-2012, points", 0)
put("d_G110_2019_2020", debt["G110"][2020] - debt["G110"][2019], "rise in AE debt ratio 2019-2020, points", 0)
put("d_G200_2008_2026", debt["G200"][2026] - debt["G200"][2008], "rise in EMDE debt ratio 2008-2026, points", 0)
put("d_CHN_2008_2026", debt["CHN"][2026] - debt["CHN"][2008], "rise in China debt ratio 2008-2026, points", 0)
lab("cross_CHN_US", next((y for y in range(2026, 2032) if debt["CHN"][y] > debt["USA"][y]), "none"), "first year China debt ratio above US (none = not by 2031)")
put("n_over100_2007", sum(1 for a in debt if len(a) == 3 and a.isalpha() and debt[a].get(2007, 0) > 100), "economies with debt above 100% of GDP, 2007", 0)
put("n_over100_2026", sum(1 for a in debt if len(a) == 3 and a.isalpha() and debt[a].get(2026, 0) > 100), "economies with debt above 100% of GDP, 2026", 0)

# ---- overall balance (net lending/borrowing)
for a in ("G110", "G200", "USA", "CHN", "DEU", "JPN", "GBR", "IND", "FRA", "ITA"):
    for y in (2007, 2009, 2019, 2020, 2022, 2025, 2026, 2031):
        if y in bal.get(a, {}):
            put(f"b_{a}_{y}", bal[a][y], f"general government net lending/borrowing, % of GDP, {a} {y}")
put("b_USA_2015_2019", avg(bal["USA"], 2015, 2019), "average US general government balance 2015-2019")
put("b_USA_2026_2031", avg(bal["USA"], 2026, 2031), "average US general government balance 2026-2031 (IMF projection)")
put("b_DEU_n_surplus", sum(1 for y in range(2012, 2020) if bal["DEU"][y] >= 0), "years 2012-2019 with German balance at or above zero", 0)

# ---- net interest = primary balance - overall balance; as % of GDP and of revenue
NI = {a: {y: pb[a][y] - bal[a][y] for y in pb.get(a, {}) if y in bal.get(a, {})} for a in pb}
NIR = {a: {y: 100 * NI[a][y] / rev[a][y] for y in NI[a] if y in rev.get(a, {}) and rev[a][y]} for a in NI}
for a in ("G110", "G200", "USA", "IND", "BRA", "CHN", "ZAF", "JPN", "ITA", "GBR", "DEU", "FRA", "MEX", "IDN"):
    for y in (2007, 2019, 2021, 2022, 2025, 2026, 2031):
        if y in NI.get(a, {}):
            put(f"ni_{a}_{y}", NI[a][y], f"net interest, % of GDP, {a} {y} (primary minus overall balance)")
        if y in NIR.get(a, {}):
            put(f"nir_{a}_{y}", NIR[a][y], f"net interest, % of general government revenue, {a} {y}")
for a in ("G110", "G200", "USA", "IND", "CHN", "BRA"):
    for y in (2000, 2001, 2007, 2019, 2025, 2026, 2031):
        if y in rev.get(a, {}):
            put(f"rev_{a}_{y}", rev[a][y], f"general government revenue, % of GDP, {a} {y}")
put("nir_IND_2014_2025", avg(NIR["IND"], 2014, 2025), "average India net interest/revenue 2014-2025")
put("nir_G200_2014_2025", avg(NIR["G200"], 2014, 2025), "average EMDE net interest/revenue 2014-2025")
put("ni_IND_2014_2025", avg(NI["IND"], 2014, 2025), "average India net interest/GDP 2014-2025")

KEYS = {"USA": "USA", "G110": "S04", "G200": "IND", "BRA": "BRA", "ZAF": "S06", "IND": "IND", "CHN": "CHN"}
ser = {a: [[str(y), round(NIR[a][y], 2)] for y in sorted(NIR[a]) if 2000 <= y <= 2031] for a in ("USA", "G110", "G200", "BRA", "ZAF", "IND", "CHN", "JPN", "ITA", "GBR", "DEU", "FRA", "MEX", "IDN")}
obj = {"id": "derived/td_int", "source": "IMF, World Economic Outlook database, October 2026",
       "code": "IMF.RES,WEO GGXONLB_NGDP, GGXCNL_NGDP, GGR_NGDP", "label": "Net interest payments, % of general government revenue",
       "unit": "% of revenue", "freq": "A", "vintage": "WEO Oct 2026 (published 2026-10-13)",
       "url": "https://api.imf.org/external/sdmx/2.1/data/IMF.RES,WEO/", "retrieved": "2026-11-22",
       "notes": "Net interest is the primary balance minus the overall balance (net lending/borrowing), divided by general government revenue. Values from 2026 are IMF projections (2025 for some economies).",
       "data": ser}
(ROOT / "data/js/derived/td_int.js").write_text(f'WE.register("derived/td_int",{json.dumps(obj, separators=(",", ":"))});\n')

# ---- US r and g: 10-year Treasury yield (annual average of monthly) and nominal GDP growth (annual average level)
y10 = J("fred/DGS10.json")["data"]["US"]; gdp = J("fred/GDP.json")["data"]["US"]
ry = {}
for p, v in y10:
    ry.setdefault(int(p[:4]), []).append(v)
ry = {y: sum(v) / len(v) for y, v in ry.items() if len(v) == 12}
gl = {}
for p, v in gdp:
    gl.setdefault(int(p[:4]), []).append(v)
gl = {y: sum(v) / 4 for y, v in gl.items() if len(v) == 4}
gg = {y: 100 * (gl[y] / gl[y - 1] - 1) for y in gl if y - 1 in gl}
yrs = [y for y in range(2000, 2026) if y in ry and y in gg]
rg = {"r": [[str(y), round(ry[y], 2)] for y in yrs], "g": [[str(y), round(gg[y], 2)] for y in yrs]}
obj = {"id": "derived/td_rg", "source": "Federal Reserve (DGS10) and US Bureau of Economic Analysis (GDP), via FRED",
       "code": "FRED DGS10, GDP", "label": "US 10-year Treasury yield and nominal GDP growth", "unit": "%", "freq": "A",
       "url": "https://fred.stlouisfed.org/series/DGS10", "retrieved": "2026-11-22",
       "notes": "Yield: annual average of monthly averages of the 10-year constant-maturity Treasury yield. Growth: annual average of quarterly nominal GDP, % change on the previous year.",
       "data": rg}
(ROOT / "data/js/derived/td_rg.js").write_text(f'WE.register("derived/td_rg",{json.dumps(obj, separators=(",", ":"))});\n')
put("r_2000_2007", avg(ry, 2000, 2007), "US 10-year yield, average 2000-2007")
put("g_2000_2007", avg(gg, 2000, 2007), "US nominal GDP growth, average 2000-2007")
put("r_2010_2019", avg(ry, 2010, 2019), "US 10-year yield, average 2010-2019")
put("g_2010_2019", avg(gg, 2010, 2019), "US nominal GDP growth, average 2010-2019")
put("rg_n_neg_2010_2025", sum(1 for y in range(2010, 2026) if ry[y] < gg[y]), "years 2010-2025 with US yield below nominal growth", 0)
for y in (2007, 2012, 2019, 2020, 2021, 2022, 2023, 2024, 2025):
    put(f"r_{y}", ry[y], f"US 10-year yield, annual average {y}", 2 if y in (2020, 2021) else 1)
    put(f"g_{y}", gg[y], f"US nominal GDP growth {y}")
put("r_2026_ytd", sum(v for p, v in y10 if p.startswith("2026")) / sum(1 for p, v in y10 if p.startswith("2026")), "US 10-year yield, average of 2026 months to date")
lab("r_2026_last_month", y10[-1][0], "last month of 10-year yield data")
put("r_2026_last", y10[-1][1], "US 10-year yield, last month")

# ---- India: centre + states
I = lambda p: dict(J(f"india/{p}.json")["data"]["IND"])
igd, igf, icf, isub = I("gg_debt_gdp"), I("gg_fd_gdp"), I("centre_fd_gdp"), I("centre_subsidies_gdp")
for y in (2001, 2003, 2007, 2008, 2009, 2011, 2019, 2020, 2021, 2023, 2024, 2025):
    put(f"igd_{y}", igd[y], f"India centre+states liabilities, % of GDP, FY{y}-{(y + 1) % 100:02d}")
    put(f"igf_{y}", igf[y], f"India centre+states gross fiscal deficit, % of GDP, FY{y}-{(y + 1) % 100:02d}")
    put(f"icf_{y}", icf[y], f"India centre gross fiscal deficit, % of GDP, FY{y}-{(y + 1) % 100:02d}")
lo = min(range(2001, 2020), key=lambda y: igd[y]); put("igd_low", igd[lo], "lowest India combined liabilities ratio 2001-2019"); lab("igd_low_yr", lo, "fiscal year (start) of lowest ratio")
lo = min(range(2001, 2020), key=lambda y: icf[y]); put("icf_low", icf[lo], "lowest centre fiscal deficit 2001-2019"); lab("icf_low_yr", lo, "fiscal year (start) of lowest centre deficit")
put("isub_2020", isub[2020], "centre subsidies, % of GDP, FY2020-21"); put("isub_2025", isub[2025], "centre subsidies, % of GDP, FY2025-26")
put("igf_avg_2001_2025", avg(igf, 2001, 2025), "India combined deficit average FY2001-02 to FY2025-26")
for y in (2019, 2020, 2025, 2026, 2031):
    put(f"dw_IND_{y}", debt["IND"][y], f"India general government gross debt, WEO, % of GDP, {y}")

(C / "derived/theme_debt.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
