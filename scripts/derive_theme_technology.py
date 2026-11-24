"""Derived figures and series for chapters/theme-technology.html.
Output: data/clean/derived/theme_technology.json and data/js/derived/te_gdphrs.js (OECD GDP per hour worked, 2000 = 100),
te_tfp.js (Penn World Table 11.0 TFP at constant national prices, 2000 = 100), te_ictx.js (ICT services exports, US$ bn).
    .venv/bin/python scripts/derive_theme_technology.py
"""
import csv, json, statistics
from collections import defaultdict
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def cagr(a, b, y0, y1):
    return 100 * ((b / a) ** (1 / (y1 - y0)) - 1)


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


W = lambda i: {a: dict(v) for a, v in json.loads((C / f"wdi/{i}.json").read_text())["data"].items()}
F = lambda s: json.loads((C / f"fred/{s}.json").read_text())["data"]["US"]

# ---- US labour productivity (BLS output per hour, nonfarm business) and TFP (private nonfarm business), by period
q = defaultdict(list)
for d, v in F("OPHNFB"):
    q[int(d[:4])].append(v)
lp = {y: statistics.fmean(v) for y, v in q.items() if len(v) == 4}
tfp = {int(d[:4]): v for d, v in F("MFPNFBS")}
PER = [(1948, 1973), (1973, 1995), (1995, 2004), (2004, 2019), (2019, 2025)]
for a, b in PER:
    put(f"uslp_{a}_{b}", cagr(lp[a], lp[b], a, b), f"US nonfarm business output per hour, average annual growth {a}-{b}, % (annual averages of quarterly index, BLS via FRED OPHNFB)", 1)
    put(f"ustfp_{a}_{b}", cagr(tfp[a], tfp[b], a, b), f"US private nonfarm business TFP, average annual growth {a}-{b}, % (BLS via FRED MFPNFBS)", 1)
for y in (2023, 2024, 2025):
    put(f"uslp_g_{y}", 100 * (lp[y] / lp[y - 1] - 1), f"US output per hour growth, {y} on {y-1}, % (annual averages)", 1)
g9504 = (lp[2004] / lp[1995]) ** (1 / 9)
put("uslp_path_higher", 100 * (lp[2004] * g9504 ** 21 / lp[2025] - 1),
    "how much higher US output per hour would have been in 2025 had 1995-2004 growth continued from 2004, %", 0)

# ---- OECD productivity database: GDP per hour worked, chain-linked volumes, national currency (index 2000 = 100)
rows = list(csv.DictReader(open(ROOT / "data/raw/oecd/pdb_gdphrs.csv")))
gh, ppp = defaultdict(dict), defaultdict(dict)
for r in rows:
    a = r["REF_AREA: Reference area"].split(":")[0]
    if not r["MEASURE: Measure"].startswith("GDPHRS:") or not r["TRANSFORMATION: Transformation"].startswith("N:"):
        continue
    y, v = int(r["TIME_PERIOD: Time period"]), float(r["OBS_VALUE"])
    if r["UNIT_MEASURE: Unit of measure"].startswith("XDC_H") and r["PRICE_BASE: Price base"].startswith("LR:"):
        gh[a][y] = v
    if r["UNIT_MEASURE: Unit of measure"].startswith("USD_PPP_H") and r["PRICE_BASE: Price base"].startswith("V:"):
        ppp[a][y] = v
AREAS = ["USA", "EA20", "GBR", "JPN", "KOR", "DEU", "FRA", "ITA", "CAN"]
for a in AREAS:
    s = gh[a]
    for y0, y1 in ((2000, 2007), (2007, 2019), (2019, 2025), (2000, 2025)):
        if y0 in s and y1 in s:
            put(f"gh_{a}_{y0}_{y1}", cagr(s[y0], s[y1], y0, y1), f"GDP per hour worked, average annual growth {y0}-{y1}, %, {a} (OECD PDB)", 1)
    if 1995 in s:
        put(f"gh_{a}_1995_2007", cagr(s[1995], s[2007], 1995, 2007), f"GDP per hour worked, average annual growth 1995-2007, %, {a}", 1)
    put(f"ghx_{a}", 100 * s[2025] / s[2000], f"GDP per hour worked 2025, index 2000 = 100, {a}", 0)
ly = max(y for y in ppp["USA"] if all(y in ppp[a] for a in ("EA20", "GBR", "JPN", "KOR", "DEU")))
out["ppp_year"] = {"value": ly, "how": "latest year with PPP levels for all"}
for a in AREAS:
    if ly in ppp[a]:
        put(f"pph_{a}", ppp[a][ly], f"GDP per hour worked, current PPP US$, {a} {ly}", 0)
        put(f"ppr_{a}", 100 * ppp[a][ly] / ppp["USA"][ly], f"GDP per hour worked relative to US, %, {a} {ly}", 0)
