# Reading notes: lens 'Sub-Saharan Africa' — part B (countries, India–Africa) (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL --max-time 120 -o file -w '%{http_code}' URL` (default user-agent, no custom
headers, no cookies), with a 3-second pause after every request; each request and its HTTP status is logged in the scratchpad file
`ssab_scripts/fetchlog_b.txt` (44 requests; no 429s). Listing pages used: the imf.org country pages https://www.imf.org/en/Countries/NGA,
/ETH, /KEN, /GHA, /ZMB, /AGO (all 200). As the earlier lens agents found, each links **only the latest Article IV issue page**; those six
issue pages (all 200) gave the PDF links for NG-IMF-3, ET-IMF-3, KE-IMF-1, GH-IMF-2, ZM-IMF-2 and AO-IMF-2. **Every earlier staff report comes
from a GUESSED URL** built on the IMF naming pattern: `/external/pubs/ft/scr/YYYY/crYYNNN.pdf` to 2016; `/-/media/files/publications/cr/
YYYY/crYYNNN.pdf` in 2018; `/-/media/files/publications/cr/YYYY/english/1<iso3>eaYYYYnnn.pdf` from 2019, where nnn is a per-country
sequence number (Ethiopia's 2024 ECF request is `1ethea2024001-print-pdf.pdf` = CR 24/253; Kenya's November 2024 reviews are
`1kenea2024003-print-pdf.pdf` = CR 24/316). Candidate report numbers came from citations in reports already in hand (CR 24/253 is cited in
CR 25/188, p. 3235 of the text) or were tried directly; for every file the title page and "IMF Country Report No." were read. All guessed
files that returned 200 turned out to be the documents wanted; 404s are under Not obtained. Downloads are in the session scratchpad folder
`lens_ssa_dl/b/` with subfolders `imf/` (country and issue pages), `imf/g/` (staff reports), `gov/` (MEA and Exim Bank) and `txt/`
(conversions). PDFs were converted with `pdftotext` (plain and `-layout`); HTML was stripped of scripts and tags; the Exim Bank spreadsheet
was read with openpyxl. Python that read downloads was run with `python3 -I` from scripts kept in `ssab_scripts/` at the scratchpad root.
Economic Survey texts were **not refetched**: they were read from the Econ Subject folder (`sources/text/es*.txt`, text page = PDF page =
"tp."), and the printed page was taken from the running header or footer. Quotes are verbatim, under 15 words, at most two per document,
and a script (`ssab_scripts/chkq.py`, whitespace-, quote- and dash-normalised) checked all 24 against the converted text: 24 matched (two
candidate Survey quotes failed because of two-column layout and were replaced by paraphrase). Everything else is paraphrase. Outturns come
from `data/clean/weo/NGDP_RPCH.json` and `PCPIPCH.json` (WEO October 2026 vintage; last actual year 2025 for NGA, KEN, GHA, ZMB, AGO and
2024 for ETH; PCPIPCH is the annual average). **Ethiopia's WEO years are fiscal years**: WEO "2015" = FY2014/15 (checked: CR 25/188 gives
8.1 percent growth for 2023/24, WEO 2024 = 8.05; CR 24/253 gives 7.2 for 2022/23, WEO 2023 = 7.17).

Printed-page offsets (staff-report body; press releases, Key Issues/Executive Summary pages and tables without a folio are cited as "PDF
p."; press-release tables carry their own small folio, given as "PR p."): CR 14/103 (NGA), CR 14/303 (ETH): printed = PDF − 1. CR 16/101
(NGA), CR 25/157 (NGA), CR 24/253 (ETH), CR 25/188 (ETH), CR 24/316 (KEN): −5. CR 24/13 (KEN), CR 24/30 (GHA): −7. CR 23/168 (GHA), CR 22/292
(ZMB), CR 25/62 (AGO): −4. CR 25/225 (ZMB): −6 (its DSA is numbered separately; DSA p. 1 = PDF p. 126). CR 18/370 (AGO): −3. A page
marked "(by offset)" has no folio of its own in the text (mostly tables). Economic Survey printed pages are given per item.

Item labels:
- NG-IMF-n, ET-IMF-n, KE-IMF-n, GH-IMF-n, ZM-IMF-n, AO-IMF-n: IMF staff reports (Article IV and programme documents) with their press
  releases.
- SA-IN-n: India–Africa links from the Economic Surveys (on disk; not refetched).
- IN-GOV-n: official Indian sources fetched by curl (Exim Bank of India).

Abbreviations: AIV = Article IV; CF = G20 Common Framework; CR = IMF Country Report; DDE(P) = Ghana's Domestic Debt Exchange (Programme);
DSA = debt sustainability analysis; ECF = Extended Credit Facility; EFF = Extended Fund Facility; eop = end of period; FX = foreign
exchange; HGER = Ethiopia's Homegrown Economic Reform agenda; KI = Key Issues page; LOC = line of credit; NBE = National Bank of Ethiopia;
OCC = Official Creditor Committee; PPG = public and publicly guaranteed; PR = press release; RSF = Resilience and Sustainability Facility;
SOE = state-owned enterprise; WEO = IMF World Economic Outlook.

---

## Nigeria

### NG-IMF-1. IMF, *Nigeria: 2013 Article IV Consultation—Staff Report; Press Release and Statement by the Executive Director for Nigeria*, IMF Country Report No. 14/103, April 2014 (staff report 6 February 2014; Board 21 February 2014)
PDF: https://www.imf.org/external/pubs/ft/scr/2014/cr14103.pdf (GUESSED; 200; 103 PDF pages; title page checked). Read: KI (PDF p. 2),
pp. 5, 7, Staff Appraisal (pp. 21–22), Table 2 (p. 24), Appendix II (p. 51), Statistical Issues annex (PDF p. 91).
- KI (PDF p. 2): strong non-oil growth, but poverty and inequality high and social indicators below the sub-Saharan average; vulnerabilities
  rising ahead of the 2015 elections and fiscal buffers reduced. "GDP is being rebased and structural shifts may suggest a refocus" of
  policy. Risks: lower oil revenue (global shifts, lower domestic output), pre-election fiscal loosening, insecurity in the North, the
  global recovery, and capital-flow reversal as US unconventional policy unwinds. Advice: curb oil theft (a sound Petroleum Industry Bill),
  rebuild buffers, keep monetary policy tight, let the naira adjust if pressures persist; power, agriculture and SME credit for inclusive
  growth.
- p. 5: oil theft and production losses drained the Excess Crude Account and Sovereign Wealth Fund from US$11 billion (end-2012) to US$3
  billion (end-2013); after the May 2013 Bernanke statement on unwinding unconventional policy outflows hit the naira and the CBN intervened, reserves falling from US$49 billion
  (mid-March) to US$43.6 billion (end-2013). p. 7: an alternative scenario with persistently lower oil prices leaves buffers severely
  depleted.
- Appendix II (p. 51): rebasing moves the base year from 1990 to 2010 and adopts the 2008 SNA; telecoms and other services have grown since
  1990; agriculture's labour share could fall from 70 to 30 percent; a larger GDP raises per-capita income, and "Nigeria could lose benefits
  afforded to low-income countries". PDF p. 91: the rebased series (base 2010) with technical assistance from the IMF, World Bank and AfDB.
- Table 2 (p. 24; 1990-base GDP): real GDP 6.6 (2012), 6.4 (2013), **7.3 (2014)**, 7.0 (2015); CPI average 8.5 (2013), **7.3 (2014)**; oil
  price assumed US$104 (2014) falling to US$88 (2018); oil and gas revenue 12.9% of GDP (2013) of total revenue 20.0%; fuel subsidies 1.6% of
  GDP (2013); FGN gross debt 19.1% of GDP (2013).
- Use: Nigeria on the eve of the 2014 rebasing and the oil-price collapse; the IMF's scenario of a persistent oil-price fall came true.

### NG-IMF-2. IMF, *Nigeria: 2016 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director for Nigeria*, IMF Country Report No. 16/101, April 2016 (staff report 17 March 2016; Board 30 March 2016)
PDF: https://www.imf.org/external/pubs/ft/scr/2016/cr16101.pdf (GUESSED; 200; 88 PDF pages). Read: PR No. 16/146 (PDF p. 2), PR table (PDF
p. 5, PR p. 4), KI (PDF p. 6), p. 5, Staff Appraisal (pp. 21–22), Box 2 (p. 26 by offset), p. 27, Statistical Issues (PDF p. 80).
- PR (PDF p. 2): non-oil sector 90% of GDP but oil central; lower oil prices were "decimating government revenues to just 7.8 percent of
  GDP" and doubled the general government deficit to about 3.7% of GDP in 2015; exports fell about 40%; reserves US$28.3 billion at
  end-2015; CBN exchange restrictions hurt firms; growth slowed from 6.3% (2014) to an estimated 2.7% (2015), forecast 2.3% in 2016;
  inflation 9.6% in January 2016, above the 6–9% target range.
