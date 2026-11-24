"""Derived figures and series for chapters/theme-money.html.
Output: data/clean/derived/theme_money.json, data/js/derived/tm_rates.js (monthly policy rates, euro area deposit rate
forward-filled), data/js/derived/tm_bs.js (central bank assets, % of GDP, annual).
    .venv/bin/python scripts/derive_theme_money.py
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
months = [f"{y}-{m:02d}" for y in range(2000, 2027) for m in range(1, 13) if f"{y}-{m:02d}" <= "2026-10"]


def ffill(pts, start="1990-01"):
    d = dict(pts); last = None; res = {}
    for y in range(int(start[:4]), 2027):
        for m in range(1, 13):
            p = f"{y}-{m:02d}"
            if p in d: last = d[p]
            if last is not None: res[p] = last
    return res


# ---- policy rates (BIS CBPOL; euro area = ECB deposit facility rate, forward-filled from change dates)
cb = J("bis/CBPOL.json")["data"]
R = {k: ffill(cb[k]) for k in ("US", "GB", "JP")}
R["EA"] = ffill(J("ecb/ECB_DFR.json")["data"]["EA"])
ser = {k: [[p, R[k][p]] for p in months if p in R[k]] for k in R}
obj = {"id": "derived/tm_rates", "source": "BIS, central bank policy rates (CBPOL); ECB, deposit facility rate",
       "code": "BIS WS_CBPOL US, GB, JP; ECB FM.D.U2.EUR.4F.KR.DFR.LEV", "label": "Central bank policy rates", "unit": "%", "freq": "M",
       "url": "https://data.bis.org/topics/CBPOL", "retrieved": "2026-11-22",
       "notes": "Monthly. Euro area: ECB deposit facility rate, carried forward from each change date. United States: midpoint of the federal funds target range as reported by the BIS.",
       "data": ser}
(ROOT / "data/js/derived/tm_rates.js").write_text(f'WE.register("derived/tm_rates",{json.dumps(obj, separators=(",", ":"))});\n')
for k in R:
    for p in ("2000-01", "2007-06", "2019-12", "2021-12", "2023-12", "2026-10"):
        if p in R[k]: put(f"r_{k}_{p.replace('-', '_')}", R[k][p], f"policy rate {k} {p}", 2)
def low_months(k, lim):
    return sum(1 for p in months if p >= "2008-01" and R[k].get(p, 9) <= lim)
put("zlb_US_months", low_months("US", 0.25), "months since 2008 with US policy rate at or below 0.25%", 0)
put("zlb_US_years", low_months("US", 0.25) / 12, "years since 2008 with US policy rate at or below 0.25%", 0)
put("neg_EA_months", sum(1 for p in months if R["EA"][p] < 0), "months with ECB deposit rate below zero", 0)
put("neg_EA_years", sum(1 for p in months if R["EA"][p] < 0) / 12, "years with ECB deposit rate below zero", 0)
lab("neg_EA_first", next(p for p in months if R["EA"][p] < 0), "first month ECB deposit rate negative")
lab("neg_EA_last", max(p for p in months if R["EA"][p] < 0), "last month ECB deposit rate negative")
lab("neg_JP_last", max(p for p in months if R["JP"].get(p, 1) < 0), "last month BoJ rate negative")
for k in ("US", "EA", "GB"):
    pk = max((p for p in months if "2022-01" <= p <= "2024-12"), key=lambda p: (R[k][p], p))
    lo = R[k]["2022-01"]
    put(f"hike_{k}", R[k][pk] - lo, f"{k} rise in policy rate Jan 2022 to peak ({pk}), percentage points", 2)

# hikes count 2022 across BIS economies (euro members counted once via XM)
euro = {"AT", "BE", "DE", "ES", "FR", "GR", "IT", "NL", "PT", "HR", "IE", "FI", "SK", "SI", "LU", "LT", "LV", "EE", "CY", "MT"}
fall = {k: ffill(v) for k, v in cb.items() if k not in euro}
have = [k for k in fall if "2021-12" in fall[k] and "2022-12" in fall[k]]
up = [k for k in have if fall[k]["2022-12"] > fall[k]["2021-12"]]
put("n_cb", len(have), "central banks in BIS policy-rate data (euro area counted once) with data for Dec 2021 and Dec 2022", 0)
put("n_cb_up_2022", len(up), "of which raised their policy rate between Dec 2021 and Dec 2022", 0)
z20 = [k for k in fall if "2020-12" in fall[k] and fall[k]["2020-12"] <= 0.25]
put("n_cb_zero_2020", len(z20), "central banks with policy rate at or below 0.25% in Dec 2020", 0)


# first rate rise after mid-2020
FIRST = {}
for k in ("BR", "RU", "MX", "CL", "KR", "ZA", "IN", "GB", "US", "CA", "AU", "JP"):
    f = ffill(cb[k]); ps = [p for p in sorted(f) if "2020-07" <= p <= "2026-10"]
    FIRST[k] = next(p for a, p in zip(ps, ps[1:]) if f[p] > f[a]); lab(f"first_up_{k}", FIRST[k], f"first month after mid-2020 with a higher policy rate than the month before, {k}")
dfr = R["EA"]; ps = [p for p in months if p >= "2020-07"]
lab("first_up_EA", next(p for a, p in zip(ps, ps[1:]) if dfr[p] > dfr[a]), "first ECB deposit rate rise after mid-2020")
# ---- central bank assets, % of GDP (December, or latest month for 2026)
W = lambda i: {a: {int(y): v for y, v in s} for a, s in J(f"weo/{i}.json")["data"].items()}
ngdp, ngdpd = W("NGDP"), W("NGDPD")
eur = dict(J("fred/DEXUSEU.json")["data"]["US"]) if "US" in J("fred/DEXUSEU.json")["data"] else dict(next(iter(J("fred/DEXUSEU.json")["data"].values())))
eur_y = {y: sum(v for p, v in eur.items() if p[:4] == str(y)) / len([1 for p in eur if p[:4] == str(y)]) for y in range(2000, 2027)}
A = {"US": (dict(J("fred/WALCL.json")["data"]["US"]), lambda y: ngdp["USA"][y] * 1e3),   # $ million / $ billion*1e3
     "EA": (dict(next(iter(J("fred/ECBASSETSW.json")["data"].values()))), lambda y: ngdpd["G163"][y] / eur_y[y] * 1e3),  # EUR million
     "JP": (dict(next(iter(J("fred/JPNASSETS.json")["data"].values()))), lambda y: ngdp["JPN"][y] * 10)}  # 100 million yen / yen billion*10
bs = {}
for k, (a, g) in A.items():
    pts = []
    for y in range(2000, 2027):
        p = f"{y}-12" if y < 2026 else max(q for q in a if q[:4] == "2026")
        if p in a:
            pts.append([y, round(a[p] / g(y) * 100, 1)])
    bs[k] = pts
    s = dict(pts)
    for y in (2007, 2019, 2021, 2025, 2026):
        if y in s: put(f"bs_{k}_{y}", s[y], f"{k} central bank assets, % of GDP, end-{y} (2026: latest month / WEO 2026 GDP)")
    pk = max(s, key=s.get); put(f"bs_{k}_peak", s[pk], f"{k} peak central bank assets % GDP"); lab(f"bs_{k}_peak_y", pk)
obj = {"id": "derived/tm_bs", "source": "Federal Reserve (WALCL), ECB (ECBASSETSW), Bank of Japan (JPNASSETS) via FRED; IMF WEO October 2026 (NGDP, NGDPD)",
       "code": "FRED WALCL, ECBASSETSW, JPNASSETS; WEO NGDP USA, JPN; NGDPD G163 / FRED DEXUSEU", "label": "Central bank total assets", "unit": "% of GDP", "freq": "A",
       "url": "https://fred.stlouisfed.org/series/WALCL", "retrieved": "2026-11-22",
       "notes": "End-December assets divided by that year's nominal GDP; 2026 uses the latest month and the IMF's 2026 GDP projection. Euro area GDP converted from US dollars at the annual average euro exchange rate.",
       "data": bs}
(ROOT / "data/js/derived/tm_bs.js").write_text(f'WE.register("derived/tm_bs",{json.dumps(obj, separators=(",", ":"))});\n')

# ---- inflation (WEO PCPIPCH)
pi = W("PCPIPCH")
avg = lambda d, a, b: sum(d[y] for y in range(a, b + 1)) / (b - a + 1)
for a in ("G001", "G110", "G200", "USA", "IND", "JPN", "TUR", "ARG"):
    for x, y in ((2000, 2007), (2010, 2019), (2020, 2020), (2022, 2022), (2026, 2026)):
        if all(t in pi[a] for t in range(x, y + 1)):
            put(f"pi_{a}_{x}_{y}" if x != y else f"pi_{a}_{x}", avg(pi[a], x, y), f"WEO PCPIPCH {a} {x}-{y} average")
for a in ("G110", "G200", "G001"):
    pk = max(range(2000, 2026), key=lambda y: pi[a][y]); put(f"pi_{a}_peak", pi[a][pk], f"{a} peak inflation 2000-2025"); lab(f"pi_{a}_peak_y", pk)
lab("pi_G110_low_y", min(range(2000, 2022), key=lambda y: pi["G110"][y]), "AE lowest inflation year 2000-2021")
put("pi_G110_low", min(pi["G110"][y] for y in range(2000, 2022)), "AE lowest inflation 2000-2021")
ae = [c for c in J("meta/weo_countries.json")["countries"] if c in pi]

# ---- US: years core PCE below 2% 2009-2020; dollar
core = dict(next(iter(J("fred/PCEPILFE.json")["data"].values())))
yo = {p: (core[p] / core[f"{int(p[:4]) - 1}{p[4:]}"] - 1) * 100 for p in core if f"{int(p[:4]) - 1}{p[4:]}" in core}
b = [p for p in yo if "2009-01" <= p <= "2020-12"]
put("us_core_below2_share", sum(1 for p in b if yo[p] < 2) / len(b) * 100, "share of months 2009-2020 with US core PCE inflation below 2%", 0)
pk = max((p for p in yo if p >= "2021-01"), key=lambda p: yo[p]); put("us_core_peak", yo[pk], "US core PCE inflation peak since 2021"); lab("us_core_peak_m", pk)
last = max(yo); put("us_core_last", yo[last], "US core PCE inflation latest"); lab("us_core_last_m", last)

# ---- India (fiscal years)
I = lambda s: {int(y): v for y, v in J(f"india/{s}.json")["data"]["IND"]}
cpi, rep = I("cpi_inflation"), I("repo_end")
for x, y in ((2000, 2007), (2008, 2013), (2014, 2019), (2016, 2025), (2020, 2022), (2023, 2025)):
    put(f"in_pi_{x}_{y}", avg(pi["IND"], x, y), f"WEO PCPIPCH IND (fiscal years) average FY{x}-FY{y}")
for y in (2010, 2012, 2013, 2019, 2022, 2024, 2025, 2026):
    put(f"in_pi_{y}", pi["IND"][y], f"WEO PCPIPCH IND FY{y}")
for y in (2008, 2013, 2019, 2020, 2022, 2025):
    put(f"in_repo_{y}", rep[y], f"RBI repo rate end of FY{y}", 2)
inl = cb["IN"][-1]; put("in_repo_last", inl[1], "RBI policy rate latest month (BIS)", 2); lab("in_repo_last_m", inl[0])
(C / "derived/theme_money.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
