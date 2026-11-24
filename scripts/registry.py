"""Series registry: every series the book uses, with its source and code.

Fetch scripts read this file; nothing is fetched that is not listed here.
Add a series here first, then run `python3 scripts/refresh.py`.
"""

# --- IMF World Economic Outlook (SDMX dataflow IMF.RES,WEO; latest vintage) ---
# All countries and aggregates are pulled for each indicator.
WEO_INDICATORS = [
    "NGDP_RPCH",    # Real GDP growth, %
    "NGDP_R",       # Real GDP, national currency (for indices)
    "NGDP",         # Nominal GDP, national currency (for ratios)
    "NGDPD",        # GDP, current US$ bn
    "NGDPDPC",      # GDP per capita, current US$
    "PPPPC",        # GDP per capita, PPP int$
    "PPPSH",        # Share of world GDP at PPP, %
    "PCPIPCH",      # CPI inflation, period average, %
    "LUR",          # Unemployment rate, %
    "GGXWDG_NGDP",  # General government gross debt, % GDP
    "GGXCNL_NGDP",  # General government net lending/borrowing, % GDP
    "GGSB_NPGDP",   # Structural balance, % potential GDP
    "GGXONLB_NGDP", # Primary balance, % GDP
    "GGR_NGDP",     # General government revenue, % GDP (added for Theme 4)
    "BCA",          # Current account balance, US$ bn
    "BCA_NGDPD",    # Current account balance, % GDP
    "TRADEPCH",     # World trade volume (goods and services), % change
    "TX_RPCH",      # Export volume, % change
    "TM_RPCH",      # Import volume, % change
    "NID_NGDP",     # Investment, % GDP
    "NGSD_NGDP",    # Gross national saving, % GDP
    "NGAP_NPGDP",   # Output gap, % potential
    "LP",           # Population, millions
    "BF", "BFD", "BFP", "BFO", "BFRA",  # Financial account, US$ bn
    "DS_BX",        # External debt service, % exports
    # Commodity prices (annual averages; reported under country code G001)
    "PALLFNFW", "PNRGW", "PMETAW", "PFOODW", "POILBRE", "PNGASEU",
]
WEO_VINTAGES = ["WEO_2025_OCT_VINTAGE", "WEO_2026_APR_VINTAGE"]
WEO_VINTAGE_INDICATORS = ["NGDP_RPCH", "PCPIPCH"]

# --- World Bank World Development Indicators (API v2) ---
WDI_INDICATORS = [
    "NY.GDP.MKTP.KD.ZG", "NY.GDP.PCAP.PP.KD", "NY.GDP.PCAP.KD",
    "NE.TRD.GNFS.ZS", "TX.VAL.MRCH.CD.WT", "BX.GSR.NFSV.CD", "BX.GSR.GNFS.CD",
    "BX.KLT.DINV.WD.GD.ZS", "FI.RES.TOTL.CD", "CM.MKT.LCAP.GD.ZS", "CM.MKT.LCAP.CD",
    "SI.POV.DDAY", "SI.POV.GINI", "SH.DYN.MORT", "SP.DYN.LE00.IN",
    "SI.POV.LMIC", "SI.POV.UMIC", "SE.LPV.PRIM", "SH.STA.MMRT", "SH.STA.STNT.ZS", "DT.ODA.ODAT.CD",  # added for Theme 6
    "SE.PRM.CMPT.ZS", "IT.NET.USER.ZS", "IT.CEL.SETS.P2",
    "SP.POP.TOTL", "SP.POP.1564.TO.ZS", "SP.POP.DPND.OL", "SP.DYN.TFRT.IN",
    "SL.TLF.CACT.FE.ZS", "BX.TRF.PWKR.DT.GD.ZS",
    "TM.TAX.MRCH.WM.AR.ZS", "BX.GSR.CCIS.ZS", "TM.VAL.MRCH.CD.WT",
    "EG.FEC.RNEW.ZS", "EG.EGY.PRIM.PP.KD", "EN.GHG.CO2.MT.CE.AR5",
    "GB.XPD.RSDV.GD.ZS", "TX.VAL.TECH.MF.ZS", "IT.NET.BBND.P2", "SP.POP.SCIE.RD.P6",  # added for Theme 7
    "SP.POP.65UP.TO.ZS", "SP.POP.0014.TO.ZS", "SL.TLF.CACT.ZS", "SL.TLF.CACT.MA.ZS", "SL.UEM.TOTL.ZS", "SL.UEM.1524.ZS",
    "SL.AGR.EMPL.ZS", "SL.IND.EMPL.ZS", "SL.SRV.EMPL.ZS", "BX.TRF.PWKR.CD.DT", "SM.POP.NETM", "SP.DYN.CBRT.IN",  # added for Theme 9
]