- KI (PDF p. 6): unemployment 9.9%; poverty above 50% in the northern states; growth to stay well below historical averages; the mix of wide
  deficits, accommodative monetary policy and an overvalued exchange rate could widen the current-account deficit.
- p. 5: in February 2015 the CBN moved transactions to the interbank market, devaluing the official rate by about 18%, and has since tightly
  managed it. p. 21 (Staff Appraisal): a large and permanent terms-of-trade shock; oil prices expected lower for longer. p. 22: easing, an
  inflexible exchange rate and restrictions had not revived activity; "Staff does not support the policies that have given rise
  to the exchange restrictions" (and multiple currency practice); petroleum subsidies to be eliminated through independent price-setting.
- p. 27: non-oil tax revenue only about 4% of GDP in 2014 against about 15% for other commodity producers; VAT at 5% is among the lowest.
- Note: the revenue ratio is on the **rebased (2010) GDP**, hence far below the 20% of NG-IMF-1 (PDF p. 80 records the completed
  rebasing). PR table (PR p. 4): real GDP (2010 basic prices) 6.3 (2014), 2.7 (2015), **2.3 (2016)**, 3.5 (2017); CPI eop 12.0 (2016).
- Use: the oil-price fall, the de facto peg and FX rationing that led into the 2016 recession (WEO outturn −1.6%).

### NG-IMF-3. IMF, *Nigeria: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director for Nigeria*, IMF Country Report No. 25/157, July 2025 (staff report 29 May 2025; Board 13 June 2025; PR 25/231 dated 2 July 2025)
Issue page: https://www.imf.org/en/publications/cr/issues/2025/07/01/nigeria-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-568220
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1ngaea2025001-print-pdf.pdf (from issue
page; 200; 85 PDF pages). Latest Nigeria AIV on the country page. Read: PR (PDF pp. 2–3), PR table (PDF pp. 4–5, PR pp. 3–4), KI (PDF p.
6), Context (pp. 4–5), Annex IV (p. 42).
- PR (PDF p. 2): over two years the authorities removed costly fuel subsidies, stopped monetary financing of the deficit and improved the FX
  market; Eurobond access regained and portfolio inflows resumed; but poverty and food insecurity have risen. Growth 3.4% in 2024 and 3.4%
  forecast for 2025; inflation 23.7% y/y in April 2025 from a 31% average in 2024 on the **backcasted rebased CPI**.
- p. 4 (Context): reforms since 2023 include liberalising the FX market, "removing fuel subsidies, and ending monetary financing"; credit
  rating upgrade in April 2025; poverty estimated at **46% in 2024**, 31 million people food insecure. p. 5: bilateral ODA US$1.5 billion in
  2023 (0.4% of GDP), US$1 billion of it from the United States.
- KI (PDF p. 6): growth steady but too low per capita; "Gains have yet to benefit all Nigerians." Advice: neutral fiscal stance, recoup
  fuel-subsidy savings, scale up cash transfers; tight money and a positive real policy rate; let the exchange rate absorb shocks, FX
  intervention only against excess volatility; Basel III and bank recapitalisation; exit the FATF grey list (PR p. 2).
- Annex IV (p. 42): the Dangote refinery, Africa's largest, began production in January 2024; investment US$20 billion (5.5% of 2023 GDP);
  expected to add about 1½ points to 2025 growth (p. 10 by offset).
- PR table (PR pp. 3–4): real GDP 2.9 (2023), 3.4 (2024), **3.4 (2025)**, **3.2 (2026)**; CPI average 24.7, 31.4, **24.0**, **23.0**; CPI eop
  28.9, 15.4, 23.0, 18.0; GDP per capita US$1,597 (2023) → US$806 (2024) after the naira's fall; public gross debt 48.7 → 52.9% of GDP
  (2023–24); implicit fuel subsidy 2.1% of GDP (2024), 0.0 from 2025; gross reserves US$40.2 billion (2024).
- Use: the 2023 reforms (FX unification, subsidy removal) and its cost-of-living fallout; the halving of dollar GDP per head.

## Ethiopia

### ET-IMF-1. IMF, *The Federal Democratic Republic of Ethiopia: 2014 Article IV Consultation—Staff Report; Press Release; and Statement by the Executive Director*, IMF Country Report No. 14/303, October 2014 (staff report 5 September 2014; Board 24 September 2014)
PDF: https://www.imf.org/external/pubs/ft/scr/2014/cr14303.pdf (GUESSED; 200; 76 PDF pages). Read: KI (PDF p. 2), Box 1 (p. 4), pp. 6–7,
Staff Appraisal (p. 28), Table 2 (p. 30 by offset).
- KI (PDF p. 2): "Ethiopia's investment-led development strategy has delivered robust growth" and MDG progress; restrained fiscal and
  monetary policy at general-government level, but financing of large-scale investment **through public enterprises** risks stability.
  Advice: prioritise public investment, monitor SOE borrowing, more room for the private sector, reserves of at least three months of
  imports, greater interest-rate and exchange-rate flexibility.
- Box 1 (p. 4): the Growth and Transformation Plan 2010/11–2014/15 targets average growth of 11.2%, middle-income status by 2020–25, via
  scaled-up public investment (roads, railways, hydro dams, sugar factories, housing).
- p. 6: staff project growth of 8.0–8.5% in 2013/14 and 2014/15, **marked down from official figures** because of weak national accounts;
  the authorities expect 11.0–11.4%. p. 7: public-enterprise external borrowing (incl. for the Grand Renaissance Dam) about 3.3% of GDP;
  overall public-sector financing about 10% of GDP; PPG external debt up from 20.5% to about 23% of GDP; current-account deficit 7.1% of
  GDP (2013/14).
