# Reading notes: country lens "The United States, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers, no cookies). URLs were taken from publisher
listing or issue pages where possible (the imf.org USA country page and its 2026 Article IV issue page; the federalreserve.gov FOMC
historical-year pages and FOMC calendar page; the federalregister.gov documents API, which gives each document's govinfo PDF link; the
supremecourt.gov 2025-term slip-opinion list; the whitehouse.gov site search; the fiscaldata.treasury.gov dataset page, which gives the API
base). Every guessed URL is flagged GUESSED. The IMF country page links only the 2026 Article IV; no imf.org listing of older US Article IV
reports could be found (see Not obtained), so the 2003–2024 staff reports come from GUESSED URLs built on the IMF's file-naming pattern;
each file was checked to be the US Article IV report of the year named (title page and "Country Report No." read in the text). Downloads are
in the session scratchpad folder `lens_us_dl/` (subfolders `imf/`, `imf/g/`, `fed/`, `oth/`, `oth/fr/`, `in/`, one new folder per batch).
PDFs were converted with `pdftotext` (plain and `-layout`) and read in the text; HTML pages were stripped of tags and read as text; one
Federal Register annex printed as an image (EO 14326 Annex I) was rendered with `pdftoppm` and read visually. Python that read downloads
was run with `python3 -I`, with scripts kept outside the download folders. Economic Survey texts were not refetched: they were read from the
Econ Subject folder (`sources/text/es*.txt`; text page = PDF page) and the printed page number was taken from the running header or footer
on that page. Quotes are verbatim, under 15 words, and were checked by a script against the converted text; everything else is paraphrase.
Page numbers are printed page numbers unless stated ("PDF p." where only the PDF page could be given, e.g. unnumbered Key Issues pages).
US federal debt levels (US-OTH-3) are my own reading of the Treasury API values and are marked "own reading".

Item labels: US-IMF-n (IMF Article IV consultations with the United States), US-FED-n (Federal Reserve / FOMC), US-OTH-n (Economic Report
of the President, US Treasury, Federal Register presidential documents, US Supreme Court), US-IN-n (India–US: Economic Surveys, US executive
orders naming India, White House India statements). Indian years are fiscal or survey years. Abbreviations: CA = current account; CR = IMF
Country Report; ERP = Economic Report of the President; EO = Executive Order; FOMC = Federal Open Market Committee; IEEPA = International
Emergency Economic Powers Act; OBBBA = One Big Beautiful Bill Act; PCE = personal consumption expenditures price index; q4/q4 = fourth
quarter on fourth quarter; BTA = Bilateral Trade Agreement.

Already in the book (cite, do not duplicate):
- `IMF_2003-2006.md`: WEO Apr 2006 US housing as "a key uncertainty"; Greenspan's "conundrum" testimony, 16 Feb 2005 ("Federal Reserve"
  section). `Theme_markets.md` MK-OTH-2: Bernanke's "global saving glut" lecture, 10 Mar 2005.
- `IMF_2007-2009.md` (WEO/GFSR 2007–09, crisis narrative); `Theme_debt.md` DF-IMF-5 (WEO Update Nov 2008 stimulus call).
- `IMF_2014-2019.md` "Other primary sources": USTR Section 301 press releases of 15 Jun and 18 Sep 2018 (Lists 1–4); FOMC 16 Dec 2015, 19
  Dec 2018 and 31 Jul 2019 decisions.
- `Theme_money.md` MO-CB-1: the FOMC Statement on Longer-Run Goals of August 2020 (average inflation targeting) and August 2025 (make-up
  language dropped; "prepared to act forcefully"), reaffirmed January 2026. Not re-read here.
- `IMF_2022-2023.md`: WEO Apr/Oct 2022 on US inflation and the Fed's 2022 hikes; WEO Oct 2023 Foreword on the US fiscal stance.
- `Theme_trade.md` TR-IMF-4 (the 2025–26 tariff episode in the WEOs) and TR-IN-5, TR-IN-6 (ES 2025-26 on the 50% US tariff; MER 2026).
- `Theme_debt.md` DF-IMF-2 (Fiscal Monitor April 2026: US gross debt 108.8 / 123.9 / 142 percent of GDP in 2019 / 2025 / 2031, peak
  132.6 in 2020; deficit 7–8 percent "despite operating near full capacity").
- `IMF_2026.md` (WEO Jan/Apr/Jul/Oct 2026 US growth, tariffs and inflation); `Theme_markets.md` MK-OTH-3/4/5 (Fed Financial Stability
  Reports 2020, 2025, Nov 2026).

---

## IMF Article IV consultations with the United States

### US-IMF-1. IMF, *United States: 2005 Article IV Consultation—Staff Report; Staff Statement; and Public Information Notice*, IMF Country Report No. 05/257, July 2005
PDF: https://www.imf.org/external/pubs/ft/scr/2005/cr05257.pdf (GUESSED; 200; 55 PDF pages; printed = PDF − 1). Read: Box 1 (p. 4), paras on
outlook, housing and imbalances (pp. 7–10), Staff Appraisal (pp. 29–31). (The 2003 and 2004 reports, CR 03/244 and 04/230, were also
downloaded from GUESSED URLs of the same pattern, 200, but not read.)
- p. 4 (Box 1, past Fund advice): the Fund backed the Fed's response to deflation risks and the mid-2004 shift to gradual tightening; staff had
  long urged an explicit inflation objective, which the authorities thought of modest benefit. The sharpest differences were on fiscal
  consolidation and global imbalances: the authorities did not accept that the CA deficit, which they saw as reflecting weak demand in
  partners, risked "disorderly adjustment".
- p. 7: the CA deficit reached 6½ percent of GDP in 2005Q1 despite a real effective depreciation of about 15 percent over three years; core
  PCE inflation just above 1½ percent, headline CPI 3½ percent; unemployment 5.1 percent.
- p. 8: financial flows "appear unsustainable": record foreign saving (net international liabilities about 25 percent of GDP); the federal
  budget swung from a 2½ percent of GDP surplus in FY2000 to a 3½ percent deficit in FY2004; household saving at record lows. Staff projected
  growth of 3½ percent in 2005 and 2006 and a CA deficit staying above 6 percent of GDP.
- p. 10 (para 15): officials saw "froth" in housing (second homes, interest-only loans) but expected prices to flatten rather than fall;
  staff agreed that "house price stagnation was the most likely scenario".
- pp. 29–31 (appraisal): "The United States has continued to be the main locomotive of global growth"; the priority is ambitious fiscal
  consolidation (budget balance excluding Social Security early in the next decade); tighter mortgage lending standards are appropriate given
  signs that home prices may exceed equilibrium in some areas; the financial sector "has proven exceptionally resilient".

### US-IMF-2. IMF, *United States: 2007 Article IV Consultation—Staff Report; Staff Statement; and Public Information Notice*, IMF Country Report No. 07/264, August 2007 (staff report dated 11 July 2007)
PDF: https://www.imf.org/external/pubs/ft/scr/2007/cr07264.pdf (GUESSED; 200; 66 PDF pages; printed = PDF − 2). Read: summary (PDF p. 3),
Staff Appraisal (pp. 26–28).
- PDF p. 3 (summary): the key topic was the prospect of a soft landing given spillovers from housing and subprime delinquencies; baseline
  growth 2 percent in 2007 and 2¾ percent in 2008. "Originate to distribute" innovation had dispersed risk, but lending standards may be
  falling. Markets were not pricing the depreciation likely needed to rebalance the CA.
- p. 26 (para 47): "The most likely scenario is a soft landing".
- p. 26 (para 49): the financial system has been "highly resilient, including to recent difficulties in the subprime mortgage market";
  innovation helped attract capital inflows.
- p. 27 (paras 50–53): new instruments make risks harder to assess just as benign conditions encourage risk-taking; fragmented regulation
  slows responses (e.g. guidance on hybrid subprime loans). "A disorderly resolution of global imbalances remains a low probability—but high
  cost—risk."
- p. 28 (paras 55–57): Congress adopted the target of budget balance by FY2012; staff wanted a stricter target (balance excluding the Social
  Security surplus); entitlement reform is the key fiscal challenge.

