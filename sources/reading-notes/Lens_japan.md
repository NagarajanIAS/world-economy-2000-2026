# Reading notes: country lens "Japan, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers, no cookies). URLs were taken from publisher
listing or issue pages where possible: the imf.org Japan country page (https://www.imf.org/en/Countries/JPN, 200; its `index.md` and
`index.json` versions list only the 2025 and 2026 Article IV issue pages, whose PDF links were used); the Bank of Japan's yearly lists of
monetary policy decisions (`/en/mopo/mpmdeci/mpr_YYYY/index.htm` for 2006, 2013, 2024, 2025 and 2026), its Outlook Report index
(`/en/mopo/outlook/index.htm`) and its broad-perspective review page (`/en/mopo/outline/bpreview/index.htm`); the Cabinet Office's English
white-paper page and archive (`www5.cao.go.jp/keizai3/whitepaper-e.html`, `…/whitepaper-e/archives.html` and the 2006 and 2013 index pages);
the Ministry of Finance budget and tax-policy pages; and JICA's India country page. Every guessed URL is flagged GUESSED. **The IMF country
page lists no Japan Article IV before 2025**, so every earlier staff report (JP-IMF-1 to JP-IMF-16) comes from a GUESSED URL built on the IMF's
file-naming pattern: `/external/pubs/ft/scr/YYYY/crYYNNN.pdf` to 2016; `/-/media/files/publications/cr/YYYY/crYYNNN.pdf` in 2017 and 2018;
`/-/media/files/publications/cr/YYYY/english/1jpneaYYYYnnn.pdf` from 2020 (Japan code "jpn"). For each file the title page and "Country
Report No." were read to confirm it is the Japan Article IV named; wrong hits (other countries, Japan Selected Issues and 2024 FSAP notes)
were discarded and are listed under Not obtained. Downloads are in the session scratchpad folder `lens_japan_dl/`, one subfolder per batch:
`imf/` (country and issue pages), `imf/g/` (staff reports), `boj/`, `gov/`, `oth/` (OECD 403 pages) and `in/` (JICA, MEA). PDFs were
converted with `pdftotext` (plain and `-layout`); HTML pages were stripped of tags and read as text. Python that read downloads was run
with `python3 -I`, from scripts kept outside the download folder. Economic Survey texts were not refetched: they were read from the Econ
Subject folder (`sources/text/es*.txt`, where text page = PDF page), and the printed page number was taken from the running header or
footer. Quotes are verbatim and under 15 words, and a script checked each one against the converted text (whitespace- and
apostrophe-normalised, with a column-split pass for two-column pages). Everything else is paraphrase. Page numbers are printed page
numbers unless stated; "PDF p." is used where only the PDF page can be given (for example the unnumbered Key Issues pages of IMF reports).
The data readings (JP-OTH-1) and the India–Japan trade balances are my own reading or arithmetic of data already held or of Survey
tables, and are marked "own reading" or "own arithmetic".

Printed-page offsets for IMF reports: CR 05/273, 06/275, 07/280, 08/253, 09/210: printed = PDF − 2. CR 11/181, 12/208, 13/253, 14/236:
printed = PDF − 1. CR 16/267, 17/242: printed = PDF − 6. CR 20/39 (2019 Article IV): printed = PDF − 5. CR 25/82: printed = PDF − 5.
CR 26/75: printed = PDF − 4.

Item labels:
- JP-IMF-n: IMF Article IV consultations with Japan.
- JP-BOJ-n: Bank of Japan decisions, Outlook Reports and the 2024 review.
- JP-GOV-n: Cabinet Office and Ministry of Finance (the Prime Minister's Office, kantei.go.jp, returned 404 to every request; see Not
  obtained).
- JP-OTH-n: data already in the book.
- JP-IN-n: India and Japan, from the Economic Surveys and JICA.

Indian years are fiscal years (April–March) or survey years. Japanese "fiscal" years also run April–March.

Abbreviations: BOJ = Bank of Japan; CEPA = Comprehensive Economic Partnership Agreement; CR = IMF Country Report; DFC = Dedicated Freight
Corridor; ETF = exchange-traded fund; JBIC = Japan Bank for International Cooperation; JCAP = JICA Country Analysis Paper; JGB = Japanese
government bond; JICA = Japan International Cooperation Agency; MAHSR = Mumbai–Ahmedabad High Speed Rail; NIRP = negative interest rate
policy; ODA = official development assistance; QE = quantitative easing (2001–06); QQE = quantitative and qualitative monetary easing (from
2013); YCC = yield curve control.

Already in the book (cite, do not duplicate):
- `Theme_money.md` MO-CB-3: BOJ "Changes in the Monetary Policy Framework", 19 March 2024, with the 29 January 2016 (negative rate, −0.1%,
  effective 16 February 2016) and 21 September 2016 (YCC) statements. Negative rate lasted about eight years; YCC September 2016 to March
  2024. **Not refetched here.** MO-IMF-4 (Box 2.1 p. 58): 2020–22 central-bank balance sheets grew by more than 20% of GDP in Japan.
- `IMF_2000-2002.md` (WEO May 2001 Ch. 1 p. 18): the BOJ's 19 March 2001 switch to a current-account-balance target (¥5 trillion), i.e.
  the start of the 2001–06 QE; `timeline_events.md` row 2001-03-19.
- `IMF_2014-2019.md` (WEO April 2016 Ch. 1 p. 7): the January 2016 negative rate.
- `IMF_2010-2014.md` (WEO April 2014): Japan to implement the remaining two "arrows".
- `IMF_2022-2023.md`: WEO October 2022 Ch. 1 p. 18 (dollar up about 25% against the yen in 2022; September intervention); WEO October 2023
  Ch. 1 p. 8 (BOJ loosened YCC).
- `IMF_2024-2025.md`: WEO July 2024 Box 1 p. 6 (yen depreciation pressure and intervention); WEO October 2024 Ch. 1 p. 5 (BOJ hike and
  yen carry-trade unwinding, August 2024); `Theme_markets.md` MK-IMF-5 ch1 p. 10 (same episode).
- `IMF_2026.md`: Japan forecasts and assumed inflation through 2026; WEO April 2026 Ch. 1 p. 3 (Japan's inflation below 2% after gasoline
  tax abolition); BOJ "rising toward about 1.5%".
- `Theme_debt.md` DF-IMF-2 (Fiscal Monitor April 2026 Table 1.2 p. 3): Japan gross debt 206.3 / 206.5 / 192.8% of GDP (2019 / 2025 / 2031,
  consolidated face value); DF-OTH-1 (Blanchard 2019 p. 2: Japan 10-year rate 0.1 vs growth about 1.4).
- `Theme_demography.md` DL-OTH-1 p. 16: Japan loses 21 million people between 2024 and 2054.
- `Theme_trade.md` TR-IN-1 (ES 2019-20 Vol 1 Ch 5 pp. 121–122 and p. 134): FTAs raised India's trade; the Korea and Japan agreements had a
  negative effect on India's manufactured exports.
- `India_ES_2010-2014.md` (ES 2010-11 and 2011-12 chapters): Japan named among the risks and causes of India's 2011-12 slowdown.
- `India_ES_2024-2026.md` (ES 2025-26 para 4.89): only the yen fell more than the rupee (5.5% vs 5.4%) from April 2025 to January 2026.
- `Lens_us.md` p. 12 (US–Japan tariff deal); `Lens_china.md` p. 7 (Chinese dual-use export ban to Japan, early 2026).

## IMF Article IV consultations with Japan

### JP-IMF-1. IMF, *Japan: 2005 Article IV Consultation—Staff Report…*, IMF Country Report No. 05/273, August 2005 (staff report dated 26 July 2005)
PDF: https://www.imf.org/external/pubs/ft/scr/2005/cr05273.pdf (GUESSED; 200; 62 PDF pages). Read: Executive Summary (p. 3), Staff
Appraisal (pp. 28–30), Table 1 (p. 36), Annex III (p. 47).
- p. 3: the economy was regaining momentum after a soft patch in late 2004; "Mild deflation persists." Banks had cut non-performing loans
  further; the BOJ kept its current-account target under QE, with short rates at zero. The deficit was large and "the debt ratio on an
  unsustainable path"; ageing added urgency.
- p. 28: progress in resolving the legacies of the bubble years: the financial system had been stabilised. p. 29: "the priority remains
  conquering deflation"; QE should stay until deflation and deflation expectations are eliminated; "it would be preferable to err on the
  side of being accommodative". An inflation objective could be part of a post-deflation framework. p. 29: plans to raise the consumption
  tax "could be put in place soon". p. 29: major banks' balance-sheet problems were largely resolved; regional-bank NPLs remained.
