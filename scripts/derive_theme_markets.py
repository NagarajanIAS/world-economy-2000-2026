"""Derived figures and series for chapters/theme-markets.html.
Output: data/clean/derived/theme_markets.json, data/js/derived/tm_flows.js (net capital flows to emerging and developing
economies, % of their GDP, WEO), data/js/derived/tm_inusd.js (Indian share prices in rupees and in US dollars, Jan 2000 = 100).
    .venv/bin/python scripts/derive_theme_markets.py
"""
import json
import statistics
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
M = lambda p, a="US": dict(J(p)["data"][a])                       # monthly or annual series -> {period: value}
W = lambda p: {a: dict(v) for a, v in J(p)["data"].items()}
avg = lambda d, a, b: sum(d[y] for y in range(a, b + 1)) / (b - a + 1)

# ---- share prices (OECD MEI via FRED, monthly, local currency, price index), Jan 2000 = 100
IDX = {"US": "USA", "JP": "JPN", "DE": "DEU", "GB": "GBR", "CN": "CHN", "BR": "BRA", "KR": "KOR", "IN": "IND"}
for k, a in IDX.items():
    s = M(f"fred/SPASTT01{k}M661N.json"); b = s["2000-01"]
    r = lambda m: 100 * s[m] / b
    pk = max((m for m in s if "2006" <= m <= "2008-06"), key=lambda m: s[m])
    tr = min((m for m in s if "2008-06" <= m <= "2009-12"), key=lambda m: s[m])
    put(f"ix_{a}_pk07", r(pk), f"share prices {a}, 2006-08 peak month ({pk}), Jan 2000 = 100", 0); lab(f"ix_{a}_pk07_m", pk)
    put(f"ix_{a}_tr09", r(tr), f"share prices {a}, 2008-09 trough month ({tr}), Jan 2000 = 100", 0); lab(f"ix_{a}_tr09_m", tr)
    put(f"ix_{a}_fall", 100 * (s[tr] / s[pk] - 1), f"share prices {a}, % change peak {pk} to trough {tr} (monthly averages)", 0)
    for m in ("2002-12", "2007-12", "2019-12", "2020-03", "2021-12", "2024-12", "2025-12", "2026-10"):
        put(f"ix_{a}_{m[:4]}{'m3' if m == '2020-03' else ''}", r(m), f"share prices {a}, {m}, Jan 2000 = 100", 0)
    lab(f"ix_{a}_last", max(s), "last month of data")

# Indian share prices in dollars (rupee index divided by the rupee-dollar rate, both monthly averages)
inr = M("fred/DEXINUS.json"); si = M("fred/SPASTT01INM661N.json")
mons = [m for m in sorted(si) if m >= "2000-01" and m in inr]
usd = {m: si[m] / inr[m] for m in mons}
put("inr_2000_01", inr["2000-01"], "rupees per US dollar, Jan 2000 (monthly average)", 2)
put("inr_2026_10", inr["2026-10"], "rupees per US dollar, Oct 2026 (monthly average)", 2)
put("ixusd_IND_2026", 100 * usd["2026-10"] / usd["2000-01"], "Indian share prices in US dollars, Oct 2026, Jan 2000 = 100", 0)
put("ixusd_IND_2007", 100 * usd["2007-12"] / usd["2000-01"], "Indian share prices in US dollars, Dec 2007, Jan 2000 = 100", 0)
obj = {"id": "derived/tm_inusd", "source": "OECD Main Economic Indicators and Federal Reserve (DEXINUS), via FRED",
       "code": "FRED SPASTT01INM661N, DEXINUS", "label": "Indian share prices in rupees and in US dollars, Jan 2000 = 100",
       "unit": "index, Jan 2000 = 100", "freq": "M", "url": "https://fred.stlouisfed.org/series/SPASTT01INM661N", "retrieved": "2026-11-23",
       "notes": "Rupee index: OECD share price index for India. Dollar index: the same divided by the monthly average rupee-dollar rate. Prices only, no dividends.",
       "data": {"INR": [[m, round(100 * si[m] / si["2000-01"], 2)] for m in mons],
                "USD": [[m, round(100 * usd[m] / usd["2000-01"], 2)] for m in mons]}}
(ROOT / "data/js/derived/tm_inusd.js").write_text(f'WE.register("derived/tm_inusd",{json.dumps(obj, separators=(",", ":"))});\n')