### US-IMF-3. IMF, *United States: 2008 Article IV Consultation—Staff Report*, IMF Country Report No. 08/255, July 2008 (staff report dated 2 July 2008)
PDF: https://www.imf.org/external/pubs/ft/scr/2008/cr08255.pdf (GUESSED; 200; 66 PDF pages; printed = PDF − 2). Read: summary (PDF p. 3),
Staff Appraisal (pp. 37–38).
- PDF p. 3: the economy had shown "remarkable resilience" to housing, finance and oil through Q2; weak 2008 and slow 2009 recovery expected;
  the shock is "unprecedented". Advice: keep rates on hold but be ready to raise them; no further generalised stimulus; use FHA guarantees
  to encourage principal write-downs; contingency plans (Treasury-backed asset swaps); bring large investment banks under Fed umbrella
  supervision. The authorities expected a faster recovery than staff. Meetings with Paulson and Bernanke on 16–17 June 2008.
- p. 37 (para 55): "extremely low" growth in 2008 (q4/q4); the outlook hinges on house prices in this "first national-level housing bust in
  at least 40 years". Para 56: bias "toward a decisive tightening once recovery is established" because of inflation expectations.
- p. 38 (para 60): dollar depreciation had moved competitiveness toward fundamentals; the narrowing external deficit was welcome.
- How it reads: ten weeks before Lehman's failure, the IMF's main US worry alongside housing was still inflation.

### US-IMF-4. IMF, *United States: 2010 Article IV Consultation—Staff Report*, IMF Country Report No. 10/249, July 2010 (staff report dated 2 July 2010)
PDF: https://www.imf.org/external/pubs/ft/scr/2010/cr10249.pdf (GUESSED; 200; 58 PDF pages; printed = PDF − 1). Read: Executive Summary
(PDF p. 2), paras 8 (p. 11) and 21 (p. 23), Staff Appraisal (pp. 41–42). (The 2009 report, CR 09/228, was downloaded from a GUESSED URL,
200, and not read.)
- PDF p. 2: recovery under way thanks to "unprecedented" stimulus and financial stabilisation, but subdued by balance-sheet headwinds; risks
  tilted down (European sovereign strains). Keep stimulus in 2010, start consolidation in 2011; cautious monetary exit; the authorities were
  more optimistic than staff.
- p. 11 (para 8): unemployment higher than in any postwar period save briefly in the 1980s; long-term unemployment, duration and involuntary
  part-time work at records; skill and geographic mismatch raised equilibrium unemployment.
- p. 23 (para 21): under current policies federal debt held by the public rises from 64 to 95 percent of GDP by 2020 and over 135 percent by
  2030.
- p. 41 (para 49): the debt ratio is set to rise to "levels not seen since the years immediately following the Second World War"; a credible
  plan is needed to stabilise debt/GDP by 2015.
- p. 42 (paras 52–53): Dodd-Frank-era draft legislation is a major step but misses the chance to consolidate regulators; "The Fed is well
  placed to manage the uncertainty of the monetary exit."

### US-IMF-5. IMF, *United States: 2013 Article IV Consultation*, IMF Country Report No. 13/236, July 2013 (staff report dated 9 July 2013)
PDF: https://www.imf.org/external/pubs/ft/scr/2013/cr13236.pdf (GUESSED; 200; 63 PDF pages; printed = PDF − 1). Read: Key Issues (PDF p.
2), para 23 (p. 17), Staff Appraisal (pp. 28–29). (The 2014 report, CR 14/221, was downloaded from a GUESSED URL, 200, and not read.)
- PDF p. 2 (Key Issues): recovery "remains modest but is gaining ground" (housing rebound, higher net worth) against strong fiscal adjustment; the
  sequester's across-the-board cuts should be replaced by back-loaded entitlement savings and new revenue; highly accommodative policy is
  appropriate; the exit needs careful timing and communication "for both the United States and other countries".
- p. 17 (para 23): staff warned that expectations of tapering "could trigger a sharper-than-expected sell-off of fixed-income assets", with
  repercussions for EM currencies and capital flows. The US authorities expressed "some skepticism" about lasting effects of higher US rates
  on emerging markets, citing more structural inflows and better fundamentals there.
- p. 28 (para 43): "The fiscal deficit reduction in 2013 is excessively rapid and ill designed."
- p. 28 (para 44): the general government deficit more than halved, from over 13 percent of GDP in 2009 to a projected 5.9 percent in 2013,
  but the long-term debt path remains unsustainable (health, Social Security, interest).

### US-IMF-6. IMF, *United States: 2017 Article IV Consultation*, IMF Country Report No. 17/239, July 2017 (staff report dated 7 July 2017)
PDF: https://www.imf.org/-/media/files/publications/cr/2017/cr17239.pdf (GUESSED; 200; the first guess under /external/pubs/ft/scr/2017/
was 404; 86 PDF pages; printed = PDF − 5). Read: Key Issues (PDF p. 6), trade section paras 43–46 (pp. 32–33), Staff Appraisal (pp.
39–40). (The 2016 report, CR 16/226, was downloaded from a GUESSED URL, 200, and not read.)
- PDF p. 6 (Key Issues): third-longest expansion since 1850, effectively at full employment, but relative to history "growth has been too
  low and too unequal"; tax reform should be revenue-enhancing; more infrastructure spending; trade integration offers gains.
- p. 33 (paras 44–45): the administration had launched reviews of bilateral goods deficits and of steel and aluminium imports on national
  security grounds; staff urged judicious use of Section 232; the US had left the Trans-Pacific Partnership and notified intent to
  renegotiate NAFTA. Authorities' view (para 46): unfair practices caused "large and persistent trade imbalances".
- p. 39 (para 61): dollar overvalued by about 10–20 percent; external position moderately weaker than fundamentals; CA deficit near 3 percent
  of GDP over the medium term. p. 40 (para 66): the Fed should raise rates gradually and accept a modest temporary overshoot of 2 percent.

### US-IMF-7. IMF, *United States: 2019 Article IV Consultation*, IMF Country Report No. 19/174, June 2019 (staff report dated 6 June 2019)
PDF: https://www.imf.org/-/media/files/publications/cr/2019/1usaea2019001.pdf (GUESSED; 200; 95 PDF pages; printed = PDF − 5). Read: Key
Issues (PDF pp. 6–7), Staff Appraisal (pp. 38–39), fiscal annex (p. 48).
- PDF p. 6: "the longest expansion in recorded history"; unemployment lowest since the late 1960s; growth to slow to about 2.6 percent (2019)
  and 1.9 percent (2020). Social indicators troubling (falling life expectancy, polarisation, eroding mobility). Leveraged corporate and
  nonbank vulnerabilities elevated.
- p. 39 (para 56): "The U.S. public debt is on an unsustainable path."; a package would need entitlement reform, higher indirect taxes and a
  federal carbon tax. Para 57: further rate rises should be deferred (the Fed had paused).
- p. 39 (paras 59–60): US–China trade tensions "represent a threat to the global outlook"; "tariff measures are likely to be ineffective at
  containing bilateral trade deficits" and will damage the US and world economy. p. 34 (PDF 39, seen in a search, not read in full):
  tariffs on steel, aluminium and some appliances remain; tariffs on US$200 billion of Chinese imports had been raised to 25 percent.
- p. 48 (fiscal annex): federal debt held by the public projected to rise from about 76 percent of GDP (2018) to about 87 percent (2028);
  general government gross debt from about 106 to 111 percent.

### US-IMF-8. IMF, *United States: 2022 Article IV Consultation*, IMF Country Report No. 22/220, July 2022 (staff report dated 24 June 2022)
PDF: https://www.imf.org/-/media/files/publications/cr/2022/english/1usaea2022001.pdf (GUESSED; 200; the .ashx variant was 404; 77 PDF
pages; printed = PDF − 5). Read: Key Issues (pp. 1–2), Outlook paras 12–13 (p. 11).
- p. 1: a strong recovery from COVID-19; unemployment back to end-2019 levels; 8.5 million jobs created since end-2020; then a sharp rise in
  wages and prices, broad-based by late 2021. The priority is to slow wage and price growth without a recession: "This will be a tricky
  task." The June 2022 FOMC hike of 75 bp with a path peaking near 4 percent "strikes the right balance".
- p. 2: "the U.S. is expected to slow but to narrowly avoid a recession"; misjudging the policy mix in either direction is costly.
- p. 11 (para 12): the broad-based inflation surge "that was viewed as the leading economic risk" at the 2021 Article IV "has become a
  reality". Para 13: growth to fall to 0.7 percent q4/q4 by end-2023; PCE inflation back to 2 percent year on year by end-2023.

