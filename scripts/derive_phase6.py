"""Derived figures quoted in chapters/phase-6.html. Output: data/clean/derived/phase6.json,
and the scarring paths as a loadable series: data/js/derived/p6_scarring.js.
    .venv/bin/python scripts/derive_phase6.py
"""
import csv, json
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

# ---- quarterly real GDP relative to 2019Q4 (OECD QNA; euro area from FRED/Eurostat)
q = {k: dict(v) for k, v in json.loads((C / "oecd/QNA_GDP.json").read_text())["data"].items()}
q["EA"] = S("fred/CLVMNACSCAB1GQEA19.json")
names = {"USA": "us", "EA": "ea", "GBR": "uk", "JPN": "jp", "IND": "in", "DEU": "de", "BRA": "br"}
for a, s in names.items():
    base = q[a]["2019-10"]
    put(f"q_{s}_2020q2", (q[a]["2020-04"] / base - 1) * 100, f"{a} real GDP 2020Q2 vs 2019Q4, % (seasonally adjusted)")
    back = next((p for p in sorted(q[a]) if p > "2020-01" and q[a][p] >= base), None)
    lab(f"q_{s}_back", back and f"{back[:4]}Q{(int(back[5:7]) - 1) // 3 + 1}", f"{a}: first quarter at or above 2019Q4 level")

# ---- labour market and oil
u = S("fred/UNRATE.json")
put("us_u_2020_02", u["2020-02"], "US unemployment rate Feb 2020, %")
put("us_u_2020_04", u["2020-04"], "US unemployment rate Apr 2020, %")
wti = [(d, float(v)) for d, v in list(csv.reader(open(ROOT / "data/raw/fred/DCOILWTICO.csv")))[1:] if v not in ("", ".")]
mn = min((x for x in wti if x[0].startswith("2020")), key=lambda x: x[1])
put("wti_min", mn[1], f"FRED DCOILWTICO daily low in 2020 ({mn[0]}), US$/bbl", 2)
lab("wti_min_date", mn[0], "date of WTI low")
b = S("fred/DCOILBRENTEU.json")
put("brent_2020_01", b["2020-01"], "Brent Jan 2020 monthly average", 0)
put("brent_2020_04", b["2020-04"], "Brent Apr 2020 monthly average", 0)
put("brent_2021_12", b["2021-12"], "Brent Dec 2021 monthly average", 0)

# ---- growth (WEO, today's vintage)
for a in ["G001", "G110", "G200", "G163", "USA", "GBR", "JPN", "CHN", "IND", "BRA", "ZAF", "DEU", "ITA", "ESP", "FRA", "MEX", "IDN", "G603"]:
    g = w("NGDP_RPCH", a)
    for y in (2019, 2020, 2021):
        put(f"gdp_{a}_{y}", g[y], f"WEO NGDP_RPCH {a} {y}")
gw = w("NGDP_RPCH", "G001")
put("gdp_G001_2009", gw[2009], "WEO NGDP_RPCH G001 2009")

# ---- fiscal: general government net lending, % of GDP
fis = {}
for a in ["USA", "GBR", "JPN", "CAN", "DEU", "FRA", "ITA", "ESP", "CHN", "IND", "BRA", "ZAF", "MEX", "IDN", "G110", "G200", "G163"]:
    g = w("GGXCNL_NGDP", a)
    put(f"bal_{a}_2019", g[2019], f"WEO GGXCNL_NGDP {a} 2019")
    put(f"bal_{a}_2020", g[2020], f"WEO GGXCNL_NGDP {a} 2020")
    put(f"dbal_{a}", g[2020] - g[2019], f"WEO GGXCNL_NGDP {a}, change 2019 to 2020, points of GDP")
    fis[a] = round(g[2020] - g[2019], 1)
for a in ["USA", "GBR", "JPN", "ITA", "G110", "G200", "CHN", "IND"]:
    d = w("GGXWDG_NGDP", a)
    put(f"debt_{a}_2019", d[2019], f"WEO GGXWDG_NGDP {a} 2019", 0)
    put(f"debt_{a}_2020", d[2020], f"WEO GGXWDG_NGDP {a} 2020", 0)
