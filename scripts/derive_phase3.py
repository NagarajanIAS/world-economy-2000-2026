"""Derived figures quoted in chapters/phase-3.html. Output: data/clean/derived/phase3.json.
Each entry: value, how computed, and inputs, so check_numbers.py can verify the prose."""
import csv, json
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
C = ROOT / "data/clean"
def S(path, area=None):
    d = json.loads((C / path).read_text())["data"]
    return dict(d[area] if area else next(iter(d.values())))
out = {}
def put(k, v, how, nd=1):
    out[k] = {"value": round(v, nd), "how": how}; print(f"{k:28s} {round(v, nd):>10}  {how}")

# daily max/min straight from raw FRED (TED, VIX, Brent)
def daily(s):
    rows = list(csv.reader(open(ROOT / f"data/raw/fred/{s}.csv")))[1:]
    return [(d, float(v)) for d, v in rows if v not in ("", ".")]
ted = [x for x in daily("TEDRATE") if "2007-01-01" <= x[0] <= "2009-12-31"]
mx = max(ted, key=lambda x: x[1]); put("ted_daily_peak", mx[1], f"FRED TEDRATE daily max 2007–09, on {mx[0]}", 2)
pre = [v for d, v in ted if "2007-01-01" <= d <= "2007-06-30"]; put("ted_h1_2007_avg", sum(pre)/len(pre), "FRED TEDRATE, average of daily values Jan–Jun 2007", 2)
vix = [x for x in daily("VIXCLS") if "2008-01-01" <= x[0] <= "2009-12-31"]; mv = max(vix, key=lambda x: x[1]); put("vix_peak", mv[1], f"FRED VIXCLS daily max 2008–09, on {mv[0]}", 1)
br = [x for x in daily("DCOILBRENTEU") if "2008-01-01" <= x[0] <= "2008-12-31"]
bmx = max(br, key=lambda x: x[1]); bmn = min([x for x in br if x[0] > bmx[0]], key=lambda x: x[1])
put("brent_2008_peak", bmx[1], f"FRED DCOILBRENTEU daily max 2008, on {bmx[0]}", 2); put("brent_2008_low", bmn[1], f"FRED DCOILBRENTEU daily min after peak in 2008, on {bmn[0]}", 2)

# equities: monthly averages, peak 2007 -> trough 2008-09
def drawdown(path, area, key, label):
    s = S(path, area); pk = max(((k, v) for k, v in s.items() if k.startswith("2007")), key=lambda x: x[1])
    tr = min(((k, v) for k, v in s.items() if "2008-01" <= k <= "2009-12"), key=lambda x: x[1])
    put(key, (tr[1] / pk[1] - 1) * 100, f"{label}: monthly average, peak {pk[0]} to trough {tr[0]}", 0)
drawdown("shiller/SP_LONG.json", "US", "sp_fall", "S&P Composite (Shiller)")
drawdown("ecb/EUROSTOXX50.json", "EA", "stoxx_fall", "Euro Stoxx 50 (ECB)")
drawdown("fred/NIKKEI225.json", "US", "nikkei_fall", "Nikkei 225 (FRED)")

# house prices
hp = S("fred/CSUSHPINSA.json", "US"); pk = max(((k, v) for k, v in hp.items() if k < "2008"), key=lambda x: x[1]); tr = min(((k, v) for k, v in hp.items() if "2008" <= k < "2014"), key=lambda x: x[1])
put("us_house_fall", (tr[1]/pk[1]-1)*100, f"Case-Shiller US National (FRED CSUSHPINSA), peak {pk[0]} to trough {tr[0]}", 0)
ur = S("fred/UNRATE.json", "US"); p = max(((k, v) for k, v in ur.items() if "2008" <= k <= "2011"), key=lambda x: x[1]); put("us_unemp_peak", p[1], f"FRED UNRATE peak 2008–11, {p[0]}", 1)
put("us_unemp_2007_05", ur["2007-05"], "FRED UNRATE May 2007", 1)

# balance sheets: Jul 2007 -> Dec 2008 / Dec 2009 (monthly avg)
for s, lab in [("WALCL", "Fed"), ("ECBASSETSW", "ECB"), ("JPNASSETS", "BoJ")]:
    d = S(f"fred/{s}.json", "US"); a = d.get("2007-07") or d.get("2007-06")
    put(f"bs_{lab}_x_2008", d["2008-12"]/a, f"FRED {s}: Dec 2008 ÷ Jul 2007 (monthly averages)", 1)

# policy rates (BIS, monthly, end of period)
cb = json.loads((C / "bis/CBPOL.json").read_text())["data"]
for a, lab in [("US", "fed"), ("XM", "ecb"), ("GB", "boe"), ("JP", "boj")]:
    d = dict(cb[a]); put(f"rate_{lab}_2007_07", d["2007-07"], f"BIS WS_CBPOL {a}, Jul 2007", 2); put(f"rate_{lab}_2009_06", d["2009-06"], f"BIS WS_CBPOL {a}, Jun 2009", 2)

