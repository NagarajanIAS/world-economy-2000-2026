"""Derived figures quoted in chapters/phase-4.html. Output: data/clean/derived/phase4.json.
Each entry: value and how it was computed, so check_numbers.py can verify the prose.
    python3 scripts/derive_phase4.py
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
    print(f"{k:28s} {round(v, nd):>10}  {how}")


ind = lambda sid: {int(y): v for y, v in json.loads((C / f"india/{sid}.json").read_text())["data"]["IND"]}
w = lambda i, a: S(f"weo/{i}.json", a)
fy = lambda y: f"FY{y}-{str(y + 1)[2:]}"

# ---- growth (WEO Oct 2026)
for a in ["G001", "G110", "G200", "USA", "G163", "JPN", "GBR", "DEU", "ITA", "ESP", "GRC", "PRT", "CHN", "IND", "BRA"]:
    d = w("NGDP_RPCH", a)
    for y in range(2010, 2015):
        put(f"gdp_{a}_{y}", d[y], f"WEO NGDP_RPCH {a} {y}")
    put(f"gdp_{a}_avg1014", sum(d[y] for y in range(2010, 2015)) / 5, f"WEO NGDP_RPCH {a}, average of 2010–2014")
put("gdp_G001_avg0307", sum(w("NGDP_RPCH", "G001")[y] for y in range(2003, 2008)) / 5, "WEO NGDP_RPCH G001, average of 2003–2007")

# ---- real GDP level, 2007 = 100
for a in ["USA", "DEU", "GBR", "JPN", "FRA", "ITA", "ESP", "GRC", "PRT", "IRL", "CHN", "IND"]:
    d = w("NGDP_R", a)
    for y in (2013, 2014):
        put(f"rgdp07_{a}_{y}", d[y] / d[2007] * 100, f"WEO NGDP_R {a}: {y} level, 2007 = 100", 0)
    lo = min(range(2008, 2015), key=lambda y: d[y])
    put(f"rgdp07_{a}_low", d[lo] / d[2007] * 100, f"WEO NGDP_R {a}: lowest level 2008–2014 ({lo}), 2007 = 100", 0)

# ---- unemployment (WEO LUR, % of labour force)
for a in ["USA", "G163", "ESP", "GRC", "PRT", "ITA", "IRL", "DEU", "GBR"]:
    d = w("LUR", a)
    pk = max(range(2009, 2015), key=lambda y: d[y])
    put(f"lur_{a}_2007", d[2007], f"WEO LUR {a} 2007")
    put(f"lur_{a}_peak", d[pk], f"WEO LUR {a}: highest 2009–2014 ({pk})")
    out[f"lur_{a}_peakyr"] = {"value": pk, "how": f"WEO LUR {a}: year of highest rate 2009–2014"}
    put(f"lur_{a}_2014", d[2014], f"WEO LUR {a} 2014")
ur = S("fred/UNRATE.json", "US")
put("us_ur_2009_10", ur["2009-10"], "FRED UNRATE, Oct 2009", 1)
put("us_ur_2014_06", ur["2014-06"], "FRED UNRATE, Jun 2014", 1)

# ---- structural fiscal balance (% of potential GDP) and its change 2010 -> 2013
for a in ["G110", "USA", "GBR", "JPN", "DEU", "FRA", "ITA", "ESP", "GRC", "PRT", "IRL", "IND"]:
    d = w("GGSB_NPGDP", a)
    put(f"sb_{a}_2010", d[2010], f"WEO GGSB_NPGDP {a} 2010, % of potential GDP")
    put(f"sb_{a}_2013", d[2013], f"WEO GGSB_NPGDP {a} 2013, % of potential GDP")
    put(f"dsb_{a}_1013", d[2013] - d[2010], f"WEO GGSB_NPGDP {a}: 2013 minus 2010, percentage points")
for a in ["GRC", "ITA", "ESP", "PRT", "IRL", "USA", "JPN", "GBR"]:
    d = w("GGXWDG_NGDP", a)
    put(f"debt_{a}_2007", d[2007], f"WEO GGXWDG_NGDP {a} 2007, % of GDP", 0)
    put(f"debt_{a}_2014", d[2014], f"WEO GGXWDG_NGDP {a} 2014, % of GDP", 0)

# ---- euro sovereign spreads over Bunds (ECB monthly 10-year rates, percentage points)
de = S("ecb/Y10_DE.json", "EA")
for cc in ["GR", "PT", "IE", "IT", "ES"]:
    y = S(f"ecb/Y10_{cc}.json", "EA")
    sp = {k: y[k] - de[k] for k in y if k in de and "2010" <= k < "2015"}
    pk = max(sp, key=sp.get)
    put(f"spr_{cc}_peak", sp[pk], f"ECB 10-year {cc} minus DE, highest monthly spread 2010–2014 ({pk}), pp")
    out[f"spr_{cc}_peakmo"] = {"value": pk, "how": f"month of highest {cc} spread 2010–2014"}
    for m in ("2010-01", "2012-07", "2014-06"):
        put(f"spr_{cc}_{m.replace('-', '_')}", sp[m], f"ECB 10-year {cc} minus DE, {m}, pp")
    put(f"y10_{cc}_peak", max(v for k, v in y.items() if "2010" <= k < "2015"), f"ECB 10-year {cc} yield, highest monthly 2010–2014, %")
put("y10_DE_2012_07", de["2012-07"], "ECB 10-year DE yield, Jul 2012, %", 2)

# ---- central banks
wal = S("fred/WALCL.json", "US")
put("fed_bs_2010_01", wal["2010-01"] / 1e6, "FRED WALCL, Jan 2010 monthly average, US$ trillion", 2)
put("fed_bs_2014_06", wal["2014-06"] / 1e6, "FRED WALCL, Jun 2014 monthly average, US$ trillion", 2)
dfr = S("ecb/ECB_DFR.json", "EA")
put("ecb_dfr_2011_07", dfr["2011-07"], "ECB deposit facility rate, Jul 2011", 2)
put("ecb_dfr_2014_06", dfr["2014-06"], "ECB deposit facility rate, Jun 2014", 2)

# ---- taper tantrum (FRED monthly averages)
t10 = S("fred/DGS10.json", "US")
for m in ("2012-07", "2013-04", "2013-09", "2013-12"):
    put(f"t10_{m.replace('-', '_')}", t10[m], f"FRED DGS10, monthly average {m}", 2)
for s, lab in [("DEXINUS", "inr"), ("DEXBZUS", "brl"), ("DEXSFUS", "zar")]:
    fx = S(f"fred/{s}.json", "US")
    pk = max((k for k in fx if "2013-05" <= k <= "2013-12"), key=fx.get)
    put(f"{lab}_2013_04", fx["2013-04"], f"FRED {s}, monthly average Apr 2013", 2)
    put(f"{lab}_peak13", fx[pk], f"FRED {s}, weakest monthly average May–Dec 2013 ({pk})", 2)
    out[f"{lab}_peak13mo"] = {"value": pk, "how": f"FRED {s}: month of weakest average May–Dec 2013"}
    put(f"{lab}_dep13", (1 - fx["2013-04"] / fx[pk]) * 100, f"FRED {s}: fall in the dollar value of the currency, Apr 2013 to {pk}, %", 0)

# ---- India (author's dataset; fiscal years plotted at start year)
g = ind("gdp_real_growth"); g04 = ind("gdpfc_growth_2004")
for y in range(2009, 2015):
    if y in g:
        put(f"in_gdp11_{y}", g[y], f"India real GDP growth, 2011-12 base, {fy(y)}")
    if y in g04:
        put(f"in_gdp04_{y}", g04[y], f"India GDP at factor cost growth, 2004-05 base, {fy(y)}")
for s, lab, nd in [("wpi_inflation", "wpi", 1), ("cpi_iw_inflation", "cpi", 1), ("cab_gdp", "cab", 1),
                   ("centre_fd_gdp", "cfd", 1), ("gg_fd_gdp", "ggfd", 1), ("gg_debt_gdp", "ggdebt", 1),
                   ("inr_usd", "inr", 1), ("fx_reserves", "res", 1), ("bop_ca", "ca", 1), ("fpi_net", "fpi", 1),
                   ("fdi_net", "fdi", 1), ("oil_imports", "oil", 1), ("gfcf_gdp", "gfcf", 1),
                   ("ext_debt_short_share", "stdebt", 1), ("import_cover_months", "cover", 1),
                   ("repo_end", "repo", 2), ("scb_credit_gdp", "credit", 1)]:
    d = ind(s)
    for y in range(2009, 2015):
        if y in d and d[y] is not None:
            put(f"in_{lab}_{y}", d[y], f"India {s} {fy(y)}", nd)

(C / "derived/phase4.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures written to data/clean/derived/phase4.json")
