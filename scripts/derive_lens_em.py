"""Derived figures and series for chapters/lens-em.html (Part III, other emerging markets).
Output: data/clean/derived/lens_em.json and data/js/derived/em_fx13.js (BIS nominal effective exchange rates of the
2013 "fragile five", rebased to April 2013 = 100). India's WEO rows are fiscal years plotted at the starting year.
    .venv/bin/python scripts/derive_lens_em.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}
CAP = "2026-10"
SEVEN = ["BRA", "MEX", "IDN", "TUR", "ZAF", "RUS", "SAU"]
NAMES = {"BRA": "Brazil", "MEX": "Mexico", "IDN": "Indonesia", "TUR": "Türkiye", "ZAF": "South Africa", "RUS": "Russia",
         "SAU": "Saudi Arabia", "ARE": "UAE", "IND": "India", "CHN": "China", "G200": "EMDEs", "G001": "world", "USA": "US",
         "PHL": "Philippines", "EGY": "Egypt"}
MON = "January February March April May June July August September October November December".split()


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def mname(t):
    return f"{MON[int(t[5:7]) - 1]} {t[:4]}"


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


def W(code, area):
    d = json.loads((C / f"weo/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def WD(code, area):
    d = json.loads((C / f"wdi/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def B(ds, area):
    d = json.loads((C / f"bis/{ds}.json").read_text())["data"][area]
    return {t: v for t, v in d if v is not None and t <= CAP}


def avg(d, y0, y1):
    xs = [d[y] for y in range(y0, y1 + 1)]
    return sum(xs) / len(xs)


def pk(d, y0, y1, lo=False):
    ys = [y for y in d if y0 <= y <= y1]
    return (min if lo else max)(ys, key=d.get)


def peak(prefix, d, y0, y1, lab, lo=False, nd=1):
    y = pk(d, y0, y1, lo); put(prefix, d[y], f"{lab}, {'lowest' if lo else 'peak'} {y0}-{y1} ({y})", nd); put(prefix + "_y", y, "year", 0)


k3 = lambda a: a.lower()

# ---- growth (WEO October 2026)
for a in SEVEN + ["ARE", "IND", "CHN", "G200", "G001"]:
    g = W("NGDP_RPCH", a)
    for y0, y1 in ((2000, 2007), (2010, 2019), (2020, 2025), (2000, 2025)):
        put(f"g_avg_{k3(a)}_{y0 % 100:02d}{y1 % 100:02d}", avg(g, y0, y1), f"{NAMES[a]} real GDP growth, average {y0}-{y1} (WEO Oct 2026)")
for a, ys in (("BRA", (2015, 2016, 2020, 2025)), ("MEX", (2009, 2020, 2025, 2026)), ("IDN", (2020, 2025)), ("TUR", (2001, 2009, 2021, 2025)),
              ("ZAF", (2009, 2020, 2025)), ("RUS", (2009, 2015, 2022, 2023, 2024, 2025, 2026)), ("SAU", (2009, 2022, 2025, 2026)), ("ARE", (2026,)),
              ("G200", (2026,))):
    g = W("NGDP_RPCH", a)
    for y in ys:
        put(f"g_{k3(a)}_{y}", g[y], f"{NAMES[a]} real GDP growth, {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")

# ---- inflation
for a, ys in (("TUR", (2000, 2002, 2005, 2010, 2018, 2021, 2022, 2023, 2025, 2026)), ("BRA", (2002, 2003, 2015, 2025)), ("RUS", (2000, 2015, 2022, 2025)),
              ("ZAF", (2025,)), ("MEX", (2022, 2025)), ("IDN", (2005, 2025)), ("SAU", (2025,)), ("G200", (2022, 2025))):
    p = W("PCPIPCH", a)
    for y in ys:
        put(f"cpi_{k3(a)}_{y}", p[y], f"{NAMES[a]} consumer price inflation, {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")
peak("cpi_tur_pk", W("PCPIPCH", "TUR"), 2010, 2025, "Türkiye inflation")

# every year, for the seven and the UAE (growth and inflation)
for a in SEVEN + ["ARE"]:
    g, p = W("NGDP_RPCH", a), W("PCPIPCH", a)
    for y in range(2000, 2027):
        put(f"g_{k3(a)}_{y}", g[y], f"{NAMES[a]} real GDP growth, {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")
        put(f"cpi_{k3(a)}_{y}", p[y], f"{NAMES[a]} consumer price inflation, {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")

# ---- current account
for a, ys in (("SAU", (2008, 2015, 2022, 2025)), ("RUS", (2000, 2022, 2025)), ("TUR", (2022, 2025)), ("ZAF", (2025,)), ("BRA", (2025,)),
              ("IDN", (2013, 2025)), ("MEX", (2025,)), ("ARE", (2025,))):
    c = W("BCA_NGDPD", a)
    for y in ys:
        put(f"ca_{k3(a)}_{y}", c[y], f"{NAMES[a]} current account, % of GDP, {y} (WEO)")
peak("ca_sau_pk", W("BCA_NGDPD", "SAU"), 2000, 2014, "Saudi current account, % of GDP")
peak("ca_tur_lo", W("BCA_NGDPD", "TUR"), 2000, 2025, "Türkiye current account, % of GDP", lo=True)
peak("ca_zaf_lo", W("BCA_NGDPD", "ZAF"), 2000, 2025, "South Africa current account, % of GDP", lo=True)
peak("ca_bra_lo", W("BCA_NGDPD", "BRA"), 2005, 2025, "Brazil current account, % of GDP", lo=True)

# ---- public finances
for a, ys in (("BRA", (2013, 2025, 2031)), ("ZAF", (2008, 2025, 2031)), ("MEX", (2007, 2025)), ("IDN", (2000, 2012, 2025)),
              ("TUR", (2001, 2013, 2025)), ("RUS", (2007, 2025, 2031)), ("SAU", (2000, 2013, 2025, 2031)), ("IND", (2025,)), ("G200", (2025,))):
    d = W("GGXWDG_NGDP", a)
    for y in ys:
        put(f"debt_{k3(a)}_{y}", d[y], f"{NAMES[a]} general government gross debt, % of GDP, {y} (WEO{', projection' if y > 2025 else ''})")
for a, ys in (("SAU", (2008, 2015, 2016, 2025, 2026)), ("BRA", (2015, 2025)), ("RUS", (2008, 2025)), ("ZAF", (2025,)), ("ARE", (2015,))):
    d = W("GGXCNL_NGDP", a)
    for y in ys:
        put(f"bal_{k3(a)}_{y}", d[y], f"{NAMES[a]} general government net lending, % of GDP, {y} (WEO{', projection' if y > 2025 else ''})")
peak("debt_tur_pk", W("GGXWDG_NGDP", "TUR"), 2000, 2025, "Türkiye gross debt")

for a in SEVEN + ["ARE"]:
    for code, pre, lab in (("GGXWDG_NGDP", "debt", "general government gross debt"), ("GGXCNL_NGDP", "bal", "general government net lending"), ("BCA_NGDPD", "ca", "current account")):
        d = W(code, a)
        for y in range(2000, 2032):
            if y in d:
                put(f"{pre}_{k3(a)}_{y}", d[y], f"{NAMES[a]} {lab}, % of GDP, {y} (WEO{', projection' if y > 2025 else ''})")

# ---- income per person relative to the US (WDI, PPP, constant 2021 $)
us = WD("NY.GDP.PCAP.PP.KD", "USA")
for a in SEVEN + ["IND", "CHN"]:
    p = WD("NY.GDP.PCAP.PP.KD", a)
    for y in (2000, 2013, 2025):
        put(f"pcus_{k3(a)}_{y}", 100 * p[y] / us[y], f"{NAMES[a]} GDP per person (PPP) as % of the US, {y} (WDI)", 0)
    put(f"pc_{k3(a)}_2025", p[2025], f"{NAMES[a]} GDP per person, PPP constant 2021 $, 2025 (WDI)", 0)

# ---- weight in the world
sh = {a: W("PPPSH", a) for a in SEVEN + ["IND", "CHN"]}
for y in (2000, 2025, 2031):
    put(f"ppp_seven_{y}", sum(sh[a][y] for a in SEVEN), f"combined share of world GDP at PPP of the seven, {y} (WEO)")
    for a in ("IND", "CHN", "RUS", "BRA", "IDN"):
        put(f"ppp_{k3(a)}_{y}", sh[a][y], f"{NAMES[a]} share of world GDP at PPP, {y} (WEO)")
for y in (2000, 2011, 2025):
    put(f"ppp_bric_{y}", sum(W("PPPSH", a)[y] for a in ("BRA", "RUS", "IND", "CHN")), f"combined share of world GDP at PPP of Brazil, Russia, India and China, {y} (WEO Oct 2026)")
put("bal_sau_2022", W("GGXCNL_NGDP", "SAU")[2022], "Saudi Arabia general government net lending, % of GDP, 2022 (WEO)")
nd = {a: W("NGDPD", a) for a in SEVEN + ["ARE", "IND"]}
for a in SEVEN + ["ARE", "IND"]:
    put(f"gdpd_{k3(a)}_2025", nd[a][2025] / 1e3, f"{NAMES[a]} GDP, US$ trillion, 2025 (WEO)", 2)
put("gdpd_seven_2025", sum(nd[a][2025] for a in SEVEN) / 1e3, "combined GDP of the seven, US$ trillion, 2025", 2)
put("gdpd_bra_2011", nd["BRA"][2011] / 1e3, "Brazil GDP, US$ trillion, 2011 (WEO)", 2)
put("gdpd_rus_2013", nd["RUS"][2013] / 1e3, "Russia GDP, US$ trillion, 2013 (WEO)", 2)

# ---- policy rates (BIS WS_CBPOL, end of month)
def rate(prefix, area, t, lab):
    r = B("CBPOL", area); put(prefix, r[t], f"{lab} policy rate, end of {mname(t)} (BIS)", 2)


def rpeak(prefix, area, t0, t1, lab, lo=False):
    r = B("CBPOL", area); ts = [t for t in r if t0 <= t <= t1]
    t = (min if lo else max)(ts, key=r.get)
    put(prefix, r[t], f"{lab} policy rate, {'lowest' if lo else 'highest'} {t0} to {t1} ({mname(t)}, BIS)", 2); out[prefix]["month"] = mname(t)


rpeak("pr_br_pk15", "BR", "2014-01", "2017-12", "Brazil"); rpeak("pr_br_lo20", "BR", "2019-01", "2022-12", "Brazil", lo=True)
rpeak("pr_br_pk25", "BR", "2023-01", CAP, "Brazil"); rate("pr_br_last", "BR", CAP, "Brazil")
rpeak("pr_tr_lo21", "TR", "2021-01", "2023-05", "Türkiye", lo=True); rpeak("pr_tr_pk24", "TR", "2023-06", CAP, "Türkiye"); rate("pr_tr_last", "TR", CAP, "Türkiye")
rate("pr_tr_2021_08", "TR", "2021-08", "Türkiye"); rate("pr_tr_2023_05", "TR", "2023-05", "Türkiye")
rate("pr_ru_2014_11", "RU", "2014-11", "Russia"); rate("pr_ru_2014_12", "RU", "2014-12", "Russia"); rate("pr_ru_2022_01", "RU", "2022-01", "Russia")
rate("pr_ru_2022_02", "RU", "2022-02", "Russia"); rpeak("pr_ru_pk24", "RU", "2023-01", CAP, "Russia"); rate("pr_ru_last", "RU", CAP, "Russia")
rpeak("pr_mx_pk23", "MX", "2022-01", CAP, "Mexico"); rate("pr_mx_last", "MX", CAP, "Mexico")
rpeak("pr_za_pk", "ZA", "2022-01", CAP, "South Africa"); rate("pr_za_last", "ZA", CAP, "South Africa")
rate("pr_id_last", "ID", CAP, "Indonesia")

# ---- the 2013 "fragile five": BIS nominal effective exchange rates, April 2013 = 100
base = "2013-04"
fx = {}
for a in ("IN", "BR", "ID", "TR", "ZA"):
    s = B("EER_N", a)
    fx[a] = {t: 100 * v / s[base] for t, v in s.items() if "2012-01" <= t <= "2014-12"}
reg("em_fx13", {"id": "derived/em_fx13", "label": "Nominal effective exchange rate, April 2013 = 100", "unit": "April 2013 = 100", "freq": "M",
                "source": "Computed for this book from BIS effective exchange rates (WS_EER, nominal, broad basket, monthly averages), rebased to April 2013 = 100",
                "notes": "A fall means the currency weakened against a trade-weighted basket of currencies.",
                "data": {a: [[t, round(v, 1)] for t, v in sorted(s.items())] for a, s in fx.items()}})
NM2 = {"IN": "India", "BR": "Brazil", "ID": "Indonesia", "TR": "Türkiye", "ZA": "South Africa"}
for a, s in fx.items():
    t = min((t for t in s if "2013-05" <= t <= "2013-12"), key=s.get)
    put(f"fx13_{a.lower()}_lo", s[t] - 100, f"{NM2[a]} nominal effective exchange rate, change from April 2013 to its 2013 low ({mname(t)}), % (BIS)", 1); out[f"fx13_{a.lower()}_lo"]["month"] = mname(t)
    put(f"fx13_{a.lower()}_dec14", s["2014-12"] - 100, f"{NM2[a]} nominal effective exchange rate, change April 2013 to December 2014, % (BIS)", 1)

tr = B("EER_N", "TR")
put("fx18_tr", 100 * (tr["2018-09"] / tr["2018-01"] - 1), "Türkiye nominal effective exchange rate, % change January to September 2018 (BIS, monthly averages)")

# ---- remittances (WDI BX.TRF.PWKR.CD.DT, current US$)
rw = WD("BX.TRF.PWKR.CD.DT", "WLD")
for a in ("IND", "MEX", "PHL", "EGY"):
    r = WD("BX.TRF.PWKR.CD.DT", a)
    for y in (2000, 2025):
        put(f"rem_{k3(a)}_{y}", r[y] / 1e9, f"{NAMES[a]} personal remittances received, US$ bn, {y} (WDI)", 1)
ri = WD("BX.TRF.PWKR.CD.DT", "IND")
put("rem_ind_sh_2025", 100 * ri[2025] / rw[2025], "India share of world remittances received, %, 2025 (WDI)", 1)
put("rem_ind_gdp_2025", WD("BX.TRF.PWKR.DT.GD.ZS", "IND")[2025], "India remittances received, % of GDP, 2025 (WDI)", 1)
put("rem_wld_2025", rw[2025] / 1e9, "world personal remittances received, US$ bn, 2025 (WDI)", 0)

iso = set(json.loads((C / "weo/NGDP_RPCH.json").read_text())["data"])
rd = json.loads((C / "wdi/BX.TRF.PWKR.CD.DT.json").read_text())["data"]
top = lambda y: max(((dict(rd[a]).get(y) or 0), a) for a in rd if a in iso)[1]
since = min(y for y in range(2000, 2026) if all(top(z) == "IND" for z in range(y, 2026)))
put("rem_ind_top_since", since, "first year from which India has been the largest recipient of remittances every year (WDI, IMF-listed economies)", 0)
put("rem_mex_rank2_2025", 1 if sorted(((dict(rd[a]).get(2025) or 0), a) for a in rd if a in iso)[-2][1] == "MEX" else 0, "1 if Mexico was the second-largest recipient in 2025", 0)

(C / "derived/lens_em.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