- p. 28: proactive policy implemented through public enterprises entails risks; "staff urges the authorities to curtail domestic
  borrowing by public enterprises".
- Table 2 (p. 30): growth (factor cost) 9.7 (2012/13), 8.2 (2013/14), **8.5 (2014/15)**; CPI average 13.5, 8.1, **8.2**; gross domestic
  investment 33.0% of GDP (2012/13) against domestic saving of 16.0%.
- Use: the state-led, investment-heavy model at its peak, and the IMF's doubts about the official growth data.

### ET-IMF-2. IMF, *The Federal Democratic Republic of Ethiopia: Request for an Arrangement Under the Extended Credit Facility—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 24/253, July 2024 (staff report 12 July 2024; Board 29 July 2024)
PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1ethea2024001-print-pdf.pdf (GUESSED; 200 after 404 on the plain and
`-source-pdf` variants; 144 PDF pages). Read: PR 24/291 (PDF pp. 2–4), PR table (PDF p. 5, PR p. 4), Executive Summary (PDF p. 6), pp. 5–7,
11, 14.
- PR (PDF p. 2): four-year ECF of SDR 2.556 billion (about US$3.4 billion, 850% of quota), US$1 billion at once; key policies: a
  **market-determined exchange rate**, modern monetary framework and no monetary financing, revenue mobilisation, debt restructuring, SOE
  repair. PDF p. 3: the Acting Chair welcomes recent measures moving to a market-determined rate and removing current-account restrictions, and
  notes the first use of the IMF's credible-official-creditor-process policy under the Common Framework. PR annex (PDF p. 4): "the public investment-led growth model
  has reached its limits".
- p. 5: reported growth averaged over 10% a year in 2004–19, life expectancy up about 10 years, infant mortality halved; growth was driven by
  public investment financed by external borrowing and by **exchange-rate distortions and financial repression**; CF treatment requested in
  February 2021, OCC standstill November 2023, Eurobond default December 2023; Tigray reconstruction cost estimated at US$20 billion.
- p. 7: parallel-market premium over 100%; "A US$33 million Eurobond coupon payment was missed on December 11, 2023, triggering default";
  reserves US$1.5 billion (end-March 2024), under one month of imports; real overvaluation estimated at 52% (2022/23).
- p. 14: the float itself was a **prior action** not yet announced when the staff report was written (12 July); directive to let dealers
  trade FX at freely negotiated rates and to scrap import rationing and the 50% queuing deposit. p. 11: inflation expected to peak at 30–35%
  in early 2025 and ease to about 16% by 2025/26.
- PR table (PR p. 4): growth 7.2 (2022/23), 6.1 (2023/24), **6.5 (2024/25)**, 7.1 (2025/26); inflation average 32.5, 26.9, **30.1**, 16.2;
  public debt 40.2 → 42.9% of GDP (2022/23 → 2024/25; jump from devaluation); reserves 0.5 → 1.2 months of imports.
- Use: default, float and the end of the state-led model in one document.

### ET-IMF-3. IMF, *The Federal Democratic Republic of Ethiopia: 2025 Article IV Consultation, Third Review Under the Extended Credit Facility Arrangement, and Financing Assurances Review—Press Release; Staff Report; Staff Supplement; and Statement by the Executive Director*, IMF Country Report No. 25/188, July 2025 (staff report 13 June 2025; Board 3 July 2025)
Issue page: https://www.imf.org/en/publications/cr/issues/2025/07/15/the-federal-democratic-republic-of-ethiopia-2025-article-iv-consultation-third-review-under-568611
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1ethea2025002-source-pdf.pdf (from issue
page; 200; 169 PDF pages). Read: PR 25/234 (PDF pp. 2–4), PR table (PDF p. 5, PR p. 4), pp. 8, 24, 32.
- PR (PDF pp. 2–3): third review, US$262.3 million, total disbursed about US$1.873 billion; all quantitative criteria met, reserves above
  target thanks to **gold exports**; the exchange-rate reform corrected misalignment and raised FX availability; Agreement in Principle with
  the OCC welcomed, MoU pending (PDF p. 4); talks with commercial creditors continue.
- p. 8: parallel premium fell below 5% in September 2024 and has hovered around 15% since March 2025; queuing and high fees persist; fuel
  prices raised three times in 2025 (diesel +30%, petrol +35%) to above cost recovery. "Inflation has been much lower than anticipated":
  14.4% y/y in April 2025; end-June 2024/25 forecast cut to 16% from 25%; pass-through lower than expected.
- p. 24: debt still unsustainable and in distress before restructuring. p. 32: the July 2024 FX reform produced large nominal and real
  depreciation, "correcting previous overvaluation".
- PR table (PR p. 4): growth 8.1 (2023/24 prel.), **7.2 (2024/25)**, **7.1 (2025/26)**; inflation average 26.6, **16.6**, **12.0**.
- Use: the first year after the float; compare ET-IMF-2's 30% inflation forecast for 2024/25 with the 16.6% now expected (outturn 16.0).

## Kenya

### KE-IMF-1. IMF, *Kenya: 2023 Article IV Consultation, Sixth Reviews Under the Extended Fund Facility and Extended Credit Facility Arrangements, Requests for Augmentations of Access, … and First Review Under the Resilience and Sustainability Facility Arrangement—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 24/13, January 2024 (staff report 22 December 2023; Board 17 January 2024)
Issue page: https://www.imf.org/en/publications/cr/issues/2024/01/17/kenya-2023-article-iv-consultation-sixth-reviews-under-the-extended-fund-facility-and-543889
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1kenea2024001.pdf (from issue page; 200; 233
PDF pages). Latest Kenya AIV on the country page. Read: PR 24/12 (PDF p. 3), PR table (PDF p. 7, PR p. 5), Executive Summary (PDF pp.
8–9), pp. 9, 16.
- PR (PDF p. 3): EFF/ECF (approved April 2021, extended to April 2025) augmented by SDR 707.27 million (about US$941 million); about US$624.5
  million disbursed at once; total EFF/ECF disbursements about US$2.6 billion; RSF review completed.
- Executive Summary (PDF p. 8): resilient economy amid "costly and uncertain international bond market access for frontier market
  economies"; growth 5.4% in H1 2023; tax shortfall of 1% of GDP in FY2022/23; reserves falling but adequate. PDF p. 9: urgent BoP need
  because the **US$2 billion Eurobond due June 2024** is unlikely to be rolled over at reasonable cost; policy rate raised 200 bp in December
  2023.
- p. 9: Kenya at **high risk of debt distress**; last Eurobond June 2021, a 2022 issue cancelled. p. 16: growth projected 5.1% (2023) and 5.0%
  (2024).
- PR table (PR p. 5): real GDP 4.8 (2022), 5.1 (2023), **5.0 (2024)**, 5.3 (2025); gross public debt 73.2% of GDP (2023), 73.3% (2024).
- No mention of M-Pesa or mobile money in this report or in the companion Selected Issues (CR 24/14, fetched and searched).