### US-IMF-9. IMF, *United States: 2024 Article IV Consultation*, IMF Country Report No. 24/232, July 2024 (staff report dated 1 July 2024)
PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1usaea2024001.pdf (GUESSED; 200; 89 PDF pages; printed = PDF − 4). Read:
Key Messages (pp. 1–2), p. 20, Box 11 (p. 36), fiscal annex (p. 47).
- p. 1: "The U.S. economy has turned in a remarkable performance over the past few years." "Hysteresis effects from the pandemic did not
  materialize"; 16 million jobs since end-2020. PCE inflation peaked at 7.1 percent in mid-2022, the highest since the early 1980s; the Fed
  raised rates by 525 bp; PCE inflation 2.7 percent in April 2024, expected at 2 percent by mid-2025. Advice: "the Federal Reserve should wait
  to reduce its policy rate until at least late 2024".
- p. 2: a front-loaded adjustment of about 4 percent of GDP is needed to reach a general government primary surplus of about 1 percent;
  tariffs, non-tariff barriers and domestic-content rules distort trade and "their costs are largely borne by U.S. firms and consumers";
  external position broadly in line with fundamentals.
- p. 20: under current policies general government debt will exceed 140 percent of GDP by 2032; the deficit stays about 2½ percent of GDP
  above the 2019 Article IV forecast. p. 47: federal debt held by the public about 97 percent of GDP in FY2023, rising to about 116 percent
  by 2033; general government gross debt from about 121 to 144 percent.
- p. 36 (Box 11): the May 2024 review kept the 2018–19 Section 301 tariffs on China and raised some; evidence shows one-for-one pass-through
  to import prices, borne by US importers; welfare loss about 0.1 percent of GDP; China retaliated with tariffs of around 21 percent on
  almost 60 percent of imports from the US; supply chains rerouted through "connector" countries.

### US-IMF-10. IMF, *United States: 2026 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director for the United States*, IMF Country Report No. 2026/076, 2 April 2026 (Board 1 April 2026; staff report dated 17 March 2026)
Listing: country page https://www.imf.org/en/Countries/USA (200; "The last Article IV Executive Board Consultation was on April 1, 2026")
→ issue page https://www.imf.org/en/publications/cr/issues/2026/04/01/united-states-2026-article-iv-consultation-press-release-staff-report-and-statement-by-the-575120
(200). PDF: https://www.imf.org/-/media/files/publications/cr/2026/english/1usaea2026001.pdf (200; 93 PDF pages; press release printed =
PDF − 1; staff report printed = PDF − 5). Read: press release (pp. 1–3), Key Issues (pp. 1–2), tariffs section (p. 12).
- Press release p. 1: growth 2 percent in 2025 despite the Q4 government shutdown; productivity growth strong; employment growth slowed,
  partly from "sharply lower immigration"; inflation moved sideways in 2025 as tariffs raised goods prices; federal deficit 6.3 → 5.9
  percent of GDP in FY2025; general government debt 123.9 percent of GDP; CA deficit 3.7 percent of GDP. Growth 2.4 percent q4/q4 in 2026;
  core PCE back to 2 percent in 2027H1; unemployment near 4 percent in 2026–27.
- Press release p. 2: general government deficit 7–7½ percent of GDP with debt exceeding 140 percent of GDP by 2031; applied effective tariff
  rate to settle at 7–8.5 percent; Directors: the 2025 rate cuts were appropriate, but "little room" to cut in 2026 given energy prices (the
  Middle East war). p. 3: Directors concerned that higher tariffs and uncertainty will reduce US activity with sizeable spillovers;
  disorderly external rebalancing a risk as the NIIP worsens.
- Key Issues p. 1: strong productivity "has set the U.S. economy apart from its peers"; "there is little scope to lower the policy rate over
  the coming year"; adjustment of about 4 percent of GDP still needed. p. 2: CA deficit to stay around 3½–4 percent of GDP; national-security
  trade measures should be applied narrowly.
- p. 12 (paras 14–15): bilateral deals with the EU, Japan, Korea and the UK institutionalise higher US tariffs; in February, after a Supreme
  Court ruling, an EO ended the IEEPA tariffs and a 10 percent surcharge under section 122 (150 days) was imposed; the administration
  signalled other authorities would replicate the IEEPA tariffs. Footnote 8: the switch cut the statutory effective rate from 16.9 to 13.5
  percent (WTO-IMF Tariff Tracker). Tariff revenue about 0.7 percent of GDP in FY25/26 (CBO: about 1 percent).
- FLAG (source typo): para 15 says the statutory rate was 13.5 percent "at end-February 2025"; footnote 8 and the context show end-February
  2026. Do not copy the year.

## Federal Reserve (FOMC statements and press releases)

Listings: https://www.federalreserve.gov/monetarypolicy/fomchistorical2008.htm, ...2009.htm, ...2012.htm, ...2015.htm, ...2020.htm (all 200)
and https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm (200; links 2021–2026 statements). Each statement read in full. Rates
are the federal funds target range.

### US-FED-1. Federal Reserve, press release of 25 November 2008 (GSE debt and MBS purchases) and FOMC statement of 16 December 2008
URLs: https://www.federalreserve.gov/newsevents/press/monetary/20081125b.htm (GUESSED; not on the FOMC listing because it is a Board release;
200) and https://www.federalreserve.gov/newsevents/press/monetary/20081216b.htm (from the 2008 listing; 200).
- 25 Nov 2008: purchases of up to $100 billion of GSE direct obligations and up to $500 billion of MBS backed by Fannie Mae, Freddie Mac and
  Ginnie Mae, to reduce the cost of credit for house purchases (the start of what was later called QE1).
- 16 Dec 2008: decided "to establish a target range for the federal funds rate of 0 to 1/4 percent"; "The Federal Reserve will employ all
  available tools"; rates likely to stay exceptionally low "for some time"; evaluating purchases of longer-term Treasuries; TALF early in
  2009. Discount rate cut 75 bp to ½ percent.

### US-FED-2. FOMC statement, 18 March 2009
URL: https://www.federalreserve.gov/newsevents/press/monetary/20090318a.htm (from the 2009 listing; 200).
- Rate kept at 0 to ¼ percent "for an extended period". Additional agency MBS purchases of up to $750 billion (total up to $1.25 trillion this
  year), agency debt up to $200 billion, and up to $300 billion of longer-term Treasuries over six months. The Committee saw "some risk"
  of inflation persisting below desirable rates.

### US-FED-3. FOMC statement, 13 September 2012 (QE3)
URL: https://www.federalreserve.gov/newsevents/pressreleases/monetary20120913a.htm (from the 2012 listing; 200).
- Agency MBS purchases of $40 billion a month; with Operation Twist and reinvestment, longer-term holdings rise about $85 billion a month to
  year-end. Open-ended: "If the outlook for the labor market does not improve substantially" purchases continue. Rate 0 to ¼ percent;
  accommodation to stay "for a considerable time after the economic recovery strengthens".

### US-FED-4. FOMC statement, 16 December 2015 (first rise after the crisis)
URL: https://www.federalreserve.gov/newsevents/pressreleases/monetary20151216a.htm (from the 2015 listing; 200).
- Target range raised to ¼ to ½ percent; "it is reasonably confident that inflation will rise" to 2 percent over the medium term; increases
  expected to be "only gradual". (Later 2018 peak of 2¼–2½ percent and the July 2019 cut: `IMF_2014-2019.md`.)

### US-FED-5. FOMC statements of 3, 15 and 23 March 2020
URLs: https://www.federalreserve.gov/newsevents/pressreleases/monetary20200303a.htm, ...monetary20200315a.htm, ...monetary20200323a.htm
(from the 2020 listing; all 200).
- 3 Mar (unscheduled): "The fundamentals of the U.S. economy remain strong."; range cut ½ point to 1–1¼ percent because of coronavirus risks.
- 15 Mar (Sunday): range cut to 0 to ¼ percent, to be held until the economy "has weathered recent events"; Treasury holdings to rise by at
  least $500 billion and agency MBS by at least $200 billion.
- 23 Mar: purchases of Treasuries and agency MBS "in the amounts needed to support smooth market functioning", i.e. open-ended; agency CMBS
  added.

