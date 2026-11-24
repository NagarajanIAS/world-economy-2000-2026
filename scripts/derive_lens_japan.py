"""Derived figures and series for chapters/lens-japan.html (Part III, Japan).
Output: data/clean/derived/lens_japan.json and data/js/derived/jp_inr.js (rupees per 100 yen, monthly, computed from
FRED DEXINUS and DEXJPUS).
    .venv/bin/python scripts/derive_lens_japan.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}
CAP = "2026-10"   # last complete month


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


def W(code, area="JPN"):
    d = json.loads((C / f"weo/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def WD(code, area="JPN"):
    d = json.loads((C / f"wdi/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def M(path, area=None):
    d = json.loads((C / f"{path}.json").read_text())["data"]
    s = d[area] if area else list(d.values())[0]
    return {t: v for t, v in s if v is not None and t <= CAP}


def avg(d, y0, y1):
    xs = [d[y] for y in range(y0, y1 + 1)]
    return sum(xs) / len(xs)


def mname(t):
    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][int(t[5:]) - 1] + " " + t[:4]


# ---- growth, inflation, unemployment (WEO October 2026; actual data to 2025)
g = W("NGDP_RPCH")
for y in (2000, 2002, 2007, 2008, 2009, 2010, 2011, 2014, 2019, 2020, 2021, 2024, 2025, 2026, 2031):
    put(f"g_{y}", g[y], f"Japan real GDP growth {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")
put("g_avg_0007", avg(g, 2000, 2007), "Japan growth, average 2000-07")
put("g_avg_1019", avg(g, 2010, 2019), "Japan growth, average 2010-19")
put("g_avg_2125", avg(g, 2021, 2025), "Japan growth, average 2021-25")
put("g_avg_2731", avg(g, 2027, 2031), "Japan growth, average 2027-31 (projection)")
r = W("NGDP_R")
put("lvl_25v07", 100 * (r[2025] / r[2007] - 1), "Japan real GDP 2025 vs 2007, % change")
put("lvl_25v00", 100 * (r[2025] / r[2000] - 1), "Japan real GDP 2025 vs 2000, % change")
lp = W("LP")
rpc = {y: r[y] / lp[y] for y in r if y in lp}
put("lvlpc_25v00", 100 * (rpc[2025] / rpc[2000] - 1), "Japan real GDP per person 2025 vs 2000, % change (NGDP_R / LP)")
us = W("NGDP_R", "USA"); usl = W("LP", "USA")
put("us_lvlpc_25v00", 100 * ((us[2025] / usl[2025]) / (us[2000] / usl[2000]) - 1), "US real GDP per person 2025 vs 2000, % change")
p = W("PCPIPCH")
for y in (2000, 2008, 2009, 2010, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024, 2025, 2026):
    put(f"cpi_{y}", p[y], f"Japan CPI inflation {y}, annual average (WEO{', projection' if y > 2025 else ''})")
neg = [y for y in range(2000, 2013) if round(p[y], 1) < 0]; print("   falling-price years", neg)
put("cpi_neg_yrs_0012", len(neg), "years with falling consumer prices, 2000-12", 0)
put("cpi_avg_0012", avg(p, 2000, 2012), "Japan inflation, average 2000-12")
put("cpi_avg_1321", avg(p, 2013, 2021), "Japan inflation, average 2013-21")
put("cpi_avg_2225", avg(p, 2022, 2025), "Japan inflation, average 2022-25")
u = W("LUR")
pk = max((y for y in u if 2000 <= y <= 2025), key=u.get)
put("lur_pk", u[pk], f"Japan unemployment rate, peak 2000-25 ({pk})"); put("lur_pk_y", pk, "year of that peak", 0)
for y in (2009, 2019, 2025):
    put(f"lur_{y}", u[y], f"Japan unemployment rate {y}")

# ---- policy rate (BIS, end of month) and 10-year JGB yield (FRED / OECD MEI, monthly)
pr = M("bis/CBPOL", "JP")
for t in ("2000-08", "2001-03", "2006-07", "2007-02", "2008-12", "2010-10", "2016-09", "2024-03", "2024-08", "2025-01", "2025-12", "2026-06", CAP):
    put(f"pr_{t.replace('-', '_')}", pr[t], f"BOJ policy rate (BIS), end of {mname(t)}", 2)
gaps = [t for t in ("2001-04", "2006-02", "2013-05", "2016-08") if t not in pr]
print("   BIS gaps confirmed at", gaps)
chg = [t for t in sorted(pr) if t >= "2024-01" and pr[t] != pr[max(k for k in pr if k < t)]]
print("   policy-rate changes since 2024:", [(t, pr[t]) for t in chg])
y10 = M("fred/IRLTLT01JPM156N")
for t in ("2000-01", "2007-06", "2012-12", "2016-07", "2022-12", "2024-03", "2025-01", CAP):
    put(f"y10_{t.replace('-', '_')}", y10[t], f"10-year JGB yield, {mname(t)}", 2)
lo = min((t for t in y10 if t >= "2000-01"), key=y10.get)
put("y10_lo", y10[lo], f"10-year JGB yield, lowest month ({lo})", 2); out["y10_lo"]["month"] = mname(lo)
put("y10_neg_months", sum(1 for v in y10.values() if v < 0), "months with a negative 10-year yield", 0)
hi = max((t for t in y10 if t >= "2000-01"), key=y10.get)
put("y10_hi", y10[hi], f"10-year JGB yield, highest month since 2000 ({hi})", 2)
y10a = dict(json.loads((C / "fred/IRLTLT01JPM156N.json").read_text())["data"]["US"])
put("y10_above3_prev_y", int(max(t for t, v in y10a.items() if v is not None and v > 3 and t < "2026-09")[:4]), "last year before September 2026 with a monthly 10-year yield above 3%", 0)

# ---- BOJ balance sheet (FRED JPNASSETS, 100 million yen) against nominal GDP (WEO NGDP, yen billion)
bs = M("fred/JPNASSETS")
ng = W("NGDP")
T = lambda t: bs[t] / 1e4  # yen trillion
for t in ("2001-03", "2006-03", "2012-12", "2013-03", "2016-09", "2020-03", "2024-03", CAP):
    put(f"bs_{t.replace('-', '_')}", T(t), f"BOJ total assets, ¥ trillion, {mname(t)}", 0)
pk = max(bs, key=bs.get); put("bs_pk", T(pk), f"BOJ total assets, peak (¥ trillion, {pk})", 0); put("bs_pk_y", int(pk[:4]), "year", 0)
ratio = {t: 100 * T(t) / (ng[int(t[:4])] / 1e3) for t in bs if int(t[:4]) in ng}
for t in ("2012-12", CAP):
    put(f"bsgdp_{t.replace('-', '_')}", ratio[t], f"BOJ total assets as % of that year's nominal GDP, {mname(t)}", 0)
rk = max(ratio, key=ratio.get); put("bsgdp_pk", ratio[rk], f"BOJ assets / nominal GDP, peak ({rk})", 0); put("bsgdp_pk_y", int(rk[:4]), "year", 0)
put("bs_x_1225", T(CAP) / T("2012-12"), "BOJ assets, October 2026 as a multiple of December 2012", 1)

# ---- yen per dollar (FRED DEXJPUS, monthly averages)
fx = M("fred/DEXJPUS")
for t in ("2000-01", "2007-06", "2012-09", "2013-12", "2015-06", "2020-12", "2022-10", CAP):
    put(f"fx_{t.replace('-', '_')}", fx[t], f"yen per US dollar, {mname(t)}", 1)
s = min((t for t in fx if t >= "2000-01"), key=fx.get); put("fx_strong", fx[s], f"strongest yen since 2000, yen per $ ({s})", 1); out["fx_strong"]["month"] = mname(s)
w = max((t for t in fx if t >= "2000-01"), key=fx.get); put("fx_weak", fx[w], f"weakest yen since 2000, yen per $ ({w})", 1); out["fx_weak"]["month"] = mname(w)
w1 = max((t for t in fx if "1987-01" <= t < "2000-01"), key=fx.get); print("   weakest 1987-99:", w1, fx[w1])
prev = [t for t in fx if t < w and fx[t] >= fx[w]]; print("   last month as weak before", w, ":", prev[-1] if prev else None)
if prev:
    put("fx_weak_since_y", int(prev[-1][:4]), "last year the yen was as weak before that month", 0)

# ---- Nikkei 225 (FRED, monthly averages)
nk = M("fred/NIKKEI225")
pk = max((t for t in nk if t < "2000-01"), key=nk.get); put("nk_1989", nk[pk], f"Nikkei 225, pre-2000 peak monthly average ({pk})", 0); out["nk_1989"]["month"] = mname(pk)
tr = min((t for t in nk if t >= "2000-01"), key=nk.get); put("nk_lo", nk[tr], f"Nikkei 225, lowest monthly average since 2000 ({tr})", 0); out["nk_lo"]["month"] = mname(tr)
above = [t for t in sorted(nk) if t > pk and nk[t] > nk[pk]]
put("nk_above_y", int(above[0][:4]), f"first month the monthly average beat the {pk} peak ({above[0]})", 0); out["nk_above_y"]["month"] = mname(above[0])
put("nk_last", nk[CAP], f"Nikkei 225, {mname(CAP)} average", 0)
put("nk_x_1215", nk["2015-06"] / nk["2012-09"], "Nikkei 225, June 2015 average as a multiple of September 2012", 1)

# ---- public finances (WEO)
d = W("GGXWDG_NGDP")
for y in (2000, 2007, 2019, 2025, 2031):
    put(f"debt_{y}", d[y], f"Japan general government gross debt, % of GDP, {y}")
pk = max((y for y in d if y <= 2025), key=d.get); put("debt_pk", d[pk], f"Japan gross debt peak ({pk})"); put("debt_pk_y", pk, "year", 0)
for a, k in (("USA", "us"), ("ITA", "it"), ("IND", "ind"), ("G163", "ea")):
    put(f"debt_{k}_2025", W("GGXWDG_NGDP", a)[2025], f"{a} gross debt, % of GDP, 2025")
b = W("GGXCNL_NGDP")
for y in (2000, 2009, 2020, 2025, 2031):
    put(f"bal_{y}", b[y], f"Japan general government net lending, % of GDP, {y}")
ca = W("BCA_NGDPD")
for y in (2007, 2014, 2025):
    put(f"ca_{y}", ca[y], f"Japan current account, % of GDP, {y}")

# ---- demography (WEO population; World Bank WDI)
pk = max(lp, key=lambda y: lp[y] if y <= 2025 else 0); put("pop_pk", lp[pk], f"Japan population, million, peak to 2025 ({pk})"); put("pop_pk_y", pk, "year", 0)
put("pop_2025", lp[2025], "Japan population, million, 2025 (WEO)")
put("pop_2031", lp[2031], "Japan population, million, 2031 (WEO projection)")
o = WD("SP.POP.65UP.TO.ZS")
put("old_2000", o[2000], "Japan population aged 65+, % of total, 2000 (WDI)")
put("old_2025", o[2025], "Japan population aged 65+, % of total, 2025 (WDI)")
for a, k in (("IND", "ind"), ("CHN", "chn"), ("USA", "us"), ("WLD", "wld")):
    put(f"old_{k}_2025", WD("SP.POP.65UP.TO.ZS", a)[2025], f"{a} population aged 65+, % of total, 2025 (WDI)")
put("old_ind_2000", WD("SP.POP.65UP.TO.ZS", "IND")[2000], "India population aged 65+, % of total, 2000 (WDI)")
wa = WD("SP.POP.1564.TO.ZS")
put("wa_2000", wa[2000], "Japan population aged 15-64, % of total, 2000 (WDI)")
put("wa_2025", wa[2025], "Japan population aged 15-64, % of total, 2025 (WDI)")
tf = WD("SP.DYN.TFRT.IN")
put("tfr_last", tf[max(tf)], f"Japan fertility rate, births per woman, {max(tf)} (WDI)", 2); put("tfr_last_y", max(tf), "year", 0)
tfi = WD("SP.DYN.TFRT.IN", "IND")
put("tfr_ind_last", tfi[max(tfi)], f"India fertility rate, births per woman, {max(tfi)} (WDI)", 2)

# ---- India and Japan
jd, idd = W("NGDPD"), W("NGDPD", "IND")
for y in (2000, 2025, 2026, 2027, 2031):
    put(f"gdpd_jp_{y}", jd[y] / 1e3, f"Japan GDP, US$ trillion, {y} (WEO)", 2)
    put(f"gdpd_in_{y}", idd[y] / 1e3, f"India GDP, US$ trillion, {y} (WEO; fiscal year)", 2)
put("gdpd_jp_in_2000", jd[2000] / idd[2000], "Japan GDP as a multiple of India's, 2000", 1)
cross = min(y for y in idd if idd[y] > jd[y])
put("gdpd_cross_y", cross, "first year India's dollar GDP exceeds Japan's (WEO Oct 2026)", 0)
put("g_ind_avg_0025", avg(W("NGDP_RPCH", "IND"), 2000, 2025), "India growth, average 2000-25")
inr = M("fred/DEXINUS")
iy = {t: 100 * inr[t] / fx[t] for t in inr if t in fx}
reg("jp_inr", {"id": "derived/jp_inr", "label": "Rupees per 100 yen", "unit": "₹ per ¥100", "freq": "M",
               "source": "Computed for this book from FRED DEXINUS (rupees per US dollar) and DEXJPUS (yen per US dollar), monthly averages (Federal Reserve H.10)",
               "notes": "Rupees per dollar divided by yen per dollar, times 100; monthly averages.",
               "data": {"IN": [[t, round(v, 2)] for t, v in sorted(iy.items()) if t >= "1973-01"]}})
for t in ("2000-01", "2007-06", "2013-12", "2020-12", CAP):
    put(f"inr_jpy_{t.replace('-', '_')}", iy[t], f"rupees per 100 yen, {mname(t)}", 2)
hi = max((t for t in iy if t >= "2000-01"), key=iy.get); put("inr_jpy_hi", iy[hi], f"rupees per 100 yen, highest month since 2000 ({hi})", 2); out["inr_jpy_hi"]["month"] = mname(hi)

(C / "derived/lens_japan.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
