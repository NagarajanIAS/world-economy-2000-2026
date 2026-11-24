"""Derived figures for chapters/lens-india.html (Part III, India).
Output: data/clean/derived/lens_india.json. WEO India rows are fiscal years (April-March) plotted at the starting year;
the curated India series in data/clean/india/ are on the same convention.
    .venv/bin/python scripts/derive_lens_india.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}
CAP = "2026-10"


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def W(code, area="IND"):
    d = json.loads((C / f"weo/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def WD(code, area="IND"):
    d = json.loads((C / f"wdi/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def I(name):
    d = json.loads((C / f"india/{name}.json").read_text())["data"]
    return {int(t): v for t, v in list(d.values())[0] if v is not None}


def M(path, area="US"):
    d = json.loads((C / f"{path}.json").read_text())["data"][area]
    return {t: v for t, v in d if v is not None and t <= CAP}


def avg(d, y0, y1):
    xs = [d[y] for y in range(y0, y1 + 1)]
    return sum(xs) / len(xs)


def pk(d, y0=2000, y1=2025, lo=False):
    ys = [y for y in d if y0 <= y <= y1]
    return (min if lo else max)(ys, key=d.get)


# ---- growth and inflation (WEO October 2026, fiscal years; actual data to FY2025-26)
g = W("NGDP_RPCH")
for y in (2000, 2002, 2003, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2016, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2031):
    put(f"g_{y}", g[y], f"India real GDP growth FY{y} (WEO Oct 2026{', projection' if y > 2025 else ''})")
for a, b in ((2000, 2025), (2000, 2002), (2003, 2007), (2008, 2010), (2011, 2013), (2014, 2019), (2022, 2025), (2027, 2031)):
    put(f"g_avg_{a % 100:02d}{b % 100:02d}", avg(g, a, b), f"India growth, average FY{a}-FY{b}")
cn, wd = W("NGDP_RPCH", "CHN"), W("NGDP_RPCH", "G001")
for a, b in ((2000, 2025), (2014, 2025), (2022, 2025)):
    put(f"g_cn_avg_{a % 100:02d}{b % 100:02d}", avg(cn, a, b), f"China growth, average {a}-{b}")
    put(f"g_wd_avg_{a % 100:02d}{b % 100:02d}", avg(wd, a, b), f"world growth, average {a}-{b}")
p = W("PCPIPCH")
for y in (2009, 2010, 2013, 2017, 2019, 2022, 2024, 2025, 2026):
    put(f"cpi_{y}", p[y], f"India CPI inflation FY{y} (WEO{', projection' if y > 2025 else ''})")
for a, b in ((2000, 2007), (2008, 2013), (2016, 2019), (2022, 2025)):
    put(f"cpi_avg_{a % 100:02d}{b % 100:02d}", avg(p, a, b), f"India inflation, average FY{a}-FY{b}")
y = pk(p, 2008, 2013); put("cpi_pk_0813", p[y], f"India inflation, peak FY2008-13 (FY{y})"); put("cpi_pk_0813_y", y, "year", 0)

# ---- saving, investment, current account (curated India series: ES/RBI; WEO for the current account)
sv, iv = I("sav_total_gdp"), I("gcf_total_gdp")
for d, k, lab in ((sv, "sav", "gross domestic saving"), (iv, "inv", "gross capital formation")):
    y = pk(d); put(f"{k}_pk", d[y], f"India {lab}, % of GDP, peak (FY{y})"); put(f"{k}_pk_y", y, "year", 0)
    put(f"{k}_2000", d[2000], f"India {lab}, % of GDP, FY2000")
    put(f"{k}_last", d[max(d)], f"India {lab}, % of GDP, FY{max(d)}"); put(f"{k}_last_y", max(d), "year", 0)
ca = I("cab_gdp")
y = pk(ca, lo=True); put("ca_lo", ca[y], f"India current account, % of GDP, lowest (FY{y})"); put("ca_lo_y", y, "year", 0)
for yy in (2003, 2025):
    put(f"ca_{yy}", ca[yy], f"India current account, % of GDP, FY{yy}")
fx = I("fx_reserves")
for yy in (2000, 2007, 2013, 2025):
    put(f"res_{yy}", fx[yy], f"India foreign exchange reserves, US$ bn, end-March of FY{yy}", 0)
ic = I("import_cover_months"); put("cover_2025", ic[2025], "India import cover of reserves, months, FY2025")
r = I("inr_usd")
for yy in (2000, 2007, 2013, 2025):
    put(f"inr_{yy}", r[yy], f"rupees per US dollar, FY{yy} average", 2)
dx = M("fred/DEXINUS")
put("inr_m_last", dx[CAP], "rupees per US dollar, October 2026 average (FRED)", 2)

# ---- RBI and prices (curated series)
rp = I("repo_end")
for yy in (2008, 2013, 2019, 2020, 2022, 2025):
    put(f"repo_{yy}", rp[yy], f"RBI repo rate at end of FY{yy}", 2)
cc = I("cpi_inflation")
put("cpic_avg_1215", avg(cc, 2012, 2015), "India CPI (combined) inflation, average FY2012-15")
put("cpic_avg_1619", avg(cc, 2016, 2019), "India CPI (combined) inflation, average FY2016-19")
put("cpic_2024", cc[2024], "India CPI (combined) inflation, FY2024")

# ---- public finances (WEO; general government)
db, bl = W("GGXWDG_NGDP"), W("GGXCNL_NGDP")
for yy in (2001, 2007, 2010, 2019, 2020, 2025, 2031):
    put(f"debt_{yy}", db[yy], f"India general government gross debt, % of GDP, FY{yy}")
for yy in (2001, 2007, 2008, 2019, 2020, 2025, 2031):
    put(f"bal_{yy}", bl[yy], f"India general government net lending, % of GDP, FY{yy}")
y = pk(db); put("debt_pk", db[y], f"India gross debt peak (FY{y})"); put("debt_pk_y", y, "year", 0)

# ---- trade and credit (curated series)
ex = I("exports_gs_gdp")
y = pk(ex); put("exgdp_pk", ex[y], f"India exports of goods and services, % of GDP, peak (FY{y})"); put("exgdp_pk_y", y, "year", 0)
put("exgdp_2000", ex[2000], "India exports of goods and services, % of GDP, FY2000"); put("exgdp_2025", ex[2025], "same, FY2025")
se = I("services_exports_gross"); put("svc_2025", se[2025], "India gross services exports, US$ bn, FY2025", 0); put("svc_2006", se[2006], "same, FY2006", 0)
sw = I("bop_software_net"); put("soft_2025", sw[2025], "India net software services exports, US$ bn, FY2025", 0)
cr = I("scb_credit_gdp"); put("credit_2001", cr[2001], "scheduled commercial bank credit, % of GDP, FY2001"); put("credit_2025", cr[2025], "same, FY2025")
y = pk(cr, 2005, 2020); put("credit_pk_0520", cr[y], f"bank credit, % of GDP, peak FY2005-20 (FY{y})"); put("credit_pk_0520_y", y, "year", 0)

# ---- poverty and income (World Bank WDI)
pv = WD("SI.POV.DDAY")
for yy in (2004, 2011, 2022, 2023):
    put(f"pov_{yy}", pv[yy], f"India population below $3.00 a day (2021 PPP), %, {yy} (WDI)")
pc, pw, pcn = WD("NY.GDP.PCAP.PP.KD"), WD("NY.GDP.PCAP.PP.KD", "WLD"), WD("NY.GDP.PCAP.PP.KD", "CHN")
for yy in (2000, 2025):
    put(f"pc_{yy}", pc[yy], f"India GDP per person, PPP constant 2021 $, {yy} (WDI)", 0)
    put(f"pc_wld_pct_{yy}", 100 * pc[yy] / pw[yy], f"India GDP per person as % of world average, {yy}", 0)
    put(f"pc_chn_pct_{yy}", 100 * pc[yy] / pcn[yy], f"India GDP per person as % of China's, {yy}", 0)
put("pc_x_0025", pc[2025] / pc[2000], "India GDP per person (PPP), 2025 as a multiple of 2000", 1)

# ---- India in the world
sh = W("PPPSH")
for a, k in (("IND", "in"), ("CHN", "cn"), ("USA", "us"), ("JPN", "jp")):
    for yy in (2000, 2025, 2031):
        put(f"ppp_{k}_{yy}", sh[yy] if a == "IND" else W("PPPSH", a)[yy], f"{a} share of world GDP at PPP, %, {yy} (WEO)")
nd = json.loads((C / "weo/NGDPD.json").read_text())["data"]


def rank(yy):
    vals = sorted(((v, a) for a, s in nd.items() if len(a) == 3 and not any(ch.isdigit() for ch in a) and not a.startswith("GX") for t, v in s if int(t) == yy and v), reverse=True)
    return [a for v, a in vals].index("IND") + 1


for yy in (2000, 2010, 2019, 2022, 2024, 2025, 2026, 2027, 2028, 2031):
    put(f"rank_{yy}", rank(yy), f"India's rank by GDP at market exchange rates, {yy} (WEO Oct 2026; fiscal year)", 0)
ngd = W("NGDPD")
put("gdpd_2000", ngd[2000] / 1e3, "India GDP, US$ trillion, FY2000", 2); put("gdpd_2025", ngd[2025] / 1e3, "India GDP, US$ trillion, FY2025", 2)
put("gdpd_2031", ngd[2031] / 1e3, "India GDP, US$ trillion, FY2031 (projection)", 2)
svx = WD("BX.GSR.NFSV.CD"); swl = WD("BX.GSR.NFSV.CD", "WLD"); scn = WD("BX.GSR.NFSV.CD", "CHN")
shr = {yy: 100 * svx[yy] / swl[yy] for yy in svx if yy in swl}
shc = {yy: 100 * scn[yy] / swl[yy] for yy in scn if yy in swl}
for yy in (2000, 2010, 2025):
    put(f"svcsh_{yy}", shr[yy], f"India share of world services exports, %, {yy} (WDI BX.GSR.NFSV.CD)", 2)
put("svcsh_cn_2025", shc[2025], "China share of world services exports, %, 2025 (WDI)", 2)
first = min(yy for yy in shr if yy in shc and shr[yy] > shc[yy] and all(shr[z] > shc[z] for z in shr if z >= yy and z in shc))
put("svcsh_pass_y", first, "first year from which India's share of world services exports stays above China's (WDI)", 0)
gx = WD("TX.VAL.MRCH.CD.WT"); gw = WD("TX.VAL.MRCH.CD.WT", "WLD")
for yy in (2000, max(y for y in gx if y in gw)):
    put(f"gxsh_{yy}", 100 * gx[yy] / gw[yy], f"India share of world merchandise exports, %, {yy} (WDI)", 2)

(C / "derived/lens_india.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
