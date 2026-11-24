"""Derived figures quoted in chapters/phase-9.html (2026, history in progress). Output: data/clean/derived/phase9.json
    .venv/bin/python scripts/derive_phase9.py
Monthly market data run to the latest month retrieved; WEO figures are the October 2026 vintage
(2026 values are IMF staff estimates, 2027 projections).
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
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def lab(k, v, how=""):
    out[k] = {"value": v, "how": how}
    print(f"{k:28s} {v!s:>12}  {how}")


w = lambda i, a: S(f"weo/{i}.json", a)
ind = lambda sid: {int(y): v for y, v in json.loads((C / f"india/{sid}.json").read_text())["data"]["IND"]}
fy = lambda y: f"FY{y}-{str(y + 1)[2:]}"
mon = lambda p: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][int(p[5:7]) - 1] + " " + p[:4]
latest = lambda d: max(d)

# ---- energy prices (monthly averages)
br, gas = S("fred/DCOILBRENTEU.json"), S("fred/PNGASEUUSDM.json")
put("brent_2025_12", br["2025-12"], "Brent, US$/barrel, Dec 2025 monthly average")
put("brent_2026_02", br["2026-02"], "Brent, Feb 2026")
put("brent_2026_03", br["2026-03"], "Brent, Mar 2026")
put("brent_2026_04", br["2026-04"], "Brent, Apr 2026")
put("brent_2026_07", br["2026-07"], "Brent, Jul 2026")
put("brent_2026_09", br["2026-09"], "Brent, Sep 2026")
put("brent_2026_10", br["2026-10"], "Brent, Oct 2026")
lb = latest(br); put("brent_latest", br[lb], f"Brent, {lb} (month to date)"); lab("brent_latest_m", mon(lb))
put("brent_2025avg", sum(v for p, v in br.items() if p.startswith("2025")) / 12, "Brent, 2025 average of monthly averages")
pk = max((p for p in br if p >= "2026-01"), key=lambda p: br[p]); put("brent_pk", br[pk], f"Brent peak monthly average 2026 ({pk})"); lab("brent_pk_m", mon(pk))
put("brent_rise_pk", (br[pk] / br["2025-12"] - 1) * 100, "Brent, Dec 2025 to 2026 peak month, %", 0)
# daily peak
import csv
rows = [(d, float(v)) for d, v in list(csv.reader(open(ROOT / "data/raw/fred/DCOILBRENTEU.csv")))[1:] if v not in ("", ".")]
dp = max((r for r in rows if r[0] >= "2026-01-01"), key=lambda r: r[1])
put("brent_daily_pk", dp[1], f"Brent, highest daily price in 2026 ({dp[0]})", 0); lab("brent_daily_pk_d", dp[0])
put("gas_2025_12", gas["2025-12"], "European natural gas, US$/MMBtu, Dec 2025")
put("gas_2026_03", gas["2026-03"], "European gas, Mar 2026")
lg = latest(gas); put("gas_latest", gas[lg], f"European gas, {lg}"); lab("gas_latest_m", mon(lg))
put("gas_x", gas[lg] / gas["2025-12"], "European gas, latest / Dec 2025, times", 1)
put("gas_2022_08", gas["2022-08"], "European gas, Aug 2022 (2022 peak month, for comparison)", 0)
for i, k in [("POILBRE", "oil"), ("PNGASEU", "gasw"), ("PNRGW", "nrg")]:
    d = w(i, "G001")
    for yy in (2025, 2026, 2027): put(f"weo_{k}_{yy}", d[yy], f"WEO Oct 2026 {i} {yy}")
put("weo_nrg_2026_pct", (w("PNRGW", "G001")[2026] / w("PNRGW", "G001")[2025] - 1) * 100, "WEO energy price index, 2026 vs 2025, %", 0)

# ---- inflation (monthly, % on a year earlier)
cpi = S("fred/CPIAUCSL.json")
us = {p: (v / cpi[f"{int(p[:4]) - 1}{p[4:]}"] - 1) * 100 for p, v in cpi.items() if f"{int(p[:4]) - 1}{p[4:]}" in cpi}
ea, uk = S("eurostat/EA_HICP_ANR.json"), S("ons/UK_CPI_D7G7.json")
for k, d in [("us", us), ("ea", ea), ("uk", uk)]:
    put(f"inf_{k}_2025_12", d["2025-12"], f"{k} inflation, Dec 2025")
    lo = min((p for p in d if p >= "2026-01"), key=lambda p: d[p]); put(f"inf_{k}_low26", d[lo], f"{k} lowest 2026 month ({lo})"); lab(f"inf_{k}_low26_m", mon(lo))
    l = latest(d); put(f"inf_{k}_latest", d[l], f"{k} inflation, {l}"); lab(f"inf_{k}_latest_m", mon(l))
    pk = max((p for p in d if p >= "2026-01"), key=lambda p: (d[p], p)); put(f"inf_{k}_pk26", d[pk], f"{k} highest 2026 month ({pk})"); lab(f"inf_{k}_pk26_m", mon(pk))
put("inf_us_2026_05", us["2026-05"], "US CPI-U, May 2026")

# ---- policy rates (BIS, monthly) and moves in 2026
pol = {k: S("bis/CBPOL.json", k) for k in ["US", "XM", "GB", "JP", "IN", "BR", "CN"]}
for k, d in pol.items():
    put(f"pol_{k}_2025_12", d["2025-12"], f"BIS policy rate {k}, Dec 2025", 2)
    l = latest(d); put(f"pol_{k}_latest", d[l], f"BIS policy rate {k}, {l}", 2)
    m = sorted(p for p in d if p >= "2025-12")
    ch = [p for a, p in zip(m, m[1:]) if d[p] != d[a]]
    lab(f"pol_{k}_moves26", ", ".join(f"{p} {d[p]}" for p in ch), f"BIS {k}: months in 2026 when the rate changed")
put("pol_US_hike", pol["US"]["2026-09"] - pol["US"]["2026-08"], "US: change in Sep 2026, percentage points", 2)
dfr = S("ecb/ECB_DFR.json"); put("ecb_dfr_latest", dfr[max(dfr)], f"ECB deposit rate, latest change ({max(dfr)})", 2)

# ---- markets
n, dx, y = (S(f"fred/{i}.json") for i in ["NASDAQCOM", "DTWEXBGS", "DGS10"])
put("y10_2025_12", y["2025-12"], "US 10-year yield, Dec 2025 average", 2)
yp = max((p for p in y if p >= "2026-01"), key=lambda p: y[p]); put("y10_pk26", y[yp], f"US 10-year yield, highest 2026 month ({yp})", 2); lab("y10_pk26_m", mon(yp))
put("y10_since2007", max(v for p, v in y.items() if "2007-08" <= p < "2026-01"), "highest monthly average Aug 2007 to Dec 2025", 2)
put("ndq_mar26", (n["2026-03"] / n["2025-12"] - 1) * 100, "Nasdaq, Dec 2025 to Mar 2026, %", 0)
np_ = max((p for p in n if p >= "2026-01"), key=lambda p: n[p]); put("ndq_pk26", (n[np_] / n["2025-12"] - 1) * 100, f"Nasdaq, Dec 2025 to 2026 high month ({np_}), %", 0)
ln = latest(n); put("ndq_latest_from_pk", (n[ln] / n[np_] - 1) * 100, f"Nasdaq, {np_} to {ln}, %", 0)
put("usd_2026", (dx[latest(dx)] / dx["2025-12"] - 1) * 100, f"US dollar broad index, Dec 2025 to {latest(dx)}, %")
inr = S("fred/DEXINUS.json"); put("inr_2025_12", inr["2025-12"], "rupees per US$, Dec 2025", 2); put("inr_latest", inr[latest(inr)], f"rupees per US$, {latest(inr)}", 2)
put("inr_dep26", (inr[latest(inr)] / inr["2025-12"] - 1) * 100, "rupee depreciation vs US$, Dec 2025 to latest month, % (rise in rupees per dollar)")
ip = max((p for p in inr if p >= "2026-01"), key=lambda p: inr[p]); put("inr_pk26", inr[ip], f"weakest monthly average 2026 ({ip})", 2); lab("inr_pk26_m", mon(ip))

# ---- WEO October 2026
for a in ["G001", "G110", "G200", "USA", "G163", "DEU", "GBR", "JPN", "CHN", "IND", "RUS", "BRA", "SAU", "G400", "QAT", "KWT", "IRQ", "ARE", "IRN", "NOR", "KOR", "TUR", "EGY", "PAK"]:
    gg, ii = w("NGDP_RPCH", a), w("PCPIPCH", a)
    for yy in (2025, 2026, 2027):
        put(f"gdp_{a}_{yy}", gg[yy], f"WEO Oct 2026 NGDP_RPCH {a} {yy}")
        put(f"cpi_{a}_{yy}", ii[yy], f"WEO Oct 2026 PCPIPCH {a} {yy}")
tr = w("TRADEPCH", "G001")
for yy in (2025, 2026, 2027): put(f"trade_{yy}", tr[yy], f"WEO TRADEPCH world trade volume {yy}")
for a in ["IND", "SAU", "USA", "CHN", "JPN", "DEU", "KOR", "NOR", "EGY", "TUR", "PAK"]:
    for yy in (2025, 2026, 2027): put(f"ca_{a}_{yy}", w("BCA_NGDPD", a)[yy], f"WEO current account % GDP {a} {yy}")

# ---- how the 2026 forecast moved: earlier WEO database vintages
for v, tag in [("WEO_2025_OCT_VINTAGE", "o25"), ("WEO_2026_APR_VINTAGE", "a26")]:
    for i, k in [("NGDP_RPCH", "gdp"), ("PCPIPCH", "cpi")]:
        d = json.loads((C / f"weo_vintage/{v}__{i}.json").read_text())["data"]
        for a in ["G001", "G110", "G200", "USA", "G163", "CHN", "IND", "SAU", "G400", "JPN"]:
            dd = dict(d[a])
            for yy in (2026, 2027): put(f"v{tag}_{k}_{a}_{yy}", dd[yy], f"{v} {i} {a} {yy}")

# ---- India (author's dataset; fiscal years at start year)
for sid, k, nd in [("gdp_real_growth", "gdp", 1), ("cpi_inflation", "cpi", 1), ("repo_end", "repo", 2), ("cab_gdp", "cab", 1),
                   ("fx_reserves", "res", 0), ("inr_usd", "inr", 1), ("oil_imports", "oil", 0), ("imports_goods", "mg", 0),
                   ("enr_crude_import_share", "crude_share", 0), ("centre_subsidies_gdp", "subs", 1)]:
    s = ind(sid)
    for yy in range(2021, 2026):
        if s.get(yy) is not None: put(f"in_{k}_{yy}", s[yy], f"India {sid} {fy(yy)}", nd)
oil = ind("oil_imports"); put("in_oil_pk", max(oil.values()), f"India oil imports, highest year ({fy(max(oil, key=oil.get))}), US$ bn", 0)

(C / "derived/phase9.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