- Table 1, p. 36: real GDP 2002 −0.3%, 2003 1.4, 2004 2.6; CPI −1.0 (2002), −0.2 (2003), 0.0 (2004), −0.4 projected for 2005; GDP deflator
  −1.2 to −1.5 every year 2000–2004; structural balance −6.6% of GDP (2004); current account 3.7% of GDP (2004); yen 108.2 per
  dollar (2004).
- Annex III, p. 47: net debt to rise to almost 110% of GDP by 2010, from 82% at end-2004.

### JP-IMF-2. IMF, *Japan: 2006 Article IV Consultation*, IMF Country Report No. 06/275, July 2006
PDF: https://www.imf.org/external/pubs/ft/scr/2006/cr06275.pdf (GUESSED; 200; 57 PDF pages). Read: Executive Summary (p. 3), Staff Appraisal
(pp. 29–30), Table 1 (p. 35).
- p. 3: "The post-bubble adjustment is essentially complete." In March the BOJ shifted from targeting reserves to the overnight rate (still
  zero), with core CPI positive for a few months.
- p. 29 (appraisal): "Japan’s post-bubble legacies have essentially been resolved and deflation has ended." The risk of a deflationary
  relapse had receded. p. 30: the end of deflation and the smooth exit from QE were "milestones"; policy should stay accommodative so that
  inflation expectations drift up; the floor of the BOJ's "understanding of price stability" could be raised over time.
- p. 29 (authorities' views): officials saw limited risk in a disorderly unwinding of yen carry trades.
- Table 1, p. 35: gross public debt 175.4% of GDP (2005); CPI −0.3 (2005), projected 0.6 in 2006 and 2007; real GDP 2.6 (2005).

### JP-IMF-3. IMF, *Japan: 2007 Article IV Consultation*, IMF Country Report No. 07/280, August 2007
PDF: https://www.imf.org/external/pubs/ft/scr/2007/cr07280.pdf (GUESSED; 200; 51 PDF pages). Read: Executive Summary (p. 3).
- p. 3: the expansion was in its sixth year; CPI inflation was very weak (moderate wages, global competition); "the Bank of Japan has opted
  for a very gradual pace of tightening". Low rates had contributed to capital outflows that weakened the yen, which was below its long-term
  equilibrium. Raising the consumption tax would be "more equitable and supportive of growth" (paraphrase of the revenue options).

### JP-IMF-4. IMF, *Japan: 2008 Article IV Consultation*, IMF Country Report No. 08/253, July 2008
PDF: https://www.imf.org/external/pubs/ft/scr/2008/cr08253.pdf (GUESSED; 200; 49 PDF pages). Read: Executive Summary and Staff Appraisal
(p. 3), Table 1 (p. 30).
- p. 3: "Japan appears headed for a modest slowdown"; subprime fallout limited; exports to non-US destinations strong; underlying
  inflation about zero, so the BOJ could hold rates; the yen still undervalued despite a 10% real effective rise since mid-2007; on the
  consumption tax, "this opportunity to raise the consumption tax rate should be seized".
- Table 1, p. 30 (projections for 2009): real GDP 1.5%, exports 4.6%, CPI 0.8%, gross public debt 197.3% of GDP; overnight call rate 0.53%
  in 2008 (latest).

### JP-IMF-5. IMF, *Japan: 2009 Article IV Consultation*, IMF Country Report No. 09/210, July 2009
PDF: https://www.imf.org/external/pubs/ft/scr/2009/cr09210.pdf (GUESSED; 200; 53 PDF pages). Read: Executive Summary and Introduction
(p. 3), Staff Appraisal (pp. 31–32), Table 1 (p. 33).
- p. 3: "The global recession has derailed Japan’s export-led boom." The economy was expected to contract 6% in 2009, and "inflation is
  projected to remain negative through 2011". Dependence on manufacturing exports left Japan exposed to the collapse in external demand:
  "The result has been the most severe recession in decades."
- pp. 31–32: the BOJ's response was timely; fiscal stimulus in 2008 and 2009 gave valuable support; once recovery took hold Japan needed a
  consolidation strategy and "a commitment to raise the consumption tax"; growth should be rebalanced to domestic demand.
- Table 1, p. 33 (projections): 2009 GDP −6.0%, exports −29.3%, CPI −1.1%; unemployment 5.1% (2009) and 5.8% (2010); gross debt 217.4% of GDP
  (2009) and 226.3% (2010).

### JP-IMF-6. IMF, *Japan: 2011 Article IV Consultation*, IMF Country Report No. 11/181, July 2011 (staff report dated 28 June 2011)
PDF: https://www.imf.org/external/pubs/ft/scr/2011/cr11181.pdf (GUESSED; 200; 45 PDF pages). Read: Key Issues (PDF p. 2), p. 3, Table 1 (p.
23).
- PDF p. 2: GDP forecast to fall 0.7% in 2011 and rise 2.9% in 2012; reconstruction should be financed with new taxes; staff recommended "a
  moderate increase in the consumption tax, from 5 percent to 7–8 percent" in 2012; the BOJ could buy more longer-dated securities; the
  main spillover risk was a disruption in the JGB market.
- p. 3: the earthquake and tsunami of 11 March 2011 "brought Japan’s nascent recovery to a halt". Damage to capital estimated at 3–5% of
  GDP; electricity shortages in the Kanto region (40% of GDP); supply-chain disruption in cars and electronics. Q1 2011 GDP −3.5% (q/q
  saar); industrial production fell 15% in March.
- Table 1, p. 23 (outturns): real GDP 2008 −1.2%, **2009 −6.3%**, 2010 4.0%; exports **2009 −23.9%**, 2010 23.9%; CPI 2009 −1.4%, 2010 −0.7%;
  gross public debt 216.3% of GDP (2009), 220.4% (2010), 233.1% projected for 2011.

### JP-IMF-7. IMF, *Japan: 2012 Article IV Consultation*, IMF Country Report No. 12/208, August 2012 (staff report dated 10 July 2012)
PDF: https://www.imf.org/external/pubs/ft/scr/2012/cr12208.pdf (GUESSED; 200; 50 PDF pages). Read: Key Issues (PDF p. 2), Staff Appraisal
(pp. 26–27), Table 1 (p. 28).
- PDF p. 2: "A fiscal adjustment of 10 percent of GDP over the next decade is necessary". Further easing would speed achievement of the BOJ's
  new 1 percent inflation goal; reforms should raise female and older workers' participation and boost immigration.
- p. 26: legislation to double the consumption tax to 10% by 2015 was "a crucial step", but a further 5% of GDP adjustment was needed. p.
  27: the yen appeared "moderately overvalued" after its post-crisis appreciation.
- Table 1, p. 28: yen 79.8 per dollar (2011); gross debt 229.9% of GDP (2011), 234.5 (2012 proj.), 240.0 (2013 proj.).

### JP-IMF-8. IMF, *Japan: 2013 Article IV Consultation*, IMF Country Report No. 13/253, August 2013 (staff report dated 12 July 2013)
PDF: https://www.imf.org/external/pubs/ft/scr/2013/cr13253.pdf (GUESSED; 200; 58 PDF pages). Read: Key Issues (PDF p. 2), p. 7, Staff
Appraisal (pp. 25–26), Table 1 (p. 34), Table 4 (p. 37).
- PDF p. 2: the "three-arrows" (aggressive monetary easing, flexible fiscal policy, structural reforms) offered "a unique opportunity to end
  decades-long deflation and sluggish growth"; but "all three arrows need to be launched for the policies to succeed". GDP growth projected
  at 2 percent in 2013.
- p. 7: staff's baseline: inflation reaches 2 percent "in the medium term", potential growth about 1 percent; the yen moderately undervalued
  after the depreciation.
- pp. 25–26: debt reduction needs an 11% of GDP adjustment over a decade; without fiscal and structural follow-through, monetary policy
  would be overburdened and further depreciation would hurt trading partners, especially emerging Asia.
- **Table 4, p. 37 (Medium-Term Projections)**: headline CPI 0.1 (2013), 2.9 (2014), **1.9 (2015), 1.9 (2016), 2.0 (2017), 2.0 (2018)**
  (excluding the planned tax rises: 1.2, 1.6, 1.9, 2.0, 2.0 for 2014–18); real GDP about 1.1–1.2% a year 2014–18; **gross debt 246.9% of
  GDP (2013) rising to 248.3% (2018)**; net debt 144.3 to 158.2%.

### JP-IMF-9. IMF, *Japan: 2014 Article IV Consultation*, IMF Country Report No. 14/236, July 2014 (staff report dated 3 July 2014)
PDF: https://www.imf.org/external/pubs/ft/scr/2014/cr14236.pdf (GUESSED; 200; 61 PDF pages). Read: Key Issues (PDF p. 2), pp. 4–5, Table 4
(p. 38).
- PDF p. 2: "Abenomics is gaining traction, but progress across the three arrows has been uneven"; the second consumption tax rise was
  "critical" for fiscal credibility; no further easing needed "at this point".
