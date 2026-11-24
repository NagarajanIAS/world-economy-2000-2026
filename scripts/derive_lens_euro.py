"""Derived figures and series for chapters/lens-euro.html (Part III, euro area).
Output: data/clean/derived/lens_euro.json and data/js/derived/ea_inr.js (rupees per euro, monthly, computed from FRED
DEXINUS and DEXUSEU).
    .venv/bin/python scripts/derive_lens_euro.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
out = {}
CAP = "2026-10"   # last complete month


def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}
    print(f"{k:28s} {round(v, nd):>12}  {how}")


def reg(name, obj):
    (ROOT / f"data/js/derived/{name}.js").write_text(f'WE.register("derived/{name}",{json.dumps(obj, separators=(",", ":"))});\n')


def W(code, area="G163"):
    d = json.loads((C / f"weo/{code}.json").read_text())["data"][area]
    return {int(t): v for t, v in d if v is not None}


def M(path, area=None):
    d = json.loads((C / f"{path}.json").read_text())["data"]
    s = d[area] if area else list(d.values())[0]
    return {t: v for t, v in s if v is not None and t <= CAP}


def avg(d, y0, y1):
    xs = [d[y] for y in range(y0, y1 + 1)]
    return sum(xs) / len(xs)


def mname(t):
    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][int(t[5:]) - 1] + " " + t[:4]


# ---- growth, inflation, unemployment (WEO October 2026; actual data to 2025)
g = W("NGDP_RPCH")
for y in (2000, 2007, 2009, 2010, 2012, 2013, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2031):
    put(f"g_{y}", g[y], f"euro-area real GDP growth {y} (WEO Oct 2026{', projection' if y > 2025 else ''})")
put("g_avg_0007", avg(g, 2000, 2007), "euro-area growth, average 2000-07")
put("g_avg_1019", avg(g, 2010, 2019), "euro-area growth, average 2010-19")
put("g_avg_2325", avg(g, 2023, 2025), "euro-area growth, average 2023-25")
us = W("NGDP_RPCH", "USA")
put("g_us_avg_1019", avg(us, 2010, 2019), "US growth, average 2010-19")
put("g_us_avg_2325", avg(us, 2023, 2025), "US growth, average 2023-25")
for a in ("DEU", "ITA"):
    s = W("NGDP_RPCH", a)
    put(f"g_{a}_avg_1925", avg(s, 2019, 2025), f"{a} growth, average 2019-25")
p = W("PCPIPCH")
for y in (2009, 2015, 2020, 2022, 2023, 2025, 2026):
    put(f"cpi_{y}", p[y], f"euro-area HICP inflation {y}, annual average (WEO)")
put("cpi_avg_0007", avg(p, 2000, 2007), "euro-area inflation, average 2000-07")
put("cpi_avg_1320", avg(p, 2013, 2020), "euro-area inflation, average 2013-20")
for a, k in (("G163", "ea"), ("ESP", "es"), ("GRC", "gr"), ("DEU", "de"), ("ITA", "it")):
    u = W("LUR", a)
    pk = max((y for y in u if 2000 <= y <= 2025), key=u.get)
    put(f"lur_{k}_pk", u[pk], f"{a} unemployment rate, peak 2000-25 ({pk})"); put(f"lur_{k}_pk_y", pk, "year of that peak", 0)
    put(f"lur_{k}_2007", u[2007], f"{a} unemployment rate 2007")
    put(f"lur_{k}_2025", u[2025], f"{a} unemployment rate 2025")
# real GDP level: Greece and Italy against 2007 (from NGDP_R)
for a in ("GRC", "ITA", "ESP", "DEU", "IRL"):
    r = W("NGDP_R", a)
    put(f"lvl_{a}_25v07", 100 * (r[2025] / r[2007] - 1), f"{a} real GDP 2025 vs 2007, % change")
gr = W("NGDP_R", "GRC")
tr = min((y for y in gr if 2008 <= y <= 2020), key=gr.get)
put("gr_trough_loss", 100 * (gr[tr] / gr[2007] - 1), f"Greece real GDP, trough ({tr}) vs 2007, % change"); put("gr_trough_y", tr, "year of that trough", 0)

# ---- imbalances (current account, % of GDP)
for a, k in (("DEU", "de"), ("ESP", "es"), ("GRC", "gr"), ("PRT", "pt")):
    ca = W("BCA_NGDPD", a)
    for y in (2007, 2025):
        put(f"ca_{k}_{y}", ca[y], f"{a} current account, % of GDP, {y}")
cad = W("BCA_NGDPD", "DEU"); pk = max((y for y in cad if 2000 <= y <= 2025), key=cad.get)
put("ca_de_pk", cad[pk], f"Germany current account, peak 2000-25 ({pk})"); put("ca_de_pk_y", pk, "year", 0)

# ---- spreads over Germany (ECB long-term rates, monthly)
de = M("ecb/Y10_DE", "EA")
for cc, k in (("GR", "gr"), ("IT", "it"), ("ES", "es"), ("PT", "pt"), ("IE", "ie"), ("FR", "fr")):
    y = M(f"ecb/Y10_{cc}", "EA")
    sp = {t: y[t] - de[t] for t in y if t in de}
    pk = max((t for t in sp if t >= "2008"), key=sp.get)
    put(f"sp_{k}_pk", sp[pk], f"{cc} 10-year spread over Germany, peak since 2008 ({pk}), percentage points", 2)
    put(f"sp_{k}_pk_m", int(pk[5:]), "month of that peak", 0); put(f"sp_{k}_pk_y", int(pk[:4]), "year of that peak", 0)
    put(f"sp_{k}_2007_06", sp["2007-06"], f"{cc} spread, June 2007", 2)
    put(f"sp_{k}_last", sp[CAP], f"{cc} spread, {mname(CAP)}", 2)
    if cc == "IT":
        put("sp_it_2012_06", sp["2012-06"], "Italy spread, June 2012", 2)
        put("sp_it_2012_12", sp["2012-12"], "Italy spread, December 2012", 2)
    if cc == "ES":
        put("sp_es_2012_12", sp["2012-12"], "Spain spread, December 2012", 2)
put("y10_de_last", de[CAP], f"German 10-year yield, {mname(CAP)}", 2)
neg = [t for t, v in de.items() if v < 0]
put("y10_de_neg_months", len(neg), f"months with a negative German 10-year yield ({neg[0]} to {neg[-1]})", 0)
put("y10_de_low", min(de.values()), f"German 10-year yield, lowest month ({min(de, key=de.get)})", 2)

# ---- the ECB
r = json.loads((ROOT / "data/js/derived/tm_rates.js").read_text()[len('WE.register("derived/tm_rates",'):-3])["data"]["EA"]
r = {t: v for t, v in r if t <= CAP}
put("dfr_2008_pk", max(v for t, v in r.items() if "2008" <= t < "2009"), "ECB deposit rate, 2008 high", 2)
neg = [t for t, v in r.items() if v < 0]
put("dfr_neg_months", len(neg), f"months with a negative ECB deposit rate ({neg[0]} to {neg[-1]})", 0)
put("dfr_low", min(r.values()), "ECB deposit rate, lowest", 2)
put("dfr_pk23", max(v for t, v in r.items() if t >= "2022"), "ECB deposit rate, high since 2022", 2)
put("dfr_last", r[CAP], f"ECB deposit rate, {mname(CAP)}", 2)
h = M("eurostat/EA_HICP_ANR", "EA")
pk = max(h, key=h.get)
put("hicp_pk", h[pk], f"euro-area HICP inflation, monthly peak ({pk})"); put("hicp_pk_m", int(pk[5:]), "month", 0); put("hicp_pk_y", int(pk[:4]), "year", 0)
lo = min((t for t in h if "2014" <= t <= "2016"), key=h.get)
put("hicp_lo_1416", h[lo], f"euro-area HICP inflation, low 2014-16 ({lo})")
put("hicp_last", h[CAP], f"euro-area HICP inflation, {mname(CAP)}")
bs = M("fred/ECBASSETSW")
put("bs_2007_12", bs["2007-12"] / 1e6, "Eurosystem total assets, December 2007, EUR trillion", 2)
put("bs_2014_09", bs["2014-09"] / 1e6, "Eurosystem total assets, September 2014, EUR trillion", 2)
pkb = max(bs, key=bs.get)
put("bs_pk", bs[pkb] / 1e6, f"Eurosystem total assets, peak ({pkb}), EUR trillion", 2); put("bs_pk_y", int(pkb[:4]), "year", 0)
put("bs_last", bs[CAP] / 1e6, f"Eurosystem total assets, {mname(CAP)}, EUR trillion", 2)

# ---- public debt and balance
for a, k in (("G163", "ea"), ("DEU", "de"), ("FRA", "fr"), ("ITA", "it"), ("GRC", "gr"), ("ESP", "es"), ("IRL", "ie"), ("PRT", "pt")):
    d = W("GGXWDG_NGDP", a)
    for y in (2007, 2025, 2031):
        put(f"debt_{k}_{y}", d[y], f"{a} general government gross debt, % of GDP, {y}")
    pk = max((y for y in d if 2000 <= y <= 2025), key=d.get)
    put(f"debt_{k}_pk", d[pk], f"{a} debt, peak 2000-25 ({pk})"); put(f"debt_{k}_pk_y", pk, "year", 0)
b = W("GGXCNL_NGDP")
for y in (2007, 2009, 2020, 2025):
    put(f"bal_ea_{y}", b[y], f"euro-area general government balance, % of GDP, {y}")
put("bal_fr_2025", W("GGXCNL_NGDP", "FRA")[2025], "France general government balance, % of GDP, 2025")
put("bal_gr_2025", W("GGXCNL_NGDP", "GRC")[2025], "Greece general government balance, % of GDP, 2025")
put("bal_ie_2010", W("GGXCNL_NGDP", "IRL")[2010], "Ireland general government balance, % of GDP, 2010")

# ---- India and the euro area
inr = M("fred/DEXINUS"); eur = M("fred/DEXUSEU")
ie = {t: inr[t] * eur[t] for t in inr if t in eur}
reg("ea_inr", {"id": "derived/ea_inr", "label": "Rupees per euro", "unit": "₹ per €", "freq": "M",
               "source": "Computed for this book from FRED DEXINUS (rupees per US dollar) and DEXUSEU (US dollars per euro), monthly averages (Federal Reserve H.10)",
               "notes": "Rupees per dollar multiplied by dollars per euro, monthly averages.",
               "data": {"IN": [[t, round(v, 2)] for t, v in sorted(ie.items())]}})
put("inr_eur_1999", sum(v for t, v in ie.items() if t.startswith("1999")) / 12, "rupees per euro, 1999 average", 2)
lo = min(ie, key=ie.get); put("inr_eur_lo", ie[lo], f"rupees per euro, lowest month ({lo})", 2); put("inr_eur_lo_y", int(lo[:4]), "year", 0)
put("inr_eur_2008_04", ie["2008-04"], "rupees per euro, April 2008", 2)
put("inr_eur_2013_08", ie["2013-08"], "rupees per euro, August 2013", 2)
put("inr_eur_last", ie[CAP], f"rupees per euro, {mname(CAP)}", 2)
nd, ni = W("NGDPD"), W("NGDPD", "IND")
for y in (2000, 2025, 2031):
    put(f"gdpd_ea_{y}", nd[y] / 1000, f"euro-area GDP, US$ trillion, {y}")
    put(f"gdpd_in_{y}", ni[y] / 1000, f"India GDP, US$ trillion, {y}", 2)
    put(f"gdpd_in_ea_{y}", 100 * ni[y] / nd[y], f"India's GDP as % of the euro area's, at market exchange rates, {y}")
gi = W("NGDP_RPCH", "IND")
put("g_ind_avg_1019", avg(gi, 2010, 2019), "India growth, average 2010-19")
put("g_ind_2012", gi[2012], "India growth 2012 (fiscal year 2012-13)")

(C / "derived/lens_euro.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures")