### KE-IMF-2. IMF, *Kenya: Seventh and Eighth Reviews Under the Extended Fund Facility and Extended Credit Facility Arrangements, Requests for Reduction of Access …, Augmentation of Access …, and Review Under the Resilience and Sustainability Facility Arrangement—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 24/316, November 2024 (staff report 18 October 2024)
PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1kenea2024003-print-pdf.pdf (GUESSED; 200 after 404 on the plain and
`-source-pdf` variants; 177 PDF pages). Read: PR table (PDF p. 5, PR p. 3), Executive Summary (PDF pp. 6–7), pp. 9–10, 22, 33.
- Executive Summary (PDF p. 6): protests from June 2024, with loss of life, were triggered by tax proposals in the 2024 Finance Bill meant
  to close a large FY2023/24 revenue gap; "The protests forced the President to withdraw the Bill", cut spending in a July supplementary
  budget and reshape the Cabinet in August. The June 2024 US$2 billion Eurobond was dealt with earlier in the year, strengthening the
  shilling and reserves. PDF p. 7: growth 5.6% in 2023, 4.8% y/y in H1 2024; tax shortfall close to 2% of GDP; policy rate cut 100 bp since
  August; programme performance weakened markedly.
- p. 9: public debt at a multi-decade high by end-2023; periodic protests against new taxes raise wider questions of governance and the
  accountability of spending and borrowing. p. 10: spreads up from post-issuance lows; ratings downgraded.
- p. 33: thanks to "Kenya's success in issuing a Eurobond in February to early buyback" much of the 2024 bond, plus TDB (US$506 million)
  and World Bank (US$1.2 billion) money, the exceptional BoP need disappeared; remaining EFF access cut by 40.3% of quota.
- p. 22 and PR table (PR p. 3): public debt **73.1% of GDP in 2023**, 67.0% (2024 est.); real GDP 5.6 (2023), 5.0 (2024), **5.0 (2025)**;
  inflation average 7.7 (2023), 5.0 (2024), **5.3 (2025)**; policy rate 12.5% (end-2023).
- Use: the 2024 tax protests and the Eurobond buyback, both described in an IMF document.

## Ghana

### GH-IMF-1. IMF, *Ghana: Request for an Arrangement Under the Extended Credit Facility—Press Release; Staff Report; and Statement by the Executive Director for Ghana*, IMF Country Report No. 23/168, May 2023 (Board 17 May 2023)
PDF: https://www.imf.org/-/media/files/publications/cr/2023/english/1ghaea2023001.pdf (GUESSED; 200; 126 PDF pages). Read: PR 23/151 (PDF p.
2), PR table (PDF p. 4, PR p. 3), pp. 4–6, Box 2 (p. 18).
- PR (PDF p. 2): 36-month ECF of SDR 2.242 billion (about US$3 billion, 304% of quota), US$600 million at once, built on the Post COVID-19
  Programme for Economic Growth; external shocks on top of fiscal and debt weaknesses meant loss of market access, monetary financing,
  falling reserves, cedi depreciation and rising inflation that "eventually triggered an acute crisis"; timely external restructuring
  essential.
- p. 4: market access lost in late 2021. p. 5: growth fell to 2.9% y/y in Q3 2022 (6.4% a year earlier); about 3.2% for 2022; central-bank
  reserves critically low; inflation reached **54% in December 2022**. p. 6: public debt **88.1% of GDP at end-2022** and unsustainable; the
  new e-levy underperformed.
- p. 18: DDE launched 5 December 2022 (all medium/long-term local-currency bonds; T-bills and, later, pension funds excluded) and settled 21
  February 2023: "85 percent of the face value of bonds held by investors" other than pension funds was exchanged (28% of all domestic
  debt); external commercial debt service suspended 19 December 2022; Common Framework treatment requested 12 December 2022.
- PR table (PR p. 3): GDP 5.4 (2021), 3.2 (2022), **1.5 (2023)**, **2.8 (2024)**; CPI average 31.9, **44.0 (2023)**, 22.2 (2024); CPI eop 54.1
  (2022); public debt 79.6 (2021), 88.1 (2022), 98.1 (2023 pre-restructuring).

### GH-IMF-2. IMF, *Ghana: 2023 Article IV Consultation, First Review Under the Arrangement Under the Extended Credit Facility, Request for Modification of Performance Criteria, and Financing Assurances Review—Press Release; Staff Report; Staff Supplement; and Statement by the Executive Director for Ghana*, IMF Country Report No. 24/30, January 2024 (staff report 18 December 2023; Board 19 January 2024)
Issue page: https://www.imf.org/en/publications/cr/issues/2024/01/25/ghana-2023-article-iv-consultation-first-review-under-the-extended-credit-facility-544137
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1ghaea2024001.pdf (from issue page; 200;
155 PDF pages). Latest Ghana AIV on the country page. Read: PR 24/17 (PDF pp. 3–4), PR table (PDF p. 7, PR p. 5), p. 5.
- PR (PDF p. 3): first review completed, US$600 million, total about US$1.2 billion; all quantitative criteria met; "signs of economic
  stabilization are emerging"; Ghana's history of boom and bust traced to overly accommodative fiscal policy; primary deficit to fall by
  about 4 points of GDP in 2023.
- PR (PDF p. 4): domestic restructuring completed over the summer; **on 12 January 2024 Ghana reached agreement with the OCC under the
  Common Framework**, which gave the financing assurances for the review.
- p. 5: inflation down from 54.1% (December 2022) to about 26% (November 2023).
- PR table (PR p. 5): GDP 3.1 (2022), 2.3 (2023), **2.8 (2024)**, 4.4 (2025); CPI average 31.9, 40.2, **22.3 (2024)**; CPI eop 27.6 (2023);
  public debt 93.3 (2022), 86.1 (2023), 83.6 (2024).
- Use: the restructuring sequence (domestic first, official CF next, bondholders later — the 2024 bond deal is in `Theme_debt.md` DF-WB-2).

## Zambia

### ZM-IMF-1. IMF, *Zambia: Request for an Arrangement Under the Extended Credit Facility—Press Release; Staff Report; Staff Supplement; Staff Statement; and Statement by the Executive Director for Zambia*, IMF Country Report No. 22/292, September 2022 (staff report 9 August 2022; Board 31 August 2022)
PDF: https://www.imf.org/-/media/files/publications/cr/2022/english/1zmbea2022001.pdf (GUESSED; 200; 135 PDF pages). Read: PR 22/297 (PDF p.
2), pp. 4, 8–9, 14, Table 1 (p. 32 by offset).
- PR (PDF p. 2): 38-month ECF of SDR 978.2 million (about US$1.3 billion, 100% of quota), US$185 million at once; legacy of mismanagement and
  an inefficient public investment drive; poverty, inequality and malnutrition among the highest in the world; in debt distress, needing a
  deep debt treatment; Managing Director: end regressive fuel subsidies.
- p. 4: "Years of fiscal profligacy led to Zambia accumulating large fiscal and external imbalances"; copper slump 2015–16, 2019 drought,
  COVID; usable reserves about US$970 million by end-October 2020 against about US$1.4 billion of 2021 FX debt service; **Eurobond default
  November 2020**; President Hichilema's landslide in August 2021, explicit fuel subsidies removed.
- p. 8: external PPG debt more than quadrupled in 2014–19; arrears US$2.4 billion by end-March 2022; external PPG debt US$20 billion (78% of
  GDP) and total PPG debt **US$33.8 billion (133% of GDP)** at end-2021. p. 9 (chart): Eurobonds 17% and non-Paris Club bilateral 18% of
  external PPG debt.
