"""Derived figures and series for chapters/lens-us.html (Part III, United States).
Output: data/clean/derived/lens_us.json and data/js/derived/us_india.js (India's merchandise exports to the US as a
share of its total merchandise exports, fiscal years; computed from the Economic Survey / RBI series in data/clean/india).
    .venv/bin/python scripts/derive_lens_us.py
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


def W(code, area="USA"):
    d = json.loads((C / f"weo/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def F(code):
    d = json.loads((C / f"fred/{code}.json").read_text())["data"]
    return {t: v for t, v in list(d.values())[0] if v is not None}


def I(code):
    return {int(t): v for t, v in json.loads((C / f"india/{code}.json").read_text())["data"]["IND"] if v is not None}


def avg(d, y0, y1):
    xs = [d[y] for y in range(y0, y1 + 1)]
    return sum(xs) / len(xs)


# ---- growth, inflation, unemployment (IMF WEO, October 2026; actual data to 2025)
g = W("NGDP_RPCH")
for y in (2000, 2001, 2008, 2009, 2020, 2021, 2024, 2025, 2026, 2027, 2031):
    put(f"g_{y}", g[y], f"US real GDP growth {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")
put("g_avg_0007", avg(g, 2000, 2007), "US real GDP growth, average 2000-07")
put("g_avg_1019", avg(g, 2010, 2019), "US real GDP growth, average 2010-19")
put("g_avg_2225", avg(g, 2022, 2025), "US real GDP growth, average 2022-25")
for a, k in (("G163", "ea"), ("G110", "ae")):
    ga = W("NGDP_RPCH", a)
    put(f"g_{k}_avg_1019", avg(ga, 2010, 2019), f"{a} real GDP growth, average 2010-19")
    put(f"g_{k}_avg_2225", avg(ga, 2022, 2025), f"{a} real GDP growth, average 2022-25")
p = W("PCPIPCH")
for y in (2009, 2015, 2021, 2022, 2025, 2026):
    put(f"cpi_{y}", p[y], f"US CPI inflation {y}, annual average")
put("cpi_avg_1019", avg(p, 2010, 2019), "US CPI inflation, average 2010-19")
u = W("LUR")
put("lur_2025", u[2025], "US unemployment rate 2025 (WEO)")

# ---- money (FRED)
ff = F("FEDFUNDS")
put("ff_2000pk", max(v for t, v in ff.items() if t.startswith("2000")), "effective fed funds, 2000 high (monthly)", 2)
put("ff_2007pk", max(v for t, v in ff.items() if "2006" <= t < "2008"), "effective fed funds, 2006-07 high", 2)
zero = [t for t, v in ff.items() if "2008-12" <= t <= "2016-01" and v < 0.25]
put("ff_zero_months", len(zero), f"months with effective fed funds below 0.25%, {zero[0]} to {zero[-1]}", 0)
put("ff_2019pk", max(v for t, v in ff.items() if t.startswith("2019")), "effective fed funds, 2019 high", 2)
pk23 = max((t for t in ff if t >= "2022"), key=ff.get)
put("ff_2023pk", ff[pk23], f"effective fed funds, 2022-26 high ({pk23})", 2)
put("ff_last", ff[max(ff)], f"effective fed funds, latest month ({max(ff)})", 2)
t10 = F("DGS10")
t10 = {t: v for t, v in t10.items() if t <= "2026-10"}          # last complete month
put("t10_2000", sum(v for t, v in t10.items() if t.startswith("2000")) / 12, "10-year Treasury yield, 2000 average", 2)
lo = min((t for t in t10 if t >= "2020"), key=t10.get)
put("t10_low20", t10[lo], f"10-year Treasury yield, 2020 monthly low ({lo})", 2)
pk = max((t for t in t10 if t >= "2022"), key=t10.get)
put("t10_pk", t10[pk], f"10-year Treasury yield, high since 2022 ({pk})", 2)
put("t10_last", t10["2026-10"], "10-year Treasury yield, October 2026 average", 2)
prev = max(t for t, v in t10.items() if t < "2026-10" and v >= t10["2026-10"])
put("t10_last_since", int(prev[:4]), f"last month before Oct 2026 with a 10-year yield at least as high ({prev})", 0)
lo = min((t for t in ff if t >= "2024-09"), key=ff.get)
put("ff_low_2526", ff[lo], f"effective fed funds, low since Sep 2024 ({lo})", 2)
put("ff_low_2526_m", int(lo[5:]), "month of that low", 0)
put("ff_low_2526_y", int(lo[:4]), "year of that low", 0)
fb = {t: v for t, v in F("WALCL").items() if t <= "2026-10"}
put("fed_bs_2007", fb["2007-12"] / 1e6 if "2007-12" in fb else fb[min(fb)] / 1e6, "Fed total assets, Dec 2007, $ trillion", 2)
pkb = max(fb, key=fb.get)
put("fed_bs_pk", fb[pkb] / 1e6, f"Fed total assets, peak ({pkb}), $ trillion", 2)
put("fed_bs_last", fb[max(fb)] / 1e6, f"Fed total assets, latest ({max(fb)}), $ trillion", 2)

# ---- public finances and the external balance (WEO)
d = W("GGXWDG_NGDP"); b = W("GGXCNL_NGDP"); ca = W("BCA_NGDPD")
for y in (2001, 2007, 2009, 2012, 2019, 2020, 2025, 2031):
    put(f"debt_{y}", d[y], f"US general government gross debt, % of GDP, {y}")
for y in (2001, 2007, 2009, 2019, 2020, 2025, 2026, 2031):
    put(f"bal_{y}", b[y], f"US general government net lending/borrowing, % of GDP, {y}")
dea = W("GGXWDG_NGDP", "G163")
put("debt_ea_2025", dea[2025], "euro area general government gross debt, % of GDP, 2025")
put("debt_ea_2031", dea[2031], "euro area gross debt, % of GDP, 2031 (projection)")
put("bal_avg_1519", avg(b, 2015, 2019), "US general government balance, average 2015-19, % of GDP")
put("bal_avg_2325", avg(b, 2023, 2025), "US general government balance, average 2023-25, % of GDP")
lo = min((y for y in ca if 2000 <= y <= 2025), key=ca.get)
put("ca_low", ca[lo], f"US current account, % of GDP, low 2000-25 ({lo})")
put("ca_low_y", lo, "year of that low", 0)
for y in (2009, 2025, 2031):
    put(f"ca_{y}", ca[y], f"US current account, % of GDP, {y}")

# ---- weight in the world economy (PPP shares)
for a in ("USA", "CHN", "IND"):
    s = W("PPPSH", a)
    for y in (2000, 2025):
        put(f"ppp_{a}_{y}", s[y], f"{a} share of world GDP at PPP, {y}, %")
us, cn = W("PPPSH", "USA"), W("PPPSH", "CHN")
put("ppp_cross", min(y for y in cn if cn[y] > us[y]), "first year China's PPP share exceeds the US's", 0)

# ---- India and the US
ex, tot = I("exports_to_us"), I("exports_goods")
share = {y: 100 * ex[y] / tot[y] for y in ex if y in tot}
reg("us_india", {"id": "derived/us_india", "label": "US share of India's merchandise exports", "unit": "%", "freq": "A",
                 "source": "Computed for this book from India's merchandise exports to the USA and total merchandise exports (Economic Survey statistical appendices and RBI Handbook of Statistics, via the author's Indian-economy dataset)",
                 "notes": "Indian fiscal years (April–March), plotted at the year in which they start.",
                 "data": {"IND": [[y, round(v, 1)] for y, v in sorted(share.items())]}})
for y in (2003, 2010, 2024):
    put(f"in_share_{y}", share[y], f"US share of India's merchandise exports, FY{y}-{str(y + 1)[2:]}")
for y in (2003, 2010, 2024, 2025):
    put(f"in_exus_{y}", ex[y], f"India's merchandise exports to the US, FY{y}-{str(y + 1)[2:]}, US$ bn")
inr = {t: v for t, v in F("DEXINUS").items() if t <= "2026-10"}   # last complete month
put("inr_2013_05", inr["2013-05"], "rupees per dollar, May 2013 average", 2)
put("inr_2013_08", inr["2013-08"], "rupees per dollar, August 2013 average", 2)
put("inr_2013_fall", 100 * (inr["2013-08"] / inr["2013-05"] - 1), "rise in rupees per dollar, May to August 2013, %")
put("inr_2000", sum(v for t, v in inr.items() if t.startswith("2000")) / 12, "rupees per dollar, 2000 average", 2)
put("inr_last", inr[max(inr)], f"rupees per dollar, latest ({max(inr)})", 2)

(C / "derived/lens_us.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
