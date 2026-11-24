"""Derived figures quoted in chapters/phase-2.html. Output: data/clean/derived/phase2.json.
Each entry: value and how it was computed, so check_numbers.py can verify the prose.
    python3 scripts/derive_phase2.py
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}


def S(path, area=None):
    d = json.loads((C / path).read_text())["data"]
    return {(int(k) if isinstance(k, int) or str(k).isdigit() else k): v for k, v in (d[area] if area else next(iter(d.values())))}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:26s} {round(v, nd):>10}  {how}")


ind = lambda sid: {int(y): v for y, v in json.loads((C / f"india/{sid}.json").read_text())["data"]["IND"]}
w = lambda i, a: S(f"weo/{i}.json", a)

# ---- growth (WEO Oct 2026)
for a in ["G001", "G110", "G200", "USA", "CHN", "IND", "G163", "JPN"]:
    d = w("NGDP_RPCH", a)
    put(f"gdp_{a}_avg0307", sum(d[y] for y in range(2003, 2008)) / 5, f"WEO NGDP_RPCH {a}, average of 2003–2007")
    for y in (2002, 2003, 2007):
        put(f"gdp_{a}_{y}", d[y], f"WEO NGDP_RPCH {a} {y}")
put("gdp_G001_avg9002", sum(w("NGDP_RPCH", "G001")[y] for y in range(1990, 2003)) / 13, "WEO NGDP_RPCH G001, average of 1990–2002")
# share of world growth: EMDE growth contribution needs weights; stated in text only via IMF quote

# ---- current accounts (US$ bn and % GDP)
for a in ["USA", "CHN", "DEU", "JPN", "SAU", "RUS", "IND", "G001"]:
    d = w("BCA", a)
    for y in (2002, 2006, 2007, 2008):
        put(f"bca_{a}_{y}", d[y], f"WEO BCA {a} {y}, US$ bn", 0)
for a in ["USA", "CHN", "DEU", "JPN", "IND"]:
    d = w("BCA_NGDPD", a)
    for y in (2002, 2006, 2007):
        put(f"ca_{a}_{y}", d[y], f"WEO BCA_NGDPD {a} {y}, % of GDP")

# ---- commodity prices (WEO annual indices) and Brent
for i, nm in [("PNRGW", "energy"), ("PMETAW", "metals"), ("PFOODW", "food"), ("POILBRE", "brent")]:
    d = w(i, "G001")
    put(f"{nm}_2002", d[2002], f"WEO {i} 2002", 2 if nm == "brent" else 1)
    put(f"{nm}_2008", d[2008], f"WEO {i} 2008", 2 if nm == "brent" else 1)
    put(f"{nm}_x0208", d[2008] / d[2002], f"WEO {i}: 2008 ÷ 2002")
    put(f"{nm}_x0207", d[2007] / d[2002], f"WEO {i}: 2007 ÷ 2002")

# ---- reserves (WDI, US$ bn, end-year)
r = json.loads((C / "wdi/FI.RES.TOTL.CD.json").read_text())["data"]
for a in ["CHN", "JPN", "IND", "RUS", "SAU", "KOR"]:
    d = {int(k): v for k, v in r[a]}
    for y in (2002, 2007, 2008):
        put(f"res_{a}_{y}", d[y] / 1e9, f"WDI FI.RES.TOTL.CD {a} {y}, US$ bn (end-year, incl. gold)", 0)

# ---- US housing and household credit
hp = S("fred/CSUSHPINSA.json", "US")
pk = max(((k, v) for k, v in hp.items() if k < "2008"), key=lambda x: x[1])
put("us_hp_rise", (pk[1] / hp["2000-01"] - 1) * 100, f"Case-Shiller US National (FRED CSUSHPINSA), Jan 2000 to peak {pk[0]}", 0)
put("us_hp_rise_0206", (pk[1] / hp["2002-01"] - 1) * 100, f"Case-Shiller US National, Jan 2002 to peak {pk[0]}", 0)
th = S("bis/TC_H.json", "US")
put("us_hh_credit_2000", th["2000-01"], "BIS WS_TC household credit, US, % of GDP, 2000 Q1")
q = max((k for k in th if k.startswith("2007")))
put("us_hh_credit_2007", th[q], f"BIS WS_TC household credit, US, % of GDP, {q[:4]} Q4")
for a, lab in [("GB", "uk"), ("ES", "spain")]:
    t = S("bis/TC_H.json", a)
    put(f"{lab}_hh_credit_2000", t["2000-01"], f"BIS WS_TC household credit, {a}, % of GDP, 2000 Q1")
    put(f"{lab}_hh_credit_2007", t[max(k for k in t if k.startswith("2007"))], f"BIS WS_TC household credit, {a}, % of GDP, 2007 Q4")

# ---- interest rates (FRED monthly averages)
ff = S("fred/FEDFUNDS.json", "US")
put("ff_2003_low", min(v for k, v in ff.items() if "2003" <= k < "2005"), "FRED FEDFUNDS, lowest monthly average 2003–04", 2)
put("ff_2006_high", max(v for k, v in ff.items() if "2006" <= k < "2008"), "FRED FEDFUNDS, highest monthly average 2006–07", 2)
t10 = S("fred/DGS10.json", "US")
put("t10_2004_06", t10["2004-06"], "FRED DGS10, monthly average June 2004", 2)
put("t10_2005_06", t10["2005-06"], "FRED DGS10, monthly average June 2005", 2)


# ---- policy rates (BIS WS_CBPOL, monthly, end of period)
cb = json.loads((C / "bis/CBPOL.json").read_text())["data"]
us, rbi = dict(cb["US"]), dict(cb["IN"])
put("fed_2003_07", us["2003-07"], "BIS WS_CBPOL US, Jul 2003 (target held from Jun 2003 to May 2004)", 2)
put("fed_2006_07", us["2006-07"], "BIS WS_CBPOL US, Jul 2006 (reached Jun 2006, held to Aug 2007)", 2)
put("rbi_2004_10", rbi["2004-10"], "BIS WS_CBPOL IN, Oct 2004", 2)
put("rbi_2008_03", rbi["2008-03"], "BIS WS_CBPOL IN, Mar 2008", 2)

# ---- India (author's dataset; fiscal years plotted at start year)
put("in_gdp04_avg0307", sum(ind("gdpfc_growth_2004")[y] for y in range(2003, 2008)) / 5, "India GDP at factor cost, 2004-05 base, average FY2003-04 to FY2007-08")
put("in_gdp11_avg0307", sum(ind("gdp_real_growth")[y] for y in range(2003, 2008)) / 5, "India real GDP, 2011-12 base (back series), average FY2003-04 to FY2007-08")
for y in (2005, 2006, 2007):
    put(f"in_gdp04_{y}", ind("gdpfc_growth_2004")[y], f"India GDP at factor cost growth, 2004-05 base, FY{y}-{str(y+1)[2:]}")
put("in_gdp11_2006", ind("gdp_real_growth")[2006], "India real GDP growth, 2011-12 base back series, FY2006-07")
put("in_gdp_2002", ind("gdp_real_growth")[2002], "India real GDP growth, 2011-12 base, FY2002-03")
for s, lab in [("gfcf_gdp", "gfcf"), ("sav_total_gdp", "sav"), ("scb_credit_gdp", "credit"), ("exports_gs_gdp", "xgs"), ("mcap_bse_gdp", "mcap")]:
    d = ind(s)
    put(f"in_{lab}_2002", d[2002], f"India {s} FY2002-03, % of GDP")
    put(f"in_{lab}_2003", d[2003], f"India {s} FY2003-04, % of GDP")
    put(f"in_{lab}_2007", d[2007], f"India {s} FY2007-08, % of GDP")
for s, lab in [("fx_reserves", "res"), ("exports_goods", "exp"), ("oil_imports", "oil"), ("bop_fi", "fi"), ("imports_from_china", "chinaimp")]:
    d = ind(s)
    for y in (2002, 2003, 2007):
        if y in d:
            put(f"in_{lab}_{y}", d[y], f"India {s} FY{y}-{str(y+1)[2:]}, US$ bn", 1)
put("in_fpi_2007", ind("fpi_net")[2007], "India net portfolio investment FY2007-08, US$ bn")
put("in_fdi_2007", ind("fdi_net")[2007], "India net FDI FY2007-08, US$ bn")
put("in_fdi_2004", ind("fdi_net")[2004], "India net FDI FY2004-05, US$ bn")
put("in_svc_2007", ind("services_exports_gross")[2007], "India gross services exports FY2007-08, US$ bn")
put("in_sensex_x", ind("sensex_avg")[2007] / ind("sensex_avg")[2002], "BSE Sensex, FY2007-08 average ÷ FY2002-03 average")
put("in_sensex_2002", ind("sensex_avg")[2002], "BSE Sensex average FY2002-03", 0)
put("in_sensex_2007", ind("sensex_avg")[2007], "BSE Sensex average FY2007-08", 0)
put("in_inr_2002", ind("inr_usd")[2002], "Rupees per US dollar, FY2002-03 average", 1)
put("in_inr_2007", ind("inr_usd")[2007], "Rupees per US dollar, FY2007-08 average", 1)
for s, lab in [("centre_fd_gdp", "cfd"), ("gg_fd_gdp", "ggfd"), ("gg_debt_gdp", "ggdebt"), ("cab_gdp", "cab")]:
    d = ind(s)
    for y in (2002, 2003, 2007):
        put(f"in_{lab}_{y}", d[y], f"India {s} FY{y}-{str(y+1)[2:]}, % of GDP")
put("in_wpi_2007", ind("wpi_inflation")[2007], "India WPI inflation FY2007-08 (2004-05 base)")
put("in_cpi_2007", ind("cpi_iw_inflation")[2007], "India CPI-IW inflation FY2007-08")

(C / "derived/phase2.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures written to data/clean/derived/phase2.json")