- p. 14: CF treatment requested January 2021; bondholder committee from mid-2020; OCC formed June 2022.
- Table 1 (p. 32): GDP −2.8 (2020), 3.6 (2021), **3.0 (2022)**, **3.9 (2023)**; CPI average 15.7, 22.0, 13.0, **9.5**; kwacha depreciated 42.3%
  in 2020.

### ZM-IMF-2. IMF, *Zambia: 2025 Article IV Consultation, Fifth Review Under the Extended Credit Facility Arrangement, and Financing Assurances Review—Press Release; Staff Report; and Statement by the Executive Director for Zambia*, IMF Country Report No. 25/225, August 2025 (staff report 2 July 2025; Board 25 July 2025)
Issue page: https://www.imf.org/en/publications/cr/issues/2025/08/05/zambia-2025-article-iv-consultation-fifth-review-under-the-extended-credit-facility-569341
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1zmbea2025001-source-pdf.pdf (from issue
page; 200; 161 PDF pages). Read: PR 25/268 (PDF pp. 2–3), PR table (PDF p. 5, PR p. 4), p. 5, p. 23, DSA p. 1 (PDF p. 126).
- PR (PDF p. 3): fifth review, about US$184 million (total about US$1.55 billion); growth about 4% in 2024 despite a historic drought
  (hydropower shortfalls, power prioritised to mines and large firms), **5.8% forecast for 2025**; debt now **assessed as sustainable but at
  high risk of distress**; agreements in principle with most commercial creditors.
- p. 5: growth averaged 5% in 2022–24; inflation averaged 12% in 2022–24; elections due August 2026.
- p. 23: bilateral agreements under the MoU with the OCC under way; "agreements cover about 94 percent of Zambia's external debt within the
  restructuring perimeter". DSA p. 1: the framework includes the OCC treatment, the **completed Eurobond exchange** (haircut) and AIPs with
  some other commercial creditors.
- PR table (PR p. 4): GDP 5.2 (2022), 5.4 (2023), 4.0 (2024), **5.8 (2025)**, 6.4 (2026); inflation average 10.9 (2023), 15.0 (2024), **14.2
  (2025)**; public debt 133.4% (2023) → 91.9% (2025) → 69.4% (2027); poverty rate 64.3% (2022); main export market China.
- Use: the Common Framework's test case, from 2020 default to the 2024–25 deals.

## Angola

### AO-IMF-1. IMF, *Angola: Request for an Extended Arrangement Under the Extended Fund Facility—Press Release; Staff Report; and Statement by the Executive Director for Angola*, IMF Country Report No. 18/370, December 2018 (staff report 20 November 2018; Board 7 December 2018)
PDF: https://www.imf.org/-/media/files/publications/cr/2018/cr18370.pdf (GUESSED; 200; 97 PDF pages). Read: PR No. 18/463 (PDF p. 2), KI
(PDF p. 4), pp. 4–5, 11, Table 1 (p. 24 by offset).
- PR (PDF p. 2): three-year EFF of SDR 2.673 billion (about US$3.7 billion, 361% of quota), US$990.7 million at once: fiscal consolidation,
  exchange-rate flexibility, lower inflation, bank repair, AML/CFT, governance.
- KI (PDF p. 4): bring debt close to the 65% of GDP target; end FX distortions and multiple currency practices; restructure the state oil
  company (Sonangol) and the largest state bank; risks led by a sharp fall in oil prices.
- p. 4: government in office since September 2017; "The political transition represents an extraordinary break in Angola's recent history";
  Angola third-largest economy in SSA; third straight year of contraction in 2018 as oil output falls after underinvestment.
- p. 11: "After abandoning the peg to the U.S. dollar in January" 2018 the kwanza fell 45% by end-October; ban on new oil-collateralised debt
  (PDF p. 14 text).
- Table 1 (p. 24): GDP −2.6 (2016), −0.2 (2017), **−1.7 (2018)**, **2.5 (2019)**; CPI average 30.7 (2016), 20.7 (2018), **22.8 (2019)**; oil and
  gas exports 39.2% of GDP of 40.4% total (2018); oil revenue 14.2% of 20.5% total revenue; public debt 39.8% (2014) → **91.0% (2018)**; oil
  output 1.617 mb/d (2018).

### AO-IMF-2. IMF, *Angola: 2024 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director for Angola*, IMF Country Report No. 25/62, March 2025 (staff report 6 February 2025; Board 20 February 2025)
Issue page: https://www.imf.org/en/publications/cr/issues/2025/03/05/angola-2024-article-iv-consultation-press-release-staff-report-and-statement-by-the-562971
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1agoea2025001-print-pdf.pdf (from issue
page; 200; 79 PDF pages). Latest Angola AIV on the country page. Read: PR 25/41 (PDF p. 2), p. 4, p. 12, Table 1 (p. 30).
- PR (PDF p. 2): growth about 3.8% in 2024 as oil rebounded; debt ratio fell; buffers from the 2018–21 EFF eroded by capital-spending
  overruns and slow fuel-subsidy reform; kwanza down over 10% in 2024; growth 3% expected in 2025; elections 2027; upside from the Lobito
  Corridor.
- p. 4: 44% depreciation in June 2023. Oil is **95% of exports, over 60% of fiscal revenue** and, with linkages, more than three-quarters of
  activity; "Oil dependence remains a drag on medium-term growth."
- p. 12: relaxation of the China escrow account frees about US$150–200 million a month; footnote: up to US$2 billion withdrawn from the
  escrow account in 2024 to **prepay debt to China**; a US$1 billion total-return swap collateralised with a Eurobond.
- Table 1 (p. 30): GDP −4.0 (2020), 1.0 (2023), 3.8 (2024), **3.0 (2025)**, 3.2 (2026); CPI average 13.6 (2023), 28.2 (2024), **21.0
  (2025)**; public debt 119.1% (2020) → 62.4% (2024); oil output 1.388 mb/d (2020) → 1.262 (2024).
- Use: oil dependence, China-backed debt and the post-programme slippage.

---

## India–Africa links

### SA-IN-1. *Economic Survey 2002-03*, Ch. 6 (External Sector), Box 6.1 "Export import (EXIM) policy 2002-07", tp. 120 (no printed folio in the text)
- The EXIM Policy 2002–07 introduced a "Focus Africa" programme, with Focus CIS to follow, to diversify markets.

### SA-IN-2. *Economic Survey 2003-04*, Ch. 6 (External Sector), para 6.34, p. 114 (tp. 198)
- Market diversification sustained export growth; Focus Africa was extended to the remaining 11 countries of the region and Focus CIS
  launched from 1 April 2003.

### SA-IN-3. *Economic Survey 2004-05*, Ch. 7 "Industry", para on pharmaceuticals, p. 151 (tp. 148)
- India's reputation as a low-cost producer of antiretroviral drugs, supplied to international organisations and "to the needy patients in
  Africa", is well known (same passage repeated in ES 2005-06, tp. 148).

### SA-IN-4. *Economic Survey 2006-07*, Ch. 6 (External Sector), p. 121 (tp. 122); see also p. 120 (tp. 121)
- April–October 2006: imports from Africa grew very fast because of five-digit growth in imports from **Nigeria (mainly crude oil)**, whose
  share of India's imports rose to 4.4%; exports to Africa also grew strongly (p. 120).

