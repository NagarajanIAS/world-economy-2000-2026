"""Derived figures quoted in chapters/phase-7.html. Output: data/clean/derived/phase7.json
and the inflation forecast-vs-outturn table as data/js/derived/p7_inflation_forecasts.js.
    .venv/bin/python scripts/derive_phase7.py
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
mon = lambda d, a, b: {p: v for p, v in d.items() if a <= p <= b}


def peak(d, a, b):
    p = max(mon(d, a, b), key=lambda k: d[k]); return p, d[p]


# ---- headline inflation, monthly
cpi = S("fred/CPIAUCSL.json")
us = {p: (v / cpi[f"{int(p[:4]) - 1}{p[4:]}"] - 1) * 100 for p, v in cpi.items() if f"{int(p[:4]) - 1}{p[4:]}" in cpi}
for k, d, src in [("us", us, "US CPI-U (FRED CPIAUCSL), % change on a year earlier (computed)"),
                  ("ea", S("ecb/EA_HICP.json"), "Euro area HICP, annual rate (ECB)"),
                  ("uk", S("fred/CPALTT01GBM659N.json"), "UK CPI, % change on a year earlier (OECD via FRED)")]:
    p, v = peak(d, "2021-01", "2023-12")
    put(f"inf_{k}_peak", v, f"{src}: peak 2021-23 ({p})"); lab(f"inf_{k}_peak_month", p, "month of peak")
    put(f"inf_{k}_2021_01", d["2021-01"], f"{src}: Jan 2021")
    put(f"inf_{k}_2023_12", d["2023-12"], f"{src}: Dec 2023")
# when was US inflation last this high
pk = out["inf_us_peak"]["value"]
last = max(p for p, v in us.items() if p < "2021-01" and v >= pk)
lab("inf_us_last_higher", last, "last month before 2021 with US CPI inflation at or above the 2022 peak")

# ---- policy rates (BIS, monthly)
pol = {k: S("bis/CBPOL.json", k) for k in ["US", "XM", "GB", "JP", "IN", "BR"]}
for k, d in pol.items():
    put(f"pol_{k}_2022_01", d["2022-01"], f"BIS policy rate {k}, Jan 2022", 2)
    p, v = peak(d, "2022-01", "2023-12")
    put(f"pol_{k}_peak", v, f"BIS policy rate {k}, peak 2022-23 ({p})", 2); lab(f"pol_{k}_peak_month", p, "first month at peak" if False else "month of peak")
first = next(p for p in sorted(pol["US"]) if p >= "2022-01" and pol["US"][p] > pol["US"]["2022-01"])
lab("fed_first_hike_month", first, "first month with BIS US policy rate above Jan 2022")
put("fed_rise_pts", out["pol_US_peak"]["value"] - out["pol_US_2022_01"]["value"], "Fed rate rise 2022-23, points (BIS midpoints)", 2)
dfr = S("ecb/ECB_DFR.json")
put("ecb_dfr_2022_06", dfr[max(k for k in dfr if k <= "2022-06")], "ECB deposit rate in force Jun 2022 (series lists changes only)", 2)
lab("ecb_first_hike", min(k for k in dfr if k > "2022-06"), "month of first ECB deposit-rate rise after Jun 2022")
p, v = peak(dfr, "2022-01", "2023-12"); put("ecb_dfr_peak", v, f"ECB deposit rate peak 2022-23 ({p})", 2)

# ---- energy, dollar, yields
gas = S("fred/PNGASEUUSDM.json")
put("gas_2019", sum(v for p, v in gas.items() if p.startswith("2019")) / 12, "Europe natural gas, US$/MMBtu, 2019 average")
p, v = peak(gas, "2021-01", "2023-12"); put("gas_peak", v, f"Europe gas peak ({p})"); lab("gas_peak_month", p, "")
put("gas_2023_12", gas["2023-12"], "Europe gas Dec 2023")
put("gas_x", v / out["gas_2019"]["value"], "gas peak / 2019 average, times")
b = S("fred/DCOILBRENTEU.json")
put("brent_2022_01", b["2022-01"], "Brent Jan 2022", 0)
p, v = peak(b, "2022-01", "2023-12"); put("brent_peak", v, f"Brent peak monthly average ({p})", 0); lab("brent_peak_month", p, "")
put("brent_2023_12", b["2023-12"], "Brent Dec 2023", 0)
dx = S("fred/DTWEXBGS.json")
p, v = peak(dx, "2022-01", "2023-12")
put("usd_rise", (v / dx["2021-12"] - 1) * 100, f"US dollar broad index, Dec 2021 to peak ({p}), %"); lab("usd_peak_month", p, "")
y = S("fred/DGS10.json")
put("y10_us_2021_12", y["2021-12"], "US 10-year yield Dec 2021", 2)
p, v = peak(y, "2022-01", "2023-12"); put("y10_us_peak", v, f"US 10-year yield peak ({p})", 2); lab("y10_us_peak_month", p, "")
pf = w("PFOODW", "G001"); put("food_2022", (pf[2022] / pf[2020] - 1) * 100, "IMF food price index, 2022 vs 2020, %", 0)
pe = w("PNRGW", "G001"); put("energy_2022", (pe[2022] / pe[2020] - 1) * 100, "IMF energy price index, 2022 vs 2020, %", 0)

# ---- WEO growth and inflation (today's vintage)
for a in ["G001", "G110", "G200", "USA", "G163", "GBR", "DEU", "JPN", "CHN", "IND", "RUS", "UKR", "BRA", "TUR", "ARG"]:
    g, i = w("NGDP_RPCH", a), w("PCPIPCH", a)
    for yy in (2021, 2022, 2023):
        put(f"gdp_{a}_{yy}", g[yy], f"WEO NGDP_RPCH {a} {yy}")
        put(f"cpi_{a}_{yy}", i[yy], f"WEO PCPIPCH {a} {yy}")

# ---- inflation forecasts vs outturn (IMF historical WEO forecasts)
import pandas as pd
h = pd.read_excel(ROOT / "data/raw/imf_weo_vintage/weohistorical.xlsx", sheet_name="pcpi_pch")
nm = {"G110": "Advanced Economies", "G200": "Emerging Market and Developing Economies", "USA": "United States", "G163": "Euro area", "IND": "India"}
rows = []
for code, n in nm.items():
    r = h[h.country == n].set_index("year")
    f21, s22 = float(r.loc[2022, "F2021pcpi_pch"]), float(r.loc[2022, "S2022pcpi_pch"])
    act = w("PCPIPCH", code)[2022]
    put(f"f21_{code}_2022", f21, f"{n}: October 2021 WEO forecast of 2022 inflation")
    put(f"s22_{code}_2022", s22, f"{n}: April 2022 WEO forecast of 2022 inflation")
    rows.append({"label": {"G110": "Advanced economies", "G200": "Emerging and developing", "USA": "United States", "G163": "Euro area", "IND": "India"}[code],
                 "oct2021": round(f21, 1), "apr2022": round(s22, 1), "actual": round(act, 1)})
obj = {"id": "derived/p7_inflation_forecasts", "label": "Inflation in 2022: IMF forecasts and outturn", "unit": "%",
       "source": "IMF WEO historical forecasts database (weohistorical.xlsx, sheet pcpi_pch: F2021 and S2022 columns) and WEO database, October 2026 (PCPIPCH)",
       "url": "https://www.imf.org/external/pubs/ft/weo/data/weohistorical.xlsx", "retrieved": "2026-11-22", "rows": rows,
       "notes": "Average annual consumer price inflation. India on a fiscal-year basis in the WEO."}
(ROOT / "data/js/derived/p7_inflation_forecasts.js").write_text(f'WE.register("derived/p7_inflation_forecasts",{json.dumps(obj, separators=(",", ":"))});\n')

# ---- India (author's dataset; fiscal years at start year)
for sid, k, nd in [("gdp_real_growth", "gdp", 1), ("cpi_inflation", "cpi", 1), ("cpi_food_inflation", "cpif", 1), ("repo_end", "repo", 2),
                   ("cab_gdp", "cab", 1), ("fx_reserves", "res", 0), ("centre_fd_gdp", "cfd", 1), ("gg_fd_gdp", "ggfd", 1),
                   ("inr_usd", "inr", 1), ("oil_imports", "oil", 0), ("imports_goods", "mg", 0), ("exports_goods", "xg", 0)]:
    s = ind(sid)
    for yy in range(2020, 2025):
        if s.get(yy) is not None:
            put(f"in_{k}_{yy}", s[yy], f"India {sid} {fy(yy)}", nd)

(C / "derived/phase7.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
