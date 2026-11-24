"""Derived figures for chapters/theme-trade.html. Output: data/clean/derived/theme_trade.json.
    .venv/bin/python scripts/derive_theme_trade.py
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


def A(path, area):
    return {int(str(p)[:4]): v for p, v in json.loads((C / path).read_text())["data"][area]}


def Q(path):
    return dict(next(iter(json.loads((C / path).read_text())["data"].values())))


avg = lambda d, a, b: sum(d[y] for y in range(a, b + 1)) / (b - a + 1)

# ---- world trade volume vs world GDP (WEO, annual % change)
tr, g = A("weo/TRADEPCH.json", "G001"), A("weo/NGDP_RPCH.json", "G001")
for a, b in [(1990, 1999), (2000, 2007), (2012, 2019), (2020, 2025), (2026, 2031)]:
    put(f"tr_{a}_{b}", avg(tr, a, b), f"WEO TRADEPCH G001, average annual growth of world trade volume {a}-{b}")
    put(f"gw_{a}_{b}", avg(g, a, b), f"WEO NGDP_RPCH G001, average annual world GDP growth {a}-{b}")
    put(f"el_{a}_{b}", avg(tr, a, b) / avg(g, a, b), f"ratio of average trade growth to average GDP growth {a}-{b}", 1)
for y in (2009, 2019, 2020, 2021, 2023, 2025, 2026):
    put(f"tr_{y}", tr[y], f"WEO TRADEPCH G001 {y}, %")

# ---- trade (exports + imports) as % of GDP, WDI NE.TRD.GNFS.ZS
for c, ys in {"WLD": (2000, 2008, 2009, 2019, 2022, 2024), "CHN": (2000, 2006, 2024), "IND": (2000, 2008, 2024),
              "USA": (2000, 2024), "VNM": (2000, 2024), "DEU": (2000, 2024)}.items():
    o = A("wdi/NE.TRD.GNFS.ZS.json", c)
    for y in ys:
        put(f"op_{c}_{y}", o[y], f"WDI NE.TRD.GNFS.ZS {c} {y}, trade % of GDP")
o = A("wdi/NE.TRD.GNFS.ZS.json", "WLD")
lab("op_WLD_peak_year", max((y for y in range(2000, 2025)), key=lambda y: o[y]), "year of highest world trade/GDP 2000-2024")

# ---- shares of world merchandise exports (WDI TX.VAL.MRCH.CD.WT)
w = A("wdi/TX.VAL.MRCH.CD.WT.json", "WLD")
sh = {c: {y: v / w[y] * 100 for y, v in A("wdi/TX.VAL.MRCH.CD.WT.json", c).items() if y in w} for c in ["CHN", "USA", "DEU", "JPN", "IND", "VNM", "MEX"]}
for c in sh:
    for y in (2000, 2007, 2019, 2025):
        put(f"xs_{c}_{y}", sh[c][y], f"{c} merchandise exports, % of world, {y} (WDI TX.VAL.MRCH.CD.WT)")
lab("xs_chn_over_usa", next(y for y in range(2000, 2026) if sh["CHN"][y] > sh["USA"][y]), "first year China's export share exceeds the US's")
lab("xs_chn_over_deu", next(y for y in range(2000, 2026) if sh["CHN"][y] > sh["DEU"][y]), "first year China's export share exceeds Germany's")
put("x_wld_2000", w[2000] / 1e12, "world merchandise exports, $ trillion, 2000", 1)
put("x_wld_2025", w[2025] / 1e12, "world merchandise exports, $ trillion, 2025", 1)

# ---- services in world exports (WDI BX.GSR.NFSV.CD / BX.GSR.GNFS.CD)
sv, gs = A("wdi/BX.GSR.NFSV.CD.json", "WLD"), A("wdi/BX.GSR.GNFS.CD.json", "WLD")
for y in (2000, 2008, 2025):
    put(f"svs_{y}", sv[y] / gs[y] * 100, f"services exports, % of world exports of goods and services, {y}")
for c in ["IND", "IRL", "USA", "CHN"]:
    s = A("wdi/BX.GSR.NFSV.CD.json", c)
    for y in (2000, 2024):
        if y in s:
            put(f"svw_{c}_{y}", s[y] / sv[y] * 100, f"{c} services exports, % of world services exports, {y}")
ict = A("wdi/BX.GSR.CCIS.ZS.json", "IND")
put("ict_IND_2025", ict[2025], "ICT services, % of India's services exports, 2025 (WDI BX.GSR.CCIS.ZS)")

# ---- applied tariffs (WDI TM.TAX.MRCH.WM.AR.ZS, weighted mean, all products)
for c, ys in {"CHN": (2000, 2001, 2005, 2022), "IND": (2000, 2001, 2008, 2022), "BRA": (2000, 2022), "EUU": (2000, 2022)}.items():
    t = A("wdi/TM.TAX.MRCH.WM.AR.ZS.json", c)
    for y in ys:
        put(f"tf_{c}_{y}", t[y], f"WDI applied tariff, trade-weighted mean, {c} {y}, %")

# ---- US effective tariff rate (BEA customs duties / imports of goods)
cd, mg = Q("fred/B235RC1Q027SBEA.json"), Q("fred/A255RC1Q027SBEA.json")
t = {p: cd[p] / mg[p] * 100 for p in cd if p in mg}
yr = lambda y: sum(t[f"{y}-{m}"] for m in ("01", "04", "07", "10")) / 4
for y in (2000, 2017, 2019, 2024):
    put(f"ut_{y}", yr(y), f"US customs duties / goods imports, annual average of quarters, {y}, %")
pk = max((p for p in t if p >= "2025-01"), key=lambda p: t[p])
qq = lambda p: f"{p[:4]} Q{(int(p[5:7]) - 1) // 3 + 1}"
put("ut_peak", t[pk], "US customs duties / goods imports, highest quarter since 2025, %"); lab("ut_peak_q", qq(pk))
last = max(t)
put("ut_last", t[last], "US customs duties / goods imports, latest quarter, %"); lab("ut_last_q", qq(last))
put("ut_prev_high", max(v for p, v in t.items() if "1975" <= p < "2025"), "highest quarter 1975-2024, %")

# ---- India (fiscal years, plotted at start year)
I = lambda s: {int(y): v for y, v in json.loads((C / f"india/{s}.json").read_text())["data"]["IND"]}
xg, svx, sw, xus, mcn, xgdp = I("exports_goods"), I("services_exports_gross"), I("bop_software_net"), I("exports_to_us"), I("imports_from_china"), I("exports_gs_gdp")
put("in_xg_2000", xg[2000], "India merchandise exports, $bn, 2000-01", 0)
put("in_xg_2024", xg[2024], "India merchandise exports, $bn, 2024-25", 0)
put("in_sv_2006", svx[2006], "India services exports, $bn, 2006-07", 0)
put("in_sv_2025", svx[2025], "India services exports, $bn, 2025-26 (provisional)", 0)
put("in_sw_2025", sw[2025], "India net software services exports, $bn, 2025-26 (provisional)", 0)
put("in_xus_2003", xus[2003], "India exports to US, $bn, 2003-04", 1)
put("in_xus_2025", xus[2025], "India exports to US, $bn, 2025-26 (provisional)", 1)
put("in_mcn_2003", mcn[2003], "India imports from China, $bn, 2003-04", 1)
put("in_mcn_2025", mcn[2025], "India imports from China, $bn, 2025-26 (provisional)", 1)
for y in (2000, 2013, 2019, 2022, 2025):
    put(f"in_xgdp_{y}", xgdp[y], f"India exports of goods and services, % of GDP, FY{y}")
put("svw_IND_2025", A("wdi/BX.GSR.NFSV.CD.json", "IND")[2025] / sv[2025] * 100, "IND services exports, % of world services exports, 2025")
for y in (2008, 2018):
    put(f"in_xus_{y}", xus[y], f"India exports to US, $bn, FY{y}", 1)
    put(f"in_mcn_{y}", mcn[y], f"India imports from China, $bn, FY{y}", 1)
lab("in_mcn_over_xus", next(y for y in sorted(mcn) if y in xus and mcn[y] > xus[y]), "first fiscal year imports from China exceed exports to US")
lab("ut_series_start", 1959, "first year of BEA customs duties series (FRED B235RC1Q027SBEA)")
(C / "derived/theme_trade.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