### SA-IN-5. *Economic Survey 2007-08*, Ch. 6 (External Sector), para 6.103 and adjacent text, p. 144 (tp. 145)
- April–September 2007: exports to Africa grew 33.9%, against 16.5% to Asia, 23.2% to Europe and 5% to the United States; the share of
  trade with Iran and Nigeria rose with mineral-fuel imports.

### SA-IN-6. *Economic Survey 2011-12*, Ch. 7 "International Trade", p. 163 (Table 7.10) and Box 7.3 p. 169
- p. 163: Nigeria was India's 14th-largest trading partner (2.39% of trade in 2011-12 H1); India runs a large deficit with oil exporters
  Saudi Arabia, Iran and Nigeria; imports from Nigeria grew more than 60% in April–September 2011 on crude (p. 164).
- p. 169: a Special Focus Market Scheme for 41 countries, **22 of them African**, adds 1% duty credit (4% in all) on exports to them.

### SA-IN-7. *Economic Survey 2013-14*, Ch. 7 "International Trade", Box 7.4 p. 133 and Box 7.3 p. 130
- p. 133: India's Duty Free Tariff Preference scheme for LDCs (announced 2008) gave duty-free access on about 85% of tariff lines; the
  expanded scheme from 1 April 2014 covers 96.4% duty-free plus 2% preferential, with only 1.6% excluded; 31 of 48 LDCs benefit, **21 of them
  in Africa**.
- p. 130: the Incremental Exports Incentivisation Scheme was extended in 2013-14 with 53 Latin American and African countries added.

### SA-IN-8. *Economic Survey 2014-15*, Vol. 2, Ch. 4 (External Sector), paras 4.15–4.16, p. 54 (tp. 204)
- Africa's share of India's exports rose from 6.7% (2004-05) to **9.9% (2013-14)**, Asia's from 47.9% to 49.4%, while Europe and America fell;
  in April–December 2014 exports to Africa grew 12.9% against 0.2% to Europe.

### SA-IN-9. *Economic Survey 2015-16*, Vol. 1, Ch. 5 "Mother and Child", para 5.20, p. 91
- Comparison: 61% of rural Indians defecated in the open in 2015 (WHO/UNICEF JMP) against 32% of rural people in sub-Saharan Africa; Kenya
  15%, Afghanistan 17%.

### SA-IN-10. *Economic Survey 2016-17*, Vol. 2, Ch. 6 (External Sector), paras 6.19–6.20, p. 149 (tp. 500)
- In 2016-17 India's exports to Africa fell (negative growth) while exports to Asia, Europe and America rose; Africa supplied 7.5% of
  India's imports.

### SA-IN-11. *Economic Survey 2020-21*, Vol. 1, Ch. 5 (health), para 5.14, p. 156 (tp. 173)
- On healthcare access and quality India ranked 145th of 180 (Global Burden of Disease 2016); only a few sub-Saharan countries, some Pacific
  islands, Nepal and Pakistan ranked lower.

### SA-IN-12. *Economic Survey 2021-22*, Ch. 1 "State of the Economy", Table 8, p. 39 (tp. 65)
- WEO January 2022 table: sub-Saharan Africa −1.7 (2020), 4.0 (2021), 3.7 (2022), 4.0 (2023); Nigeria −1.8, 3.0, 2.7, 2.7; India (fiscal
  year) −7.3, 9.0, 9.0, 7.1.

### SA-IN-13. *Economic Survey 2022-23*, Ch. (external sector, trade agreements), p. 324 (tp. 367); *Economic Survey 2023-24*, Ch. "External Sector", para 4.31, pp. 126–127 (tp. 173–174)
- 2022-23 p. 324: AfCFTA (signed 21 March 2018) listed among major regional trade agreements.
- 2023-24 p. 126: India signed four FTAs in 2021–24, the first with **Mauritius (February 2021)**; p. 127: the new FTAs aim at access to
  Western and **African markets** and complementary partners.

### SA-IN-14. *Economic Survey 2025-26*, Ch. 4 "External Sector", Table IV.1 p. 162 and para 4.42 p. 163 (tp. 213–214)
- p. 162 (exports April–November FY26, y/y growth): with US tariffs at 50%, pharmaceutical exports were redirected; drug formulations and
  biologicals to Nigeria +58.0% and Tanzania +50.6%; surgicals to Nigeria +154.6%; books and printing to Kenya +280.7%, Ethiopia +340.5%,
  Malawi +450.0%; cotton fabrics to Nigeria +72%, Uganda +221.5%.
- p. 163: Nigeria's share of India's crude imports rose to 3.3% from 2.2% (April–November 2025).

Not found in the Surveys (searched all `es*.txt`): the India–Africa Forum Summits, the African Union's G20 membership (2023), Exim Bank
lines of credit to Africa, India–Africa trade totals in a single figure, and remittances from or diaspora in Africa.

### IN-GOV-1. Export-Import Bank of India, "Lines of Credit" web page and "GOI LOC Statistics" spreadsheet (updated as of 31 October 2026), accessed 23 Nov 2026
Page: https://www.eximbankindia.in/lines-of-credit (200; HTML). Spreadsheet:
https://www.eximbankindia.in/sites/default/files/2026-11/GOILOC%20Statistics_31.10.2026.xlsx (linked from the page; 200; sheet
"SignedLOCStatisticsReport", "Exim Bank's list of signed LOCs", amounts in US$ million).
- Page: Government of India-supported LOCs go back to the Indian Development Initiative of 2003-04, now the Indian Development and Economic
  Assistance Scheme (IDEAS); the MEA's Development Partnership Administration runs them through Exim Bank; at least 75% of contract value
  must be sourced from India (10% relaxation possible).
- Spreadsheet (own arithmetic over the rows with US$ amounts; seven rows in EUR or INR left out): 295 signed LOCs worth about US$25.5
  billion; region "Africa" (includes North Africa and island states) **201 LOCs, about US$9.8 billion**, against Asia 57 LOCs, about US$14.9
  billion (Bangladesh alone US$7.9 billion). Six lens countries: Ethiopia 12 LOCs (US$712 million), Ghana 9 (US$227 million), Kenya 4 (US$207
  million), Zambia 5 (US$110 million), Nigeria 1 (US$100 million), Angola 3 (US$85 million; the first, US$40 million for railway
  rehabilitation, signed 11 August 2004). Several recent African rows are restructurings (e.g. Cameroon 2023, "G20 DSSI Deferment of dues").

---

## Forecast vs outturn pairs (own arithmetic; outturns from WEO October 2026, `NGDP_RPCH.json` / `PCPIPCH.json`; gap = outturn − forecast;
2025 values are estimates for Ethiopia and partly estimates elsewhere; 2026 values are WEO projections; WEO inflation is the annual average)