### US-FED-6. FOMC statements of 16 March 2022 (first hike) and 26 July 2023 (cycle peak)
URLs: https://www.federalreserve.gov/newsevents/pressreleases/monetary20220316a.htm (calendar page; 200) and ...monetary20230726a.htm (calendar
page; 200).
- 16 Mar 2022: range raised to ¼ to ½ percent with "ongoing increases" expected; inflation elevated by pandemic imbalances, energy and
  broader pressures; Russia's invasion adds upward pressure. Bullard dissented, preferring ½ point.
- 26 Jul 2023: range raised to 5¼ to 5½ percent (the 525 bp total cited in US-IMF-9 p. 1).

### US-FED-7. FOMC statements of 18 September 2024 (first cut) and 18 December 2024
URLs: https://www.federalreserve.gov/newsevents/pressreleases/monetary20240918a.htm and ...monetary20241218a.htm (calendar page; both 200).
- 18 Sep 2024: range cut ½ point to 4¾ to 5 percent; "greater confidence" that inflation is moving sustainably to 2 percent; Bowman dissented
  for ¼ point. (The IMF had advised waiting "until at least late 2024", US-IMF-9 p. 1.)
- 18 Dec 2024: cut ¼ point to 4¼ to 4½ percent; Hammack dissented for no change.

### US-FED-8. FOMC statements of 17 September, 29 October and 10 December 2025
URLs: https://www.federalreserve.gov/newsevents/pressreleases/monetary20250917a.htm, ...monetary20251029a.htm, ...monetary20251210a.htm
(calendar page; all 200).
- 17 Sep 2025 (first cut of 2025, after holding at 4¼–4½ since December 2024): ¼ point to 4–4¼ percent, "in light of the shift in the
  balance of risks"; downside risks to employment had risen; inflation "has moved up". Miran dissented for ½ point.
- 29 Oct 2025: ¼ point to 3¾–4 percent; balance-sheet runoff to end on 1 December; Miran (½ point) and Schmid (no change) dissented.
- 10 Dec 2025: ¼ point to 3½–3¾ percent; Miran (½ point), Goolsbee and Schmid (no change) dissented.
- Framework: the August 2025 revised Statement on Longer-Run Goals is MO-CB-1 (`Theme_money.md`).

### US-FED-9. FOMC statements of 28 January, 18 March, 29 April, 17 June, 29 July, 16 September and 28 October 2026
URLs: https://www.federalreserve.gov/newsevents/pressreleases/monetary20260128a.htm, ...20260318a, ...20260429a, ...20260617a,
...20260729a, ...20260916a, ...20261028a (calendar page; all 200).
- January–July 2026: range held at 3½–3¾ percent. January: Miran and Waller dissented for a ¼ point cut. April: Miran (cut) dissented, and
  Hammack, Kashkari and Logan dissented against an "easing bias" in the statement (wording cut off in my extract). The April statement is the
  last one that lists Powell as Chair.
- From 17 June 2026 the statement is much shorter, opens with the vote ("12 – 0"), drops the named voting list and ends: "The Committee will
  deliver price stability." June: inflation elevated partly from supply shocks including energy; the Middle East conflict adds uncertainty.
  July: held 9–3; Hammack, Kashkari and Logan wanted a ¼ point rise.
- 16 Sep 2026: range raised ¼ point to 3¾–4 percent (12–0): "Today's policy action will support a timelier return to the Committee's 2
  percent goal." Productivity growth strong, capital investment robust.
- 28 Oct 2026 (latest): held at 3¾–4 percent (10–2); activity "expanding at a strong pace"; Cook and Hammack dissented for another ¼ point
  rise.
- Who chaired the FOMC from June 2026 is not stated in these statements; not checked elsewhere.

## US fiscal, trade and legal sources

### US-OTH-1. Council of Economic Advisers, *Economic Report of the President*, February 2002, Chapter 1 "Restoring Prosperity"
Listing: govinfo ERP collection https://www.govinfo.gov/app/collection/erp (200, script shell) and its browse API
https://www.govinfo.gov/wssearch/rb/erp?fetchChildrenOnly=0 (200; lists years only). PDF: https://www.govinfo.gov/content/pkg/ERP-2002/pdf/ERP-2002.pdf
(GUESSED package name; 200; 446 PDF pages). Read: CEA introduction (p. 15), Chapter 1 opening (pp. 23–24), fiscal policy (p. 43).
- p. 15: much of the late-1990s productivity acceleration is judged permanent, credited to new technology and better business methods.
- pp. 23–24: real GDP growth over the first three quarters of 2001 was 0.1 percent annualised, with Q3 at −1.3 percent; the September 11
  attacks tipped a stalling economy into the first recession in a decade.
- p. 43: the federal surplus, "still substantial by historical standards", fell in 2001; the February 2001 budget planned on "continuing the
  retirement of the Federal debt" alongside tax relief.

### US-OTH-2. Council of Economic Advisers, *Economic Report of the President*, 2026 (President's letter dated "April 13"; Chapter 3 on trade)
PDF: https://www.govinfo.gov/content/pkg/ERP-2026/pdf/ERP-2026.pdf (GUESSED package name, same pattern; 200; 450 PDF pages; printed = PDF −
5). Read: President's letter (pp. 3–5), tariff and deal passages in Chapter 3 (pp. 67–72). (ERP 2025 also downloaded, 200; not read.)
- pp. 3–4: OBBBA called the largest tax cut in history; the CEA estimates it raises real GDP 4.6–4.9 percent over four years; with
  deregulation and tariffs, "our policies will decrease federal debt to 94 percent of GDP" in ten years versus a 117 percent baseline; the
  federal deficit down $362 billion in 2025 versus 2024.
- p. 5: "Tariffs have already catalyzed trade deals" that open markets and aim to close the trade deficit; illegal border crossings reduced
  "to effectively zero".
- p. 67 (Table 3-1): January–October 2025 versus 2024, goods imports from China fell $97.1 billion (−26.7 percent); imports from Taiwan rose
  $59.6 billion (+61.5 percent).
- p. 72: in February 2026 the US and India reached a framework for a reciprocal trade agreement; India to eliminate or cut tariffs on US
  industrial and farm goods; US tariff on Indian goods cut to 18 percent; India committed to buy $500 billion of US exports over five years.
- Contrast (for the box): the IMF in the same weeks projected general government debt above 140 percent of GDP by 2031 (US-IMF-10), and
  the Fiscal Monitor 142 percent (DF-IMF-2). The ERP's 94 percent refers to federal debt (held by the public, by its baseline comparison),
  a narrower measure; the two are not directly comparable.

### US-OTH-3. US Treasury, Bureau of the Fiscal Service, "Debt to the Penny" dataset (fiscaldata.treasury.gov)
Dataset page https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/ (200; gives the API base
https://api.fiscaldata.treasury.gov/services/api/fiscal_service/). Queries (endpoint path v2/accounting/od/debt_to_penny from the dataset's
API documentation pattern, GUESSED): e.g. ...debt_to_penny?filter=record_date:eq:2008-09-30 (200). Own reading of values, in trillions of
dollars, total public debt outstanding / debt held by the public:
- 29 Sep 2000: 5.67 / 3.41. 28 Sep 2007: 9.01 / 5.05. 30 Sep 2008: 10.02 / 5.81. 30 Sep 2009: 11.91 / 7.55. 30 Sep 2019: 22.72 / 16.81.
  30 Sep 2020: 26.95 / 21.02. 30 Sep 2025: 37.64 / 30.28. 30 Sep 2026: 40.17 / 32.43. Latest, 19 Nov 2026: 40.71 / 32.90.
- No ratios to GDP computed (no GDP series fetched); use IMF ratios (US-IMF-9, US-IMF-10, DF-IMF-2) for shares of GDP.

### US-OTH-4. Proclamation 9705 of 8 March 2018, "Adjusting Imports of Steel Into the United States" (83 FR 11625, 15 March 2018)
Listing: Federal Register API search (presidential documents, 2018, "Adjusting Imports of Steel", 200) → document 2018-05478 → govinfo PDF
https://www.govinfo.gov/content/pkg/FR-2018-03-15/pdf/2018-05478.pdf (200). Read: operative paragraphs.
- Section 232 steel tariff: an additional 25 percent ad valorem duty effective 23 March 2018. (Aluminium: Proclamation 9704 of the same day,
  named in EO 14257; not read.) China Section 301 lists of 2018: `IMF_2014-2019.md`.

