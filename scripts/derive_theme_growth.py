"""Derived figures and series for chapters/theme-growth.html. Output: data/clean/derived/theme_growth.json,
data/js/derived/tg_fcst5.js (five-years-ahead growth forecasts by WEO edition).
    .venv/bin/python scripts/derive_theme_growth.py
"""
import json
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:30s} {round(v, nd):>10}  {how}")


def lab(k, v, how=""):
    out[k] = {"value": v, "how": how}
    print(f"{k:30s} {v!s:>10}  {how}")


def W(i):
    return {a: {int(y): v for y, v in s} for a, s in json.loads((C / f"weo/{i}.json").read_text())["data"].items()}


gdp, sh, pc = W("NGDP_RPCH"), W("PPPSH"), W("PPPPC")
avg = lambda d, a, b: sum(d[y] for y in range(a, b + 1)) / (b - a + 1)

# ---- shares of world GDP at PPP
for a in ["USA", "CHN", "IND", "JPN", "G998", "G110", "G200", "G505", "G603", "G205"]:
    for y in (2000, 2007, 2019, 2025, 2031):
        put(f"sh_{a}_{y}", sh[a][y], f"WEO PPPSH {a} {y}, % of world GDP at PPP")
lab("sh_cross_year", next(y for y in range(2000, 2032) if sh["G200"][y] > sh["G110"][y]), "first year EMDE share of world PPP GDP exceeds AE share")
lab("sh_chn_usa_year", next(y for y in range(2000, 2032) if sh["CHN"][y] > sh["USA"][y]), "first year China's PPP share exceeds US share")

# ---- growth by period (WEO real GDP growth, simple averages of annual rates)
P = [(2000, 2007), (2008, 2019), (2010, 2019), (2020, 2025), (2026, 2031)]
for a in ["G001", "G110", "G200", "CHN", "IND", "USA", "G603", "G205", "G505"]:
    for x, y in P:
        put(f"g_{a}_{x}_{y}", avg(gdp[a], x, y), f"WEO NGDP_RPCH {a}, average of annual growth {x}-{y}")
for x, y in P:
    put(f"gap_{x}_{y}", avg(gdp["G200"], x, y) - avg(gdp["G110"], x, y), f"EMDE minus AE average growth {x}-{y}, percentage points")

# ---- income per person relative to the US (PPP, current international $)
for a in ["CHN", "IND", "BRA", "MEX", "ZAF", "IDN", "TUR", "RUS", "NGA", "G200", "G603", "G205", "JPN", "DEU", "KOR", "VNM", "BGD", "POL"]:
    for y in (2000, 2010, 2019, 2025, 2031):
        if a in pc and y in pc[a]:
            put(f"rel_{a}_{y}", pc[a][y] / pc["USA"][y] * 100, f"WEO PPPPC {a} as % of USA, {y}")