| Country | Report (date) | Forecast | Outturn (WEO Oct 2026) | Gap |
|---|---|---|---|---|
| Nigeria | CR 14/103 (Feb 2014), Table 2 p. 24 | growth 7.3 (2014), 7.0 (2015); CPI avg 7.3 (2014) | 6.3; 2.7; 8.0 | −1.0 (base change: forecast on 1990 base); −4.3; +0.7 |
| Nigeria | CR 16/101 (Mar 2016), PR table PR p. 4 | growth 2.3 (2016), 3.5 (2017); CPI eop 12.0 (2016) | −1.6; 0.8; 15.7 (avg) | **−3.9**; −2.7; n/c |
| Nigeria | CR 25/157 (May 2025), PR table PR p. 3 | growth 3.4 (2025), 3.2 (2026); CPI avg 24.0 (2025), 23.0 (2026) | 4.0; 4.2 (proj.); 23.0; 15.6 (proj.) | +0.6; +1.0; −1.0; −7.4 |
| Ethiopia | CR 14/303 (Sep 2014), Table 2 p. 30 | growth 8.5 (2014/15); CPI avg 8.2 | 10.4 (official data); 7.7 | +1.9; −0.5 |
| Ethiopia | CR 24/253 (Jul 2024), PR table PR p. 4 | growth 6.5 (2024/25); inflation avg 30.1 (2024/25) | 9.2 (est.); 16.0 (est.) | +2.7; **−14.1** |
| Ethiopia | CR 25/188 (Jun 2025), PR table PR p. 4 | growth 7.2 (2024/25), 7.1 (2025/26); inflation avg 16.6, 12.0 | 9.2 (est.), 9.2 (proj.); 16.0, 11.7 (proj.) | +2.0, +2.1; −0.6, −0.3 |
| Kenya | CR 24/13 (Dec 2023), PR table PR p. 5 | growth 5.0 (2024) | 4.7 | −0.3 |
| Kenya | CR 24/316 (Oct 2024), PR table PR p. 3 | growth 5.0 (2025); inflation avg 5.3 (2025) | 4.6; 4.1 | −0.4; −1.2 |
| Ghana | CR 23/168 (May 2023), PR table PR p. 3 | growth 1.5 (2023), 2.8 (2024); CPI avg 44.0 (2023), 22.2 (2024) | 3.1; 5.8; 39.2; 22.9 | +1.6; **+3.0**; −4.8; +0.7 |
| Ghana | CR 24/30 (Dec 2023), PR table PR p. 5 | growth 2.8 (2024); CPI avg 22.3 (2024) | 5.8; 22.9 | +3.0; +0.6 |
| Zambia | CR 22/292 (Aug 2022), Table 1 p. 32 | growth 3.0 (2022), 3.9 (2023); CPI avg 9.5 (2023) | 5.2; 5.4; 10.9 | +2.2; +1.5; +1.4 |
| Zambia | CR 25/225 (Jul 2025), PR table PR p. 4 | growth 5.8 (2025); inflation avg 14.2 (2025) | 3.8; 13.9 | **−2.0**; −0.3 |
| Angola | CR 18/370 (Nov 2018), Table 1 p. 24 | growth −1.7 (2018), 2.5 (2019); CPI avg 22.8 (2019) | −0.6; −0.2; 17.1 | +1.1; −2.7; −5.7 |
| Angola | CR 25/62 (Feb 2025), Table 1 p. 30 | growth 3.0 (2025); CPI avg 21.0 (2025) | 3.1; 20.2 | +0.1; −0.8 |

n/c = not comparable (end-period forecast against an annual average). Notes: Nigeria's 2014 forecast was on the 1990 base, the outturn on
the rebased series; the WEO's Ethiopian growth figures follow official data, which the IMF marked down in 2014 (ET-IMF-1 p. 6), so the
positive Ethiopian gaps partly measure that statistical dispute. Strongest boxes: Ethiopia's post-float inflation (forecast 30.1, outturn
16.0); Nigeria 2016 (forecast +2.3, outturn −1.6); Ghana's recovery (2024 forecast 2.8, outturn 5.8).

---

## Already in the book (cite; not refetched)
- `Theme_debt.md` DF-WB-2 (World Bank International Debt Report 2026), pp. 44–45: Common Framework MoUs for Ghana (December 2023) and Zambia
  (June 2024), bondholder deals in 2024, MoU also signed with Ethiopia; summary paragraph (line ~517) on Ghana and Zambia finishing
  restructurings (DF-WB-2 pp. 22, 26, 44–45). DF-WB-3 (DSSI brief) points to the same pages.
- `Theme_demography.md` DL-WB-3 (WDR 2023 Overview) p. 2: Nigeria projected to grow from 213 million to 791 million and become the second
  most populous country after India by 2100. DL-OTH-1 (WPP 2024) PDF p. 9: Angola among nine countries whose population is likely to double
  in 2024–54. DL-WB-5 (Global Jobs Challenge 2026) p. 1: over 330 million young people in Sub-Saharan Africa in 2035.
- `Theme_development.md` DV-WB-3 (June 2025 poverty update) p. 4: SSA poverty at $3.00 46.2 → 44.4 percent (2020–25); Nigeria's last survey
  is from 2018. DV-WB-10 (WDR 2018) PDF 15: three-quarters of grade 3 pupils in Kenya, Tanzania and Uganda could not read a simple sentence.
  DV-WB-12 (WDR 2026) Overview: Ghana's Rori AI tutor.
- `Theme_growth.md` GR-IMF-1 (WEO April 2003 Ch. III) p. 95: incomes from about $100 a year (Ethiopia); pp. 106 ff.: SSA gains from better
  institutions.
- `Theme_trade.md` TR-WB-1 (WDR 2020) p. 3: Ethiopian GVC firms more than twice as productive.
- `Theme_technology.md` TE-WB-3 (WDR 2026) p. 15: AI chatbot use by small firms in Kenya and Nigeria among others.
- `Theme_energy.md` EN-IN-8 (ES 2025-26) PDF 214: Nigeria's share of India's crude imports up (same passage as SA-IN-14).
- `Lens_em_b.md` EM-X-5 (BRICS declarations): Ethiopia invited to join BRICS from 1 January 2024; Nigeria among the 2025 partner countries.
- `IMF_2003-2006.md` (WEO Ch. 1 p. 17; Foreword p. xi) and `IMF_2022-2023.md` (WEO Ch. 1 p. 7: food about 40% of the SSA consumption
  basket); `IMF_2026.md` (food insecurity risk in SSA).
- India_* and Lens_india files: no Africa-specific item found by grep ("Africa", "African Union", the six country names).

---

## Not obtained
- IMF guessed URLs, 404: https://www.imf.org/-/media/files/publications/cr/2024/english/1ethea2024001.pdf and `…1ethea2024001-source-pdf.pdf`
  (the `-print-pdf` file worked); `…/2024/english/1ethea2024002.pdf`; `…/2024/english/1zmbea2024001.pdf` (a 2024 Zambia review was not
  needed); `…/2024/english/1kenea2024002-print-pdf.pdf` and `-source-pdf.pdf` (the plain file is CR 24/14, Selected Issues);
  `…/2024/english/1kenea2024003.pdf` and `-source-pdf.pdf` (the `-print-pdf` file worked).
- Fetched and title-checked but not read in depth: Ethiopia CR 15/300 (2015 AIV, https://www.imf.org/external/pubs/ft/scr/2015/cr15300.pdf,
  GUESSED, 200) and CR 16/322 (2016 AIV, https://www.imf.org/external/pubs/ft/scr/2016/cr16322.pdf, GUESSED, 200); Kenya CR 24/14 (Selected
  Issues, searched only).