# ---- Nasdaq and the dot-com bust
nas = M("fred/NASDAQCOM.json")
put("nas_2000_03", nas["2000-03"], "Nasdaq Composite, Mar 2000 monthly average", 0)
lo = min((m for m in nas if "2001" <= m <= "2003-12"), key=lambda m: nas[m]); put("nas_lo", nas[lo], f"Nasdaq low monthly average ({lo})", 0); lab("nas_lo_m", lo)
put("nas_fall", 100 * (nas[lo] / nas["2000-03"] - 1), "Nasdaq % change Mar 2000 to low", 0)
back = next(m for m in sorted(nas) if m > "2003" and nas[m] > nas["2000-03"]); lab("nas_back_m", back, "first month Nasdaq monthly average above Mar 2000")

# ---- CAPE (Shiller)
cape = M("shiller/CAPE.json")
for lab_, a, b in (("1999", "1999-01", "2000-12"), ("2009", "2008-06", "2009-12"), ("2021", "2021-01", "2022-06"), ("2026", "2025-01", "2026-12")):
    f = max if lab_ != "2009" else min
    m = f((m for m in cape if a <= m <= b), key=lambda m: cape[m])
    put(f"cape_{lab_}", cape[m], f"CAPE {'low' if lab_ == '2009' else 'high'} in {a}..{b} ({m})", 1); lab(f"cape_{lab_}_m", m)
m29 = max((m for m in cape if "1928" <= m <= "1929-12"), key=lambda m: cape[m]); put("cape_1929", cape[m29], f"CAPE high 1928-29 ({m29})", 1)
put("cape_mean", statistics.mean(cape.values()), "CAPE mean, all months from 1881", 1)
put("cape_mean_1950", statistics.mean(v for m, v in cape.items() if m >= "1950"), "CAPE mean, months from 1950", 1)
lab("cape_last_m", max(cape)); put("cape_last", cape[max(cape)], "CAPE, last month")
put("cape_n_above_now", sum(1 for v in cape.values() if v > cape[max(cape)]), "months since 1881 with CAPE above the latest", 0)

# ---- VIX (monthly averages of daily close)
vix = M("fred/VIXCLS.json")
for m in ("2008-10", "2008-11", "2020-03", "2025-04", "2022-03", "2026-03", "2026-04", "2026-10"):
    if m in vix:
        put(f"vix_{m.replace('-', '_')}", vix[m], f"VIX monthly average {m}", 0)
put("vix_mean", statistics.mean(vix.values()), "VIX average of monthly averages, 1990 onwards", 0)

# ---- market value: WDI, % of GDP and US$ (2025 left out: the WDI India figure doubles in one year, see NOTES)
mc, mcd = W("wdi/CM.MKT.LCAP.GD.ZS.json"), W("wdi/CM.MKT.LCAP.CD.json")
for a in ("WLD", "USA", "IND", "CHN", "JPN", "DEU", "BRA", "KOR", "ZAF", "LMY"):
    for y in (2000, 2003, 2007, 2008, 2019, 2020, 2021, 2024):
        if y in mc.get(a, {}):
            put(f"mc_{a}_{y}", mc[a][y], f"market capitalisation of listed domestic companies, % of GDP, {a} {y} (WDI)", 0)
        if y in mcd.get(a, {}) and y in mcd["WLD"]:
            put(f"mcs_{a}_{y}", 100 * mcd[a][y] / mcd["WLD"][y], f"{a} share of world market capitalisation, % {y} (WDI, US$)", 1)
            put(f"mcd_{a}_{y}", mcd[a][y] / 1e12, f"market capitalisation, US$ trillion, {a} {y} (WDI)", 1)
for y in (2025,):
    put(f"mcd_IND_{y}", mcd["IND"][y] / 1e12, f"WDI India market capitalisation, US$ trillion, {y} (looks wrong: doubles in a year)", 1)

# ---- capital flows to emerging and developing economies (WEO, group G200): net inflows = -(assets - liabilities)
G = "G200"
gdp = dict(J("weo/NGDPD.json")["data"][G])
F = {c: dict(J(f"weo/{c}.json")["data"][G]) for c in ("BF", "BFD", "BFP", "BFO", "BFRA")}
yrs = [y for y in range(2000, 2032) if all(y in F[c] for c in F) and y in gdp]
pct = lambda c, y, sgn=-1: sgn * 100 * F[c][y] / gdp[y]
ser = {"fdi": [[str(y), round(pct("BFD", y), 2)] for y in yrs], "port": [[str(y), round(pct("BFP", y), 2)] for y in yrs],
       "other": [[str(y), round(pct("BFO", y), 2)] for y in yrs], "res": [[str(y), round(pct("BFRA", y, 1), 2)] for y in yrs]}
