"""Derived figures quoted in chapters/phase-1.html. Output: data/clean/derived/phase1.json.
Each entry: value and how it was computed, so check_numbers.py can verify the prose.
    python3 scripts/derive_phase1.py
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
    print(f"{k:28s} {v:>12}  {how}")


ind = lambda sid: {int(y): v for y, v in json.loads((C / f"india/{sid}.json").read_text())["data"]["IND"]}
w = lambda i, a: S(f"weo/{i}.json", a)
fy = lambda y: f"FY{y}-{str(y + 1)[2:]}"

# ---- the bust: Nasdaq, S&P 500 and CAPE (monthly averages)
nq = S("fred/NASDAQCOM.json", "US")
pk = max((k for k in nq if "1999" <= k < "2001"), key=nq.get)
lo = min((k for k in nq if "2000" <= k < "2004"), key=nq.get)
put("nq_peak", nq[pk], f"FRED NASDAQCOM, highest monthly average 1999–2000 ({pk})", 0); lab("nq_peakmo", pk, "month of Nasdaq peak")
put("nq_low", nq[lo], f"FRED NASDAQCOM, lowest monthly average 2000–2003 ({lo})", 0); lab("nq_lowmo", lo, "month of Nasdaq low")
put("nq_fall", (1 - nq[lo] / nq[pk]) * 100, "Nasdaq fall from peak to low month, %", 0)
put("nq_1998_01", nq["1998-01"], "FRED NASDAQCOM, Jan 1998 monthly average", 0)
sp = S("shiller/SP_PRICE.json", "US")
spk = max((k for k in sp if "1999" <= k < "2001"), key=sp.get)
slo = min((k for k in sp if "2001" <= k < "2004"), key=sp.get)
put("sp_peak", sp[spk], f"Shiller S&P composite, highest monthly 1999–2000 ({spk})", 0); lab("sp_peakmo", spk, "month of S&P peak")
put("sp_low", sp[slo], f"Shiller S&P composite, lowest monthly 2001–2003 ({slo})", 0); lab("sp_lowmo", slo, "month of S&P low")
put("sp_fall", (1 - sp[slo] / sp[spk]) * 100, "S&P composite fall, peak to low month, %", 0)
cape = S("shiller/CAPE.json", "US")
cpk = max(cape, key=cape.get)
put("cape_peak", cape[cpk], f"Shiller CAPE, all-time highest monthly value ({cpk})", 1); lab("cape_peakmo", cpk, "month of CAPE peak")
put("cape_avg_1881_1995", sum(v for k, v in cape.items() if k < "1996") / len([k for k in cape if k < "1996"]), "Shiller CAPE, average of all months before 1996", 1)
clo = min((k for k in cape if "2001" <= k < "2004"), key=cape.get)
put("cape_low", cape[clo], f"Shiller CAPE, lowest 2001–2003 ({clo})", 1); lab("cape_lowmo", clo, "month of CAPE low 2001–03")

# ---- growth (WEO Oct 2026)
for a in ["G001", "G110", "G200", "USA", "G163", "JPN", "DEU", "GBR", "CHN", "IND", "ARG", "BRA", "TUR", "KOR"]:
    d = w("NGDP_RPCH", a)
    for y in range(1998, 2004):
        put(f"gdp_{a}_{y}", d[y], f"WEO NGDP_RPCH {a} {y}")
ur = S("fred/UNRATE.json", "US")
for m in ("2000-04", "2001-03", "2001-11", "2003-06"):
    put(f"us_ur_{m.replace('-', '_')}", ur[m], f"FRED UNRATE, {m}")
for y in (2000, 2001, 2002, 2003):
    put(f"us_ca_{y}", w("BCA_NGDPD", "USA")[y], f"WEO BCA_NGDPD USA {y}, % of GDP")
oil = w("POILBRE", "G001")
for y in (1998, 1999, 2000, 2001, 2002):
    put(f"oil_{y}", oil[y], f"WEO POILBRE (Brent, US$ a barrel) {y}", 0)

# ---- policy rates (BIS CBPOL, end of month)
cb = {k: S("bis/CBPOL.json", k) for k in ("US", "XM", "GB", "JP", "IN")}
for k in ("US", "XM", "GB"):
    s = {m: v for m, v in cb[k].items() if "1999-01" <= m <= "2004-12"}
    hi = max(s, key=s.get); lo = min(s, key=s.get)
    put(f"cb_{k}_hi", s[hi], f"BIS CBPOL {k}, highest 1999–2004 ({hi})", 2); lab(f"cb_{k}_himo", hi, f"month {k} rate first reached its 1999–2004 high")
    put(f"cb_{k}_lo", s[lo], f"BIS CBPOL {k}, lowest 1999–2004 ({lo})", 2); lab(f"cb_{k}_lomo", lo, f"month {k} rate first reached its 1999–2004 low")
    put(f"cb_{k}_2001_12", cb[k]["2001-12"], f"BIS CBPOL {k}, Dec 2001", 2)
us = cb["US"]
cuts = [m for m in sorted(us) if "2001-01" <= m <= "2001-12"]
put("fed_cut_2001", us["2000-12"] - us["2001-12"], "BIS CBPOL US: Dec 2000 minus Dec 2001, percentage points", 2)
put("cb_JP_2001_03", cb["JP"]["2001-03"], "BIS CBPOL JP, Mar 2001 (last month recorded before 2006)", 2)
for m in ("2000-03", "2003-03"):
    put(f"cb_IN_{m.replace('-', '_')}", cb["IN"][m], f"BIS CBPOL IN (RBI policy rate as BIS records it), {m}", 2)

# ---- China's share of world merchandise exports (WDI)
x = json.loads((C / "wdi/TX.VAL.MRCH.CD.WT.json").read_text())["data"]
cn, wl = dict(x["CHN"]), dict(x["WLD"])
for y in (1990, 2000, 2001, 2002, 2003, 2007, 2010):
    put(f"cn_xsh_{y}", cn[y] / wl[y] * 100, f"WDI TX.VAL.MRCH.CD.WT CHN / WLD {y}, %", 1)
put("cn_x_2000", cn[2000] / 1e9, "WDI China merchandise exports 2000, US$ bn", 0)
put("cn_x_2003", cn[2003] / 1e9, "WDI China merchandise exports 2003, US$ bn", 0)

# ---- Argentina
eer = S("bis/EER_N.json", "AR")
put("ar_eer_fall", (1 - eer["2002-06"] / eer["2001-12"]) * 100, "BIS nominal effective exchange rate, Argentina: fall Dec 2001 to Jun 2002, %", 0)
rer = S("bis/EER_R.json", "AR")
put("ar_reer_fall", (1 - rer["2002-06"] / rer["2001-12"]) * 100, "BIS real effective exchange rate, Argentina: fall Dec 2001 to Jun 2002, %", 0)
ar = w("NGDP_R", "ARG")
put("ar_gdp_9802", (ar[2002] / ar[1998] - 1) * 100, "WEO NGDP_R ARG: 2002 level vs 1998, %", 0)
ar_lur = w("LUR", "ARG")
put("ar_lur_2002", ar_lur[2002], "WEO LUR ARG 2002", 1)

# ---- forecasts of 2001 (hand file) vs today
h = json.loads((ROOT / "data/hand/weo_forecasts_2001.json").read_text())["rows"]
for r in h[:-1]:
    put("f01_" + r["label"].split(" WEO")[0].replace(" ", "_").lower(), r["value"], f"world 2001 growth, {r['cite']}")

# ---- India (author's dataset; fiscal years plotted at start year)
for s, l, nd in [("gdp_real_growth", "gdp11", 1), ("gdpfc_growth_1999", "gdp99", 1), ("wpi_inflation", "wpi", 1),
                 ("cab_gdp", "cab", 1), ("centre_fd_gdp", "cfd", 1), ("gg_fd_gdp", "ggfd", 1), ("fx_reserves", "res", 0),
                 ("bop_software_net", "soft", 1), ("bop_services_net", "serv", 1), ("exports_goods", "xg", 1),
                 ("inr_usd", "inr", 1), ("gfcf_gdp", "gfcf", 1), ("sensex_avg", "sensex", 0), ("exports_gs_real_growth", "xgr", 1)]:
    d = ind(s)
    for y in range(1998, 2005):
        if y in d and d[y] is not None:
            put(f"in_{l}_{y}", d[y], f"India {s} {fy(y)}", nd)

(C / "derived/phase1.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures written to data/clean/derived/phase1.json")