### US-OTH-5. Executive Order 14257 of 2 April 2025, "Regulating Imports With a Reciprocal Tariff To Rectify Trade Practices That Contribute to Large and Persistent Annual United States Goods Trade Deficits" (90 FR 15041, 7 April 2025)
Listing: Federal Register API (term "reciprocal tariff", presidential documents; 200) → document 2025-06063 → govinfo PDF
https://www.govinfo.gov/content/pkg/FR-2025-04-07/pdf/2025-06063.pdf (200 on the second attempt; the first download was truncated). The
federalregister.gov full-text pages returned a "Request Access" page (not pursued). Read: secs. 1–3 and Annex I.
- Sec. 2–3: an additional duty on all imports from all trading partners that "shall start at 10 percent" (from 5 April 2025), with higher
  country rates in Annex I from 9 April 2025; steel, aluminium and autos under Section 232, and Annex II goods (copper, pharmaceuticals,
  semiconductors, lumber, some critical minerals, energy) excluded.
- Annex I: India 26 percent (printed "subject to an additional duty of26%"); EU 20 percent; Indonesia 32 percent.
- The order's background cites India's tariffs on some goods (e.g. 70 and 80 percent rates) as examples of non-reciprocity.

### US-OTH-6. Executive Order 14326 of 31 July 2025, "Further Modifying the Reciprocal Tariff Rates" (90 FR 37963, 6 August 2025)
Federal Register API → document 2025-15010 → https://www.govinfo.gov/content/pkg/FR-2025-08-06/pdf/2025-15010.pdf (200). Read: secs. 1–2;
Annex I (90 FR 37967, an image, read visually).
- Replaces the April country rates with "adjusted" rates from 7 days after the order; partners that agreed or neared deals were contrasted
  with those that "failed to align". Annex I: India 25 percent; Bangladesh 20; Indonesia 19; Cambodia 19; Brazil 10; EU goods topped up to
  15 percent.

### US-OTH-7. Supreme Court of the United States, *Learning Resources, Inc. v. Trump*, No. 24–1287, decided 20 February 2026 (together with *Trump v. V.O.S. Selections*, No. 25–250), 607 U.S. 229
Listing: https://www.supremecourt.gov/opinions/slipopinion/25 (200; row 12, dated 2/20/26, with the link and the summary "does not authorize
the President to impose tariffs"). PDF: https://www.supremecourt.gov/opinions/25pdf/607us2r12_8nj9.pdf (200; preliminary print, 164 PDF
pages). Read: syllabus (pp. 229–234).
- Held: "IEEPA does not authorize the President to impose tariffs." The case covered the fentanyl tariffs (25 percent on most Canadian and
  Mexican goods, 10 percent on most Chinese goods) and the reciprocal tariffs (at least 10 percent on all partners). Argued 5 November 2025.
- Line-up (p. 234): Roberts wrote for the Court, joined in the key parts by Sotomayor, Kagan, Gorsuch, Barrett and Jackson; Thomas,
  Kavanaugh and Alito dissented (a 6–3 split, my count from the syllabus).

### US-OTH-8. Executive Order 14389 of 20 February 2026, "Ending Certain Tariff Actions" (91 FR 9437), and Proclamation 11012 of 20 February 2026, "Imposing a Temporary Import Surcharge To Address Fundamental International Payments Problems" (91 FR 9339; both published 25 February 2026)
Federal Register API → documents 2026-03832 and 2026-03824 → govinfo PDFs https://www.govinfo.gov/content/pkg/FR-2026-02-25/pdf/2026-03832.pdf
and .../2026-03824.pdf (both 200). Read: EO in full; proclamation paras 1–3, 13–18 and the first operative clauses.
- EO 14389: the IEEPA duties under EOs 14193–14195, 14245, 14257, 14323 (Brazil), 14329 (India/Russian oil), 14380 and 14382 "shall no
  longer be in effect", "In light of recent events" (the order does not name the Court).
- Proclamation 11012: under section 122 of the Trade Act of 1974, a "temporary import surcharge of 10 percent ad valorem" for 150 days from
  24 February 2026, citing a "large and serious" balance-of-payments deficit; section 122 allows up to 15 percent for 150 days unless
  Congress extends it; exemptions in Annexes I–II (e.g. certain critical minerals).

### US-OTH-9. Presidential memorandum of 23 July 2026, "Actions by the United States in the Investigations Under Section 301 of the Trade Act of 1974 of the Acts, Policies, and Practices of 60 Economies Related to the Failure of Each Economy To Impose and Effectively Enforce a Prohibition on the Importation of Goods Produced With Forced Labor" (91 FR 47717, 28 July 2026)
Federal Register API → document 2026-15274 → https://www.govinfo.gov/content/pkg/FR-2026-07-28/pdf/2026-15274.pdf (200 on the second
attempt). Read: pp. 47717–47721.
- USTR opened Section 301 investigations of 60 economies on 12 March 2026 (India is no. 24). Directed tariffs: 10 percent on 17 economies
  including India, Canada, Mexico and the UK; for the EU and Taiwan, MFN plus Section 301 capped at 10 percent; for Japan, Korea and
  Switzerland capped at 12.5 percent; 12.5 percent for other actionable economies (China among the 60). India is moved to the 10 percent
  group because it imposed a forced-labour import prohibition after consultation. Product exemptions in an annex. Effective date not found in
  the pages read.
- Reads as the replacement for the 150-day section 122 surcharge (US-OTH-8), as the IMF anticipated (US-IMF-10 p. 12); that link is my
  inference, not stated in the memorandum pages read.

## India and the United States

### US-IN-1. Government of India, Ministry of Finance, *Economic Survey 2008-09* (on disk)
File: `es2008-09.txt` (Ch. 1: printed = PDF; Ch. 2 onward: printed = PDF − 1). Read: pp. 13, 18, 156.
- p. 13: merchandise exports to the United States, the largest market, fell 1.6 percent in April–February 2008-09, while exports to Asia rose
  6.9 percent.
- p. 18 (paras 2.11–2.15): the crisis began in US subprime-based structured products; India first saw a "positive shock" (net FII inflows of
  US$22.5 billion, September 2007–January 2008), then a reversal of US$15.8 billion in February–June 2008; after Lehman, trade finance
  dried up. "The impact on Indian economy was less severe" thanks to lower export dependence; Indian banks had very limited exposure to the
  US mortgage market.
- p. 156: China became India's largest trading partner in April–February 2008-09, with the US share down about 2 points; India ran a trade
  surplus with the US.

### US-IN-2. *Economic Survey 2013-14* (on disk)
File: `es2013-14.txt` (printed = PDF). Read: pp. 16, 113.
- p. 16 (paras 1.44–1.45): in May 2013 signals of Fed tapering triggered capital outflows and a sharp rupee fall; easing was interrupted; in
  mid-July 2013 the RBI raised the MSF rate 200 bp to 10.25 percent and capped LAF borrowing.
- p. 113 (paras 6.28–6.29): the rupee fell sharply from May 2013 on a high CAD and FII debt outflows, averaging ₹63.75 per dollar at its
  September 2013 peak, then ₹61.62 in October; "the rupee became resilient when the US Fed taper actually happened subsequently".

### US-IN-3. *Economic Survey 2016-17*, Vol. 2 (released 2017), Chapter "Services Sector", Box 2 "IT-BPM: Slowdown Challenges" (on disk)
File: `es2016-17.txt` (p. 249 = PDF 600). Read: p. 249.
- The "Buy American, Hire American" order (2017) led to tighter scrutiny of high-skill visas; a USCIS memo said "computer programmers" do not
  automatically qualify for H-1B; the Survey argues that "Misconstruing mobility of skilled people as an immigration issue is a deterrent"
  to the business. Similar UK and Australian curbs noted.

### US-IN-4. *Economic Survey 2018-19*, Vol. 2, and *Economic Survey 2019-20*, Vol. 2, Chapter "External Sector" (on disk)
Files: `es2018-19.txt` (p. 153 = PDF 393), `es2019-20.txt` (p. 75 = PDF 391, p. 78 = PDF 394). Read: those pages.
- ES 2018-19 p. 153: the USA remained India's largest export destination, 16 percent of exports in 2018-19.
- ES 2019-20 p. 75 (Table 3): India has run a trade surplus with the USA every year since 2014-15: US$20.63 bn (2014-15), 18.55, 19.90,
  21.27, 16.86 (2018-19), 10.91 (April–November 2019); deficit with China US$53.57 bn in 2018-19. p. 78 (para 3.16): the USA is still the
  largest export destination, and exports to it grew fastest between 2011-12 and 2019-20.

