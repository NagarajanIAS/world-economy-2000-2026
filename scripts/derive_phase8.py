"""Derived figures quoted in chapters/phase-8.html. Output: data/clean/derived/phase8.json
    .venv/bin/python scripts/derive_phase8.py
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


def lab(k, v, how):
    out[k] = {"value": v, "how": how}
    print(f"{k:28s} {v!s:>12}  {how}")


w = lambda i, a: S(f"weo/{i}.json", a)
ind = lambda sid: {int(y): v for y, v in json.loads((C / f"india/{sid}.json").read_text())["data"]["IND"]}
fy = lambda y: f"FY{y}-{str(y + 1)[2:]}"
q = lambda p: f"{p[:4]}Q{(int(p[5:7]) - 1) // 3 + 1}"

# ---- US effective tariff rate: customs duties / imports of goods (BEA NIPA, quarterly SAAR)
cd, mg = S("fred/B235RC1Q027SBEA.json"), S("fred/A255RC1Q027SBEA.json")
t = {p: cd[p] / mg[p] * 100 for p in cd if p in mg}
put("tar_2024q4", t["2024-10"], "US customs duties / goods imports, %, 2024Q4")
put("tar_2025q1", t["2025-01"], "US customs duties / goods imports, %, 2025Q1")
put("tar_2025q2", t["2025-04"], "US customs duties / goods imports, %, 2025Q2")
pk = max((p for p in t if "2025-01" <= p <= "2025-12"), key=lambda p: t[p])
put("tar_2025_peak", t[pk], f"US customs duties / goods imports, %, peak quarter of 2025 ({q(pk)})"); lab("tar_2025_peak_q", q(pk), "")
put("tar_avg_1519", sum(v for p, v in t.items() if "2015" <= p[:4] <= "2019") / 20, "average 2015-2019, %")
put("cd_2024q4", cd["2024-10"], "US customs duties, $bn SAAR, 2024Q4", 0)
put("cd_2025q4", cd["2025-10"], "US customs duties, $bn SAAR, 2025Q4", 0)

# ---- AI-related investment (BEA, $bn SAAR)
ip, comp, sw, gdp = (S(f"fred/{i}.json") for i in ["A679RC1Q027SBEA", "B935RC1Q027SBEA", "B985RC1Q027SBEA", "GDP"])
for p in ["2019-10", "2022-10", "2024-10", "2025-10"]:
    put(f"ipes_gdp_{q(p).lower()}", ip[p] / gdp[p] * 100, f"US info-processing equipment and software investment, % of GDP, {q(p)}", 2)
    put(f"comp_{q(p).lower()}", comp[p], f"US investment in computers and peripherals, $bn SAAR, {q(p)}", 0)
    put(f"sw_{q(p).lower()}", sw[p], f"US investment in software, $bn SAAR, {q(p)}", 0)
put("comp_x_2425", comp["2025-10"] / comp["2024-10"], "computers and peripherals, 2025Q4 / 2024Q4, times", 2)
put("comp_x_1925", comp["2025-10"] / comp["2019-10"], "computers and peripherals, 2025Q4 / 2019Q4, times", 2)
g = {p: gdp[p] for p in gdp}
put("ipes_contrib_2025", (ip["2025-10"] - ip["2024-10"]) / (gdp["2025-10"] - gdp["2024-10"]) * 100,
    "increase in info-processing investment as % of increase in nominal GDP, 2024Q4 to 2025Q4", 0)

# ---- policy rates (BIS, monthly)
pol = {k: S("bis/CBPOL.json", k) for k in ["US", "XM", "GB", "JP", "IN", "BR", "CN"]}
for k, d in pol.items():
    for p in ["2024-01", "2024-12", "2025-12"]:
        put(f"pol_{k}_{p.replace('-', '_')}", d[p], f"BIS policy rate {k}, {p}", 2)
for k in ["US", "XM", "GB", "IN"]:
    d = pol[k]; m = sorted(p for p in d if p >= "2024-01")
    first = next(p for a, p in zip(m, m[1:]) if d[p] < d[a]); lab(f"pol_{k}_first_cut", first, f"BIS {k}: first month with a lower rate than the month before, from 2024")
m = sorted(p for p in pol["JP"] if p >= "2024-01"); lab("pol_JP_first_hike", next(p for a, p in zip(m, m[1:]) if pol["JP"][p] > pol["JP"][a]), "BIS JP: first rise from 2024")
dfr = S("ecb/ECB_DFR.json"); put("ecb_dfr_2025_12", dfr[max(k for k in dfr if k <= "2025-12")], "ECB deposit rate in force Dec 2025", 2)
lab("ecb_first_cut", min(k for k in dfr if k >= "2024-01" and dfr[k] < 4.0), "first ECB deposit-rate cut")

# ---- inflation (monthly)
cpi = S("fred/CPIAUCSL.json")
us = {p: (v / cpi[f"{int(p[:4]) - 1}{p[4:]}"] - 1) * 100 for p, v in cpi.items() if f"{int(p[:4]) - 1}{p[4:]}" in cpi}
ea = S("ecb/EA_HICP.json")
for p in ["2024-12", "2025-12"]:
    put(f"inf_us_{p[:4]}_12", us[p], f"US CPI-U, % on a year earlier, {p} (computed, SA)")
    put(f"inf_ea_{p[:4]}_12", ea[p], f"Euro area HICP annual rate, {p}")
cn = S("fred/CPALTT01CNM659N.json")
put("inf_cn_2024avg", sum(v for p, v in cn.items() if p.startswith("2024")) / 12, "China CPI % on a year earlier, 2024 average of monthly (OECD)")

# ---- markets
n, sp, dx, y = (S(f"fred/{i}.json") for i in ["NASDAQCOM", "SP500", "DTWEXBGS", "DGS10"])
put("ndq_2225", (n["2025-12"] / n["2022-12"] - 1) * 100, "Nasdaq Composite, Dec 2022 to Dec 2025, % (monthly averages)", 0)
put("sp_2225", (sp["2025-12"] / sp["2022-12"] - 1) * 100, "S&P 500, Dec 2022 to Dec 2025, %", 0)
put("ndq_2025", (n["2025-12"] / n["2024-12"] - 1) * 100, "Nasdaq Composite, Dec 2024 to Dec 2025, %", 0)
ap = min((p for p in n if "2025-01" <= p <= "2025-12"), key=lambda p: n[p]); lab("ndq_low_2025", ap, "month of lowest Nasdaq monthly average in 2025")
put("ndq_fall_to_low", (n[ap] / n["2024-12"] - 1) * 100, "Nasdaq, Dec 2024 to 2025 low month, %", 0)
put("usd_2025", (dx["2025-12"] / dx["2024-12"] - 1) * 100, "US dollar broad index, Dec 2024 to Dec 2025, %")
pkd = max((p for p in dx if "2024-01" <= p <= "2025-12"), key=lambda p: dx[p]); lab("usd_peak_month", pkd, "")
put("usd_fall_from_peak", (dx["2025-12"] / dx[pkd] - 1) * 100, f"US dollar broad index, peak ({pkd}) to Dec 2025, %")
put("y10_2024_12", y["2024-12"], "US 10-year yield, Dec 2024", 2)
put("y10_2025_12", y["2025-12"], "US 10-year yield, Dec 2025", 2)

# ---- WEO (today's vintage)
for a in ["G001", "G110", "G200", "USA", "G163", "DEU", "GBR", "JPN", "CHN", "IND", "RUS", "BRA", "MEX", "CAN", "VNM", "IDN"]:
    gg, ii = w("NGDP_RPCH", a), w("PCPIPCH", a)
    for yy in (2023, 2024, 2025):
        put(f"gdp_{a}_{yy}", gg[yy], f"WEO NGDP_RPCH {a} {yy}")
        put(f"cpi_{a}_{yy}", ii[yy], f"WEO PCPIPCH {a} {yy}")
tr = w("TRADEPCH", "G001")
for yy in (2023, 2024, 2025): put(f"trade_{yy}", tr[yy], f"WEO TRADEPCH world trade volume {yy}")
b = w("BCA", "CHN")
for yy in (2023, 2024, 2025): put(f"bca_CHN_{yy}", b[yy], f"WEO BCA China {yy}, US$ bn", 0)
for a in ["USA", "G110", "CHN", "FRA", "GBR", "JPN", "IND"]:
    d = w("GGXWDG_NGDP", a)
    put(f"debt_{a}_2025", d[2025], f"WEO GGXWDG_NGDP {a} 2025", 0)
    put(f"debt_{a}_2019", d[2019], f"WEO GGXWDG_NGDP {a} 2019", 0)
for a in ["USA", "FRA", "GBR", "CHN", "IND", "G110"]:
    put(f"bal_{a}_2025", w("GGXCNL_NGDP", a)[2025], f"WEO GGXCNL_NGDP {a} 2025")

# ---- India (author's dataset; fiscal years at start year)
for sid, k, nd in [("gdp_real_growth", "gdp", 1), ("cpi_inflation", "cpi", 1), ("cpi_food_inflation", "cpif", 1), ("repo_end", "repo", 2),
                   ("cab_gdp", "cab", 1), ("fx_reserves", "res", 0), ("centre_fd_gdp", "cfd", 1), ("gg_fd_gdp", "ggfd", 1),
                   ("inr_usd", "inr", 1), ("oil_imports", "oil", 0), ("imports_goods", "mg", 0), ("exports_goods", "xg", 0)]:
    s = ind(sid)
    for yy in range(2022, 2026):
        if s.get(yy) is not None:
            put(f"in_{k}_{yy}", s[yy], f"India {sid} {fy(yy)}", nd)

(C / "derived/phase8.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