- p. 4: BOJ balance sheet 52% of GDP by end-May 2014; Board members still forecast 2% inflation "in or around fiscal year 2015"; the tax rose
  to 8% (1 April 2014), with 10% planned for October 2015; structural reforms "gradual albeit limited".
- p. 5: Q1 2014 GDP +6.7% (q/q saar) on rush demand before the tax rise (consumption +9.2%), similar to the 1997 pre-tax rush.
- Table 4, p. 38 (projections): real GDP 1.6% (2014), 1.1 (2015); CPI 2.8 (2014), 2.1 (2015), 2.7 (2016); gross debt 243.2 (2014) to 238.2%
  (2019).

### JP-IMF-10. IMF, *Japan: 2016 Article IV Consultation—Press Release; and Staff Report*, IMF Country Report No. 16/267, August 2016 (staff report dated 13 July 2016)
PDF: https://www.imf.org/external/pubs/ft/scr/2016/cr16267.pdf (GUESSED; 200; 74 PDF pages). Read: Key Issues (PDF p. 7), indicator table
(p. 4), Staff Appraisal (p. 22).
- PDF p. 7: "Abenomics needs a significant policy upgrade to regain traction." Targets for growth, inflation and the primary balance
  "remain out of reach under current policies"; the authorities had introduced negative rates and delayed the tax rise. Staff proposed
  replacing the planned 2-point rise in 2019 with gradual 0.5–1 point steps to at least 15 percent, and income policies to lift wages.
- p. 4 (outturns): real GDP **2014 0.0%**, 2015 0.5%; CPI 2014 2.7 (1.2 excluding the tax), **2015 0.8 (0.3 excluding the tax)**; gross debt
  249.1% (2014), 248.0 (2015); 10-year JGB yield −0.1 at end-2016 (proj.).
- p. 22: inflation would stay below the BOJ target over the medium term.

### JP-IMF-11. IMF, *Japan: 2017 Article IV Consultation*, IMF Country Report No. 17/242, July 2017 (staff report dated 12 July 2017)
PDF: https://www.imf.org/-/media/files/publications/cr/2017/cr17242.pdf (GUESSED; 200; 84 PDF pages; the older `/external/pubs/ft/scr/2017/`
path returned 404). Read: Key Issues (PDF p. 7).
- PDF p. 7: Abenomics improved conditions but "has not yet achieved a durable exit from deflation"; unemployment at record lows; staff again
  recommended a pre-announced schedule of 0.5–1.0 point consumption-tax rises to at least 15 percent.

### JP-IMF-12. IMF, *Japan: 2018 Article IV Consultation*, IMF Country Report No. 18/333, November 2018 (staff report dated 6 November 2018)
PDF: https://www.imf.org/-/media/files/publications/cr/2018/cr18333.pdf (GUESSED; 200; 93 PDF pages). Read: Key Issues (PDF p. 6) only.
- PDF p. 6: population ageing and shrinking "will dominate economic policy making in coming decades"; inflation likely to stay below 2% under
  current policies.