### US-IN-5. *Economic Survey 2022-23* and *Economic Survey 2023-24*, External Sector chapters (on disk)
Files: `es2022-23.txt` (p. 318 = PDF 361), `es2023-24.txt` (p. 152 = PDF 199). Read: those pages.
- ES 2022-23 p. 318 (para 11.15): the USA was the top export destination in April–November 2022; the USA's share of India's imports fell to
  6.9 percent from 7.2 percent.
- ES 2023-24 p. 152 (para 4.85): "the US was India’s second-largest trading partner in FY24 after China"; US import volume fell 1.7 percent in
  2023 (OECD), a downside risk to Indian exports.

### US-IN-6. *Economic Survey 2025-26* (January 2026), Preface and Chapter 4 "External Sector" (on disk; complements TR-IN-5)
File: `es2025-26.txt` (Preface p. vii = PDF 8; p. 174 = PDF 225; printed = PDF − 51 in the main text). Read: those pages. Tariff passages
(p. 2, p. 159, Table IV.1) are in TR-IN-5 and `India_ES_2024-2026.md`.
- Preface p. vii: the US announced "reciprocal tariffs of 25% on India in April"; India "was expected to be one of the early winners", so the
  August "additional penal tariff of 25%" on most merchandise surprised many; growth forecasts were cut but growth accelerated on reforms
  (GST overhaul, labour codes).
- FLAG (Survey vs order): EO 14257's Annex I set India at 26 percent in April 2025; 25 percent came with EO 14326 of 31 July 2025 (US-OTH-5,
  US-OTH-6). Cite the orders for rates and dates.
- p. 174 (para 4.65): RBI's sixth remittance survey (FY24): advanced economies now contribute more than the Gulf; "The US is the top
  contributor with 27.7 per cent", ahead of the UAE (19.2), UK (10.8) and Singapore (6.6).

### US-IN-7. Executive Order 14329 of 6 August 2025, "Addressing Threats to the United States by the Government of the Russian Federation" (90 FR 38701), and Executive Order 14384 of 6 February 2026, "Modifying Duties To Address Threats to the United States by the Government of the Russian Federation" (91 FR 6501)
Federal Register API → documents 2025-15267 and 2026-02818 → govinfo PDFs .../FR-2025-08-11/pdf/2025-15267.pdf and
.../FR-2026-02-11/pdf/2026-02818.pdf (both 200). Read: in full.
- EO 14329: finds India "directly or indirectly importing Russian Federation oil" and imposes "an additional ad valorem rate of duty of 25
  percent" on Indian goods from 21 days after the order, stacked on the EO 14257 duty (hence 50 percent), with Section 232 goods and EO
  14257 Annex II goods excluded.
- EO 14384: "India has committed to stop directly or indirectly importing Russian Federation oil", will buy US energy, and agreed a 10-year
  defence framework; the extra 25 percent ends from 7 February 2026.

### US-IN-8. White House: "United States-India Joint Leaders' Statement" (13 February 2025); "United States-India Joint Statement" (6 February 2026); "Fact Sheet: The United States and India Announce Historic Trade Deal" (9 February 2026)
Listing: whitehouse.gov site search https://www.whitehouse.gov/?s=India (200). URLs:
https://www.whitehouse.gov/briefings-statements/2025/02/united-states-india-joint-leaders-statement/,
https://www.whitehouse.gov/briefings-statements/2026/02/united-states-india-joint-statement/,
https://www.whitehouse.gov/fact-sheets/2026/02/fact-sheet-the-united-states-and-india-announce-historic-trade-deal/ (all 200). Read: trade
paragraphs.
- 13 Feb 2025 (Modi visit): "Mission 500", "aiming to more than double total bilateral trade to $500 billion by 2030"; first tranche of a BTA
  to be negotiated "by fall of 2025".
- 6 Feb 2026: framework for an Interim Agreement; reciprocal tariff of 18 percent under EO 14257 on Indian goods; removal, on conclusion,
  of tariffs on generic pharmaceuticals, gems and diamonds and aircraft parts; India to eliminate or cut tariffs on all US industrial goods
  and many farm goods.
- 9 Feb 2026 fact sheet: the US "will lower the Reciprocal Tariff on India from 25% to 18%" and removed the extra 25 percent; India
  "intends" to buy over $500 billion of US energy, ICT, coal and other products.
- What followed: 14 days later the IEEPA basis of the 18 percent fell (US-OTH-7, US-OTH-8), leaving the 10 percent section 122 surcharge,
  then a 10 percent Section 301 rate on India from July 2026 (US-OTH-9). The WEO April 2026 records the additional US tariff on India falling
  "from 50 to 10 percent" (`IMF_2026.md`).

### US-IN-9. Executive Order 14436 of 16 October 2026, "Implementing the Lindsey O. Graham Sanctioning Russia and Iran Act of 2026" (91 FR 66627, 21 October 2026)
Federal Register API (term "India Russian Federation oil"; 200) → document 2026-21599 → govinfo PDF .../FR-2026-10-21/pdf/2026-21599.pdf (200).
Read: secs. 1, 2 and 4.
- The Graham Act was signed on 18 September 2026. It raises duties on Russian goods by 500 percent and on goods of the largest five importers
  of Russian crude and gas by 100 percent if they make new purchases on or after 18 October 2026; the same order waives these duties and the
  related sanctions under section 115, with a certification to Congress.
- This confirms the "Graham Bill" reported in MER September 2026 (`India_2026.md` IN26-40, flagged there for verification): it became law
  but its tariffs were waived at once. India is not named in the sections read.

---

## Synthesis

1. **Imbalances were the IMF's US worry before 2008, not banks.** In 2005 the CA deficit hit 6½ percent of GDP and net foreign liabilities
   about 25 percent (US-IMF-1 pp. 7–8). The IMF judged house-price "stagnation" the likely outcome (p. 10) and the financial sector
   "exceptionally resilient" (p. 31). In July 2007 it called the system "highly resilient" to subprime problems and a soft landing most
   likely (US-IMF-2 p. 26). In July 2008 it still leaned toward tightening (US-IMF-3 p. 37). Context: Greenspan's conundrum and Bernanke's
   saving glut (`IMF_2003-2006.md`; MK-OTH-2).
2. **The crisis response: zero rates and the balance sheet.** The Fed began MBS purchases on 25 Nov 2008 and set 0–¼ percent on 16 Dec 2008
   (US-FED-1). It expanded to $1.25 trillion of MBS plus $300 billion of Treasuries in March 2009 (US-FED-2), and in September 2012 began
   open-ended QE3 at $40 billion a month (US-FED-3). It first raised rates on 16 Dec 2015, to ¼–½ percent (US-FED-4).
3. **A slow, jobless recovery and the debt shadow.** In 2010 unemployment was the highest of the postwar era bar a brief 1980s spell, and the
   IMF projected federal debt held by the public rising from 64 to 95 percent of GDP by 2020 (US-IMF-4 pp. 11, 23). By 2013 it called fiscal
   tightening "excessively rapid and ill designed" (US-IMF-5 p. 28). Treasury data show debt held by the public rising from $5.81 trillion
   (Sept 2008) to $16.81 trillion (Sept 2019) (US-OTH-3).
4. **Taper risk was flagged; India felt it.** The IMF warned in July 2013 that taper expectations could trigger a disorderly bond sell-off
   with EM spillovers; US officials were sceptical (US-IMF-5 p. 17). India's rupee fell to ₹63.75 per dollar (Sept 2013 average) and the RBI
   tightened (US-IN-2 pp. 16, 113).
5. **2017–19: "too low and too unequal", then tariffs.** The IMF called post-crisis growth "too low and too unequal" (US-IMF-6 PDF p. 6) and
   urged restraint on Section 232 (p. 33). Steel tariffs of 25 percent started on 23 Mar 2018 (US-OTH-4); China lists followed
   (`IMF_2014-2019.md`). By 2019 the expansion was the longest on record, but the IMF called debt "on an unsustainable path" and tariffs
   ineffective against bilateral deficits (US-IMF-7 pp. 38–39).
6. **The pandemic: a rapid policy response, then inflation.** On 3–23 March 2020 the Fed cut to zero and moved to open-ended purchases
   (US-FED-5). By mid-2022 jobs were back but inflation was broad-based; the IMF expected a narrow escape from recession and PCE at 2 percent
   by end-2023 (US-IMF-8 pp. 1–2, 11). The Fed hiked from 16 Mar 2022 to 5¼–5½ percent by July 2023 (US-FED-6). PCE inflation peaked at 7.1
   percent (US-IMF-9 p. 1). The August 2020 framework and its 2025 rewrite are in MO-CB-1.
