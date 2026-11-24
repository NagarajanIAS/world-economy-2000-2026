"""Derived figures for chapters/lens-ssa.html (Part III, Sub-Saharan Africa).
Output: data/clean/derived/lens_ssa.json. WEO aggregate G603 = Sub-Saharan Africa; WDI aggregate SSF = Sub-Saharan Africa.
India's WEO rows are fiscal years plotted at the starting year; WDI rows for India are calendar years.
    .venv/bin/python scripts/derive_lens_ssa.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}
NAMES = {"G603": "Sub-Saharan Africa", "SSF": "Sub-Saharan Africa", "G001": "world", "WLD": "world", "G200": "EMDEs", "G110": "advanced economies",
         "NGA": "Nigeria", "ZAF": "South Africa", "ETH": "Ethiopia", "KEN": "Kenya", "GHA": "Ghana", "AGO": "Angola", "ZMB": "Zambia",
         "CIV": "Côte d'Ivoire", "RWA": "Rwanda", "SEN": "Senegal", "TZA": "Tanzania", "IND": "India", "CHN": "China", "SAS": "South Asia"}
COUNTRIES = ["NGA", "ZAF", "ETH", "KEN", "GHA", "AGO", "ZMB", "CIV", "RWA", "SEN", "TZA"]


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}


def W(code, area):
    d = json.loads((C / f"weo/{code}.json").read_text())["data"].get(area, [])
    return {int(t): v for t, v in d if v is not None}


def WD(code, area):
    d = json.loads((C / f"wdi/{code}.json").read_text())["data"].get(area, [])
    return {int(t): v for t, v in d if v is not None}


def avg(d, y0, y1):
    xs = [d[y] for y in range(y0, y1 + 1)]
    return sum(xs) / len(xs)


k = lambda a: a.lower()
proj = lambda y: ", projection" if y > 2025 else ""

# ---- every year: WEO growth, inflation, debt for the region and countries
for code, pre, lab in (("NGDP_RPCH", "g", "real GDP growth, %"), ("PCPIPCH", "cpi", "consumer price inflation, %"),
                       ("GGXWDG_NGDP", "debt", "general government gross debt, % of GDP"), ("GGXCNL_NGDP", "bal", "general government net lending, % of GDP")):
    for a in ["G603", "G001", "G200", "IND"] + COUNTRIES:
        d = W(code, a)
        for y in range(2000, 2032):
            if y in d:
                put(f"{pre}_{k(a)}_{y}", d[y], f"{NAMES[a]} {lab}, {y} (WEO Oct 2026{proj(y)})")
ds = W("DS_BX", "G603")
for y in range(2000, 2028):
    put(f"ds_{y}", ds[y], f"Sub-Saharan Africa external debt service, % of exports of goods and services, {y} (WEO{proj(y)})")
y = min((y for y in range(2005, 2020)), key=ds.get); put("ds_lo", ds[y], f"SSA debt service, % of exports, lowest 2005-2019 ({y})"); put("ds_lo_y", y, "year", 0)

for a in ["G603", "G001", "G200", "IND", "CHN"] + COUNTRIES:
    g = W("NGDP_RPCH", a)
    for y0, y1 in ((2000, 2014), (2015, 2025), (2000, 2025), (2004, 2008), (2010, 2014)):
        put(f"g_avg_{k(a)}_{y0 % 100:02d}{y1 % 100:02d}", avg(g, y0, y1), f"{NAMES[a]} real GDP growth, average {y0}-{y1} (WEO Oct 2026)")
for a in ["G603", "NGA", "GHA", "ZMB", "ETH", "KEN", "AGO"]:
    d = W("GGXWDG_NGDP", a)
    y = min((y for y in range(2005, 2015) if y in d), key=d.get); put(f"debt_{k(a)}_lo", d[y], f"{NAMES[a]} gross debt, lowest 2005-2014 ({y})"); put(f"debt_{k(a)}_lo_y", y, "year", 0)
    y = max((y for y in range(2015, 2026) if y in d), key=d.get); put(f"debt_{k(a)}_pk", d[y], f"{NAMES[a]} gross debt, highest 2015-2025 ({y})"); put(f"debt_{k(a)}_pk_y", y, "year", 0)

# ---- weight in the world
sh = W("PPPSH", "G603")
for y in (2000, 2014, 2025, 2031):
    put(f"ppp_ssa_{y}", sh[y], f"Sub-Saharan Africa share of world GDP at PPP, %, {y} (WEO{proj(y)})")
    put(f"ppp_ind_{y}", W("PPPSH", "IND")[y], f"India share of world GDP at PPP, %, {y} (WEO{proj(y)})")
put("gdpd_nga_2014", W("NGDPD", "NGA")[2014] / 1e3, "Nigeria GDP, US$ trillion, 2014 (WEO)", 2)
put("gdpd_nga_2025", W("NGDPD", "NGA")[2025] / 1e3, "Nigeria GDP, US$ trillion, 2025 (WEO)", 2)
put("gdpd_zaf_2025", W("NGDPD", "ZAF")[2025] / 1e3, "South Africa GDP, US$ trillion, 2025 (WEO)", 2)

# ---- income per person (WDI, PPP constant 2021 $)
pc = {a: WD("NY.GDP.PCAP.PP.KD", a) for a in ("SSF", "WLD", "IND", "SAS")}
for y in (2000, 2014, 2025):
    put(f"pc_ssa_{y}", pc["SSF"][y], f"Sub-Saharan Africa GDP per person, PPP constant 2021 $, {y} (WDI)", 0)
    put(f"pc_ind_{y}", pc["IND"][y], f"India GDP per person, PPP constant 2021 $, {y} (WDI)", 0)
    put(f"pcw_ssa_{y}", 100 * pc["SSF"][y] / pc["WLD"][y], f"Sub-Saharan Africa GDP per person as % of world, {y} (WDI)", 0)
put("pc_ssa_g_0014", 100 * ((pc["SSF"][2014] / pc["SSF"][2000]) ** (1 / 14) - 1), "SSA GDP per person (PPP), average growth 2000-2014, % a year (WDI)")
put("pc_ssa_g_1425", 100 * ((pc["SSF"][2025] / pc["SSF"][2014]) ** (1 / 11) - 1), "SSA GDP per person (PPP), average growth 2014-2025, % a year (WDI)")
put("pc_ssa_2025_vs_2014", 100 * (pc["SSF"][2025] / pc["SSF"][2014] - 1), "SSA GDP per person (PPP), % change 2014 to 2025 (WDI)")
cross = min(y for y in pc["IND"] if y in pc["SSF"] and pc["IND"][y] > pc["SSF"][y] and y >= 1990)
put("pc_ind_pass_y", cross, "first year from 1990 India's GDP per person (PPP) exceeds the SSA average (WDI)", 0)
put("pc_ind_ssa_2025", pc["IND"][2025] / pc["SSF"][2025], "India GDP per person as a multiple of the SSA average, 2025 (WDI)", 1)
put("pc_ind_ssa_2000", pc["IND"][2000] / pc["SSF"][2000], "India GDP per person as a multiple of the SSA average, 2000 (WDI)", 2)

# ---- poverty ($3.00 a day, 2021 PPP) and the share of the world's poor
pv, pop = {a: WD("SI.POV.DDAY", a) for a in ("SSF", "WLD", "IND", "SAS")}, {a: WD("SP.POP.TOTL", a) for a in ("SSF", "WLD", "IND", "SAS")}
for y in (2000, 2014, 2024):
    put(f"pov_ssa_{y}", pv["SSF"][y], f"SSA share of population below $3.00 a day, %, {y} (WDI)")
    put(f"pov_wld_{y}", pv["WLD"][y], f"world share of population below $3.00 a day, %, {y} (WDI)")
    put(f"poor_ssa_{y}", pv["SSF"][y] * pop["SSF"][y] / 1e8, f"SSA people below $3.00 a day, million, {y} (WDI rate x population)", 0)
    put(f"poorsh_ssa_{y}", 100 * pv["SSF"][y] * pop["SSF"][y] / (pv["WLD"][y] * pop["WLD"][y]), f"SSA share of the world's people below $3.00 a day, %, {y} (own arithmetic from WDI)", 0)
put("pov_ind_2023", pv["IND"][2023], "India share of population below $3.00 a day, %, 2023 (WDI)")
put("pov_wld_last_y", max(pv["WLD"]), "latest year of the WDI world poverty estimate", 0)

# ---- people
for y in (2000, 2025):
    put(f"popsh_ssa_{y}", 100 * pop["SSF"][y] / pop["WLD"][y], f"SSA share of world population, %, {y} (WDI)")
    put(f"pop_ssa_{y}", pop["SSF"][y] / 1e9, f"SSA population, billion, {y} (WDI)", 2)
    put(f"pop_ind_{y}", pop["IND"][y] / 1e9, f"India population, billion, {y} (WDI)", 2)
tf = {a: WD("SP.DYN.TFRT.IN", a) for a in ("SSF", "WLD", "IND")}
ly = max(tf["SSF"])
for a in ("SSF", "WLD", "IND"):
    put(f"tfr_{k(a)}_2000", tf[a][2000], f"{NAMES[a] if a in NAMES else a} fertility rate, births per woman, 2000 (WDI)", 2)
    put(f"tfr_{k(a)}_last", tf[a][ly], f"{NAMES.get(a, a)} fertility rate, births per woman, {ly} (WDI)", 2)
put("tfr_last_y", ly, "latest year of the fertility series", 0)
wa = {a: WD("SP.POP.1564.TO.ZS", a) for a in ("SSF", "IND")}
for a in ("SSF", "IND"):
    for y in (2000, 2025):
        put(f"wa_{k(a)}_{y}", wa[a][y], f"{NAMES[a]} population aged 15-64, % of total, {y} (WDI)")
cel = WD("IT.CEL.SETS.P2", "SSF")
put("cel_ssa_2000", cel[2000], "SSA mobile subscriptions per 100 people, 2000 (WDI)"); put("cel_ssa_2025", cel[2025], "SSA mobile subscriptions per 100 people, 2025 (WDI)", 0)
oda = WD("DT.ODA.ODAT.CD", "SSF")
put("oda_ssa_2000", oda[2000] / 1e9, "net ODA received by SSA, US$ bn, 2000 (WDI)"); put("oda_ssa_last", oda[max(oda)] / 1e9, f"net ODA received by SSA, US$ bn, {max(oda)} (WDI)"); put("oda_ssa_last_y", max(oda), "year", 0)

(C / "derived/lens_ssa.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
for kk in [x for x in out if not any(x.startswith(p) for p in ("g_", "cpi_", "debt_", "bal_", "ds_2"))]:
    print(f"{kk:24s} {out[kk]['value']}")