### JP-IMF-13. IMF, *Japan: 2019 Article IV Consultation*, IMF Country Report No. 20/39, February 2020 (staff report dated 14 January 2020; Board 30 January 2020)
PDF: https://www.imf.org/-/media/files/publications/cr/2020/english/1jpnea2020001.pdf (GUESSED; 200; 119 PDF pages; `…/2019/english/
1jpnea2019001.pdf` returned 404). Read: Key Issues (PDF p. 6), indicator table (PDF p. 5), p. 10, p. 25, Annex XV (pp. 100–101).
- PDF p. 6: "The rapid aging and shrinking of Japan’s population has become central to macroeconomic policies". Front-loading before the
  October 2019 tax rise (8 to 10 percent) was smaller than in 2014, partly due to countermeasures; inflation to stay below 2%.
- p. 10: official projections: the 65-plus share rises from 28 to 38 percent and "the total population will shrink by over 25 percent"
  (127 million to 95 million by 2058) over 40 years. p. 25: demographics could cut real GDP by 25% in four decades versus a no-headwinds path.
- PDF p. 5 (outturns): real GDP 2017 2.2%, 2018 0.3%; headline CPI **2017 0.5, 2018 1.0**, 2019 0.6 (est.); gross debt **2018 237.9%**.
- **Annex XV, p. 100, and Table 1, p. 101 (India)**: Japan's bilateral swap lines with Asian central banks; "the arrangement with India is by
  far the largest size (US$ 75 billion)". The India line is US dollar against rupee only (fn. 2), Ministry of Finance of Japan, renewed
  February 2019.

### JP-IMF-14. IMF, *Japan: 2022 Article IV Consultation*, IMF Country Report No. 22/99, April 2022 (staff report dated 16 March 2022)
PDF: https://www.imf.org/-/media/files/publications/cr/2022/english/1jpnea2022001.pdf (GUESSED; 200; 83 PDF pages). Read: Key Issues (PDF
p. 5), indicator table (PDF p. 4).
- PDF p. 5: pre-COVID Abenomics helped exit deflation and raise participation but "fell short on the deep reforms needed to raise
  productivity"; the BOJ should keep accommodation.
- PDF p. 4 (projections): **headline CPI 1.0 (2022), 0.8 (2023)**; real GDP −4.5 (2020), 1.6 (2021), 2.4 (2022 proj.); gross debt 259.0%
  (2020), 263.1 (2021).

### JP-IMF-15. IMF, *Japan: 2023 Article IV Consultation*, IMF Country Report No. 23/127, March 2023 (staff report dated 7 March 2023)
PDF: https://www.imf.org/-/media/files/publications/cr/2023/english/1jpnea2023001.pdf (GUESSED; 200; 99 PDF pages). Read: Key Issues (PDF
p. 5), indicator table (PDF p. 4).
- PDF p. 5: "Headline inflation has recorded levels not seen in four decades." Accommodation still appropriate, but "more flexibility in
  longer term yields is warranted" to manage the side effects of prolonged easing (YCC).
- PDF p. 4: CPI 2022 2.5 (est.), 2023 2.7 (proj.); yen 131.5 per dollar (2022); CPI-based real effective exchange rate 60.9 (2010 = 100) in 2022.

### JP-IMF-16. IMF, *Japan: 2024 Article IV Consultation*, IMF Country Report No. 24/118, May 2024 (staff report dated 15 April 2024)
PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1jpnea2024010.pdf (GUESSED; 200; 81 PDF pages; numbers 001–009 of 2024
are FSAP papers, CR 24/109–24/117). Read: Key Issues (PDF p. 6).
- PDF p. 6: broad-based price increases after three decades of low inflation; core inflation to stay above 2% until the second half of 2025;
  "further hikes in the short-term policy rate should proceed at a gradual pace".

### JP-IMF-17. IMF, *Japan: 2025 Article IV Consultation*, IMF Country Report No. 25/82, April 2025 (staff report dated 11 March 2025; Board 26 March 2025)
Issue page: https://www.imf.org/en/publications/cr/issues/2025/04/01/japan-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-565846
(listed on the country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1jpnea2025001-print-pdf.pdf (from the
issue page; 200; 99 PDF pages). Read: Key Issues (PDF p. 6), Table 1 (p. 39).
- PDF p. 6: "After three decades of near-zero inflation, signs are growing" of a new equilibrium at 2%; potential growth 0.5%; inflation to
  converge from above to 2% in late 2025; debt expected to rise from 2030; accommodation to be withdrawn gradually.
- Table 1, p. 39: CPI 2.5 (2022), 3.2 (2023), 2.7 (2024 est.), **2.4 (2025 proj.)**; real GDP 0.1 (2024 est.), 1.2 (2025 proj.); gross debt
  240.0% (2023), 236.7 (2024); 10-year JGB yield 1.1% end-2024; yen 151.4 per dollar (2024); CPI-based REER 55.0 (2010 = 100).

### JP-IMF-18. IMF, *Japan: 2026 Article IV Consultation*, IMF Country Report No. 26/75, April 2026 (staff report dated 12 March 2026; Board 27 March 2026)
Issue page: https://www.imf.org/en/publications/cr/issues/2026/04/02/japan-2026-article-iv-consultation-press-release-staff-report-and-statement-by-the-575112
(listed; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2026/english/1jpnea2026001.pdf (from the issue page; 200; 104 PDF
pages). Read: Key Issues (PDF p. 5), indicator table (PDF p. 4), pp. 4–5, p. 9.
- PDF p. 5: prices grew faster than 2% for over three and a half years before moderating in January 2026; "nominal wages are rising at a
  historic pace"; inflation to converge to target in 2027; debt-to-GDP to rise again from 2035; "Monetary policy accommodation is
  appropriately being withdrawn", with gradual hikes toward neutral.
- p. 4: inflation fell to 1.5 percent in January 2026; "a 6-percent fall in real wages since 2022"; Takaichi succeeded Ishiba in October 2025
  and the LDP won a lower-house supermajority in February 2026; working-age population peaked in 1995 and shrinks about 0.6% a year.
- p. 5: GDP −0.2% in 2024, 1.1% in 2025; July 2025 US–Japan deal capped most tariffs at 15% with a Japanese investment pledge of up to
  $550 billion; Chinese measures against Japan from November 2025.
- p. 9: policy rate "currently 0.75 percent" (March 2026); BOJ JGB holdings fell from 91% of GDP (June 2024) to about 80% (January 2026);
  fn. 4: **gross debt redefined from non-consolidated market value to consolidated nominal value**, and fn. 5: the December 2025 GDP rebasing
  raised nominal GDP about 4%, lowering debt ratios. Debt about 207% of GDP in 2025Q3.
- PDF p. 4 (new definition): CPI **2025 3.2**, 2026 1.9 (proj.); core (ex fresh food and energy) 3.9 (2023), 3.0 (2025); gross debt 227.8%
  (2022), 214.5 (2024), 206.8 (2025), 193.1 (2031 proj.); 10-year JGB yield 2.1% end-2025; yen 149.7 per dollar (2025).

## Bank of Japan (URLs from the BOJ yearly decision lists unless flagged)

### JP-BOJ-1. BOJ, "Change in the Guideline for Money Market Operations" and "The Introduction of a New Framework for the Conduct of Monetary Policy", 9 March 2006
https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2006/k060309.htm and …/k060309b.htm (both listed; 200). Read in full.
- k060309: the operating target moved from current-account balances back to the overnight call rate, kept at "effectively zero"; excess
  balances to be run down over a few months (vote 7-1). Since March 2001 the Bank had committed to QE until core CPI was stably at or above
  zero; "The Bank, therefore, judged that the conditions laid out in the commitment are fulfilled."
- k060309b: the Board's "understanding of medium- to long-term price stability" was "an approximate range between zero and two percent",
  with most median views around 1 percent.

### JP-BOJ-2. BOJ, "Change in the Guideline for Money Market Operations", 14 July 2006
https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2006/k060714.pdf (listed; 200). Read: p. 1.
- p. 1: unanimous decision to raise the call-rate target to around 0.25 percent, the first rise after the zero-rate period. (BIS data in
  the book show 0.5% from February 2007 and 0.1% by December 2008; own reading, JP-OTH-1.)

### JP-BOJ-3. Cabinet Office, Ministry of Finance and BOJ, "Joint Statement of the Government and the Bank of Japan on Overcoming Deflation and Achieving Sustainable Economic Growth", 22 January 2013
https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2013/k130122c.pdf (listed; 200; 2 pages). Read in full. (The same-day BOJ release k130122a.pdf,
introducing the target and open-ended purchases, was fetched but not read.)
- p. 1: "the Bank sets the price stability target at 2 percent" (year-on-year CPI) and aims to achieve it "at the earliest possible time";
  the government commits to growth measures and a sustainable fiscal structure (pp. 1–2); the Council on Economic and Fiscal Policy reviews
  progress (p. 2).

### JP-BOJ-4. BOJ, "Introduction of the 'Quantitative and Qualitative Monetary Easing'", 4 April 2013
https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2013/k130404a.pdf (listed; 200). Read: pp. 1–2.
- p. 1: 2% target "with a time horizon of about two years"; "It will double the monetary base" and JGB and ETF holdings in two years; the
  operating target becomes the monetary base, rising ¥60–70 trillion a year (fn. 1: from ¥138 trillion at end-2012 to ¥270 trillion at
  end-2014); JGB holdings up ¥50 trillion a year; average maturity of purchases from under three years to about seven.
- p. 2: the "banknote principle" suspended, citing the government's January commitment on fiscal credibility.

### JP-BOJ-5. BOJ, *Outlook for Economic Activity and Prices*, April 2013 (gor1304a) and April 2016 (gor1604a)
https://www.boj.or.jp/en/mopo/outlook/gor1304a.pdf and …/gor1604a.pdf (both listed on the Outlook index; 200). Read: 2013 pp. 3–4 and
Appendix (PDF p. 8); 2016 Appendix (PDF pp. 9–11).
- April 2013, p. 4: CPI likely to reach around 2 percent "toward the latter half of the projection period". Appendix (PDF p. 8), Board
  median forecasts of core CPI (all items less fresh food) excluding the tax rises: **FY2013 +0.7, FY2014 +1.4, FY2015 +1.9** (with the tax:
  +3.4 in FY2014 and +2.6 in FY2015); real GDP FY2013 +2.9.
- April 2016, Appendix (PDF p. 11): **FY2015 core CPI actual 0.0** (excluding tax effects); real GDP FY2015 +0.7. PDF p. 9: 2% now
  "likely to achieve around 2 percent inflation during fiscal 2017".

### JP-BOJ-6. BOJ, negative rate (29 January 2016), YCC (21 September 2016) and exit (19 March 2024) — see `Theme_money.md` MO-CB-3
Not refetched. The March 2024 statement appears on the 2024 list (`state_2024/k240319a.htm`), confirming the date.

### JP-BOJ-7. BOJ, "Change in the Guideline for Money Market Operations and Decision on the Plan for the Reduction of the Purchase Amount of Japanese Government Bonds", 31 July 2024
https://www.boj.or.jp/en/mopo/mpmdeci/state_2024/k240731a.htm (listed; 200). Read in full.
- Call rate to around 0.25 percent from 1 August 2024 (vote 7-2; Nakamura and Noguchi dissented); monthly JGB purchases to be cut by about
  ¥400 billion a quarter to about ¥3 trillion in January–March 2026. Wage rises from the spring negotiations were "significantly higher";
  "Real interest rates are expected to remain significantly negative".

### JP-BOJ-8. BOJ, "Change in the Guideline for Money Market Operations", 24 January 2025 and 19 December 2025
https://www.boj.or.jp/en/mopo/mpmdeci/state_2025/k250124a.htm and …/k251219a.htm (both listed; 200). Read in full.
- 24 January 2025: call rate to around 0.5 percent (8-1; Nakamura dissented), effective 27 January.
- 19 December 2025: call rate to around 0.75 percent (unanimous), effective 22 December; firms highly likely to keep raising wages in 2026;
  the risk of interruption to wage-setting low despite US tariffs.

### JP-BOJ-9. BOJ, decisions of 16 June, 18 September and 30 October 2026, and *Outlook for Economic Activity and Prices*, October 2026
https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260616a.pdf, …/k260918a.pdf, …/k261030a.pdf (listed; 200); Outlook
https://www.boj.or.jp/en/mopo/outlook/gor2610a.pdf (listed; 200). Read: each statement pp. 1–2; Outlook Appendix (PDF p. 10).
- 16 June 2026: call rate to around 1.0 percent (7-1), effective 17 June; Middle East situation and oil prices weighing on activity.
- 18 September 2026: to "encourage the uncollateralized overnight call rate to remain at around 1.25 percent" (7-2), effective 24
  September. p. 1: PPI high on AI-related demand, oil and "the depreciation of the yen"; underlying CPI inflation approaching 2%, with
  upside risk.
- 30 October 2026: **rate held at around 1.25 percent (8-1)** — the current policy rate. Takata proposed 1.5%, arguing "the situation had
  shifted to a new phase" (p. 2). ETF sales pace raised from about ¥330 billion to about ¥860 billion a year (book value) from January 2027.
- Outlook October 2026, Appendix: core CPI medians FY2026 +2.5, FY2027 +2.6, FY2028 +2.0; real GDP +0.7, +0.7, +0.8. Note 4: forecasts
  exclude a proposed temporary consumption-tax cut on food and beverages under deliberation in the Diet, estimated to lower FY2027 core CPI
  by about 1.3 points.

### JP-BOJ-10. BOJ, *Review of Monetary Policy from a Broad Perspective*, December 2024
Listed on https://www.boj.or.jp/en/mopo/outline/bpreview/index.htm (200) as …/mpr_2024/k241219b.pdf (200; 244 PDF pages). Read: Foreword,
"The Bank's View" pp. 4–5.
- Foreword: achieving price stability had been a challenge for 25 years since the late 1990s; the review ran from April 2023.
- p. 4: large-scale easing pushed up activity and prices "to some extent", but less than expected when the 2% target was set with a
  two-year horizon; tight labour markets (partly demographic) and import prices drove wage and price rises in the 2020s.
- p. 5: easing "did not have as large an upward effect on prices as originally expected", partly because expectations were hard to move;
  it harmed JGB market functioning; no evidence it impeded financial intermediation; on balance "the overall effect on the Japanese economy
  so far appears to have been positive".

## Japanese government

### JP-GOV-1. Cabinet Office, *Annual Report on the Japanese Economy and Public Finance 2006* (Summary), Chapter 1, July 2006
Index https://www5.cao.go.jp/keizai3/2006/0718wp-keizai/summary.html (listed on the archive page; 200); PDF …/1syo-hyoshi.pdf (200; 20
PDF pages). Read: pp. 1, 9, 18.
- p. 9: moves to overcome deflation had made progress, with signs of a change in the trend of long-term price declines.
- p. 18 (summary): "Overcoming of deflation now in sight"; "we are now close to breaking out of the deflationary trend", but consumer prices
  were rising only moderately.

### JP-GOV-2. Cabinet Office, *Annual Report on the Japanese Economy and Public Finance 2013* (Summary), Chapter 1
Index https://www5.cao.go.jp/keizai3/whitepaper-e/archives/wp2013-e.html (listed; 200); PDF …/archives/1syo-hyoushi2013.pdf (200; 12 PDF
pages). Read: p. 7.
- p. 7: since March 2013 consumer prices had been falling only more slowly; "What is critical to end deflation is to raise the expected rate
  of inflation."

### JP-GOV-3. Cabinet Office, *Annual Report on the Japanese Economy and Public Finance 2026* (Summary), July 2026
https://www5.cao.go.jp/keizai3/2026/0724wp-keizai/setsumei-e2026.pdf (listed; 200; 18 PDF pages). Read: PDF pp. 2, 4, 6.
- PDF p. 4: import prices rising sharply with pass-through to business prices; consumer price inflation "in the 1% range", partly due to
  emergency fuel-price measures; real wages on an upward trend.
- PDF p. 6: whether deflation has been overcome requires confirming that the economy "is unlikely to return" to persistent price declines;
  the four indicators show an upward trend (CPI, GDP deflator, unit labour costs; the GDP gap around zero). CPI May 2026: all items 1.5%,
  less fresh food 1.4%, less fresh food and energy 1.8% (Figure 1). (The report does not itself declare deflation over in the pages read.)

### JP-GOV-4. Ministry of Finance, *Japanese Public Finance Fact Sheet* (April 2026)
https://www.mof.go.jp/english/policy/budget/budget/fy2026/02.pdf (listed on the budget page; 200; 68 PDF pages). Read: PDF pp. 4, 8, 21.
- PDF p. 4: in the FY2026 general-account budget, national debt service is 25.6% of spending (interest payments 10.7%), social security
  31.9%.
- PDF p. 8 (printed 5): outstanding government general bonds "projected to reach 1,145 trillion yen at the end of FY2026" (about ¥1,095
  trillion excluding advance refunding bonds, Note 3).
- PDF p. 21 (printed 18): interest rates are rising; "Japan has the highest level debt-to-GDP ratio in the world."

### JP-GOV-5. Ministry of Finance, "Material on Consumption Taxation"
https://www.mof.go.jp/english/policy/tax_policy/tax_system/consumption/index.html (linked from the tax-system page; 200). Read in full.
- Standard rate 10% (7.8% national, 2.2% local) with a reduced 8% rate on food and newspapers from October 2019; invoice system from October
  2023. (The page gives no history of the 1997, 2014 and 2019 rises; those dates are from JP-IMF-9 p. 5 and JP-IMF-13.)

## Data already in the book

### JP-OTH-1. Japan series held in `data/clean/` — own reading
Files: `fred/DEXJPUS.json` (yen per dollar, monthly average), `fred/IRLTLT01JPM156N.json` (10-year JGB yield), `fred/NIKKEI225.json`,
`fred/JPNASSETS.json` (BOJ total assets), `bis/CBPOL.json` (key JP), `wdi/SP.POP.65UP.TO.ZS.json` and `wdi/SP.POP.TOTL.json` (JPN).
- Yen: strongest monthly average 76.6 per dollar (October 2011); weakest 162.3 (July 2026); 158.6 in November 2026.
- 10-year yield: low −0.28% (August 2019); 0.73% (January 2024); high 3.05% (September 2026); 2.76% (October 2026).
- BOJ assets: ¥158 trillion (December 2012) to a peak of ¥765 trillion (August 2024); ¥626 trillion (October 2026).
- Nikkei 225: December 1989 monthly average 38,115 was first exceeded in March 2024 (39,844); peak 68,340 (June 2026).
- BIS policy rate: 0.25 (July 2006), 0.5 (February 2007), 0.1 (December 2008), 0.5 (January 2025), 0.75 (December 2025), 1.0 (June 2026),
  1.25 (September and October 2026).
- Population peaked at 128.07 million in 2010; 123.37 million in 2025. Share aged 65+: 17.4% (2000), 30.0% (2025).

## India and Japan

### JP-IN-1. *Economic Survey 2010-11*, Chapter "Industry" and Statistical Appendix Table 7.4 (on disk)
`es2010-11.txt`. Read: p. 229 (PDF 229); Tables 7.4(A) and 7.4(B), pp. A94 and A99 (PDF 428, 433).
- p. 229: the 2009 JBIC survey of Japanese investors continued to "rank India as the second most promising country for overseas business
  operations", after China.
- Table 7.4(A), p. A94: imports from Japan US$ 7,886 million (2008-09), 6,734 million (2009-10). Table 7.4(B), p. A99: exports to Japan
  US$ 3,026 million and 3,630 million. Deficit with Japan about US$ 3.1 billion in 2009-10 (own arithmetic).

### JP-IN-2. *Economic Survey 2011-12* (on disk)
`es2011-12.txt`. Read: pp. 159 (Box 7.1), 176, 339.
- p. 176: India–Japan CEPA signed 16 February 2011, in force 1 August 2011; covers goods, services, investment and more than 90 per cent of
  trade; India's third CEPA after Singapore and Korea and "first with a developed country".
- p. 159 (Box 7.1): "The Tsunami in Japan which led to disruption of supply chains in Japan" could have helped India's electronics exports.
- p. 339: the 2011 global slowdown came on top of supply-chain disruption from the March 2011 earthquake and tsunami.

### JP-IN-3. *Economic Survey 2015-16*, Chapter on preferential trade agreements, and Box 6.5 "High Speed Train Project" (on disk)
`es2015-16.txt`. Read: pp. 119–128 (PDF = printed), p. 145 (Box 6.5, PDF 307).
- p. 119: India's Asian FTAs listed, ending with "Japan (2011)". p. 126 (table): average applied tariff changes for Japan imports. p. 128: in
  one product-level specification "the Japan FTA has had a significantly negative effect on exports" (a fall of 18 per cent), with zero
  effect on imports; in the country-level regressions the Japan FTA effect on trade was not statistically significant.
- **p. 145, Box 6.5**: JICA's feasibility study (July 2015); Cabinet approval December 2015; MoU 12 December 2015. Construction cost about
  ₹70,915 crore, completion cost about ₹97,636 crore; about seven years from start of construction; Japanese ODA ₹79,165 crore (81 per cent
  of cost) "for 50 years with 0.1 per cent interest and a 15-year moratorium"; 508 km, 12 stations, 320 km/h operating speed. "Thirty-five
  trains per day each way will operate by 2023", with about 36,000 daily users in 2023. Some packages reserved for Japanese prime
  contractors or Japanese-led JVs.

### JP-IN-4. *Economic Survey 2016-17*, Chapter 4 "The Festering Twin Balance Sheet Problem" (on disk)
`es2016-17.txt`. Read: pp. 87–88 (PDF 103–104).
- p. 87: India's twin-balance-sheet stress had not led to stagnation "as occurred in the U.S. and Europe after the Global Financial Crisis
  and Japan" after its bubble burst; p. 88: India instead chose to "give time to time" (forbearance).

### JP-IN-5. *Economic Survey 2017-18*, Volume 2, Chapter "Industry and Infrastructure" (on disk)
`es2017-18.txt`. Read: p. 124 (PDF 272).
- p. 124: "Mauritius, Singapore and Japan have been top three countries" by share of FDI equity inflows (36.17 per cent together; the
  sentence is broken by a box in the text file, so the base period could not be read).

### JP-IN-6. *Economic Survey 2019-20* (on disk)
`es2019-20.txt`. Read: Vol 1 p. 153 (PDF 165); Vol 2 Tables 7.4(A) p. A120 and 7.4(B) p. A129 (PDF 742, 751); p. 134 is TR-IN-1.
- p. 153: banks back great economies; in the 1980s "Japan had 15 of the top 25 largest banks then".
- Tables 7.4: imports from Japan US$ 10,973 million (2017-18), 12,773 million (2018-19); exports to Japan 4,735 and 4,862 million. Deficit
  about US$ 7.9 billion in 2018-19 (own arithmetic).

### JP-IN-7. *Economic Survey 2020-21*, Volume 1 (on disk)
`es2020-21.txt`. Read: p. 77 (PDF 94), p. 224 (PDF 241).
- p. 77 (para 2.43): front-loaded public investment under the National Infrastructure Pipeline could avoid "a low wage-growth trap, as has
  happened in Japan during the last two decades".
- p. 224 (para 7.32): India's 2015 asset quality review differed from bank clean-ups in Japan, the EU and the US: no crisis at the time and
  no forced recapitalisation or capital backstop.

### JP-IN-8. Mumbai–Ahmedabad High Speed Rail in later Surveys (on disk)
`es2022-23.txt` p. 355 (PDF 398); `es2024-25.txt` p. 167 (PDF 212); `es2025-26.txt` p. 351 (PDF 402).
- ES 2022-23 p. 355: MAHSR sanctioned in 2015 with technical and financial cooperation from Japan; survey and design finalised.
- ES 2024-25 p. 167: sanctioned December 2015; 508 km; "has a revised cost of ₹1.08 lakh crore"; 47.17 per cent physical progress by October
  2024, expenditure ₹67,486 crore.
- ES 2025-26 p. 351: over 55 per cent physical progress "as on October 2025, with land acquisition completed".

### JP-IN-9. *Economic Survey 2025-26*, Statistical Appendix, Tables 6.4(A) and 6.4(B) (on disk)
`es2025-26_statistical_appendix.txt`. Read: Table 6.4(A) PDF p. 144; Table 6.4(B) p. 148 (PDF 155).
- Imports from Japan US$ 17,696 million (2023-24), 18,915 million (2024-25; 2.6% of imports); exports to Japan 5,159 and 6,249 million
  (1.43% of exports). April–November 2025-26: imports 14,580 million (+13.4%), exports 3,872 million (−2.83%).
- Deficit with Japan about US$ 12.7 billion in 2024-25, against about US$ 3.1 billion in 2009-10 (JP-IN-1) and US$ 7.9 billion in 2018-19
  (JP-IN-6) (own arithmetic).
- **Book dataset**: `data/clean/india/` holds no series for trade with Japan or FDI from Japan (only `exports_to_us.json` and
  `imports_from_china.json` by partner, plus aggregate `fdi_net.json`).

### JP-IN-10. JICA, *JICA Country Analysis Paper for India* (last updated March 2025) and "Operational Results … (India)" (FY2023)
Both linked from https://www.jica.go.jp/english/overseas/india/index.html (200): …/__icsFiles/afieldfile/2025/05/08/jcap_in_en_202503_1.pdf
(200; 46 pages; printed = PDF) and https://www.jica.go.jp/english/overseas/n_files/india.pdf (200; 2 pages). Read: JCAP pp. 21–22, 31, 37;
results sheet p. 1.
- p. 21: cumulative Japanese ODA to India ¥7.66 trillion to FY2022, of which ¥7.44 trillion ODA loans; FY2018–FY2022 ¥2.14 trillion in loans.
- p. 22: the March 2022 Kishida–Modi statement aimed at "a total investment of 5 trillion yen in India over the next five years" (public and
  private); ODA loans averaged over ¥300 billion a year.
- p. 31: December 2015 agreement to use Japanese high-speed rail technology for Mumbai–Ahmedabad.
- p. 37: "India has the largest scale of ODA loan projects among all JICA projects".
- Results sheet: Finance and Investment Cooperation commitments to India in FY2023 of ¥827.797 billion (layout reading of a dense table).

## Synthesis

1. **The 2000s: a long fight with mild deflation, then a premature declaration of victory.**
   - In 2005 the IMF found "Mild deflation persists" with CPI −1.0 to 0.0 in 2002–04 and the deflator negative every year (JP-IMF-1 pp. 3,
     36); QE (from March 2001; `IMF_2000-2002.md`) should stay until deflation was gone (JP-IMF-1 p. 29).
   - The BOJ ended QE on 9 March 2006, judging its commitment "fulfilled" (JP-BOJ-1) and raised rates to 0.25% in July (JP-BOJ-2). The IMF
     said "deflation has ended" (JP-IMF-2 p. 29); the Cabinet Office said overcoming deflation was "now in sight" (JP-GOV-1 p. 18).
   - CPI was −1.4% in 2009 and −0.7% in 2010 (JP-IMF-6 p. 23).
2. **Bank clean-up was the decade's real achievement.** By 2005 major banks' balance-sheet problems were "largely resolved" (JP-IMF-1 p.
   29); by 2006 the "post-bubble adjustment" was "essentially complete" (JP-IMF-2 p. 3). India's Surveys later used Japan as the cautionary
   case of post-bubble stagnation and of crisis-time clean-ups (JP-IN-4 p. 87; JP-IN-7 p. 224).
3. **2008–09: an export shock, not a banking crisis.** The 2008 report expected 1.5% growth in 2009 and a "modest slowdown" (JP-IMF-4 pp. 3,
   30); outturn −6.3%, with exports −23.9% (JP-IMF-6 p. 23). The IMF: "The global recession has derailed Japan’s export-led boom" (JP-IMF-5
   p. 3).
4. **March 2011 halted recovery and showed Japan's place in supply chains.** Damage 3–5% of GDP, Kanto power shortages, car and electronics
   chains cut (JP-IMF-6 p. 3); India's Survey noted both the global drag and a possible gain for Indian electronics (JP-IN-2 pp. 159, 339).
   The yen peaked at 76.6 per dollar in October 2011 (JP-OTH-1).
5. **Abenomics was a regime change in monetary policy.** The January 2013 joint statement set a 2% target (JP-BOJ-3); QQE in April 2013
   doubled the base "with a time horizon of about two years" (JP-BOJ-4). The IMF welcomed "a unique opportunity" but warned all three
   arrows were needed (JP-IMF-8 PDF p. 2); by 2014 progress was "uneven" (JP-IMF-9 PDF p. 2), by 2016 it needed "a significant policy
   upgrade" (JP-IMF-10 PDF p. 7), and in 2017 there was still no "durable exit from deflation" (JP-IMF-11).
6. **The two-year target was missed badly.** The BOJ's April 2013 median for FY2015 core CPI (ex-tax) was 1.9%; the outturn was 0.0%
   (JP-BOJ-5). The IMF had 1.9–2.0% for 2015–18; actual CPI was 0.8 (2015) and 0.5 (2017) (JP-IMF-8 p. 37; JP-IMF-10 p. 4; JP-IMF-13 PDF
   p. 5). The BOJ's own 2024 review conceded the effect was smaller "than originally expected" (JP-BOJ-10 p. 5). Negative rates and YCC
   followed in 2016 (MO-CB-3); the 10-year yield touched −0.28% in 2019 (JP-OTH-1).
7. **Consumption tax: the IMF's constant prescription, the government's hardest step.** Recommended from 2005 onward (JP-IMF-1 p. 29;
   JP-IMF-4 p. 3; JP-IMF-6 PDF p. 2: 5 to 7–8%); raised to 8% in April 2014, with a pre-tax rush and 2014 growth of 0.0% against a
   projected 1.6% (JP-IMF-9 pp. 4–5, 38; JP-IMF-10 p. 4); delayed, then raised to 10% in October 2019 (JP-IMF-13 PDF p. 6; JP-GOV-5). The
   IMF wanted gradual steps to at least 15% (JP-IMF-10, JP-IMF-11). In 2026 a temporary cut on food was before the Diet (JP-BOJ-9).
8. **Debt: the projected explosion did not happen as a ratio, but the stock and the interest bill grew.** Old-basis gross debt rose from
   175% (2005) to about 249% (2014) and 263% (2021) (JP-IMF-2 p. 35; JP-IMF-10 p. 4; JP-IMF-14 PDF p. 4), close to the IMF's 2013 path of
   about 248% (JP-IMF-8 p. 37). Inflation then cut the ratio: 236.7% (2024, old basis; JP-IMF-17 p. 39), 206.8% (2025, new consolidated
   basis; JP-IMF-18 PDF p. 4; also DF-IMF-2). The MOF stresses rising rates: bonds ¥1,145 trillion and debt service 25.6% of the budget
   (JP-GOV-4 PDF pp. 4, 8, 21).
9. **Demography became the frame.** From 2018–19 the IMF centred its Japan work on ageing: the population will shrink by over 25% in 40
   years (JP-IMF-12; JP-IMF-13 p. 10); population peaked in 2010 and the 65+ share reached 30% in 2025 (JP-OTH-1); the working-age
   population has fallen since 1995, offset partly by more women and older workers (JP-IMF-18 p. 4).
10. **2022–26: inflation returned via the yen and import prices, and wages followed.** The IMF projected 1.0% for 2022 (JP-IMF-14) and found
    "levels not seen in four decades" a year later (JP-IMF-15). CPI 2.5, 3.2, 2.7, 3.2 in 2022–25 (JP-IMF-18 PDF p. 4). The yen fell to
    162 per dollar (July 2026; JP-OTH-1). Nominal wages rose "at a historic pace" but real wages fell 6% since 2022 (JP-IMF-18 PDF p. 5,
    p. 4).
11. **Normalisation since 2024 has been slow and deliberate.** Exit from negative rates and YCC on 19 March 2024 (MO-CB-3); 0.25% (July 2024),
    0.5% (January 2025), 0.75% (December 2025), 1.0% (June 2026), 1.25% (September 2026), held on 30 October 2026 with one vote for 1.5%
    (JP-BOJ-7 to JP-BOJ-9). The 10-year yield passed 3% in September 2026 (JP-OTH-1), and the BOJ is shrinking its JGB holdings and
    selling ETFs (JP-IMF-18 p. 9; JP-BOJ-9).
12. **For India, Japan is financier, technology partner and a structural deficit.** India holds Japan's largest bilateral swap line (US$ 75
    billion; JP-IMF-13 p. 100) and JICA's largest ODA-loan book (¥7.44 trillion in loans to FY2022; JP-IN-10 pp. 21, 37). Japan is a top-three
    FDI source (JP-IN-5 p. 124). The CEPA of 2011 (JP-IN-2 p. 176) has coincided with a widening deficit, from about US$ 3.1 billion
    (2009-10) to 12.7 billion (2024-25) (JP-IN-1; JP-IN-9; own arithmetic), and Survey studies find its export effect weak or negative
    (JP-IN-3 p. 128; TR-IN-1 p. 134). The bullet train, on 0.1% ODA, has slipped well past its 2023 start (JP-IN-3 p. 145; JP-IN-8). The
    Surveys draw a lesson from Japan's low-wage trap (JP-IN-7 p. 77).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| 2006 | IMF (JP-IMF-2 p. 29); BOJ (JP-BOJ-1) | "deflation has ended"; QE exit conditions "fulfilled" | CPI −1.4% in 2009, −0.7% in 2010 (JP-IMF-6 p. 23); IMF in 2009: inflation negative "through 2011" (JP-IMF-5 p. 3) |
| 2006 | Cabinet Office (JP-GOV-1 p. 18) | "Overcoming of deflation now in sight" | Cabinet Office 2026 still assessing whether deflation is overcome (JP-GOV-3 PDF p. 6) |
| 2008 | IMF (JP-IMF-4 pp. 3, 30) | "modest slowdown"; 2009 GDP +1.5%, exports +4.6% | 2009 GDP −6.3%, exports −23.9% (JP-IMF-6 p. 23) |
| 2011 | IMF (JP-IMF-6 PDF p. 2) | 2012 GDP +2.9% after the quake | 2012 GDP +1.7% (JP-IMF-10 p. 4) |
| Apr 2013 | BOJ (JP-BOJ-4; JP-BOJ-5 Appendix) | 2% "with a time horizon of about two years"; FY2015 core CPI 1.9% (ex-tax) | FY2015 core CPI 0.0% (JP-BOJ-5, April 2016); BOJ review: effect smaller "than originally expected" (JP-BOJ-10 p. 5) |
| 2013 | IMF (JP-IMF-8 p. 37) | CPI 1.9% (2015), 2.0% (2017); gross debt 248.3% in 2018 | CPI 0.8% (2015), 0.5% (2017); debt 237.9% in 2018 (JP-IMF-10 p. 4; JP-IMF-13 PDF p. 5) |
| 2014 | IMF (JP-IMF-9 p. 38) | 2014 GDP +1.6% despite the April tax rise | 2014 GDP 0.0% (JP-IMF-10 p. 4) |
| 2022 | IMF (JP-IMF-14 PDF p. 4) | CPI 1.0% (2022), 0.8% (2023) | 2.5% and 3.2% (JP-IMF-17 p. 39) |
| 2025 | IMF (JP-IMF-17 PDF p. 6, p. 39) | Inflation back to 2% from above in late 2025; 2025 CPI 2.4%; debt to rise from 2030 | 2025 CPI 3.2%; debt now seen rising only from 2035, on a new definition (JP-IMF-18 PDF pp. 4–5, p. 9) |
| Mar 2024 | BOJ (MO-CB-3) | Accommodative conditions "for the time being" | Five rises to 1.25% by Sep 2026; 10-yr yield above 3% (JP-BOJ-7–9; JP-OTH-1) |
| 2010 | India: ES 2010-11 (JP-IN-1 p. 229) | JBIC survey: India second most promising destination for Japanese firms | Japan among top three FDI sources (JP-IN-5 p. 124); the 2022 ¥5 trillion five-year goal's outturn not obtained (JP-IN-10 p. 22) |
| 2012 | India: ES 2011-12 (JP-IN-2 p. 176) | CEPA covers over 90% of trade; first with a developed country | Deficit with Japan up from about $3.1 bn (2009-10) to $12.7 bn (2024-25) (JP-IN-1; JP-IN-9; own arithmetic); Japan FTA export effect negative (JP-IN-3 p. 128; TR-IN-1) |
| 2016 | India: ES 2015-16 (JP-IN-3 p. 145) | MAHSR in about seven years; 35 trains a day each way by 2023; cost about ₹97,636 crore | 47.17% progress Oct 2024, cost revised to ₹1.08 lakh crore (ES 2024-25 p. 167); over 55% by Oct 2025 (ES 2025-26 p. 351) |
| 2021 | India: ES 2020-21 (JP-IN-7 p. 77) | Avoid Japan's "low wage-growth trap" | Japan's nominal wages now rising "at a historic pace", though real wages fell 6% since 2022 (JP-IMF-18 PDF p. 5, p. 4) |

### Candidate quotes (all verified by script against the converted text)

- "Mild deflation persists." (IMF 2005, JP-IMF-1 p. 3)
- "the priority remains conquering deflation" (JP-IMF-1 p. 28)
- "it would be preferable to err on the side of being accommodative" (JP-IMF-1 p. 29)
- "the debt ratio on an unsustainable path" (JP-IMF-1 p. 3)
- "The post-bubble adjustment is essentially complete." (IMF 2006, JP-IMF-2 p. 3)
- "Japan’s post-bubble legacies have essentially been resolved and deflation has ended." (JP-IMF-2 p. 29)
- "the Bank of Japan has opted for a very gradual pace of tightening" (IMF 2007, JP-IMF-3 p. 3)
- "Japan appears headed for a modest slowdown" (IMF 2008, JP-IMF-4 p. 3)
- "this opportunity to raise the consumption tax rate should be seized" (JP-IMF-4 p. 3)
- "The global recession has derailed Japan’s export-led boom." (IMF 2009, JP-IMF-5 p. 3)
- "The result has been the most severe recession in decades." (JP-IMF-5 p. 3)
- "inflation is projected to remain negative through 2011" (JP-IMF-5 p. 3)
- "brought Japan’s nascent recovery to a halt" (IMF 2011, JP-IMF-6 p. 3)
- "a moderate increase in the consumption tax, from 5 percent to 7–8 percent" (JP-IMF-6 PDF p. 2)
- "A fiscal adjustment of 10 percent of GDP over the next decade is necessary" (IMF 2012, JP-IMF-7 PDF p. 2)
- "a unique opportunity to end decades-long deflation and sluggish growth" (IMF 2013, JP-IMF-8 PDF p. 2)
- "all three arrows need to be launched for the policies to succeed" (JP-IMF-8 PDF p. 2; also p. 25)
- "Abenomics is gaining traction, but progress across the three arrows has been uneven" (IMF 2014, JP-IMF-9 PDF p. 2)
- "Abenomics needs a significant policy upgrade to regain traction." (IMF 2016, JP-IMF-10 PDF p. 7)
- "remain out of reach under current policies" (JP-IMF-10 PDF p. 7)
- "has not yet achieved a durable exit from deflation" (IMF 2017, JP-IMF-11 PDF p. 7)
- "will dominate economic policy making in coming decades" (IMF 2018, JP-IMF-12 PDF p. 6)
- "The rapid aging and shrinking of Japan’s population has become central to macroeconomic policies" (IMF 2019, JP-IMF-13 PDF p. 6)
- "the total population will shrink by over 25 percent" (JP-IMF-13 p. 10)
- "the arrangement with India is by far the largest size (US$ 75 billion)" (JP-IMF-13 p. 100)
- "fell short on the deep reforms needed to raise productivity" (IMF 2022, JP-IMF-14 PDF p. 5)
- "Headline inflation has recorded levels not seen in four decades." (IMF 2023, JP-IMF-15 PDF p. 5)
- "more flexibility in longer term yields is warranted" (JP-IMF-15 PDF p. 5)
- "further hikes in the short-term policy rate should proceed at a gradual pace" (IMF 2024, JP-IMF-16 PDF p. 6)
- "After three decades of near-zero inflation, signs are growing" (IMF 2025, JP-IMF-17 PDF p. 6)
- "nominal wages are rising at a historic pace" (IMF 2026, JP-IMF-18 PDF p. 5)
- "a 6-percent fall in real wages since 2022" (JP-IMF-18 p. 4)
- "Monetary policy accommodation is appropriately being withdrawn" (JP-IMF-18 PDF p. 5)
- "The Bank, therefore, judged that the conditions laid out in the commitment are fulfilled." (BOJ, 9 Mar 2006, JP-BOJ-1)
- "an approximate range between zero and two percent" (BOJ, 9 Mar 2006, JP-BOJ-1)
- "the Bank sets the price stability target at 2 percent" (joint statement, 22 Jan 2013, JP-BOJ-3 p. 1)
- "with a time horizon of about two years" (BOJ, 4 Apr 2013, JP-BOJ-4 p. 1)
- "It will double the monetary base" (JP-BOJ-4 p. 1)
- "likely to achieve around 2 percent inflation during fiscal 2017" (BOJ Outlook, Apr 2016, JP-BOJ-5 PDF p. 9)
- "Real interest rates are expected to remain significantly negative" (BOJ, 31 Jul 2024, JP-BOJ-7)
- "encourage the uncollateralized overnight call rate to remain at around 1.25 percent" (BOJ, 18 Sep 2026, JP-BOJ-9 p. 1)
- "the situation had shifted to a new phase" (Takata dissent, 30 Oct 2026, JP-BOJ-9 p. 2)
- "did not have as large an upward effect on prices as originally expected" (BOJ review, JP-BOJ-10 p. 5)
- "the overall effect on the Japanese economy so far appears to have been positive" (JP-BOJ-10 p. 5)
- "Overcoming of deflation now in sight" (Cabinet Office 2006, JP-GOV-1 p. 18)
- "we are now close to breaking out of the deflationary trend" (JP-GOV-1 p. 18)
- "What is critical to end deflation is to raise the expected rate of inflation." (Cabinet Office 2013, JP-GOV-2 p. 7)
- "Japan has the highest level debt-to-GDP ratio in the world." (MOF 2026, JP-GOV-4 PDF p. 21)
- "It is projected to reach 1,145 trillion yen at the end of FY2026." (JP-GOV-4 PDF p. 8)
- "India has the largest scale of ODA loan projects among all JICA projects" (JICA, JP-IN-10 p. 37)
- "a total investment of 5 trillion yen in India over the next five years" (JP-IN-10 p. 22)
- "first with a developed country" (ES 2011-12, JP-IN-2 p. 176)
- "for 50 years with 0.1 per cent interest and a 15-year moratorium" (ES 2015-16, JP-IN-3 p. 145)
- "Thirty-five trains per day each way will operate by 2023" (JP-IN-3 p. 145)
- "the Japan FTA has had a significantly negative effect on exports" (ES 2015-16, JP-IN-3 p. 128)
- "has a revised cost of ₹1.08 lakh crore" (ES 2024-25, JP-IN-8 p. 167)
- "progress has been achieved as on October 2025, with land acquisition completed" (ES 2025-26, JP-IN-8 p. 351)
- "a low wage-growth trap, as has happened in Japan during the last two decades" (ES 2020-21, JP-IN-7 p. 77)
- "Japan had 15 of the top 25 largest banks then" (ES 2019-20, JP-IN-6 p. 153)
- "The Tsunami in Japan which led to disruption of supply chains in Japan" (ES 2011-12, JP-IN-2 p. 159)
- "Mauritius, Singapore and Japan have been top three countries" (ES 2017-18, JP-IN-5 p. 124)
- "rank India as the second most promising country for overseas business operations" (ES 2010-11, JP-IN-1 p. 229)
- "as occurred in the U.S. and Europe after the Global Financial Crisis and Japan" (ES 2016-17, JP-IN-4 p. 87)

Short phrases quoted inside the item notes but not run through the script ("effectively zero", "milestones", "a crucial step",
"moderately overvalued", "uneven", "critical", "in or around fiscal year 2015", "gradual albeit limited", "currently 0.75 percent",
"significantly higher", "give time to time", "to some extent", "is unlikely to return", "in the 1% range", "more equitable and supportive of
growth", "a commitment to raise the consumption tax", "toward the latter half of the projection period", "at the earliest possible time")
were read in the source but should be rechecked before they are printed as quotations.

## Not obtained

- **IMF listing.** https://www.imf.org/en/Countries/JPN (200) and its index.md/index.json list only the 2025 and 2026 Article IVs ("See All
  Documents" is a dynamic section not present in the fetched page). All earlier reports are GUESSED URLs (title pages confirmed).
- **IMF 2003 Article IV**: https://www.imf.org/external/pubs/ft/scr/2003/cr03275.pdf (GUESSED; 200; 56 pages) is image-only, with no text
  layer, and no OCR tool was available, so it is not read or cited (the title page could not be confirmed either). cr03274.pdf (GUESSED; 200)
  also has no text layer.
- **IMF 2004 Article IV**: GUESSED cr04245 (Sweden Selected Issues), cr04246 (Bhutan PRSP), cr04247 (Japan: Selected Issues) — none is the
  2004 Japan staff report; not pursued further.
- **IMF 2010, 2015, 2020 and 2021 Article IVs**: not attempted, except …/2021/english/1jpnea2021001.pdf (GUESSED) — 404. Also 404:
  …/scr/2017/cr17242.pdf (old path) and …/2019/english/1jpnea2019001.pdf. Discarded wrong hits: cr08247 (Lithuania), cr08248 (Cape Verde),
  1jpnea2024001–009 (Japan FSAP papers, CR 24/109–24/117).
- **OECD Economic Survey of Japan**: https://www.oecd.org/en/countries/japan.html, …/publications/serials/oecd-economic-surveys-japan_g1gh91c5.html
  and …/topics/sub-issues/economic-surveys/japan-economic-snapshot.html — all 403. Not pursued.
- **Prime Minister's Office (Abenomics, 2013 growth strategy "Japan Revitalization Strategy")**: https://japan.kantei.go.jp/,
  …/index.html, …/96_abe/index.html, https://www.kantei.go.jp/foreign/index-e.html and https://www.kantei.go.jp/jp/singi/keizaisaisei/pdf/
  en_saikou_jpn_hon.pdf (GUESSED) — all 404; https://www.japan.go.jp/abenomics/index.html — 404. The arrows are described from the IMF
  (JP-IMF-8, JP-IMF-9) instead.
- **Cabinet Office English top page** https://www.cao.go.jp/en/ — 403 (the www5.cao.go.jp white-paper pages worked).
- **MOFA Japan–India pages**: https://www.mofa.go.jp/region/asia-paci/india/index.html and …/data.html — 403.
- **MEA India–Japan bilateral brief**: https://www.mea.gov.in/Portal/ForeignRelation/Japan_Bilateral_Brief.pdf (GUESSED) — HTTP 200 but a
  "404 | Page Not Found" HTML page; https://www.mea.gov.in/foreign-relations.htm (200) carried no Japan link in the fetched HTML.
- **JICA ODA-loan project database** (www2.jica.go.jp yen_loan search) — linked but not fetched. commerce.gov.in and PIB — not attempted
  this round (the euro-area lens found commerce.gov.in a script shell and PIB showing only current releases).
- **India–Japan currency swap of 2008 and later renewals**: not found in any Economic Survey (grep for "swap" with Japan returned nothing);
  the only source is the IMF 2019 annex (JP-IMF-13 pp. 100–101, US$ 75 billion, February 2019). The 2008 swap amount is not obtained.
- **Outturns not obtained**: progress against the 2022 ¥5 trillion five-year investment goal (JP-IN-10 p. 22); MAHSR completion date; FDI
  from Japan by year (no Survey series found beyond the ES 2017-18 sentence; none in `data/clean/india`).
- **Fetched but not read**: BOJ k130122a.pdf (22 January 2013 price-stability-target release); Cabinet Office 2019 summary
  (setsumei-e2019.pdf); the BOJ review beyond pp. 4–5; IMF 2026 Staff Appraisal (p. 30); IMF 2018 report beyond Key Issues.
- **Abenomics' second and third arrows** (fiscal packages, the growth strategy, TPP entry) are covered only through the IMF's
  assessments; no Japanese government primary source on them was obtained.