# --- FRED (fredgraph CSV; titles scraped from the series page) ---
FRED_SERIES = [
    "NASDAQCOM", "SP500", "NIKKEI225", "VIXCLS", "USREC", "USRECM",
    "FEDFUNDS", "DFF", "DGS10", "DFII10", "T10YIE", "TEDRATE", "BAA10Y",
    "WALCL", "ECBASSETSW", "JPNASSETS",
    "CPIAUCSL", "PCEPILFE", "UNRATE", "GDPC1", "OPHNFB",
    "CSUSHPINSA", "MORTGAGE30US",
    "DCOILBRENTEU", "DTWEXBGS",
    "DEXUSEU", "DEXCHUS", "DEXJPUS", "DEXBZUS", "DEXINUS", "DEXSFUS",
    "SPASTT01INM661N",  # India share prices, OECD MEI (monthly index, 2015=100)
    "SPASTT01USM661N", "SPASTT01JPM661N", "SPASTT01DEM661N", "SPASTT01GBM661N", "SPASTT01CNM661N", "SPASTT01BRM661N", "SPASTT01KRM661N",  # share prices, OECD MEI (added for Theme 5)
    "IRLTLT01DEM156N", "IRLTLT01JPM156N",
    "B235RC1Q027SBEA", "A255RC1Q027SBEA",
    "CLVMNACSCAB1GQEA19",  # Euro area real GDP, quarterly, SA (Eurostat via FRED)
    "CPALTT01GBM659N",  # UK CPI, % change on a year earlier (OECD MEI)
    "PNGASEUUSDM",  # Natural gas, Europe, US$/MMBtu, monthly (IMF primary commodity prices)
    "A679RC1Q027SBEA",  # US private fixed investment in information processing equipment and software, $bn SAAR (BEA)
    "B935RC1Q027SBEA",  # US private fixed investment: computers and peripheral equipment, $bn SAAR (BEA)
    "B985RC1Q027SBEA",  # US private fixed investment: software, $bn SAAR (BEA)
    "GDP",  # US nominal GDP, $bn SAAR (BEA)
    "CPALTT01CNM659N",  # China CPI, % change on a year earlier (OECD MEI)
    "DCOILWTICO",  # WTI crude, daily (negative on 20 April 2020)
    "MFPNFBS",  # US private nonfarm business total factor productivity, annual index (BLS) (added for Theme 7)
    "CIVPART", "LNS11300060", "JTSJOL", "JTSQUR", "PRS85006173", "CES0500000003", "UNEMPLOY",  # US participation, prime-age participation, job openings, quits rate, nonfarm business labour share, average hourly earnings (added for Theme 9)
]

# --- OECD Data Explorer (SDMX REST): quarterly national accounts ---
# Real GDP, chain-linked volumes, national currency, seasonally adjusted (QNA, table T0102).
OECD_QNA_URL = ("https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN1@DF_QNA,/"
                "Q.Y.{areas}.S1..B1GQ._Z._Z._Z.XDC.LR..T0102?startPeriod=2015-Q1")
OECD_QNA_AREAS = ["USA", "GBR", "JPN", "IND", "DEU", "BRA"]  # EA20 and CHN not returned by this query (22 Nov 2026)

# --- ECB Data Portal (SDMX REST, csvdata) ---
ECB_SERIES = {
    "EUROSTOXX50": ("FM", "M.U2.EUR.DS.EI.DJES50I.HSTA"),
    "ECB_DFR":     ("FM", "B.U2.EUR.4F.KR.DFR.LEV"),
    "EA_HICP":     ("ICP", "M.U2.N.000000.4.ANR"),
    **{f"Y10_{cc}": ("IRS", f"M.{cc}.L.L40.CI.0000.EUR.N.Z")
       for cc in ["DE", "IT", "ES", "GR", "PT", "IE", "FR"]},
}

# --- BIS bulk data sets (flat CSV zips) ---
BIS_DATASETS = ["WS_CBPOL", "WS_TC", "WS_EER"]

# --- Shiller (Yale): monthly S&P composite, CAPE ---
# The Yale file stopped updating in Oct 2023; the Yale data page now links to shillerdata.com (Theme 5, 23 Nov 2026).
# Download link taken from the shillerdata.com home page; the ?ver= parameter changes when the file is updated.
SHILLER_URL_OLD = "http://www.econ.yale.edu/~shiller/data/ie_data.xls"
SHILLER_URL = "https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/249997aa-1eef-4237-93ec-2d319f7881ab/ie_data.xls?ver=1794837439406"

# --- Natural Earth (public domain) ---
NE_URL = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
