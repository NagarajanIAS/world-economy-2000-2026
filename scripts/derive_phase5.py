"""Derived figures quoted in chapters/phase-5.html. Output: data/clean/derived/phase5.json.
    python3 scripts/derive_phase5.py
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

# ---- oil (FRED Brent, monthly averages)
b = S("fred/DCOILBRENTEU.json")
put("brent_2014_06", b["2014-06"], "FRED DCOILBRENTEU, Jun 2014 monthly average, US$/bbl", 0)
lo = min((k for k in b if "2014-07" <= k <= "2016-12"), key=b.get)
put("brent_low", b[lo], f"FRED DCOILBRENTEU, lowest monthly average Jul 2014–Dec 2016 ({lo})", 0); lab("brent_lowmo", lo, "month of Brent low")
put("brent_fall", (1 - b[lo] / b["2014-06"]) * 100, "Brent fall Jun 2014 to low month, %", 0)
hi = max((k for k in b if "2017" <= k <= "2019-12"), key=b.get)
put("brent_hi1819", b[hi], f"FRED DCOILBRENTEU, highest monthly average 2017–2019 ({hi})", 0); lab("brent_hi1819mo", hi, "month")
for y in (2014, 2015, 2016):
    put(f"poil_{y}", w("POILBRE", "G001")[y], f"WEO POILBRE {y}, US$/bbl", 0)

# ---- growth (WEO)
for a in ["G001", "G110", "G200", "USA", "G163", "JPN", "DEU", "GBR", "CHN", "IND", "BRA", "RUS", "SAU", "NGA", "ARG", "TUR"]:
    d = w("NGDP_RPCH", a)
    for y in range(2014, 2020):
        put(f"gdp_{a}_{y}", d[y], f"WEO NGDP_RPCH {a} {y}")
    put(f"gdp_{a}_avg1419", sum(d[y] for y in range(2014, 2020)) / 6, f"WEO NGDP_RPCH {a}, average of 2014–2019")

# ---- trade vs GDP (WEO world)
t, g = w("TRADEPCH", "G001"), w("NGDP_RPCH", "G001")
for y in range(2014, 2020):
    put(f"trade_{y}", t[y], f"WEO TRADEPCH G001 {y}, world trade volume growth %")
avg = lambda s, a, z: sum(s[y] for y in range(a, z + 1)) / (z - a + 1)
for a, z in [(1990, 1999), (2000, 2007), (2012, 2019)]:
    put(f"trade_avg_{a}_{z}", avg(t, a, z), f"WEO TRADEPCH G001 average {a}–{z}")
    put(f"gdpw_avg_{a}_{z}", avg(g, a, z), f"WEO NGDP_RPCH G001 average {a}–{z}")
    put(f"ratio_{a}_{z}", avg(t, a, z) / avg(g, a, z), f"ratio of average world trade growth to average world GDP growth, {a}–{z}", 2)

# ---- US effective tariff rate (customs duties / goods imports, quarterly SAAR)
cd, im = S("fred/B235RC1Q027SBEA.json"), S("fred/A255RC1Q027SBEA.json")
tr = {k: cd[k] / im[k] * 100 for k in cd if k in im}
for k in ("2017-10", "2018-07", "2019-10"):
    put(f"tariff_{k.replace('-', '_')}", tr[k], f"FRED B235RC1Q027SBEA / A255RC1Q027SBEA, quarter starting {k}, %", 1)
put("tariff_avg_2010_2017", sum(v for k, v in tr.items() if "2010" <= k < "2018") / len([k for k in tr if "2010" <= k < "2018"]), "US customs duties / goods imports, average 2010–2017, %", 1)

# ---- negative yields (FRED/OECD monthly 10-year)
for sid, c in [("IRLTLT01DEM156N", "de"), ("IRLTLT01JPM156N", "jp")]:
    s = S(f"fred/{sid}.json")
    lo = min((k for k in s if "2014" <= k <= "2019-12"), key=s.get)
    put(f"y10_{c}_low", s[lo], f"FRED {sid}, lowest monthly 2014–2019 ({lo}), %", 2); lab(f"y10_{c}_lowmo", lo, "month")
    put(f"y10_{c}_2014_06", s["2014-06"], f"FRED {sid}, Jun 2014, %", 2)
neg = [k for k, v in S("fred/IRLTLT01DEM156N.json").items() if v < 0 and k <= "2019-12"]
lab("y10_de_firstneg", neg[0], "first month German 10-year yield below zero (FRED IRLTLT01DEM156N)")
us = S("fred/DGS10.json")
put("y10_us_2019_08", us["2019-08"], "FRED DGS10, Aug 2019 monthly average, %", 2)
dfr = S("ecb/ECB_DFR.json", "EA")
put("ecb_dfr_2019_09", dfr["2019-09"], "ECB deposit facility rate, Sep 2019", 2)
cb = S("bis/CBPOL.json", "US")
put("fed_2015_11", cb["2015-11"], "BIS CBPOL US, Nov 2015", 2); put("fed_2018_12", cb["2018-12"], "BIS CBPOL US, Dec 2018", 2); put("fed_2019_12", cb["2019-12"], "BIS CBPOL US, Dec 2019", 2)

# ---- China
cn = S("bis/TC_P.json", "CN")
for k in ("2008-10", "2014-07", "2019-10"):
    put(f"cn_credit_{k.replace('-', '_')}", cn[k], f"BIS TC_P (credit to private non-financial sector, % GDP) CN, {k}", 0)
pk = max((k for k in cn if k <= "2019-12"), key=cn.get)
put("cn_credit_peak", cn[pk], f"BIS TC_P CN, highest to 2019 ({pk}), % GDP", 0); lab("cn_credit_peakq", pk, "quarter")
fx = S("fred/DEXCHUS.json")
put("cny_2015_07", fx["2015-07"], "FRED DEXCHUS, Jul 2015 monthly average, yuan per US$", 2)
put("cny_2016_12", fx["2016-12"], "FRED DEXCHUS, Dec 2016 monthly average", 2)
put("cny_2019_09", fx["2019-09"], "FRED DEXCHUS, Sep 2019 monthly average", 2)
put("cn_fx_2014", w("NGDPD", "CHN")[2014], "WEO NGDPD CHN 2014, US$ bn", 0) if False else None

# ---- India (author's dataset; fiscal years plotted at start year)
for s, l, nd in [("gdp_real_growth", "gdp", 1), ("cpi_inflation", "cpi", 1), ("oil_imports", "oil", 0), ("repo_end", "repo", 2),
                 ("cab_gdp", "cab", 1), ("gg_fd_gdp", "ggfd", 1), ("centre_fd_gdp", "cfd", 1), ("fx_reserves", "res", 0),
                 ("inr_usd", "inr", 1), ("exports_goods", "xg", 0), ("gfcf_gdp", "gfcf", 1), ("scb_credit_gdp", "credit", 1)]:
    d = ind(s)
    for y in range(2013, 2021):
        if y in d and d[y] is not None:
            put(f"in_{l}_{y}", d[y], f"India {s} {fy(y)}", nd)

(C / "derived/phase5.json").write_text(json.dumps(out, indent=1))
print(len(out), "figures written to data/clean/derived/phase5.json")