7. **The soft landing that happened.** By July 2024 the IMF described a "remarkable performance": no hysteresis, 16 million jobs, PCE 2.7
   percent (US-IMF-9 p. 1). The Fed began cutting on 18 Sep 2024 with ½ point (US-FED-7), earlier than the IMF's "at least late 2024". The
   2024 report found the 2018–19 tariffs' costs borne by US importers (p. 36).
8. **2025: tariffs at century highs, then rate cuts.** EO 14257 imposed a 10 percent baseline from 5 April 2025 and country rates from 9 April
   (India 26 percent) (US-OTH-5). EO 14326 reset rates from August (India 25 percent) (US-OTH-6); the WEO trail is in TR-IMF-4. The Fed cut
   three times from September to 3½–3¾ percent by December 2025, amid split votes (US-FED-8).
9. **2026: the courts, workarounds and a hike.** On 20 Feb 2026 the Supreme Court held that IEEPA does not authorise tariffs (US-OTH-7). The
   same day the IEEPA duties were ended and a 10 percent section 122 surcharge was imposed for 150 days (US-OTH-8). July brought Section 301
   tariffs of 10–12.5 percent on 60 economies (US-OTH-9). The IMF puts the applied effective rate at 7–8.5 percent (US-IMF-10 p. 12). With
   the Middle East war lifting energy prices, the Fed held, then raised rates to 3¾–4 percent on 16 Sep 2026 (US-FED-9).
10. **The fiscal gap is the constant.** Every Article IV from 2005 to 2026 asked for consolidation (US-IMF-1 p. 30; US-IMF-9 p. 2). General
    government debt was 123.9 percent of GDP in 2025 and is projected above 140 percent by 2031, with deficits of 7–7½ percent (US-IMF-10
    pp. 1–2; DF-IMF-2). The ERP 2026 instead projects federal debt falling to 94 percent through growth and tariffs (US-OTH-2 p. 4). Total
    public debt reached $40.71 trillion on 19 Nov 2026 (US-OTH-3).
11. **India, part 1: the US as market, paymaster and shock-transmitter.** The US was India's largest export market through the period (US-IN-1
    p. 13; US-IN-4; US-IN-5). India ran surpluses of about US$17–21 billion a year with it in 2014-15 to 2018-19 (US-IN-4 p. 75). The US
    became the top source of remittances (27.7 percent in FY24) (US-IN-6 p. 174). Shocks came through US finance in 2008 and 2013 (US-IN-1 p.
    18; US-IN-2 p. 113) and through visas in 2017 (US-IN-3 p. 249).
12. **India, part 2: from "early winner" to 50 percent and back.** In February 2025 the leaders promised a BTA tranche by fall 2025 (US-IN-8).
    Instead India faced 25 percent plus a 25 percent Russian-oil penalty from August 2025 (US-OTH-6; US-IN-7), a surprise to the Survey
    (US-IN-6 p. vii). On 6 February 2026 came a framework at 18 percent and the end of the penalty (US-IN-7; US-IN-8; US-OTH-2 p. 72). After
    the Court ruling the rate became 10 percent under section 122, then 10 percent under Section 301 (US-OTH-8; US-OTH-9). The Graham Act's
    100 percent Russian-oil tariff was waived on enactment (US-IN-9). The MER still calls relations "unsettled" (`India_2026.md`).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| 2002 | ERP 2002 (US-OTH-1) | Budget plans assume "continuing the retirement of the Federal debt" | Debt held by the public rose from $3.41 tn (Sept 2000) to $32.90 tn (Nov 2026) (US-OTH-3) |
| 2005 | IMF Art. IV (US-IMF-1) | House prices most likely to stagnate; financial sector "exceptionally resilient" | 2008: "first national-level housing bust in at least 40 years" (US-IMF-3 p. 37); zero rates by Dec 2008 (US-FED-1) |
| 2005 | IMF Art. IV (US-IMF-1) | CA deficit above 6% of GDP; risk of disorderly adjustment | The deficit narrowed with the dollar's fall by 2008 (US-IMF-3 p. 38) and was 3.7% in 2025 (US-IMF-10 p. 1); no dollar crisis, but the IMF still flags disorderly rebalancing (US-IMF-10 p. 3) |
| 2007 | IMF Art. IV (US-IMF-2) | System "highly resilient" to subprime; soft landing most likely | Recession and crisis; Fed at 0–¼% and buying $1.25 tn of MBS by March 2009 (US-FED-1, US-FED-2) |
| 2008 (Jul) | IMF Art. IV (US-IMF-3) | Be ready to tighten once recovery is established | Rates stayed at 0–¼% from Dec 2008 until Dec 2015 (US-FED-1, US-FED-4) |
| 2010 | IMF Art. IV (US-IMF-4) | Federal debt held by public 64% → 95% of GDP by 2020 under current policies | About 97% in FY2023; general government 121% (US-IMF-9 p. 47) |
| 2013 | IMF Art. IV (US-IMF-5) | Taper expectations could trigger a disorderly sell-off with EM spillovers; US officials sceptical | May–Sept 2013 rupee slide to ₹63.75/$, RBI tightening (US-IN-2 pp. 16, 113) |
| 2019 | IMF Art. IV (US-IMF-7) | Gross general government debt 106% → 111% by 2028 | 123.9% in 2025, >140% projected by 2031 (US-IMF-10 pp. 1–2) |
| 2019 | IMF Art. IV (US-IMF-7) | Tariffs ineffective at cutting bilateral deficits | 2024: costs borne by US importers, supply chains rerouted via connector countries (US-IMF-9 p. 36); CA deficit 3.7% in 2025 (US-IMF-10 p. 1) |
| 2022 | IMF Art. IV (US-IMF-8) | Growth 0.7% q4/q4 by end-2023; PCE 2% by end-2023; narrowly avoid recession | No recession; 16 mn jobs; PCE 2.7% in Apr 2024 (US-IMF-9 p. 1); core PCE 2% only in 2027H1 (US-IMF-10) |
| 2024 | IMF Art. IV (US-IMF-9) | Fed should wait until at least late 2024 to cut; PCE 2% by mid-2025 | Fed cut ½ point on 18 Sep 2024 (US-FED-7); inflation "moved sideways" in 2025 (US-IMF-10 p. 1); Fed raised rates again in Sep 2026 (US-FED-9) |
| 2026 (Apr) | ERP 2026 (US-OTH-2) | Federal debt to fall to 94% of GDP over 10 years | IMF: general government debt >140% by 2031 (US-IMF-10; DF-IMF-2); measures differ |
| 2009 | ES 2008-09 (US-IN-1) | Impact on India less severe thanks to low export dependence; banks barely exposed to US mortgages | FII reversal of US$15.8 bn and falling exports to the US still slowed growth (US-IN-1 pp. 13, 18) |
| 2014 | ES 2013-14 (US-IN-2) | The taper announcement shook the rupee, but it held when tapering began | The rupee recovered to ₹61.62/$ by Oct 2013 (US-IN-2 p. 113) |
| 2017 | ES 2016-17 (US-IN-3) | US visa curbs a threat to IT-BPM | By FY24 the US was India's top remittance source at 27.7% (US-IN-6 p. 174) |
| 2025 (Feb) | Joint Leaders' Statement (US-IN-8) | BTA first tranche by fall 2025; $500 bn trade by 2030 | 50% US tariff from Aug 2025 (US-OTH-6, US-IN-7); only a framework by Feb 2026; relations "unsettled" in Sept 2026 (`India_2026.md`) |
| 2026 (Jan) | ES 2025-26 (US-IN-6) | India expected to be an "early winner"; surprise at the 25% penalty | Penalty removed 7 Feb 2026; 18% deal rate overtaken by the court ruling; India at 10% (US-IN-7, US-OTH-8, US-OTH-9) |