# WEO
g = lambda ind, a: S(f"weo/{ind}.json", a)
for a in ["G001", "G110", "G200", "USA", "G163", "DEU", "JPN", "GBR", "CHN", "IND", "BRA", "RUS", "MEX", "KOR"]:
    d = g("NGDP_RPCH", a); [put(f"gdp_{a}_{y}", d[y], f"WEO NGDP_RPCH {a} {y}") for y in (2007, 2008, 2009, 2010)]
t = g("TRADEPCH", "G001"); [put(f"trade_{y}", t[y], f"WEO TRADEPCH G001 {y}") for y in (2007, 2008, 2009, 2010)]
for a in ["USA", "CHN", "DEU", "JPN"]:
    put(f"ca_{a}_2006", g("BCA_NGDPD", a)[2006], f"WEO BCA_NGDPD {a} 2006"); put(f"ca_{a}_2007", g("BCA_NGDPD", a)[2007], f"WEO BCA_NGDPD {a} 2007")
for a in ["G110", "USA", "GBR", "G163", "CHN"]:
    d = g("GGXCNL_NGDP", a); put(f"bal_{a}_2007", d[2007], f"WEO GGXCNL_NGDP {a} 2007"); put(f"bal_{a}_2009", d[2009], f"WEO GGXCNL_NGDP {a} 2009")
    e = g("GGXWDG_NGDP", a); put(f"debt_{a}_2007", e[2007], f"WEO GGXWDG_NGDP {a} 2007"); put(f"debt_{a}_2012", e[2012], f"WEO GGXWDG_NGDP {a} 2012")
lu = g("LUR", "ESP"); put("unemp_ESP_2007", lu[2007], "WEO LUR ESP 2007"); put("unemp_ESP_2009", lu[2009], "WEO LUR ESP 2009")

# ---------------- India (added for the India section)
ind = lambda sid: {int(y): v for y, v in json.loads((C / f"india/{sid}.json").read_text())["data"]["IND"]}
sh = S("fred/SPASTT01INM661N.json", "US")
pk = max(((k, v) for k, v in sh.items() if "2007" <= k <= "2008-06"), key=lambda x: x[1]); tr = min(((k, v) for k, v in sh.items() if "2008-01" <= k <= "2009-12"), key=lambda x: x[1])
put("in_shares_fall", (tr[1] / pk[1] - 1) * 100, f"FRED SPASTT01INM661N (OECD share prices, India), monthly, peak {pk[0]} to trough {tr[0]}", 0)
fx = S("fred/DEXINUS.json", "US")
lo = min(((k, v) for k, v in fx.items() if "2007-06" <= k <= "2008-06"), key=lambda x: x[1]); hi = max(((k, v) for k, v in fx.items() if "2008-06" <= k <= "2009-12"), key=lambda x: x[1])
put("in_rupee_strong", lo[1], f"FRED DEXINUS monthly average, strongest rupee mid-2007 to mid-2008, {lo[0]}", 1)
put("in_rupee_weak", hi[1], f"FRED DEXINUS monthly average, weakest rupee mid-2008 to 2009, {hi[0]}", 1)
put("in_rupee_dep", (hi[1] / lo[1] - 1) * 100, "Rise in rupees per dollar between the two months above", 0)
rr = dict(cb["IN"])
put("in_repo_peak", max(v for k, v in rr.items() if "2008" <= k <= "2008-12"), "BIS WS_CBPOL IN, highest month-end rate in 2008", 2)
put("in_repo_low", min(v for k, v in rr.items() if "2009" <= k <= "2009-12"), "BIS WS_CBPOL IN, lowest month-end rate in 2009", 2)
for sid, key, ys, dec in [("fpi_net", "in_fpi", (2007, 2008, 2009), 1), ("bop_fi", "in_fi", (2007, 2008, 2009), 1),
                          ("fx_reserves", "in_res", (2007, 2008), 1), ("centre_fd_gdp", "in_cfd", (2007, 2008, 2009), 1),
                          ("gg_fd_gdp", "in_ggfd", (2007, 2008, 2009), 1), ("gdp_real_growth", "in_gdp", (2007, 2008, 2009, 2010), 1),
                          ("gdpfc_growth_2004", "in_gdpfc04", (2008,), 1), ("exports_goods", "in_exp", (2008, 2009), 1),
                          ("cab_gdp", "in_cab", (2007, 2008), 1), ("wpi_inflation", "in_wpi", (2008,), 1),
                          ("gdpfc_growth_ae_first", "in_ae", (2008,), 1)]:
    try:
        d = ind(sid)
    except FileNotFoundError:
        continue
    for y in ys:
        put(f"{key}_{y}", d[y], f"India dataset {sid}, FY{y}-{str(y+1)[2:]} (Economic Survey / RBI Handbook)", dec)
(C / "derived").mkdir(exist_ok=True)
(C / "derived/phase3.json").write_text(json.dumps(out, indent=1))