reg("te_gdphrs", {"id": "derived/te_gdphrs", "source": "OECD Productivity Database (OECD data API, DSD_PDB@DF_PDB 2.0)",
    "code": "GDPHRS, total economy, chain-linked volumes, national currency; rebased 2000 = 100",
    "label": "GDP per hour worked, index 2000 = 100", "unit": "index, 2000 = 100", "freq": "A",
    "url": "https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_PDB@DF_PDB,2.0/", "retrieved": "2026-11-23",
    "notes": "Rebased from the OECD's 2020 = 100 volume index. Euro area = 20 members.",
    "data": {a: [[str(y), round(100 * v / gh[a][2000], 1)] for y, v in sorted(gh[a].items())] for a in AREAS}})

# ---- Penn World Table 11.0: TFP at constant national prices (rtfpna, 2017 = 1); labour productivity rgdpna / emp
wb = openpyxl.load_workbook(ROOT / "data/raw/pwt/pwt110.xlsx", read_only=True)
it = wb["Data"].iter_rows(values_only=True); h = next(it); ix = {k: i for i, k in enumerate(h)}
pt, pl = defaultdict(dict), defaultdict(dict)
for r in it:
    c, y = r[ix["countrycode"]], r[ix["year"]]
    if r[ix["rtfpna"]] is not None:
        pt[c][y] = r[ix["rtfpna"]]
    if r[ix["rgdpna"]] and r[ix["emp"]]:
        pl[c][y] = r[ix["rgdpna"]] / r[ix["emp"]]
PA = ["USA", "DEU", "GBR", "JPN", "FRA", "ITA", "KOR", "IND", "CHN", "BRA"]
for a in PA:
    for y0, y1 in ((1990, 2000), (2000, 2007), (2010, 2019), (2000, 2023)):
        put(f"tfp_{a}_{y0}_{y1}", cagr(pt[a][y0], pt[a][y1], y0, y1), f"TFP (PWT 11.0 rtfpna), average annual growth {y0}-{y1}, %, {a}", 1)
        put(f"lpw_{a}_{y0}_{y1}", cagr(pl[a][y0], pl[a][y1], y0, y1), f"real GDP per worker (PWT 11.0 rgdpna/emp), average annual growth {y0}-{y1}, %, {a}", 1)
    put(f"tfpx_{a}", 100 * pt[a][2023] / pt[a][2000], f"TFP 2023, index 2000 = 100, {a} (PWT 11.0)", 0)
reg("te_tfp", {"id": "derived/te_tfp", "source": "Penn World Table 11.0 (Groningen Growth and Development Centre, October 2025)",
    "code": "PWT 11.0 rtfpna (TFP at constant national prices, 2017 = 1), rebased 2000 = 100",
    "label": "Total factor productivity, index 2000 = 100", "unit": "index, 2000 = 100", "freq": "A",
    "url": "https://www.rug.nl/ggdc/productivity/pwt/", "retrieved": "2026-11-23",
    "notes": "Rebased from the Penn World Table's 2017 = 1.",
    "data": {a: [[str(y), round(100 * v / pt[a][2000], 1)] for y, v in sorted(pt[a].items()) if y >= 1990] for a in PA}})

# ---- US ICT investment share of GDP (information processing equipment and software / GDP)
ict, gdp = dict(F("A679RC1Q027SBEA")), dict(F("GDP"))
ann = defaultdict(list)
for d in ict:
    if d in gdp:
        ann[int(d[:4])].append(100 * ict[d] / gdp[d])
for y in (1980, 1990, 2000, 2010, 2019, 2024, 2025):
    put(f"usict_{y}", statistics.fmean(ann[y]), f"US private investment in information processing equipment and software, % of GDP, {y} (annual average of quarters)", 1)
put("usict_last", 100 * ict["2026-07"] / gdp["2026-07"], "same, 2026 Q3", 1)

# ---- diffusion: internet, mobile, broadband, R&D, researchers, high-tech exports
net, mob, bb, rd = W("IT.NET.USER.ZS"), W("IT.CEL.SETS.P2"), W("IT.NET.BBND.P2"), W("GB.XPD.RSDV.GD.ZS")
res, htx, pop = W("SP.POP.SCIE.RD.P6"), W("TX.VAL.TECH.MF.ZS"), W("SP.POP.TOTL")
for a in ("WLD", "SSF", "IND", "CHN", "USA", "LIC", "HIC"):
    for y in (2000, 2005, 2010, 2015, 2019, 2024, 2025):
        if y in net.get(a, {}):
            put(f"net_{a}_{y}", net[a][y], f"individuals using the internet, % of population, {a} {y}", 0 if a != "IND" else 1)
        if y in mob.get(a, {}):
            put(f"mob_{a}_{y}", mob[a][y], f"mobile cellular subscriptions per 100 people, {a} {y}", 0)
    if a in ("WLD", "IND", "CHN", "USA") and 2024 in net.get(a, {}) and 2024 in pop.get(a, {}):
        put(f"netn_{a}_2024", net[a][2024] * pop[a][2024] / 1e8, f"internet users, millions, {a} 2024 (rate x population)", 0)