Candidate quotes (all verified by script against the converted text, under 15 words):
- "house price stagnation was the most likely scenario" (IMF 2005 Art. IV, US-IMF-1 p. 10)
- "The United States has continued to be the main locomotive of global growth" (US-IMF-1 p. 29)
- "highly resilient, including to recent difficulties in the subprime mortgage market" (IMF 2007 Art. IV, US-IMF-2 p. 26)
- "A disorderly resolution of global imbalances remains a low probability—but high cost—risk" (US-IMF-2 p. 27)
- "first national-level housing bust in at least 40 years" (IMF 2008 Art. IV, US-IMF-3 p. 37)
- "levels not seen since the years immediately following the Second World War" (IMF 2010 Art. IV, US-IMF-4 p. 41)
- "The fiscal deficit reduction in 2013 is excessively rapid and ill designed." (IMF 2013 Art. IV, US-IMF-5 p. 28)
- "could trigger a sharper-than-expected sell-off of fixed-income assets" (US-IMF-5 p. 17)
- "growth has been too low and too unequal" (IMF 2017 Art. IV, US-IMF-6 PDF p. 6)
- "The U.S. public debt is on an unsustainable path." (IMF 2019 Art. IV, US-IMF-7 p. 39)
- "tariff measures are likely to be ineffective at containing bilateral trade deficits" (US-IMF-7 p. 39)
- "This will be a tricky task." (IMF 2022 Art. IV, US-IMF-8 p. 1)
- "the U.S. is expected to slow but to narrowly avoid a recession" (US-IMF-8 p. 2)
- "The U.S. economy has turned in a remarkable performance over the past few years." (IMF 2024 Art. IV, US-IMF-9 p. 1)
- "Hysteresis effects from the pandemic did not materialize" (US-IMF-9 p. 1)
- "their costs are largely borne by U.S. firms and consumers" (US-IMF-9 p. 2)
- "has set the U.S. economy apart from its peers" (IMF 2026 Art. IV, US-IMF-10 Key Issues p. 1)
- "there is little scope to lower the policy rate over the coming year" (US-IMF-10 Key Issues p. 1)
- "establish a target range for the federal funds rate of 0 to 1/4 percent" (FOMC, 16 Dec 2008, US-FED-1)
- "The Federal Reserve will employ all available tools" (FOMC, 16 Dec 2008, US-FED-1)
- "If the outlook for the labor market does not improve substantially" (FOMC, 13 Sep 2012, US-FED-3)
- "it is reasonably confident that inflation will rise" (FOMC, 16 Dec 2015, US-FED-4)
- "The fundamentals of the U.S. economy remain strong." (FOMC, 3 Mar 2020, US-FED-5)
- "in the amounts needed to support smooth market functioning" (FOMC, 23 Mar 2020, US-FED-5)
- "Today's policy action will support a timelier return to the Committee's 2 percent goal." (FOMC, 16 Sep 2026, US-FED-9)
- "The Committee will deliver price stability." (FOMC statements from 17 Jun 2026, US-FED-9)
- "continuing the retirement of the Federal debt" (ERP 2002, US-OTH-1 p. 43)
- "Tariffs have already catalyzed trade deals" (ERP 2026, US-OTH-2 p. 5)
- "our policies will decrease federal debt to 94 percent of GDP" (ERP 2026, US-OTH-2 p. 4)
- "shall start at 10 percent" (EO 14257, US-OTH-5)
- "IEEPA does not authorize the President to impose tariffs." (*Learning Resources v. Trump*, US-OTH-7, syllabus p. 230)
- "temporary import surcharge of 10 percent ad valorem" (Proclamation 11012, US-OTH-8)
- "an additional ad valorem rate of duty of 25 percent" (EO 14329 on India, US-IN-7)
- "India has committed to stop directly or indirectly importing Russian Federation oil" (EO 14384, US-IN-7)
- "aiming to more than double total bilateral trade to $500 billion by 2030" (Joint Leaders' Statement, 13 Feb 2025, US-IN-8)
- "will lower the Reciprocal Tariff on India from 25% to 18%" (White House fact sheet, 9 Feb 2026, US-IN-8)
- "The impact on Indian economy was less severe" (ES 2008-09, US-IN-1 p. 18)
- "the rupee became resilient when the US Fed taper actually happened subsequently" (ES 2013-14, US-IN-2 p. 113)
- "Misconstruing mobility of skilled people as an immigration issue is a deterrent" (ES 2016-17 Vol. 2, US-IN-3 p. 249)
- "the US was India’s second-largest trading partner in FY24 after China" (ES 2023-24, US-IN-5 p. 152)
- "India was expected to be one of the early winners" (ES 2025-26 Preface, US-IN-6 p. vii)
- "The US is the top contributor with 27.7 per cent" (ES 2025-26, US-IN-6 p. 174)

## Not obtained

- IMF listing of past US Article IV reports: the country page https://www.imf.org/en/Countries/USA (200) and its index.md/index.json (200)
  link only the 2026 report; "See All Documents" points to #whatsnew on the same page. Tried: https://www.imf.org/en/Countries/USA/Article-IV-Staff-Reports
  — 404; https://www.imf.org/en/Publications/Search?series=IMF+Staff+Country+Reports&country=United+States — 404;
  https://www.imf.org/en/publications/cr?country=United%20States — 404; https://www.imf.org/en/Publications/CR — 404;
  https://www.imf.org/external/pubs/cat/scr1_sp.cfm?s_year=2007&e_year=2007&brtype=default — 403;
  https://www.imf.org/external/pubs/cat/longres.cfm — 403; https://www.imf.org/en/about/executive-board/ebc-archive/country — 404;
  https://www.imf.org/sitemap.xml — 404; IMF eLibrary search https://www.elibrary.imf.org/search?q=United+States+Article+IV+Consultation... —
  403. Hence the GUESSED report URLs above. Not found by guessing: .../scr/2017/cr17239.pdf and .../scr/2019/cr19174.pdf (404); the 2018,
  2021 and 2023 reports were not attempted, and https://www.imf.org/-/media/files/publications/cr/2025/english/1usaea2025001.pdf (GUESSED) —
  404 (no 2025 US Article IV appears to exist; the 2026 page says the last Board consultation was 1 April 2026).
- IMF US Article IV concluding statements (mission-end statements): no listing found; not attempted by guessing. Staff reports used instead.
- CBO (*Budget and Economic Outlook*, latest and 2007–2010): https://www.cbo.gov/ — 403;
  https://www.cbo.gov/topics/budget/outlook-budget-and-economy — 403; https://www.cbo.gov/about/products/major-recurring-reports — 403. CBO
  figures appear only as cited in US-IMF-10 (tariff revenue about 1 percent of GDP).
- Federal Register full-text pages (e.g. https://www.federalregister.gov/documents/full_text/text/2025/04/07/2025-06063.txt) — 200 but a
  "Request Access" bot page; not pursued. The govinfo PDFs linked by the API were used instead.
- US Section 232 aluminium Proclamation 9704 (2018), the China Section 301 Federal Register notices, EO 14346 (5 Sept 2025, "aligned
  partners" annex) and the November 2025 US–China EO (document 2025-19826, listed by the API): not read.
- USTR: https://ustr.gov/issue-areas/enforcement/section-301-investigations/tariff-actions (200) downloaded but not re-read (2018 lists are in
  `IMF_2014-2019.md`). The USTR notice opening the 60-economy forced-labour investigations (91 FR 12884, 12 March 2026) not read.
- Court of International Trade and Federal Circuit rulings in *V.O.S. Selections* (2025): not attempted; known here only from the Supreme
  Court syllabus (149 F. 4th 1312).
- Indian official sources on the 2025–26 tariff episode and the February 2026 framework: https://www.commerce.gov.in/ — 200 but a 9 KB
  script shell; https://www.commerce.gov.in/press-releases/ (GUESSED) — 404; https://www.pib.gov.in/ and https://pib.gov.in/allRel.aspx —
  200 but no US trade items on the current listings; https://www.mea.gov.in/press-releases.htm and
  https://www.mea.gov.in/bilateral-documents.htm?dtl/ — 200 but no US items on the current pages. No Indian government text on the 18
  percent framework or the Section 301 rate was obtained; the Indian side is from the Economic Surveys and `India_2026.md` (MER).
- Economic Report of the President 2025 (downloaded, 200, not read); ERP opening chapters other than 2002 and 2026 not read.
- FOMC chair from June 2026: not established (statements no longer list voters by name); the FOMC calendar page and Board pages were not
  searched for it.
- Survey passages not used: ES 2008-09 quote on banks' "very limited exposure" and ES 2019-20 "largest export destination" sentence failed
  the quote check because of two-column text interleaving (paraphrased instead).
