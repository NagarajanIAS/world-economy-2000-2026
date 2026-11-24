"""Build data/js/meta/catalogue.js: the indicators offered by the explorer and the map.

Only annual, country-level series that the book already holds are listed (IMF WEO
October 2026 and World Bank WDI). Short names and display units are rewordings of
each series' own label, which is printed beside it so the two can be compared.
The script fails if a file is missing or covers fewer than 30 economies.

Run: .venv/bin/python scripts/build_catalogue.py
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(ROOT, *p)

# (id, short name, group, display unit, scale, decimals, map colouring)
# map: "seq" = more is darker; "div" = diverging around zero
CAT = [
    ("weo/NGDP_RPCH", "Real GDP growth", "Growth and income", "%", 1, 1, "div"),
    ("weo/NGDPD", "GDP, current US dollars", "Growth and income", "US$ billion", 1, 0, "seq"),
    ("weo/NGDPDPC", "GDP per person, current US dollars", "Growth and income", "US$", 1, 0, "seq"),
    ("weo/PPPPC", "GDP per person at purchasing-power parity", "Growth and income", "international $", 1, 0, "seq"),
    ("weo/PPPSH", "Share of world GDP at purchasing-power parity", "Growth and income", "% of world", 1, 2, "seq"),
    ("wdi/NY.GDP.PCAP.KD", "GDP per person, constant 2015 US dollars", "Growth and income", "constant 2015 US$", 1, 0, "seq"),
    ("weo/NGAP_NPGDP", "Output gap", "Growth and income", "% of potential GDP", 1, 1, "div"),
    ("weo/PCPIPCH", "Consumer price inflation", "Prices and jobs", "%", 1, 1, "seq"),
    ("weo/LUR", "Unemployment rate (IMF)", "Prices and jobs", "% of labour force", 1, 1, "seq"),
    ("wdi/SL.UEM.TOTL.ZS", "Unemployment rate (ILO model estimate)", "Prices and jobs", "% of labour force", 1, 1, "seq"),
    ("wdi/SL.UEM.1524.ZS", "Youth unemployment, ages 15–24", "Prices and jobs", "% of labour force 15–24", 1, 1, "seq"),
    ("wdi/SL.TLF.CACT.FE.ZS", "Women's labour-force participation", "Prices and jobs", "% of women 15+", 1, 1, "seq"),
    ("wdi/SL.AGR.EMPL.ZS", "Employment in agriculture", "Prices and jobs", "% of employment", 1, 1, "seq"),
    ("weo/GGXWDG_NGDP", "Government gross debt", "Public finances", "% of GDP", 1, 1, "seq"),
    ("weo/GGXCNL_NGDP", "Government net lending (+) or borrowing (−)", "Public finances", "% of GDP", 1, 1, "div"),
    ("weo/GGXONLB_NGDP", "Government primary balance", "Public finances", "% of GDP", 1, 1, "div"),
    ("weo/GGR_NGDP", "Government revenue", "Public finances", "% of GDP", 1, 1, "seq"),
    ("weo/GGSB_NPGDP", "Government structural balance", "Public finances", "% of potential GDP", 1, 1, "div"),
    ("weo/BCA_NGDPD", "Current-account balance", "Trade and money", "% of GDP", 1, 1, "div"),
    ("weo/BCA", "Current-account balance, US dollars", "Trade and money", "US$ billion", 1, 1, "div"),
    ("weo/TX_RPCH", "Export volume growth, goods and services", "Trade and money", "%", 1, 1, "div"),
    ("weo/TM_RPCH", "Import volume growth, goods and services", "Trade and money", "%", 1, 1, "div"),
    ("weo/NGSD_NGDP", "Gross national saving", "Trade and money", "% of GDP", 1, 1, "seq"),
    ("weo/NID_NGDP", "Investment (gross capital formation)", "Trade and money", "% of GDP", 1, 1, "seq"),
    ("wdi/NE.TRD.GNFS.ZS", "Trade (exports plus imports)", "Trade and money", "% of GDP", 1, 1, "seq"),
    ("wdi/TX.VAL.MRCH.CD.WT", "Merchandise exports", "Trade and money", "US$ billion", 1e-9, 1, "seq"),
    ("wdi/TM.TAX.MRCH.WM.AR.ZS", "Applied tariff, weighted mean", "Trade and money", "%", 1, 1, "seq"),
    ("wdi/BX.KLT.DINV.WD.GD.ZS", "Foreign direct investment, net inflows", "Trade and money", "% of GDP", 1, 1, "div"),
    ("wdi/BX.TRF.PWKR.DT.GD.ZS", "Remittances received", "Trade and money", "% of GDP", 1, 1, "seq"),
    ("wdi/FI.RES.TOTL.CD", "Foreign-exchange reserves, including gold", "Trade and money", "US$ billion", 1e-9, 1, "seq"),
    ("wdi/CM.MKT.LCAP.GD.ZS", "Stock-market capitalisation", "Trade and money", "% of GDP", 1, 1, "seq"),
    ("wdi/SP.POP.TOTL", "Population", "People", "million", 1e-6, 1, "seq"),
    ("wdi/SP.DYN.TFRT.IN", "Fertility rate", "People", "births per woman", 1, 2, "seq"),
    ("wdi/SP.DYN.LE00.IN", "Life expectancy at birth", "People", "years", 1, 1, "seq"),
    ("wdi/SP.POP.65UP.TO.ZS", "Population aged 65 and over", "People", "% of population", 1, 1, "seq"),
    ("wdi/SP.POP.DPND.OL", "Old-age dependency ratio", "People", "% of working-age population", 1, 1, "seq"),
    ("wdi/SI.POV.DDAY", "Extreme poverty, $3.00 a day (2021 PPP)", "Development", "% of population", 1, 1, "seq"),
    ("wdi/SI.POV.GINI", "Gini index of inequality", "Development", "index (0–100)", 1, 1, "seq"),
    ("wdi/SH.DYN.MORT", "Under-5 mortality", "Development", "per 1,000 live births", 1, 1, "seq"),
    ("wdi/SE.PRM.CMPT.ZS", "Primary completion rate", "Development", "% of relevant age group", 1, 1, "seq"),
    ("wdi/DT.ODA.ODAT.CD", "Net official development assistance received", "Development", "US$ billion", 1e-9, 2, "seq"),
    ("wdi/IT.NET.USER.ZS", "Internet users", "Technology and energy", "% of population", 1, 1, "seq"),
    ("wdi/IT.CEL.SETS.P2", "Mobile phone subscriptions", "Technology and energy", "per 100 people", 1, 1, "seq"),
    ("wdi/GB.XPD.RSDV.GD.ZS", "Research and development spending", "Technology and energy", "% of GDP", 1, 2, "seq"),
    ("wdi/EG.FEC.RNEW.ZS", "Renewable share of final energy use", "Technology and energy", "% of final energy", 1, 1, "seq"),
    ("wdi/EN.GHG.CO2.MT.CE.AR5", "CO₂ emissions, excluding land use", "Technology and energy", "Mt CO₂e", 1, 1, "seq"),
    ("wdi/EG.EGY.PRIM.PP.KD", "Energy intensity of GDP", "Technology and energy", "MJ per $2021 PPP of GDP", 1, 2, "seq"),
]

out = []
for id_, name, group, unit, scale, dec, cmap in CAT:
    src, code = id_.split("/", 1)
    d = json.load(open(J("data", "clean", src, code + ".json")))
    n = sum(1 for v in d["data"].values() if v)
    assert n >= 30, (id_, n)
    years = sorted({int(p) for v in d["data"].values() for p, x in v if x is not None})
    out.append({"id": id_, "name": name, "group": group, "unit": unit, "scale": scale, "dec": dec, "map": cmap,
                "label": d["label"], "source": "IMF WEO" if src == "weo" else "World Bank WDI",
                "names": "meta/weo_countries" if src == "weo" else "meta/wdi_countries",
                "first": years[0], "last": years[-1], "n": n,
                "last_actual_default": d.get("last_actual_default")})

js = 'WE.register("meta/catalogue",' + json.dumps({"id": "meta/catalogue", "items": out}, ensure_ascii=False) + ");\n"
open(J("data", "js", "meta", "catalogue.js"), "w").write(js)
print(len(out), "indicators;", sum(1 for o in out if o["source"] == "IMF WEO"), "WEO,", sum(1 for o in out if o["source"] != "IMF WEO"), "WDI")