# ---- convergence test on WDI constant-PPP income per person
wdi = {a: {int(y): v for y, v in s} for a, s in json.loads((C / "wdi/NY.GDP.PCAP.PP.KD.json").read_text())["data"].items()}
econ = set(json.loads((C / "meta/weo_countries.json").read_text())["countries"]) 
econ = {c for c in econ if not c.startswith("G") or len(c) == 3 and c.isalpha() and c not in ("G001",)}
econ = {c for c in econ if c in wdi and not c[1:].isdigit()}
us = wdi["USA"]
poor = [c for c in econ if c != "USA" and 2000 in wdi[c] and wdi[c][2000] < 0.5 * us[2000]]
put("conv_n_poor", len(poor), "economies with WDI PPP income per person below half the US level in 2000 (WEO economies with WDI data)", 0)
rows = []
for x, y in [(2000, 2010), (2010, 2019), (2019, 2025)]:
    cs = [c for c in poor if x in wdi[c] and y in wdi[c]]
    gus = (us[y] / us[x]) ** (1 / (y - x)) - 1
    faster = [c for c in cs if (wdi[c][y] / wdi[c][x]) ** (1 / (y - x)) - 1 > gus]
    put(f"conv_share_{x}_{y}", len(faster) / len(cs) * 100, f"% of those economies whose income per person grew faster than the US's, {x}-{y} (n={len(cs)})", 0)
    put(f"conv_us_g_{x}_{y}", gus * 100, f"US growth of real income per person, % a year, {x}-{y}")
    med = sorted((wdi[c][y] / wdi[c][x]) ** (1 / (y - x)) * 100 - 100 for c in cs)[len(cs) // 2]
    put(f"conv_med_g_{x}_{y}", med, f"median growth of income per person among them, % a year, {x}-{y}")
    rows.append(len(faster) / len(cs) * 100)
put("wdi_last", max(us), "last year of WDI PPP per-capita data", 0)
# India vs world and China
for y in (2000, 2010, 2019, 2024):
    put(f"in_wld_{y}", wdi["IND"][y] / wdi["WLD"][y] * 100, f"India income per person (WDI, const PPP) as % of world, {y}", 0)
    put(f"in_chn_{y}", wdi["IND"][y] / wdi["CHN"][y] * 100, f"India as % of China, {y}", 0)
put("in_pc_x_0024", wdi["IND"][2024] / wdi["IND"][2000], "India income per person 2024 / 2000, times")
put("chn_pc_x_0024", wdi["CHN"][2024] / wdi["CHN"][2000], "China income per person 2024 / 2000, times")

# ---- the fading forecast: growth five years ahead in each WEO edition
h = pd.read_excel(ROOT / "data/raw/imf_weo_vintage/weohistorical.xlsx", sheet_name="ngdp_rpch")
names = {"G001": "World", "G110": "Advanced Economies", "G200": "Emerging Market and Developing Economies"}
ser = {k: [] for k in names}
for col in [c for c in h.columns if c.endswith("ngdp_rpch")]:
    yr, sf = int(col[1:5]), col[0]
    if yr < 2000: continue
    for k, nm in names.items():
        r = h[h.country == nm].set_index("year")[col]
        v = r.get(yr + 5)
        if v is not None and v != ".":
            ser[k].append([f"{yr}-{'04' if sf == 'S' else '10'}", round(float(v), 2)])
for v, p, tgt in [("WEO_2025_OCT_VINTAGE", "2025-10", 2030), ("WEO_2026_APR_VINTAGE", "2026-04", 2031)]:
    d = json.loads((C / f"weo_vintage/{v}__NGDP_RPCH.json").read_text())["data"]
    for k in names: ser[k].append([p, round(dict(d[k])[tgt], 2)])
for k in names: ser[k].append(["2026-10", round(gdp[k][2031], 2)])
for k in names:
    s = dict(ser[k])
    for p in ["2000-04", "2007-10", "2008-10", "2012-10", "2019-10", "2022-10", "2026-10"]:
        if p in s: put(f"f5_{k}_{p.replace('-', '_')}", s[p], f"{names[k]}: growth forecast five years ahead in the WEO of {p}")
missing = sorted(set(c for c in h.columns if c.endswith("ngdp_rpch") and int(c[1:5]) >= 2000) )
lab("f5_editions", f"{ser['G001'][0][0]} to {ser['G001'][-1][0]}, {len(ser['G001'])} editions", "")
obj = {"id": "derived/tg_fcst5", "source": "IMF, WEO historical forecasts database (weohistorical.xlsx, editions spring 2000 to fall 2022); WEO database vintages October 2025 and April 2026; WEO database, October 2026",
       "code": "IMF weohistorical.xlsx ngdp_rpch; WEO NGDP_RPCH vintages", "label": "Real GDP growth forecast for the year five years after each WEO edition",
       "unit": "%", "freq": "M", "url": "https://www.imf.org/external/pubs/ft/weo/data/weohistorical.xlsx", "retrieved": "2026-11-22",
       "notes": "Each point is the forecast, in a given spring (April) or fall (October) WEO, for growth five years after the year of publication. The country groups were defined as at each edition. Editions from 2023 to spring 2025 are not in the files held and are left as a gap.",
       "data": ser}
(ROOT / "data/js/derived/tg_fcst5.js").write_text(f'WE.register("derived/tg_fcst5",{json.dumps(obj, separators=(",", ":"))});\n')
(C / "derived/theme_growth.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