print("fiscal chart values:", fis)

# ---- central bank balance sheets (FRED monthly averages)
for sid, k, unit, div in [("WALCL", "fed", "US$ trillion", 1e6), ("ECBASSETSW", "ecb", "EUR trillion", 1e6), ("JPNASSETS", "boj", "yen trillion", 1e4)]:
    s = S(f"fred/{sid}.json")
    put(f"{k}_2020_02", s["2020-02"] / div, f"{sid} Feb 2020, {unit}", 2)
    pk = max((p for p in s if "2020-01" <= p <= "2022-12"), key=lambda p: s[p])
    put(f"{k}_peak", s[pk] / div, f"{sid} peak monthly average 2020-22 ({pk}), {unit}", 2)
    lab(f"{k}_peak_month", pk, f"{sid} peak month")
    put(f"{k}_2021_12", s["2021-12"] / div, f"{sid} Dec 2021, {unit}", 2)
    put(f"{k}_x_2021_12", s["2021-12"] / s["2020-02"], f"{sid} Dec 2021 / Feb 2020, times", 2)

# ---- scarring: real GDP level, 2019 = 100, October 2019 WEO path vs today's outturn
import pandas as pd
h = pd.read_excel(ROOT / "data/raw/imf_weo_vintage/weohistorical.xlsx", sheet_name="ngdp_rpch")
groups = {"G001": "World", "G110": "Advanced Economies", "G200": "Emerging Market and Developing Economies", "IND": "India"}
series = {}
for code, nm in groups.items():
    r = h[h.country == nm].set_index("year")["F2019ngdp_rpch"]
    pre, act = [[2019, 100.0]], [[2019, 100.0]]
    g = w("NGDP_RPCH", code)
    for y in range(2020, 2025):
        pre.append([y, round(pre[-1][1] * (1 + float(r[y]) / 100), 2)])
        act.append([y, round(act[-1][1] * (1 + g[y] / 100), 2)])
    series[code + "_pre"], series[code] = pre, act
    put(f"scar_{code}_2024", (act[-1][1] / pre[-1][1] - 1) * 100, f"{nm}: 2024 real GDP level, today's WEO vs October 2019 WEO path, % gap")
    put(f"pre19_{code}_2020", float(r[2020]), f"{nm}: October 2019 WEO projection for 2020 growth")
obj = {"id": "derived/p6_scarring", "source": "IMF, WEO historical forecasts database (October 2019 vintage) and WEO database, October 2026",
       "code": "IMF weohistorical.xlsx F2019ngdp_rpch; WEO NGDP_RPCH", "label": "Real GDP level, 2019 = 100: October 2019 projection and outturn",
       "unit": "2019 = 100", "freq": "A", "url": "https://www.imf.org/external/pubs/ft/weo/data/weohistorical.xlsx", "retrieved": "2026-11-22",
       "notes": "Levels chained from annual growth rates. The October 2019 path uses that edition's growth projections for 2020-2024; the outturn uses today's figures, whose PPP weights differ.",
       "data": series}
(ROOT / "data/js/derived").mkdir(parents=True, exist_ok=True)
(ROOT / "data/js/derived/p6_scarring.js").write_text(f'WE.register("derived/p6_scarring",{json.dumps(obj, separators=(",", ":"))});\n')

# ---- India (author's dataset; fiscal years plotted at start year)
for sid, k, nd in [("gdp_real_growth", "gdp", 1), ("cpi_inflation", "cpi", 1), ("cpi_food_inflation", "cpif", 1), ("repo_end", "repo", 2),
                   ("cab_gdp", "cab", 1), ("fx_reserves", "res", 0), ("gg_fd_gdp", "ggfd", 1), ("centre_fd_gdp", "cfd", 1),
                   ("gg_debt_gdp", "ggdebt", 1), ("fdi_net", "fdi", 1), ("fpi_net", "fpi", 1), ("inr_usd", "inr", 1)]:
    s = ind(sid)
    for y in range(2018, 2023):
        if y in s and s[y] is not None:
            put(f"in_{k}_{y}", s[y], f"India {sid} {fy(y)}", nd)

(C / "derived").mkdir(exist_ok=True)
(C / "derived/phase6.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