- **M-Pesa / mobile money:** not mentioned in any Kenya document obtained (CR 24/13, 24/14, 24/316); no earlier Kenya Article IV was tried.
- **G20 New Delhi Leaders' Declaration (African Union admission):** https://www.mea.gov.in/Images/CPV/G20-New-Delhi-Leaders-Declaration.pdf
  (GUESSED) — HTTP 200 but an MEA "404 | Page Not Found" page (16,981 bytes); https://www.mea.gov.in/bilateral-documents.htm?dtl/37084/G20_New_Delhi_Leaders_Declaration
  (GUESSED) — 200, title "G20 New Delhi Leaders' Declaration", but the body is not in the static HTML (script-rendered), so no text could be
  read; https://www.g20.org/content/dam/gtwenty/gtwenty_new/document/G20-New-Delhi-Leaders-Declaration.pdf (GUESSED) — **403**. Not
  retried. The AU's G20 membership is therefore **not sourced** in these notes.
- **India–Africa Forum Summit:** https://www.mea.gov.in/india-africa-forum-summit.htm (GUESSED) — HTTP 200 but the same MEA "Page Not
  Found" page. Not obtained.
- PIB press releases: not attempted (no known release IDs; PIB search is a form).
- Ghana's 2024 Eurobond exchange and Zambia's bond exchange terms: not read in an IMF document here (Zambia's completed exchange is only
  mentioned, DSA p. 1); see `Theme_debt.md` DF-WB-2.

---

## Bibliography rows

| Key | Title | Publisher | Year | Edition / report no. | URL |
|---|---|---|---|---|---|
| imf-nga-2014 | Nigeria: 2013 Article IV Consultation | IMF | 2014 | CR 14/103 | https://www.imf.org/external/pubs/ft/scr/2014/cr14103.pdf |
| imf-nga-2016 | Nigeria: 2016 Article IV Consultation | IMF | 2016 | CR 16/101 | https://www.imf.org/external/pubs/ft/scr/2016/cr16101.pdf |
| imf-nga-2025 | Nigeria: 2025 Article IV Consultation | IMF | 2025 | CR 25/157 | https://www.imf.org/-/media/files/publications/cr/2025/english/1ngaea2025001-print-pdf.pdf |
| imf-eth-2014 | The Federal Democratic Republic of Ethiopia: 2014 Article IV Consultation | IMF | 2014 | CR 14/303 | https://www.imf.org/external/pubs/ft/scr/2014/cr14303.pdf |
| imf-eth-2024 | Ethiopia: Request for an Arrangement Under the Extended Credit Facility | IMF | 2024 | CR 24/253 | https://www.imf.org/-/media/files/publications/cr/2024/english/1ethea2024001-print-pdf.pdf |
| imf-eth-2025 | Ethiopia: 2025 Article IV Consultation, Third Review Under the ECF | IMF | 2025 | CR 25/188 | https://www.imf.org/-/media/files/publications/cr/2025/english/1ethea2025002-source-pdf.pdf |
| imf-ken-2024a | Kenya: 2023 Article IV Consultation, Sixth Reviews Under the EFF and ECF | IMF | 2024 | CR 24/13 | https://www.imf.org/-/media/files/publications/cr/2024/english/1kenea2024001.pdf |
| imf-ken-2024b | Kenya: Seventh and Eighth Reviews Under the EFF and ECF | IMF | 2024 | CR 24/316 | https://www.imf.org/-/media/files/publications/cr/2024/english/1kenea2024003-print-pdf.pdf |
| imf-gha-2023 | Ghana: Request for an Arrangement Under the Extended Credit Facility | IMF | 2023 | CR 23/168 | https://www.imf.org/-/media/files/publications/cr/2023/english/1ghaea2023001.pdf |
| imf-gha-2024 | Ghana: 2023 Article IV Consultation, First Review Under the ECF | IMF | 2024 | CR 24/30 | https://www.imf.org/-/media/files/publications/cr/2024/english/1ghaea2024001.pdf |
| imf-zmb-2022 | Zambia: Request for an Arrangement Under the Extended Credit Facility | IMF | 2022 | CR 22/292 | https://www.imf.org/-/media/files/publications/cr/2022/english/1zmbea2022001.pdf |
| imf-zmb-2025 | Zambia: 2025 Article IV Consultation, Fifth Review Under the ECF | IMF | 2025 | CR 25/225 | https://www.imf.org/-/media/files/publications/cr/2025/english/1zmbea2025001-source-pdf.pdf |
| imf-ago-2018 | Angola: Request for an Extended Arrangement Under the Extended Fund Facility | IMF | 2018 | CR 18/370 | https://www.imf.org/-/media/files/publications/cr/2018/cr18370.pdf |
| imf-ago-2025 | Angola: 2024 Article IV Consultation | IMF | 2025 | CR 25/62 | https://www.imf.org/-/media/files/publications/cr/2025/english/1agoea2025001-print-pdf.pdf |
| exim-loc-2026 | Lines of Credit; GOI LOC Statistics (as of 31 Oct 2026) | Export-Import Bank of India | 2026 | web page and spreadsheet | https://www.eximbankindia.in/lines-of-credit |
| es-2002-03 | Economic Survey 2002-03 | Ministry of Finance, India | 2003 | Ch. 6, Box 6.1 | on disk (es2002-03.txt) |
| es-2003-04 | Economic Survey 2003-04 | Ministry of Finance, India | 2004 | Ch. 6 | on disk (es2003-04.txt) |
| es-2004-05 | Economic Survey 2004-05 | Ministry of Finance, India | 2005 | Ch. 7 | on disk (es2004-05.txt) |
| es-2006-07 | Economic Survey 2006-07 | Ministry of Finance, India | 2007 | Ch. 6 | on disk (es2006-07.txt) |
| es-2007-08 | Economic Survey 2007-08 | Ministry of Finance, India | 2008 | Ch. 7 | on disk (es2007-08.txt) |
| es-2011-12 | Economic Survey 2011-12 | Ministry of Finance, India | 2012 | Ch. 7 | on disk (es2011-12.txt) |
| es-2013-14 | Economic Survey 2013-14 | Ministry of Finance, India | 2014 | Ch. 7, Boxes 7.3–7.4 | on disk (es2013-14.txt) |
| es-2014-15 | Economic Survey 2014-15 | Ministry of Finance, India | 2015 | Vol. 2 Ch. 4 | on disk (es2014-15.txt) |
| es-2015-16 | Economic Survey 2015-16 | Ministry of Finance, India | 2016 | Vol. 1 Ch. 5 | on disk (es2015-16.txt) |
| es-2016-17 | Economic Survey 2016-17 | Ministry of Finance, India | 2017 | Vol. 2 Ch. 6 | on disk (es2016-17.txt) |
| es-2020-21 | Economic Survey 2020-21 | Ministry of Finance, India | 2021 | Vol. 1 Ch. 5 | on disk (es2020-21.txt) |
| es-2021-22 | Economic Survey 2021-22 | Ministry of Finance, India | 2022 | Ch. 1, Table 8 | on disk (es2021-22.txt) |
| es-2022-23 | Economic Survey 2022-23 | Ministry of Finance, India | 2023 | external sector chapter | on disk (es2022-23.txt) |
| es-2023-24 | Economic Survey 2023-24 | Ministry of Finance, India | 2024 | Ch. 4 | on disk (es2023-24.txt) |
| es-2025-26 | Economic Survey 2025-26 | Ministry of Finance, India | 2026 | Ch. 4, Table IV.1 | on disk (es2025-26.txt) |
