"""Derived figures and series for chapters/lens-china.html (Part III, China).
Output: data/clean/derived/lens_china.json and data/js/derived/cn_india.js (China's share of India's merchandise imports,
fiscal years; computed from the Economic Survey / RBI series in data/clean/india).
    .venv/bin/python scripts/derive_lens_china.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


def W(code, area="CHN"):
    d = json.loads((C / f"weo/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def B(code, area="CN"):
    return {t: v for t, v in json.loads((C / f"bis/{code}.json").read_text())["data"][area] if v is not None}


def F(code):
    d = json.loads((C / f"fred/{code}.json").read_text())["data"]
    return {t: v for t, v in list(d.values())[0] if v is not None}


def I(code):
    return {int(t): v for t, v in json.loads((C / f"india/{code}.json").read_text())["data"]["IND"] if v is not None}


def avg(d, y0, y1):
    xs = [d[y] for y in range(y0, y1 + 1)]
    return sum(xs) / len(xs)


def q(t):  # BIS quarter label: '2008-10' -> 2008 Q4
    return f"{t[:4]} Q{(int(t[5:]) - 1) // 3 + 1}"


# ---- growth and inflation (IMF WEO, October 2026; actual data to 2025)
g = W("NGDP_RPCH")
for y in (2000, 2001, 2006, 2007, 2008, 2009, 2010, 2015, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2031):
    put(f"g_{y}", g[y], f"China real GDP growth {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")
put("g_avg_0011", avg(g, 2000, 2011), "China real GDP growth, average 2000-11")
put("g_avg_1219", avg(g, 2012, 2019), "China real GDP growth, average 2012-19")
put("g_avg_2125", avg(g, 2021, 2025), "China real GDP growth, average 2021-25")
put("g_avg_2631", avg(g, 2026, 2031), "China real GDP growth, average 2026-31 (projection)")
gi = W("NGDP_RPCH", "IND")
put("g_ind_avg_1219", avg(gi, 2012, 2019), "India real GDP growth, average 2012-19")
put("g_ind_avg_2125", avg(gi, 2021, 2025), "India real GDP growth, average 2021-25")
p = W("PCPIPCH")
for y in (2002, 2008, 2011, 2023, 2024, 2025, 2026):
    put(f"cpi_{y}", p[y], f"China CPI inflation {y}, annual average", 2)
put("cpi_avg_2325", avg(p, 2023, 2025), "China CPI inflation, average 2023-25", 2)

# ---- saving, investment, the external surplus (WEO, % of GDP)
inv, sav, ca = W("NID_NGDP"), W("NGSD_NGDP"), W("BCA_NGDPD")
for y in (2000, 2025, 2031):
    put(f"inv_{y}", inv[y], f"China gross capital formation, % of GDP, {y}")
pk = max((y for y in inv if 2000 <= y <= 2025), key=inv.get)
put("inv_pk", inv[pk], f"China investment, % of GDP, peak 2000-25 ({pk})"); put("inv_pk_y", pk, "year of that peak", 0)
pk = max((y for y in sav if 2000 <= y <= 2025), key=sav.get)
put("sav_pk", sav[pk], f"China gross national saving, % of GDP, peak 2000-25 ({pk})"); put("sav_pk_y", pk, "year of that peak", 0)
put("sav_2025", sav[2025], "China gross national saving, % of GDP, 2025")
pk = max((y for y in ca if 2000 <= y <= 2025), key=ca.get)
put("ca_pk", ca[pk], f"China current account, % of GDP, peak 2000-25 ({pk})"); put("ca_pk_y", pk, "year of that peak", 0)
lo = min((y for y in ca if 2009 <= y <= 2025), key=ca.get)
put("ca_lo", ca[lo], f"China current account, % of GDP, low 2009-25 ({lo})"); put("ca_lo_y", lo, "year of that low", 0)
for y in (2000, 2025, 2026):
    put(f"ca_{y}", ca[y], f"China current account, % of GDP, {y}")
put("inv_ind_2025", W("NID_NGDP", "IND")[2025], "India gross capital formation, % of GDP, 2025")
put("inv_usa_2025", W("NID_NGDP", "USA")[2025], "US gross capital formation, % of GDP, 2025")

# ---- credit (BIS total credit, % of GDP, quarterly)
for code, k, lab in (("TC_N", "nfc", "non-financial corporations"), ("TC_H", "hh", "households"),
                     ("TC_G", "gov", "general government"), ("TC_P", "priv", "private non-financial sector")):
    s = B(code)
    for t in ("2008-10", "2016-10"):
        put(f"bis_{k}_{t[:4]}", s[t], f"BIS credit to {lab}, % of GDP, {q(t)}")
    last = max(s)
    put(f"bis_{k}_last", s[last], f"BIS credit to {lab}, % of GDP, latest ({q(last)})")
    pkt = max(s, key=s.get)
    put(f"bis_{k}_pk", s[pkt], f"BIS credit to {lab}, % of GDP, peak ({q(pkt)})")
hh = B("TC_H"); put("bis_hh_2006", hh["2006-01"], "BIS credit to households, % of GDP, 2006 Q1")
tot = {t: B("TC_P")[t] + B("TC_G")[t] for t in B("TC_P") if t in B("TC_G")}
for t in ("2008-10", max(tot)):
    put(f"bis_tot_{t[:4]}", tot[t], f"BIS credit to the non-financial sector (private + government), % of GDP, {q(t)}")

# ---- the renminbi (FRED DEXCHUS, yuan per dollar, monthly averages; BIS real effective rate)
fx = {t: v for t, v in F("DEXCHUS").items() if t <= "2026-10"}     # last complete month
put("fx_2005_06", fx["2005-06"], "yuan per dollar, June 2005 average", 4)
put("fx_2008_07", fx["2008-07"], "yuan per dollar, July 2008 average", 4)
lo = min((t for t in fx if "2010" <= t <= "2015-07"), key=fx.get)
put("fx_lo", fx[lo], f"yuan per dollar, strongest month 2010-15 ({lo})", 4)
put("fx_lo_y", int(lo[:4]), "year of that month", 0)
put("fx_2015_07", fx["2015-07"], "yuan per dollar, July 2015 average", 4)
put("fx_2015_09", fx["2015-09"], "yuan per dollar, September 2015 average", 4)
pk = max((t for t in fx if t >= "2016"), key=fx.get)
put("fx_pk", fx[pk], f"yuan per dollar, weakest month since 2016 ({pk})", 4)
put("fx_pk_y", int(pk[:4]), "year of that month", 0)
prev = max(t for t, v in fx.items() if t < pk and v >= fx[pk])
put("fx_pk_since", int(prev[:4]), f"last month before then with a weaker yuan ({prev})", 0)
put("fx_last", fx["2026-10"], "yuan per dollar, October 2026 average", 4)
put("fx_apprec_0514", 100 * (fx["2005-06"] / fx[lo] - 1), "rise in the dollar value of the yuan, June 2005 to its 2010-15 peak, %")
reer = {t: v for t, v in json.loads((C / "bis/EER_R.json").read_text())["data"]["CN"] if v is not None}
put("reer_2005_06", reer["2005-06"], "China real effective exchange rate, June 2005 (2020=100)")
pk = max(reer, key=reer.get)
put("reer_pk", reer[pk], f"China real effective exchange rate, peak ({pk})")
put("reer_rise", 100 * (reer[pk] / reer["2005-06"] - 1), "rise in China's real effective exchange rate, June 2005 to peak, %")
put("reer_last", reer["2026-10"], "China real effective exchange rate, October 2026")
res = {int(t): v for t, v in json.loads((C / "wdi/FI.RES.TOTL.CD.json").read_text())["data"]["CHN"] if v is not None}
for y in (2000, 2025):
    put(f"res_{y}", res[y] / 1e12, f"China total reserves incl. gold, US$ trillion, {y} (WDI)", 2)
pk = max(res, key=res.get); put("res_pk", res[pk] / 1e12, f"China total reserves, peak ({pk}), US$ trillion", 2); put("res_pk_y", pk, "year", 0)

# ---- public finances (WEO)
d, b = W("GGXWDG_NGDP"), W("GGXCNL_NGDP")
for y in (2000, 2007, 2019, 2020, 2025, 2031):
    put(f"debt_{y}", d[y], f"China general government gross debt, % of GDP, {y}")
for y in (2007, 2019, 2025, 2026):
    put(f"bal_{y}", b[y], f"China general government net lending/borrowing, % of GDP, {y}")
put("debt_ind_2025", W("GGXWDG_NGDP", "IND")[2025], "India general government gross debt, % of GDP, 2025")

# ---- size
gd = W("NGDPD"); us = W("NGDPD", "USA")
for y in (2000, 2025):
    put(f"gdpd_{y}", gd[y] / 1000, f"China GDP, current US$ trillion, {y}", 1)
    put(f"gdpd_us_{y}", 100 * gd[y] / us[y], f"China GDP as % of US GDP at market exchange rates, {y}")
pc, pcu, pci = W("PPPPC"), W("PPPPC", "USA"), W("PPPPC", "IND")
for y in (2000, 2025):
    put(f"pc_us_{y}", 100 * pc[y] / pcu[y], f"China GDP per head at PPP as % of US, {y}")
    put(f"pc_ind_{y}", pc[y] / pci[y], f"China GDP per head at PPP, multiple of India's, {y}")

# ---- India and China
im, tot = I("imports_from_china"), I("imports_goods")
share = {y: 100 * im[y] / tot[y] for y in im if y in tot}
reg("cn_india", {"id": "derived/cn_india", "label": "China's share of India's merchandise imports", "unit": "%", "freq": "A",
                 "source": "Computed for this book from India's merchandise imports from China and total merchandise imports (Economic Survey statistical appendices and RBI Handbook of Statistics, via the author's Indian-economy dataset)",
                 "notes": "Indian fiscal years (April–March), plotted at the year in which they start.",
                 "data": {"IND": [[y, round(v, 1)] for y, v in sorted(share.items())]}})
for y in (2003, 2019, 2020, 2024):
    put(f"in_share_{y}", share[y], f"China share of India's merchandise imports, FY{y}-{str(y + 1)[2:]}")
for y in (2003, 2013, 2019, 2020, 2024, 2025):
    put(f"in_imcn_{y}", im[y], f"India's merchandise imports from China, FY{y}-{str(y + 1)[2:]}, US$ bn")
put("in_imcn_mult", im[2024] / im[2003], "imports from China, FY2024-25 as a multiple of FY2003-04", 0)

(C / "derived/lens_china.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