la = J("weo/BFD.json").get("last_actual", {})
obj = {"id": "derived/tm_flows", "source": "IMF, World Economic Outlook database, October 2026",
       "code": "IMF.RES,WEO BFD, BFP, BFO, BFRA, NGDPD (group G200)", "label": "Emerging market and developing economies: net capital flows, % of GDP",
       "unit": "% of GDP", "freq": "A", "vintage": "WEO Oct 2026 (published 2026-10-13)",
       "url": "https://api.imf.org/external/sdmx/2.1/data/IMF.RES,WEO/", "retrieved": "2026-11-23",
       "notes": "Net inflows are liabilities less assets (the WEO series with the sign reversed): a positive value means foreigners invested more in these economies than their residents invested abroad. Reserve accumulation is the change in official reserve assets (positive = reserves rising). Values from 2026 are IMF projections.",
       "data": ser}
(ROOT / "data/js/derived/tm_flows.js").write_text(f'WE.register("derived/tm_flows",{json.dumps(obj, separators=(",", ":"))});\n')
for y in (2000, 2003, 2006, 2007, 2008, 2009, 2010, 2013, 2015, 2016, 2019, 2020, 2021, 2022, 2024, 2025, 2026):
    put(f"fl_fdi_{y}", pct("BFD", y), f"EMDE net FDI inflows, % of GDP, {y}", 1)
    put(f"fl_port_{y}", pct("BFP", y), f"EMDE net portfolio inflows, % of GDP, {y}", 1)
    put(f"fl_res_{y}", pct("BFRA", y, 1), f"EMDE reserve accumulation, % of GDP, {y}", 1)
    put(f"flb_res_{y}", F["BFRA"][y], f"EMDE reserve accumulation, US$ billion, {y}", 0)
    put(f"flb_port_{y}", -F["BFP"][y], f"EMDE net portfolio inflows, US$ billion, {y}", 0)
    put(f"flb_fdi_{y}", -F["BFD"][y], f"EMDE net FDI inflows, US$ billion, {y}", 0)
put("fl_fdi_avg_2000_2025", avg({y: pct("BFD", y) for y in yrs}, 2000, 2025), "EMDE net FDI inflows, % of GDP, average 2000-2025")
put("flb_res_2003_2008", sum(F["BFRA"][y] for y in range(2003, 2009)) / 1000, "EMDE reserve accumulation, cumulative 2003-2008, US$ trillion", 1)

# ---- India (fiscal years)
I = lambda p: dict(J(f"india/{p}.json")["data"]["IND"])
fdi, fpi, mcb, sx, res = I("fdi_net"), I("fpi_net"), I("mcap_bse_gdp"), I("sensex_avg"), I("fx_reserves")
for y in sorted(fdi):
    put(f"ifdi_{y}", fdi[y], f"India net FDI, US$ bn, FY{y}-{(y + 1) % 100:02d} (RBI HBS Table 143)")
    put(f"ifpi_{y}", fpi[y], f"India net portfolio investment, US$ bn, FY{y}-{(y + 1) % 100:02d} (RBI HBS Table 143)")
put("ifdi_2015_2021_avg", avg(fdi, 2015, 2021), "India net FDI, average FY2015-16 to FY2021-22, US$ bn")
put("ifpi_n_neg", sum(1 for v in fpi.values() if v < 0), "fiscal years 2004-05 to 2025-26 with net portfolio outflow", 0)
lab("ifpi_neg_yrs", [y for y in sorted(fpi) if fpi[y] < 0], "start years of fiscal years with net portfolio outflow")
for y in (2001, 2002, 2007, 2008, 2009, 2019, 2020, 2023, 2024, 2025):
    put(f"imc_{y}", mcb[y], f"BSE market capitalisation, end-March, % of GDP, FY{y}-{(y + 1) % 100:02d}", 0)
for y in (2001, 2002, 2007, 2008, 2019, 2024, 2025):
    put(f"isx_{y}", sx[y], f"Sensex annual average, FY{y}-{(y + 1) % 100:02d}", 0)
put("isx_x_2001_2025", sx[2025] / sx[2001], "Sensex annual average FY2025-26 / FY2001-02", 0)
for y in (2007, 2008, 2013, 2024, 2025):
    put(f"ires_{y}", res[y], f"India FX reserves, end-March, US$ bn, FY{y}-{(y + 1) % 100:02d}", 0)

(C / "derived/theme_markets.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