put("netoff_WLD_2025", (100 - net["WLD"][2025]) / 100 * pop["WLD"][2024] / 1e9 if 2025 not in pop["WLD"] else (100 - net["WLD"][2025]) / 100 * pop["WLD"][2025] / 1e9,
    "people not using the internet, billions, world 2025 (share offline x population)", 1)
for a in ("IND", "CHN", "USA", "WLD"):
    for y in (2010, 2015, 2024):
        if y in bb.get(a, {}):
            put(f"bb_{a}_{y}", bb[a][y], f"fixed broadband subscriptions per 100 people, {a} {y}", 1)
for a in ("WLD", "USA", "CHN", "KOR", "EUU", "JPN", "IND", "GBR", "DEU", "ISR"):
    s = rd.get(a, {})
    for y in (2000, 2010, 2019, 2020, 2022, 2023):
        if y in s:
            put(f"rd_{a}_{y}", s[y], f"R&D spending, % of GDP, {a} {y}", 2)
    if s:
        put(f"rd_{a}_last", s[max(s)], f"R&D spending, % of GDP, {a} latest ({max(s)})", 2); out[f"rd_{a}_last_yr"] = {"value": max(s), "how": ""}
for a in ("WLD", "IND", "CHN", "USA", "KOR"):
    s = res.get(a, {})
    if s:
        put(f"res_{a}_last", s[max(s)], f"researchers per million people, {a} {max(s)}", 0); out[f"res_{a}_last_yr"] = {"value": max(s), "how": ""}
for a in ("WLD", "IND", "CHN", "USA"):
    s = htx.get(a, {})
    for y in (2010, 2024):
        if y in s:
            put(f"htx_{a}_{y}", s[y], f"high-technology exports, % of manufactured exports, {a} {y}", 0)

# ---- ICT services exports (WDI BX.GSR.CCIS.ZS x BX.GSR.NFSV.CD), US$ bn
z, sv = W("BX.GSR.CCIS.ZS"), W("BX.GSR.NFSV.CD")
IX = ["IND", "IRL", "CHN", "USA", "ISR", "WLD"]
ictx = {a: {y: z[a][y] * sv[a][y] / 1e11 for y in sorted(z.get(a, {})) if y in sv.get(a, {}) and y >= 2000} for a in IX}
for a in IX:
    for y in (2000, 2005, 2010, 2019, 2024):
        if y in ictx[a]:
            put(f"ictx_{a}_{y}", ictx[a][y], f"ICT services exports, US$ billion, {a} {y}", 0 if ictx[a][y] >= 10 else 1)
for y in (2000, 2010, 2024):
    put(f"ictsh_IND_{y}", 100 * ictx["IND"][y] / ictx["WLD"][y], f"India's share of world ICT services exports, % {y}", 1)
put("ictsv_IND_2024", z["IND"][2024], "ICT services, % of India's services exports, 2024", 0)
reg("te_ictx", {"id": "derived/te_ictx", "source": "World Bank, World Development Indicators (from IMF balance of payments statistics)",
    "code": "WDI BX.GSR.CCIS.ZS x BX.GSR.NFSV.CD", "label": "Exports of ICT services (telecommunications, computer and information services), US$ billion",
    "unit": "US$ bn", "freq": "A", "url": "https://data.worldbank.org/indicator/BX.GSR.CCIS.ZS", "retrieved": "2026-11-23",
    "notes": "ICT share of service exports times service exports, calendar years. Ireland's figures include the exports of multinational technology firms based there.",
    "data": {a: [[str(y), round(v, 1)] for y, v in ictx[a].items()] for a in IX if a != "WLD"}})

# ---- India
gdppc = W("NY.GDP.PCAP.PP.KD")
put("tfpsh_IND_2000_2023", 100 * out["tfp_IND_2000_2023"]["value"] / out["lpw_IND_2000_2023"]["value"], "TFP growth as % of labour-productivity growth, India 2000-2023 (PWT, rough)", 0)
for y in (2015, 2019, 2024, 2025):
    if y in net["IND"]:
        put(f"netind_{y}", net["IND"][y], f"India internet users, % {y}", 1)
(C / "derived/theme_technology.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
