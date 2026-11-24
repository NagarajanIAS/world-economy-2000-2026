# Reading notes: country lens "China, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers, no cookies). URLs were taken from publisher
listing or issue pages where possible (the imf.org CHN country page and its 2025 Article IV issue page; the NBS English "Latest Releases" and
"Statistical Communiqués" listing pages; the PBC English annual-report listing; the WTO China accession page; the USTR Phase One page; the
World Bank China country page; the World Bank documents API). Every guessed URL is flagged GUESSED. As for the US lens (`Lens_us.md`), the
IMF country page links only the latest Article IV (CR 26/44), so the 2004–2023 staff reports come from GUESSED URLs built on the IMF's
file-naming pattern (`/external/pubs/ft/scr/YYYY/crYYNNN.pdf` to 2016; `/-/media/files/publications/cr/YYYY/[english/]1chneaYYYYnnn.pdf`
from 2019); each file's title page and "Country Report No." were read to confirm it is the China Article IV of the year named (two guesses
returned other China papers and are noted). Downloads are in the session scratchpad folder `lens_china_dl/` (subfolders `imf/`, `imf/g/`,
`imf/g2/`, `imf/g3/`, `off/`–`off4/`, `pbc/`, `gov/`–`gov4/`, `oth/`, `ustr/`, `wb/`, `wb2/`, `in/`, one new folder per batch). PDFs were
converted with `pdftotext` (plain and `-layout`); HTML pages were stripped of tags and read as text. Python that read downloads was run with
`python3 -I`, with scripts kept outside the download folders. Economic Survey texts were not refetched: they were read from the Econ Subject
folder (`sources/text/es*.txt`; text page = PDF page) and the printed page number was taken from the running header or footer. Quotes are
verbatim, under 15 words, and were checked by a script against the converted text; everything else is paraphrase. Page numbers are printed
page numbers unless stated ("PDF p." where only the PDF page could be given, e.g. unnumbered Key Issues and press-release pages). BIS credit
ratios (CN-OTH-4) and the India–China deficit for 2024-25 are my own reading/arithmetic of data already held and are marked "own reading".

Item labels: CN-IMF-n (IMF Article IV consultations with China), CN-OFF-n (Chinese official sources: NBS, PBC), CN-OTH-n (WTO, USTR, World
Bank, BIS data held by the book), CN-IN-n (India–China: Economic Surveys). Indian years are fiscal (April–March) or survey years. Abbreviations:
CA = current account; CR = IMF Country Report; LGFV = local government financing vehicle; TSF = total social financing; REER = real effective
exchange rate; FYP = Five-Year Plan; PLI = Production Linked Incentive; API = active pharmaceutical ingredient; PN3 = Press Note 3 (2020).

Already in the book (cite, do not duplicate):
- `IMF_2003-2006.md`: WEO Table 1.1 China growth 2002–2005; WEO Apr 2005 China investment "unsustainably high"; WEO Sep 2005 Ch. 1 p. 3 on the
  21 July 2005 reform (2.1 percent revaluation, basket reference, narrow band).
- `IMF_2014-2019.md`: WEO Oct 2015/Apr 2016 on China's slowdown and the 2015–16 turmoil (renminbi down about 4 percent after the August 2015
  change); WEO Oct 2019 Box (US–China tariffs, China output −2 percent); USTR Section 301 releases of 15 Jun and 18 Sep 2018 ($34 bn at 25
  percent; $200 bn at 10 then 25 percent).
- `IMF_2024-2025.md` and `IMF_2026.md`: WEO China forecast trail 2024–26 (property downturn "never resolve themselves quickly"; China 5.0 percent
  in 2025, 4.4–4.6 percent for 2026; record $1.2 trillion goods surplus in 2025; the October 2025 truce to November 2026).
- `Theme_trade.md`: TR-IMF-1 (China rebalancing and trade; Autor–Dorn–Hanson), TR-IMF-4 (2025 tariff chronology: US 115 percent / China 146
  percent at the peak), TR-WTO-3 (US imports from China −29 percent in 2025; China 14.4 percent of world goods exports), TR-IN-1 (ES 2019-20
  "Assemble in India": China's labour-intensive export model, 12.8 percent world share). Its "Not obtained" note on China's WTO accession is
  now answered by CN-OTH-1.
- `Theme_debt.md`: DF-IMF-2 (Fiscal Monitor Apr 2026: China general government debt 59.8 / 99.2 / 126.8 percent of GDP in 2019 / 2025 / 2031;
  deficit 7.9 percent in 2025); the World Bank IDR items on China's external debt.
- `Theme_growth.md`: GR-IMF-2 (China and the commodity upswing), GR-WB-2 p. 26 (China's slower capital accumulation), GR-IN items on China
  "too rich given its weak democratic institutions" and potential-growth scenarios.
- `Theme_demography.md`: DL-OTH-7 (NBS 19 Jan 2026: end-2025 population 1,404.89 million, −3.39 million; births 7.92 million), DL-OTH-1
  (WPP 2024: China −204 million by 2054), DL-OTH-3 (UNFPA 2023: India passes China).
- `Lens_us.md`: US-OTH-2 (ERP 2026: goods imports from China −26.7 percent Jan–Oct 2025), US-OTH-5/-6/-8/-9 (2025–26 US tariff instruments
  covering China), US-IMF-7 and US-IMF-9 (IMF on the US–China tariffs), US-IN-1 (ES 2008-09: China became India's largest trading partner),
  US-IN-4 (ES 2018-19/2019-20: deficit with China US$53.57 bn in 2018-19), US-IN-5 (ES 2023-24: US second-largest partner after China).
- `India_ES_2003-2008.md` ES05-10 (ES 2005-06 Box 6.1 on China's exchange-rate reform), `India_ES_2015-2020.md` ES15-2, ES15-16, ES16-7 (the
  2015 "China scare" and the August 2015 devaluation in the Surveys), `India_ES_2001-2003.md` ES02-17 (China as a new WTO member).

---

## IMF Article IV consultations with China

### CN-IMF-1. IMF, *People's Republic of China: 2004 Article IV Consultation—Staff Report; Staff Statement; and Public Information Notice on the Executive Board Discussion*, IMF Country Report No. 04/351, November 2004
PDF: https://www.imf.org/external/pubs/ft/scr/2004/cr04351.pdf (GUESSED; 200; 72 PDF pages; printed = PDF − 2). Read: Executive Summary
(p. 3), paras 1–3 (p. 4), paras 18–21 (pp. 12–13), Staff Appraisal (pp. 23–24).
- p. 3: GDP grew at a 10 percent annual rate in 2003Q4 and about the same in 2004Q1, led by investment; CPI inflation 4.4 percent in May 2004;
  money and credit growth still 18–19 percent. Local-government projects were a major source of the investment surge; the aim was a "soft
  landing". The authorities agreed "in principle" on more exchange-rate flexibility but feared the employment effect of appreciation.
- p. 4: fixed capital formation rose about 20 percent in real terms in 2003 to 44 percent of GDP; a footnote notes speculation that official
  statistics understate growth (expenditure-side nominal GDP grew 2 points faster).
- p. 12 (para 19): staff saw greater flexibility as best done by widening the band, perhaps with a basket, but "it is difficult to find
  persuasive evidence that the renminbi is substantially undervalued". Footnote 6: estimates of undervaluation by academics and analysts
  range from 0 to 35 percent. p. 13 (para 21): the authorities said China needs 20–25 million new jobs a year.
- pp. 23–24 (appraisal): favourable medium-term prospects; the main near-term risk is failing to secure a soft landing; further monetary
  tightening needed; a move to flexibility "should not be unduly delayed"; medium-term fiscal consolidation of ¼–½ percent of GDP a year, with
  contingent liabilities from bank NPLs, pensions and local governments.

### CN-IMF-2. IMF, *People's Republic of China: 2005 Article IV Consultation—Staff Report; Staff Supplement; and Public Information Notice*, IMF Country Report No. 05/411, November 2005 (discussions ended 25 May 2005)
PDF: https://www.imf.org/external/pubs/ft/scr/2005/cr05411.pdf (GUESSED; 200; 77 PDF pages; printed = PDF − 3). Read: Executive Summary
(p. 3), Background (p. 4), Exchange Rate Regime paras 21–24 (pp. 14–15), Staff Appraisal (pp. 26–27), Annex VI (staff supplement, p. 68).
- p. 3: GDP grew 9.5 percent in 2004; the CA surplus rose to 4¼ percent of GDP; reserves nearly $700 billion at end-May 2005.
- p. 4: reserve accumulation was seen abroad as pointing to undervaluation; the end of MFA textile quotas in December 2004 sparked protectionist
  pressure.
- p. 14 (para 21): the continued external strengthening "points to" "increased undervaluation of the renminbi, adding to the urgency of making
  a move"; delay risks reserve build-up, sterilisation problems and misallocated investment.
- p. 15 (para 23): the authorities saw "no convincing evidence pointing to the undervaluation of the renminbi" and said resolving global
  imbalances needed credible US fiscal action first. Footnote 8: Premier Wen (26 June 2005) on a market-based managed float.
- p. 68 (Annex VI, staff supplement): on 21 July the PBC revalued about 2 percent (RMB 8.28 to 8.11 per US$) and moved to reference a basket
  (weights unpublished); daily band ±0.3 percent against the dollar, ±1.5 percent against other currencies; RMB 8.1046 on 1 August. Staff
  welcomed it and urged use of the flexibility. (The PBC's own 2005 announcement was not obtained; see Not obtained.)

### CN-IMF-3. IMF, *People's Republic of China: 2006 Article IV Consultation—Staff Report; Staff Statement; and Public Information Notice*, IMF Country Report No. 06/394, October 2006
PDF: https://www.imf.org/external/pubs/ft/scr/2006/cr06394.pdf (GUESSED; 200; 74 PDF pages; printed = PDF − 2). Read: Executive Summary (p. 3).
- p. 3: growth nearly 10 percent in 2005 (revised data) and 10¼ percent in 2006Q1; the CA surplus rose to more than 7 percent of GDP in 2005;
  reserves $925 billion at end-May 2006. The economy needs to be "rebalanced away from heavy dependence on export-led growth toward
  self-sustaining domestic demand". Staff urged more exchange-rate flexibility; the authorities stressed a "gradual and controlled" reform.
  Social spending (education, health, pensions) to reduce precautionary saving.
- Note: no Article IV staff report for 2007, 2008 or 2009 was found; the next found is 2010 (CN-IMF-4), whose staff report notes the PBC
  re-pegged to the dollar in July 2008. No 2007–09 China report was guessed (no report numbers known from a listing). See Not obtained.

### CN-IMF-4. IMF, *People's Republic of China: 2010 Article IV Consultation—Staff Report; Staff Statement; Public Information Notice*, IMF Country Report No. 10/238, July 2010 (Board 26 July 2010)
PDF: https://www.imf.org/external/pubs/ft/scr/2010/cr10238.pdf (GUESSED; 200; 64 PDF pages; printed = PDF − 1). Read: Executive Summary (p. 3),
paras 1–6 (pp. 4–8), Section C on local government (p. 15), CA prospects and Box 4 (pp. 16–17), tables (pp. 33, 36), Staff Appraisal (pp. 25–26).
- p. 3: "A strong fiscal response and an expansionary monetary policy have ensured that China has led the global recovery"; the agenda
  includes enforcing the ban on local-government debt guarantees, more transparency on LGFVs, a property tax, and allowing real appreciation.
- p. 4: the crisis response had three strands: a major fiscal stimulus concentrated on infrastructure (2–3 percent of GDP for social spending
  and consumption incentives); "An extraordinary credit expansion." (new bank loans of 31 percent of GDP in 2009); and re-pegging the renminbi
  to the dollar in July 2008, after appreciation of up to about 1 percent a month since July 2005. Growth averaged 9.1 percent in 2009,
  around half attributed to public spending.
- p. 8: M2 growth to be cut from 28 percent (end-2009) to 17 percent (end-2010); 2010 budget deficit target 3 percent of GDP; much support
  also came through LGFV and SOE capital spending.
- p. 15 (paras 16–18): despite legal bans, local governments borrowed through corporate vehicles with implicit or explicit guarantees,
  and in 2008–09 "significantly increased" their use; information is sparse; some lending will become NPLs.
- pp. 16–17 and Box 4: the CA surplus had almost halved since 2007; staff models (BVAR, GIMF) had it rising back to about 8–9 percent of GDP;
  the authorities expected about 4 percent. Table (p. 33): CA 2.8, 3.6, 7.1, 9.3, 10.6, 9.6, 6.0 percent of GDP in 2003–2009. Table 6 (p. 36):
  real GDP 12.7 (2006), 14.2 (2007), 9.6 (2008), 9.1 (2009) (revised data); CA projected to rise to 8.0 percent of GDP by 2015.
- pp. 25–26 (appraisal): the response was "proactive, speedy, and resolute"; the June 2010 return to a managed float is "extremely welcome";
  nationally property prices are probably not yet significantly above fundamentals, but in larger cities "a property bubble is beginning to
  inflate", with a crash a known risk.

### CN-IMF-5. IMF, *People's Republic of China: 2013 Article IV Consultation*, IMF Country Report No. 13/211, July 2013 (staff report dated 27 June 2013)
PDF: https://www.imf.org/external/pubs/ft/scr/2013/cr13211.pdf (GUESSED; 200; 93 PDF pages; printed = PDF − 1). Read: Key Issues (PDF p. 2),
paras 1–11 (pp. 4–12), Box 1 (p. 13).
- Key Issues (PDF p. 2): growth of 7¾ percent expected in 2013; since the crisis, investment, credit and fiscal stimulus underpinned activity:
  "This pattern of growth is not sustainable and is raising vulnerabilities." Buffers remain but "the margins of safety are diminishing". The
  "renminbi which staff assess as moderately undervalued" should adjust with less intervention.
- p. 6: the CA surplus edged up to 2¼ percent of GDP in 2012; a small net capital outflow in 2012.
- p. 9: external rebalancing has progressed (well below the 2007 peak of 10 percent); in the staff baseline the CA surplus rises to about 4
  percent of GDP by 2018, or about 1 percent with good rebalancing. The authorities "strongly disagreed" with the 4 percent baseline.
- p. 10: the stock of TSF rose by 60 percent of GDP in four years after 2009; WMPs and trust products could become a systemic threat.
- p. 12 and Box 1 (p. 13): counting LGFVs and off-budget funds, "augmented" government debt was 45 percent of GDP in 2012 and the augmented
  deficit about 10 percent of GDP; fiscal space is much smaller than headline data show. Real estate prone to bubbles (near-zero real deposit
  rates, capital controls, local reliance on land sales).

### CN-IMF-6. IMF, *People's Republic of China: 2014 Article IV Consultation—Staff Report; Press Release; and Statement by the Executive Director*, IMF Country Report No. 14/235, July 2014 (staff report dated 8 July 2014)
PDF: https://www.imf.org/external/pubs/ft/scr/2014/cr14235.pdf (GUESSED; 200; 115 PDF pages). Read: Key Issues (PDF p. 2) and contents.
- Key Issues: growth 7.7 percent in 2013, about 7½ percent expected in 2014, declining further; since the crisis growth "relied too much on
  investment and credit"; credit and "shadow banking", local-government finances and real estate are the interlinked vulnerabilities. "the
  risk of a hard landing is still considered low" in the near term, but "medium-likely" over the medium term without change. Annexes give a
  revised augmented-debt estimate and ask whether LGFVs are government units.

### CN-IMF-7. IMF, *The People's Republic of China: 2016 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 16/270, August 2016 (staff report dated 7 July 2016)
PDF: https://www.imf.org/external/pubs/ft/scr/2016/cr16270.pdf (GUESSED; 200; 98 PDF pages; printed = PDF − 4). Read: press release (PDF p. 2),
Key Issues (PDF p. 7), paras 1–5 (pp. 7–13), Staff Appraisal (p. 33).
- PDF p. 2: large capital outflows in 2015, mainly external debt repayment; the renminbi "broadly in line with fundamentals".
- Key Issues: rebalancing progressed (industry to services, investment to consumption) but not on credit; "Vulnerabilities are still rising
  on a dangerous trajectory"; buffers eroding. Priority: a comprehensive plan for the corporate debt problem, hard budget constraints on SOEs.
- p. 7: the REER rose close to 10 percent from mid-2014 to mid-2015 on the dollar link and fell 4½ percent after; the August 2015
  market-based fixing and the December 2015 basket reference increased flexibility.
- p. 11 (chart, BIS source): corporate credit high against peers; industrial profits fell in 2015 for the first time since the late 1990s.
- p. 13: outflows in 2015–early 2016 exceeded the CA surplus and cut reserves; expectations of depreciation were "seemingly reinforced by the
  August 2015 change". Baseline: growth about 6 percent by 2018, credit/GDP still rising, rising risk of disruptive adjustment.
- p. 33: growth 6.6 percent expected in 2016, 6.2 percent in 2017.

### CN-IMF-8. IMF, *People's Republic of China: 2017 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 17/247, August 2017 (staff report dated 13 July 2017)
PDF: https://www.imf.org/-/media/files/publications/cr/2017/cr17247.pdf (GUESSED; 200; 92 PDF pages; printed = PDF − 4). Read: Key Issues (PDF
p. 5), p. 10, para 28 (p. 19).
- Key Issues: strong growth "at the cost of further large and continuous increases in private and public debt".
- p. 10: total non-financial sector debt about 235 percent of GDP in 2016, projected to "rise further to over 290 percent of GDP by 2022".
- p. 19 (para 28): private lending rose 16 percent in 2016, twice nominal GDP growth, "pushing the credit gap to about 25 percent of GDP"; private
  debt up 80 points since 2008 to about 175 percent of GDP. The renminbi "broadly in line"; external position moderately stronger.

### CN-IMF-9. IMF, *People's Republic of China: 2019 Article IV Consultation—Press Release; Staff Report; Staff Statement and Statement by the Executive Director for China*, IMF Country Report No. 19/266, August 2019 (staff report dated 12 July 2019)
PDF: https://www.imf.org/-/media/files/publications/cr/2019/1chnea2019003.pdf (GUESSED; 200; 118 PDF pages). Read: press release (PDF p. 2),
Key Issues (PDF p. 6). (The GUESSED ...2019001.pdf and ...2019002.pdf, both 200, are the AML/CFT assessment CR 19/172 and ROSC CR 19/173.)
- PDF p. 2: growth projected to moderate to 6.2 percent in 2019, stimulus partly offsetting the US tariff hike on US$200 billion of imports;
  the CA surplus fell "to 0.4 percent of GDP in 2018", projected 0.5 percent in 2019; external position broadly in line.
- Key Issues (PDF p. 6): deleveraging and less bank–nonbank interconnectedness contained risks; if trade tensions escalate, more (mainly
  fiscal) stimulus; work with partners on trading-system shortcomings.

### CN-IMF-10. IMF, *People's Republic of China: 2021 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 22/21, January 2022 (Board 14 January 2022; staff report dated 20 December 2021)
PDF: https://www.imf.org/-/media/files/publications/cr/2022/english/1chnea2022001.pdf (GUESSED; 200; 134 PDF pages; printed = PDF − 5). Read:
Key Issues (PDF p. 6), paras 9–11 (p. 9).
- Key Issues: recovery advanced but unbalanced: rapid fiscal withdrawal, lagging consumption under recurrent COVID outbreaks, slowing real
  estate investment after deleveraging policy; tech-sector regulation raised uncertainty; productivity growth declining as "decoupling
  pressures are increasing".
- p. 9 (para 11): after years of unsuccessful attempts, the authorities in August 2020 began "imposing stringent benchmarks (the “three red
  lines”)" on developers' borrowing, plus bank lending concentration rules; this triggered financial stress among developers (Evergrande's
  restructuring talks are in a box, PDF p. 41). (No official Chinese text of the "three red lines" was found; see Not obtained.)

### CN-IMF-11. IMF, *People's Republic of China: 2022 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 23/67, February 2023 (Board 12 January 2023; staff report dated 19 December 2022)
PDF: https://www.imf.org/-/media/files/publications/cr/2023/english/1chnea2023001.pdf (GUESSED; 200; 134 PDF pages; printed = PDF − 4). Read:
press release (PDF p. 2), Key Issues (PDF p. 5), outlook (pp. 11–12).
- PDF p. 2: real estate investment contracted about one-fifth in Jan–Nov 2022; growth 2.6 percent in 2022, "improving to 4.2 percent in 2023"
  (footnoted update) after COVID measures lift. Staff report p. 11: 3.8 percent in 2023 and 5.5 percent in 2024, with unusual uncertainty.
- Key Issues: "the real estate crisis remains unresolved"; end it by funding completion of troubled projects; shift support to households.
- p. 12: end-period core inflation expected to rise from 0.4 percent (2022) to 2.0 (2023) and 2.3 (2024); CA surplus to fall to 1.4 percent.

### CN-IMF-12. IMF, *People's Republic of China: 2023 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 24/38, February 2024 (Board 10 January 2024; staff report dated 19 December 2023)
PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1chnea2024001.pdf (GUESSED; 200; 137 PDF pages; printed = PDF − 4). Read:
press release (PDF p. 2), Key Issues (PDF p. 5). (GUESSED ...2024002.pdf, 200, is the Selected Issues CR 24/50; ...2024003–006.pdf 404. The
2024 Article IV report, published later in 2024, was not found by guessing.)
- PDF p. 2: growth to slow to 4.6 percent in 2024 and about 3½ percent by 2028 (weak productivity, ageing); inflation "expected to increase
  gradually to 1.3 percent in 2024".
- Key Issues: excessive investment in infrastructure and housing raised debt of developers, local governments and LGFVs; the authorities'
  containment of developer leverage contributed to "a significant, but needed, adjustment in the property market"; restructure nonviable
  developers and unsustainable LGFVs (insolvency frameworks, central-government-led).

### CN-IMF-13. IMF, *People's Republic of China: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director for the People's Republic of China*, IMF Country Report No. 26/44, February 2026 (Board 13 February 2026; mission ended 10 December 2025; staff report dated 28 January 2026)
Listing: country page https://www.imf.org/en/Countries/CHN (200) → issue page
https://www.imf.org/en/publications/cr/issues/2026/02/17/peoples-republic-of-china-2025-article-iv-consultation-press-release-staff-report-and-574028
(200) → PDF https://www.imf.org/-/media/files/publications/cr/2026/english/1chnea2026001-source-pdf.pdf (200; 121 PDF pages; staff report
printed = PDF − 5). Also on the country page: mission-end press release PR 25/415, 10 Dec 2025
(https://www.imf.org/en/news/articles/2025/12/10/pr-25415-china-imf-staff-completes-2025-article-iv-mission-to-the-peoples-republic-of-china,
200, downloaded, not read; the CR supersedes it). Read: PR 26/053 (PDF pp. 2–3), Selected Economic Indicators (p. 4), Key Issues (PDF p. 6),
paras 1–6 (pp. 5–7), external sector (p. 10), para 26 (p. 18), Staff Appraisal (pp. 42–44), external assessment annex (p. 71).
- PR (PDF p. 2): "The Chinese economy has remained remarkably resilient despite facing multiple shocks"; GDP 5 percent in 2025, meeting the
  target; headline inflation averaged 0 percent and the GDP deflator fell again; real depreciation lifted the CA to an estimated 3.3 percent
  of GDP; growth projected at 4.5 percent in 2026.
- p. 4 (table, 2020–2030): real GDP 2.3, 8.6, 3.1, 5.4, 5.0, 5.0 (2020–25), then 4.5, 4.0, 3.9, 3.7, 3.4; CPI 0.2 (2023), 0.2 (2024), 0.0
  (2025); GDP deflator −0.4, −0.7, −1.0 (2023–25); total nonfinancial sector debt 272 (2020), 276 (2022), 313 (2025) and 347 percent of GDP
  (2030); augmented debt 97.5 (2020), 126.6 (2025), 153.7 (2030); augmented deficit 14.3 percent of GDP (2025); general budgetary government
  debt 68.4 percent (2025); reserves $3,703 billion (2025); land-sale financing fell from 2.4 percent of GDP (2020) to 0.7.
- Key Issues: the key priority is to "transition to a consumption-led growth model, away from overreliance on exports and investment";
  state-led, debt-financed investment and "unwarranted" industrial policy weakened productivity and created excess supply in some tradables.
- p. 5: China contributed around 30 percent of global growth in the last three years; the 15th FYP recommendations stress innovation,
  self-sufficiency and domestic demand; "involution" campaign; retirement-age reform.
- p. 6: US tariffs on Chinese imports peaked at over 100 percent in April 2025; the October 2025 one-year truce (Text Table 1: fentanyl tariffs
  cut 10 points, reciprocal tariffs above 10 percent suspended to November 2026, rare-earth export controls suspended); effective tariffs on
  Chinese exports to the US up about 23 points on 2024. p. 7: property contraction "now in its fourth year"; housing investment fell from
  12.3 percent of GDP (2020) to 6.1 percent (2025); completions nearly 40 percent below 2021; inventory 30 months of sales; over half of
  private developers still in distress.
- p. 10 and p. 71: preliminary 2025 external position "stronger" than fundamentals; cyclically adjusted CA 3.2 percent vs norm 0.9; REER
  assessed undervalued by 12.1–20.7 percent (midpoint 16.4). p. 18 (para 26): the authorities said average growth of 4.2 percent through
  2035 would meet their "mid-level developed economy" target; staff project slower growth (about 3½ percent by 2030, p. 16).
- pp. 42–44 (appraisal): growth model "faces mounting challenges"; "the policy steps remain modest relative to the scale of the
  challenges"; keep fiscal policy expansionary until deflation subsides; rate cuts only with real appreciation; restructure unviable LGFVs;
  long-run consolidation once reflation is durable.

---

## Chinese official sources

### CN-OFF-1. National Bureau of Statistics of China, *Statistical Communiqué on the 2006 National Economic and Social Development*, 28 February 2007
Listing: https://www.stats.gov.cn/english/StatisticalCommuniqu/index_5.html (200; item 86) → https://www.stats.gov.cn/english/NewsEvents/200703/t20070301_25866.html
(first two tries HTTP 000/connection reset, then 200; HTML). Read: General Outlook, foreign trade, reserves, fixed assets.
- GDP 20,940.7 billion yuan, up 10.7 percent; CPI up 1.5 percent; fixed-asset investment 10,987.0 billion yuan, up 24 percent; exports $969.1
  billion (+27.2 percent), imports $791.6 billion; trade surplus $177.5 billion (up $75.5 billion); reserves $1,066.3 billion at end-2006.
- Note: the IMF's revised series gives 12.7 percent for 2006 (CN-IMF-4 p. 36), a large later revision of the first estimate.

### CN-OFF-2. NBS, *Statistical Communiqué of the People's Republic of China on the 2009 National Economic and Social Development*, 26 February 2010
Listing: https://www.stats.gov.cn/english/StatisticalCommuniqu/index_4.html (200; item 63) → https://www.stats.gov.cn/english/NewsEvents/201002/t20100226_26295.html
(200; HTML). (A 2010 communiqué was not reached: listing pages index_6 and others reset; see Not obtained.) Read: General Outlook, prices,
investment, trade, reserves.
- GDP 33,535.3 billion yuan, up 8.7 percent; CPI −0.7 percent; fixed-asset investment 22,484.6 billion yuan, up 30.1 percent (urban FAI +30.5
  percent); trade $2,207.2 billion, −13.9 percent; exports −16.0 percent; surplus $196.1 billion ($102.0 billion less than 2008); reserves
  $2,399.2 billion (+$453.1 billion). (IMF later: 9.1 percent, CN-IMF-4.)

### CN-OFF-3. NBS, *Statistical Communiqué of the People's Republic of China on the 2025 National Economic and Social Development*, 28 February 2026
Listing: NBS "Latest Releases" (https://www.stats.gov.cn/english/PressRelease/, 200; link given in DL-OTH-7) → https://www.stats.gov.cn/english/PressRelease/202602/t20260228_1962661.html
(200 on this attempt; it had failed for DL-OTH-7). Read: I. General Outlook, prices, Table 7 (FAI by sector), Table 10 (trade), population.
- GDP 140,187.9 billion yuan, up 5.0 percent; quarters 5.4, 5.2, 4.8, 4.5 percent; net exports contributed 1.6 points, consumption 2.6,
  capital formation 0.8; per capita GDP 99,665 yuan. Population 1,404.89 million, down 3.39 million; urbanisation 67.89 percent.
- "consumer prices in 2025 maintained the same level as that of the previous year" (CPI 0.0); industrial producer prices −2.6 percent.
- Table 7: total FAI −3.8 percent; real estate −17.5 percent. Table 10: goods exports 26,989.0 billion yuan (+6.1 percent); total trade +3.8.

### CN-OFF-4. NBS, "National Economy was Generally Stable with Innovation-Led and High-Quality Development..." (October 2026 data), 16 November 2026; and "Consumer Price Index in October 2026", 10 November 2026
Listing: https://www.stats.gov.cn/english/PressRelease/ (200, fetched once; later fetches reset) → .../202611/t20261116_1965843.html (second
try 200) and .../202611/t20261111_1965808.html (200). (Real-estate investment release .../202611/t20261117_1965879.html: HTTP 000.)
- Jan–Oct 2026: FAI −8.1 percent (−5.1 percent excluding real estate development); retail sales of consumer goods +1.0 percent; goods
  exports +17.6 percent and imports +23.6 percent in yuan; October exports +28.7 percent. Urban unemployment 5.1 percent in October.
- CPI +0.7 percent y/y in October, core +0.8; Jan–Oct average +0.9. PPI +5.7 percent y/y in October (Jan–Oct +2.7), purchasing prices +7.9.
- NBS judgement: "the domestic imbalance between strong supply and weak demand is acute".

### CN-OFF-5. People's Bank of China, *Annual Report 2015* (English)
Listing: PBC annual-report page https://www.pbc.gov.cn/en/3688110/3688259/3689032/3709448/3709457/index.html (200) → item page (200) → PDF
https://www.pbc.gov.cn/english/fileDir/resource/cms/2016/07/2016072210452220636.pdf (200; 203 PDF pages; printed = PDF − 1). Read: pp. 25, 29.
- p. 29: on 11 August 2015 the PBC improved the quotation mechanism of the central parity against the dollar: quotes to refer to the previous
  day's interbank closing rate, to reflect supply and demand; on 11 December 2015 CFETS published an RMB index (basket).
- p. 25: end-2015 central parity RMB 6.4936 per dollar, down 5.77 percent in the year; cumulative appreciation against the dollar from the
  2005 reform to end-2015 was 27.46 percent.

---

## Others (WTO, USTR, World Bank, BIS data)

### CN-OTH-1. WTO, "Accessions: China" page, and Press/252, "WTO Ministerial Conference approves China's accession", 10 November 2001; "China – Member information"
URLs: https://www.wto.org/english/thewto_e/acc_e/a1_chine_e.htm (200), which links https://www.wto.org/english/news_e/pres01_e/pr252_e.htm
(200); https://www.wto.org/english/thewto_e/countries_e/china_e.htm (200).
- Accession page: "China became the 143rd WTO Member on 11 December 2001." Member page: member since 11 December 2001.
- Press/252: on 10 November 2001 the Ministerial Conference (Doha) approved the accession agreement by consensus; membership 30 days after
  notification of ratification.

### CN-OTH-2. USTR, *Economic and Trade Agreement Between the Government of the United States of America and the Government of the People's Republic of China* ("Phase One"), signed Washington, 15 January 2020
Listing: https://ustr.gov/countries-regions/china-mongolia-taiwan/peoples-republic-china/phase-one-trade-agreement/text (200) → PDF
https://ustr.gov/sites/default/files/files/agreements/phase%20one%20agreement/Economic_And_Trade_Agreement_Between_The_United_States_And_China_Text.pdf
(200; 91 PDF pages). Read: Chapter 6 (pp. 6-1 to 6-2), signature page.
- Article 6.2: over 1 Jan 2020–31 Dec 2021 China's purchases from the US of listed goods and services must "exceed the corresponding 2017
  baseline amount by no less than $200 billion": manufactured goods at least $32.9 bn (2020) and $44.8 bn (2021) above baseline; agriculture
  $12.5 / $19.5 bn; energy $18.5 / $33.9 bn; services $12.8 / $25.1 bn.
- The 2018–19 tariff lists are in `IMF_2014-2019.md`; 2025–26 US tariff instruments in `Lens_us.md` (US-OTH-5 to -9); outcome of the
  purchase targets not read (no USTR or Chinese assessment obtained).

### CN-OTH-3. World Bank, *China Economic Update—July 2026: Rebalancing Growth* (data cutoff 30 June 2026)
Listing: https://www.worldbank.org/en/country/china (200) → PDF https://thedocs.worldbank.org/en/doc/0cb2fc6dd88d4db3816dc0433b5cb49b-0070012026/original/CEU-July-2026-EN.pdf
(200; 44 PDF pages; Executive Summary p. 1 = PDF 8). Read: Executive Summary (pp. 1–2), risks and policy (p. 20).
- p. 1: GDP 5.0 percent y/y in 2026Q1 (4.5 in 2025Q4); momentum softened in Q2 with the global energy shock (mitigated by oil reserves,
  renewables, retail fuel price caps); inflation 1.1 percent y/y in March–May. "Growth is projected to moderate to 4.4 percent in 2026".
  Table: GDP 5.4 / 5.0 / 5.0 / 4.4 / 4.3 / 4.2 (2023–28); CPI 0.2, 0.2, 0.0, 1.1, 1.5, 1.9; CA 1.4, 2.2, 3.7, 2.1, 0.9, 0.4 percent of GDP.
- p. 2: capital spending still 43 percent of the budget; social protection 11 percent of GDP, about half the OECD average.
- p. 20: an upside risk is a supplementary budget if needed to meet "the government's annual growth target of 4.5-5 percent" (the only
  statement of the 2026 target obtained; the Government Work Report itself was not reached). The 15th FYP elevates domestic demand.
- Early World Bank China Quarterly Updates (2005–2008) were found through the WB documents API (200) but the PDFs are 403 (see Not obtained).

### CN-OTH-4. BIS total credit statistics for China, as held in the book (`data/clean/bis/TC_P.json`, `TC_N.json`) — own reading
- Credit to the private non-financial sector: 104.1 percent of GDP (2000Q1), 106.3 (2008Q4), 133.3 (2009Q4), 190.9 (2016Q1), 182.4 (2017Q4),
  194.7 (2020Q3), 200.8 (2025Q4), 204.1 (2026Q1). Non-financial corporations: 88.4 (2008Q4), 151.8 (2016Q1, peak in the extract), 131.9
  (2020Q4), 146.6 (2026Q1). The 2017 IMF credit-gap estimate (about 25 percent of GDP, CN-IMF-8 p. 19) uses BIS-type data. No BIS text on
  China's credit gap was read.

---

## India and China

### CN-IN-1. *Economic Survey 2012-13*, Chapter "International Trade" (on disk)
- p. 160: the "musical chairs" for top trading partner: the USA relegated to third in 2007-08, China displaced the UAE as top partner in
  2011-12, the UAE regained it in 2012-13 (Apr–Nov). The "growing trade deficit of India with China" (and Switzerland) rose from US$28 bn and
  $24.1 bn (2010-11) to $39.4 bn and $31.3 bn (2011-12); the export–import ratio with China fell to 0.23 (Apr–Nov 2012-13) from 0.31.

### CN-IN-2. *Economic Survey 2014-15*, Vol. 1, Chapter "What to Make in India? Manufacturing or Services?" (on disk)
- p. 110: in contrast to China, Indian states show no convergence in per capita GDP; "manufacturing has not been this escalator in India",
  owing to distortions in labour, capital and land markets and specialisation away from comparative advantage. (Growth-model comparisons:
  also `India_ES_2003-2008.md` — India's investment rate "far below that in China and East Asia" — and TR-IN-1 for ES 2019-20.)

### CN-IN-3. *Economic Survey 2016-17*, Vol. 2 (August 2017), Chapter "External Sector" (on disk)
- p. 144 (para 6.12 and Table 3): China is the biggest contributor to India's trade deficit, its share up from 19.9 percent (2011-12) to 47.3
  percent (2016-17); bilateral balance with China −36.6, −48.5, −52.7, −51.1 US$ bn (2011-12, 2014-15, 2015-16, 2016-17 P). (2018-19:
  −53.57, US-IN-4.)

### CN-IN-4. *Economic Survey 2020-21*, Vol. 2, Chapter "Industry and Infrastructure" (on disk)
- p. 98: the pandemic "exposed the excessive dependence of Indian pharmaceutical industry on China" for APIs and key starting materials;
  pharmaceuticals named among ten PLI sectors, on top of PLI schemes for bulk drugs (KSMs, intermediates, APIs) and medical devices.

### CN-IN-5. *Economic Survey 2021-22*, Chapter "Industry and Infrastructure", Box 1 "FDI Policy reforms and Other Measures during the Covid-19 Pandemic period" (on disk)
- p. 277: "Curbing opportunistic acquisitions/takeovers": by Press Note 3 (2020) dated 17 April 2020, an entity of a country sharing a land
  border with India, or whose beneficial owner is in or a citizen of such a country, may invest only under the Government route; later
  changes of beneficial ownership into that category also need approval. (China is not named in the Survey text. ES 2022-23 repeats the rule,
  PDF p. 315. DPIIT's own Press Note page was a script shell; see Not obtained.)

### CN-IN-6. *Economic Survey 2023-24*, Chapter 4 "External Sector", Box IV.6 "China Plus One strategy" (on disk)
- p. 143: firms "de-risking" from China after COVID, US–China tensions and rising costs; over 90 percent of North American manufacturers
  surveyed by BCG moved some production (Mexico, Thailand, Vietnam). India's draw: domestic market and PLI; Apple assembled US$14 bn of
  iPhones in India in FY24 (14 percent of global output); electronics trade with the US moved from a $0.6 bn deficit (FY17) to an $8.7 bn
  surplus (FY24). India "may not be an immediate beneficiary" of trade diversion.
- p. 144: countries that gained US market share (Mexico, Vietnam, Taiwan, Korea) also saw rising Chinese FDI, so "the world cannot completely
  look past China, even as it pursues China plus one". "India faces two choices to benefit from China plus one strategy": join China's supply
  chain or promote FDI from China; the Survey prefers FDI because China is India's top import partner and the deficit is growing.
- p. 145: India must balance "importing goods from China and importing capital (FDI) from China" (citing coercion risks).

### CN-IN-7. *Economic Survey 2024-25*, Chapter 3 "External Sector" and the "Medium Term Outlook" chapter (energy-transition section) (on disk)
- p. 82 (para 3.7): US dependence on China has declined, while Russia's and Vietnam's dependence on China has risen (UNCTAD).
- pp. 144–146: China hosts about 60 percent of world wind capacity sourcing and nearly 80 percent of battery manufacturing capacity; produces at
  least 80 percent of main PV components; processes 65, 68 and 60 percent of nickel, cobalt and lithium, 90 percent of rare-earth processing.
  "India sources 75 per cent of lithium-ion batteries from China" and has near-negligible polysilicon/ingot/wafer capacity (p. 146); PLI for
  advanced chemistry cells and KABIL as responses.

### CN-IN-8. *Economic Survey 2025-26* (January 2026), Preface, Chapter 1, Chapter 16, and Statistical Appendix Table 6.4 (on disk)
- p. xii (Preface): "global manufacturing is anchored in China’s scale and integrated industrial systems", which set cost and technology
  frontiers no tariff wall can override; hence lower upstream cost of capital rather than more protection.
- p. 7: China tightened export licensing on rare earths and magnets; in early 2026 banned certain dual-use exports to Japan.
- p. 630: China's 2001 WTO entry made it a manufacturing and export powerhouse "upsetting" manufacturing elsewhere. p. 647: on a
  ten-year cumulative basis India has overtaken China as the leading destination for inward investment in Asia after the US (citing a power
  index). p. 650: nearly half of the developed world's imports from China come from supply chains of about fifty multinational brands.
- Statistical Appendix Table 6.4(A) (text PDF p. 884): imports from China US$101.74 bn (2023-24), $113.45 bn (2024-25; +11.5 percent; 15.7
  percent share); Apr–Nov 2025-26 $84.26 bn (+12.6 percent; 16.4 percent share). Table 6.4(B) (PDF p. 895): exports to China $16.67 bn and
  $14.25 bn (−14.5 percent; 3.3 percent share). Implied 2024-25 deficit about $99.2 bn (own arithmetic).
- Data provenance: the book's `data/clean/india/imports_from_china.json` takes each year from the Statistical Appendix "Direction of imports"
  table, Table 7.4(A)/6.4(A), China P Rp row, of the latest Survey printing the full year (ES 2005-06 to ES 2023-24), and 2025-26 (US$131.6 bn,
  provisional) from the RBI Handbook 2025-26. `imports_goods.json` is ES 2025-26 Statistical Appendix Table 6.1B (pp. 116–117).

---

## Synthesis

1. **The exchange-rate argument came first and was settled by events, then reopened.** In 2004 the IMF found no persuasive evidence of
   substantial undervaluation (CN-IMF-1 p. 12); by mid-2005 it saw "increased undervaluation" and urgency (CN-IMF-2 p. 14). The 21 July 2005
   move was a 2 percent revaluation and a basket reference (CN-IMF-2 p. 68); the renminbi rose about 27½ percent against the dollar by end-2015
   (CN-OFF-5 p. 25). The IMF called it moderately undervalued in 2013, broadly in line in 2016–19 (CN-IMF-5 Key Issues; CN-IMF-7; CN-IMF-9),
   and in 2025 again undervalued by 12–21 percent in real terms, through deflation rather than a peg (CN-IMF-13 p. 71).
2. **The surplus peaked at about 10 percent of GDP in 2007 and IMF forecasts of its return were wrong for a decade.** The CA went from 2.8
   percent (2003) to 10.6 (2007) (CN-IMF-4 p. 33). The IMF expected 8–9 percent again in 2010 (Box 4, p. 17) and about 4 percent by 2018 in
   2013 (CN-IMF-5 p. 9); it was 0.4 percent in 2018 (CN-IMF-9 PDF p. 2). The surplus revived to 3.3–3.7 percent in 2025 with a record goods
   surplus (CN-IMF-13 p. 4; CN-OTH-3 p. 1; `IMF_2026.md`).
3. **2008–09: China "led the global recovery" with credit.** New loans equal to 31 percent of GDP in 2009, an infrastructure stimulus, and a
   dollar re-peg in July 2008 (CN-IMF-4 pp. 3–4). NBS's first estimate was 8.7 percent growth in 2009, with fixed investment up 30.1 percent
   and CPI −0.7 percent (CN-OFF-2).
4. **The cost appeared as off-budget local-government debt.** LGFV borrowing rose sharply in 2008–09 (CN-IMF-4 p. 15). The IMF's "augmented"
   debt was 45 percent of GDP in 2012 (CN-IMF-5 p. 12), 97.5 percent in 2020 and 126.6 percent in 2025, heading for 154 percent by 2030
   (CN-IMF-13 p. 4). General government debt: DF-IMF-2.
5. **Credit dependence: the IMF's warnings were consistent from 2013 to 2017.** TSF rose 60 points of GDP in four years (CN-IMF-5 p. 10);
   vulnerabilities on a "dangerous trajectory" (CN-IMF-7 Key Issues); credit gap about 25 percent of GDP, debt to exceed 290 percent by 2022
   (CN-IMF-8 pp. 10, 19). BIS private credit went from 106 percent of GDP (2008) to about 200 (2025) (CN-OTH-4).
6. **The 2015 parity change and capital flight.** On 11 August 2015 the fixing was tied to the previous close (CN-OFF-5 p. 29); outflows
   exceeded the CA surplus in 2015–early 2016, with depreciation expectations "seemingly reinforced" by the change (CN-IMF-7 p. 13); the
   renminbi ended 2015 down 5.77 percent (CN-OFF-5 p. 25). Market side: `IMF_2014-2019.md`; Indian view: ES15-16, ES16-7.
7. **Property: from "bubble beginning to inflate" (2010) to a fourth year of contraction (2025).** CN-IMF-4 p. 26; the August 2020 "three red
   lines" triggered developer distress (CN-IMF-10 p. 9); real estate investment fell about a fifth in 2022 (CN-IMF-11 PDF p. 2) and 17.5
   percent in 2025 (CN-OFF-3 Table 7); housing investment fell from 12.3 percent of GDP (2020) to 6.1 percent (2025) (CN-IMF-13 p. 7).
8. **Deflation was repeatedly underpredicted.** The IMF expected core inflation of 2.0 percent in 2023 (CN-IMF-11 p. 12) and CPI 1.3 percent in
   2024 (CN-IMF-12 PDF p. 2); outcomes were 0.2, 0.2 and 0.0 percent in 2023–25, with the deflator falling three years running (CN-IMF-13 p. 4;
   CN-OFF-3). In 2026 CPI averaged 0.9 percent to October while energy-driven PPI turned positive (CN-OFF-4); the NBS calls the supply–demand
   imbalance "acute".
9. **Rebalancing toward consumption: asked for every year, still the top priority.** CN-IMF-3 p. 3 (2006), CN-IMF-4 p. 3 (2010), CN-IMF-5 (2013),
   CN-IMF-13 Key Issues (2026); in 2025 net exports again supplied 1.6 points of the 5.0 percent growth (CN-OFF-3). The World Bank adds that
   social protection is about half the OECD level (CN-OTH-3 p. 2).
10. **Trade conflict: WTO entry, the Phase One purchase pledge, then 100-percent-plus tariffs.** Member since 11 December 2001 (CN-OTH-1). Phase
    One (15 Jan 2020) required $200 bn of extra purchases over 2020–21 (CN-OTH-2). US tariffs on Chinese goods peaked above 100 percent in April
    2025 and the October 2025 truce runs to November 2026 (CN-IMF-13 p. 6; TR-IMF-4; US-OTH-5 to -9). US imports from China fell 29 percent in
    2025 (TR-WTO-3).
11. **Outlook as of late 2026: about 4½ percent, slowing, with high debt.** 5.0 percent in 2025 (CN-OFF-3); the 2026 target is 4.5–5 percent
    (CN-OTH-3 p. 20); forecasts 4.4–4.5 percent for 2026 and about 3½ percent by 2030 (CN-OTH-3 p. 1; CN-IMF-13 p. 4; `IMF_2026.md`). The
    authorities aim at 4.2 percent average to 2035 (CN-IMF-13 p. 18). Population is falling (DL-OTH-7).
12. **India: China as supplier, deficit and model.** The deficit with China rose from $28 bn (2010-11) to $51 bn (2016-17), about half of
    India's total deficit (CN-IN-1 p. 160; CN-IN-3 p. 144), and about $99 bn in 2024-25, on imports of $113 bn (CN-IN-8 Table 6.4, own
    arithmetic). The policy response: PLI schemes framed around API and battery dependence (CN-IN-4 p. 98; CN-IN-7 p. 146), and Press Note 3
    screening of land-border investors (CN-IN-5 p. 277). Then ES 2023-24 argued for Chinese FDI as the route to "China plus one" (CN-IN-6
    p. 144). ES 2025-26 accepts that world manufacturing is "anchored in China's scale" (CN-IN-8 p. xii).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| 2004 | IMF Art. IV (CN-IMF-1 p. 12) | No persuasive evidence the renminbi is "substantially undervalued" | A year later staff saw "increased undervaluation" (CN-IMF-2 p. 14); CA rose from 3.6% (2004) to 10.6% of GDP (2007) (CN-IMF-4 p. 33) |
| 2005 | IMF Art. IV (CN-IMF-2 p. 15) | Authorities: "no convincing evidence" of undervaluation; fear of job losses from appreciation | RMB rose 27.46% vs the dollar 2005–2015 (CN-OFF-5 p. 25); growth 12.7% (2006) and 14.2% (2007) (CN-IMF-4 p. 36) |
| 2006 | NBS communiqué (CN-OFF-1) | GDP growth 10.7% in 2006 | Revised to 12.7% (CN-IMF-4 p. 36) |
| 2010 | IMF Art. IV (CN-IMF-4 Box 4, p. 36) | CA surplus back to 8–9% of GDP within two years; 8.0% by 2015 | 2¼% in 2012 (CN-IMF-5 p. 6); 0.4% in 2018 (CN-IMF-9) |
| 2010 | IMF Art. IV (CN-IMF-4 p. 26) | National property prices probably not far above fundamentals; bubble "beginning to inflate" in big cities | Property contraction in fourth year in 2025; real estate investment −17.5% in 2025 (CN-IMF-13 p. 7; CN-OFF-3) |
| 2013 | IMF Art. IV (CN-IMF-5 p. 9) | Baseline CA ~4% of GDP by 2018; authorities "strongly disagreed" | 0.4% in 2018: the authorities were right (CN-IMF-9 PDF p. 2) |
| 2013 | IMF Art. IV (CN-IMF-5 p. 12) | Augmented government debt 45% of GDP (2012); "manageable" | 126.6% in 2025, 153.7% projected for 2030 (CN-IMF-13 p. 4) |
| 2014 | IMF Art. IV (CN-IMF-6) | Hard-landing risk low near term, "medium-likely" over the medium term | No hard landing: growth slid gradually to 6.6% (2016), 5.0% (2025) (CN-IMF-7 p. 33; CN-OFF-3), but via the property bust and deflation |
| 2017 | IMF Art. IV (CN-IMF-8 p. 10) | Non-financial debt >290% of GDP by 2022 | 276% in 2022, 313% in 2025 (CN-IMF-13 p. 4; definitions may differ) |
| 2022 | IMF Art. IV (CN-IMF-11 p. 12) | Core inflation up to 2.0% in 2023, 2.3% in 2024 | CPI 0.2% (2023), 0.2% (2024), 0.0% (2025); deflator negative (CN-IMF-13 p. 4) |
| 2023 | IMF Art. IV (CN-IMF-12 PDF p. 2) | Growth 4.6% in 2024; inflation 1.3% | Growth 5.0% in 2024 and 2025; CPI 0.2% and 0.0% (CN-IMF-13 p. 4) |
| 2020 (Jan) | Phase One (CN-OTH-2 Art. 6.2) | China to buy ≥$200 bn more US goods and services over 2020–21 than in 2017 | Not checked here; by 2025 US tariffs peaked >100% and US imports from China fell 29% (CN-IMF-13 p. 6; TR-WTO-3) |
| 2013 | ES 2012-13 (CN-IN-1 p. 160) | Growing deficit with China: $39.4 bn in 2011-12 | $51.1 bn in 2016-17 (CN-IN-3 p. 144); about $99 bn in 2024-25 (CN-IN-8, own arithmetic) |
| 2021 | ES 2020-21 (CN-IN-4 p. 98) | PLI schemes to cut "excessive dependence" on China for APIs | Imports from China rose from $65.2 bn (2020-21) to $113.4 bn (2024-25) and $131.6 bn (2025-26 P) (`imports_from_china.json`; CN-IN-8); 75% of lithium-ion batteries still from China (CN-IN-7 p. 146) |
| 2022 | ES 2021-22 (CN-IN-5 p. 277) | PN3 (2020): land-border investors only via Government route | ES 2023-24 argued for promoting Chinese FDI (CN-IN-6 p. 144); ES 2025-26 says India overtook China as Asia's top investment destination (10-year cumulative, CN-IN-8 p. 647) |
| 2024 | ES 2023-24 (CN-IN-6 p. 143) | India "may not be an immediate beneficiary" of diversion from China | ES 2025-26: world manufacturing "anchored in China's scale" (CN-IN-8 p. xii); China's share of India's imports rose to 16.4% (Apr–Nov 2025-26) |

Candidate quotes (all verified by script against the converted text, under 15 words):
- "it is difficult to find persuasive evidence that the renminbi is substantially undervalued" (IMF 2004 Art. IV, CN-IMF-1 p. 12)
- "increased undervaluation of the renminbi, adding to the urgency of making a move" (IMF 2005 Art. IV, CN-IMF-2 p. 14)
- "there was no convincing evidence pointing to the undervaluation of the renminbi" (authorities' view, CN-IMF-2 p. 15)
- "rebalanced away from heavy dependence on export-led growth toward self-sustaining domestic demand" (IMF 2006 Art. IV, CN-IMF-3 p. 3)
- "ensured that China has led the global recovery" (IMF 2010 Art. IV, CN-IMF-4 p. 3)
- "An extraordinary credit expansion." (CN-IMF-4 p. 4)
- "a property bubble is beginning to inflate" (CN-IMF-4 p. 26)
- "This pattern of growth is not sustainable and is raising vulnerabilities." (IMF 2013 Art. IV, CN-IMF-5 Key Issues, PDF p. 2)
- "the margins of safety are diminishing" (CN-IMF-5 Key Issues, PDF p. 2)
- "renminbi which staff assess as moderately undervalued" (CN-IMF-5 Key Issues, PDF p. 2)
- "the risk of a hard landing is still considered low" (IMF 2014 Art. IV, CN-IMF-6 Key Issues, PDF p. 2)
- "Vulnerabilities are still rising on a dangerous trajectory" (IMF 2016 Art. IV, CN-IMF-7 Key Issues, PDF p. 7)
- "rise further to over 290 percent of GDP by 2022" (IMF 2017 Art. IV, CN-IMF-8 p. 10)
- "pushing the credit gap to about 25 percent of GDP" (CN-IMF-8 p. 19)
- "imposing stringent benchmarks (the “three red lines”)" (IMF 2021 Art. IV, CN-IMF-10 p. 9)
- "the real estate crisis remains unresolved" (IMF 2022 Art. IV, CN-IMF-11 Key Issues, PDF p. 5)
- "a significant, but needed, adjustment in the property market" (IMF 2023 Art. IV, CN-IMF-12 Key Issues, PDF p. 5)
- "The Chinese economy has remained remarkably resilient despite facing multiple shocks" (PR 26/053, CN-IMF-13 PDF p. 2)
- "transition to a consumption-led growth model, away from overreliance on exports and investment" (CN-IMF-13 Key Issues, PDF p. 6)
- "the policy steps remain modest relative to the scale of the challenges" (CN-IMF-13 p. 43)
- "consumer prices in 2025 maintained the same level as that of the previous year" (NBS, CN-OFF-3)
- "the domestic imbalance between strong supply and weak demand is acute" (NBS, 16 Nov 2026, CN-OFF-4)
- "China became the 143rd WTO Member on 11 December 2001." (WTO accession page, CN-OTH-1)
- "exceed the corresponding 2017 baseline amount by no less than $200 billion" (Phase One Art. 6.2, CN-OTH-2 p. 6-1)
- "Growth is projected to moderate to 4.4 percent in 2026" (World Bank CEU July 2026, CN-OTH-3 p. 1)
- "growing trade deficit of India with China" (ES 2012-13, CN-IN-1 p. 160)
- "manufacturing has not been this escalator in India" (ES 2014-15, CN-IN-2 p. 110)
- "exposed the excessive dependence of Indian pharmaceutical industry on China" (ES 2020-21 Vol. 2, CN-IN-4 p. 98)
- "the world cannot completely look past China, even as it pursues China plus one" (ES 2023-24, CN-IN-6 p. 144)
- "India faces two choices to benefit from China plus one strategy" (ES 2023-24, CN-IN-6 p. 144)
- "India sources 75 per cent of lithium-ion batteries from China" (ES 2024-25, CN-IN-7 p. 146)
- "global manufacturing is anchored in China’s scale and integrated industrial systems" (ES 2025-26 Preface, CN-IN-8 p. xii)
- "India has overtaken China as the leading destination for inward investment in Asia" (ES 2025-26, CN-IN-8 p. 647)
- Failed the check (column interleaving), paraphrased instead: PBC Annual Report 2015 p. 29 wording on referring to the previous closing rate.

## Not obtained

- IMF listing of past China Article IV reports: the country page https://www.imf.org/en/Countries/CHN (200) links only CR 26/44, PR 25/415, an
  IMF article of 18 Feb 2026 and the July 2026 WEO Update. As for the US (see `Lens_us.md` Not obtained), older reports are from GUESSED URLs.
  Guesses that returned other documents: .../cr/2019/1chnea2019001.pdf (CR 19/172, AML/CFT) and ...2019002.pdf (CR 19/173, ROSC);
  .../cr/2024/english/1chnea2024002.pdf (CR 24/50, Selected Issues). 404: .../cr/2024/english/1chnea2024003.pdf, ...004, ...005, ...006 (so
  the Article IV report on the 2024 consultation was not obtained). No China Article IV for 2007–2009 was found or guessed. Downloaded but
  not read in detail: CR 14/235 beyond Key Issues; PR 25/415.
- NBS (stats.gov.cn): repeated connection resets (curl HTTP 000 / error 35) after a few requests: https://www.stats.gov.cn/english/ — 000;
  https://www.stats.gov.cn/english/PressRelease/ — 000 on later tries; StatisticalCommuniqu/index_6.html — 000; .../202611/t20261117_1965879.html
  (real estate investment Jan–Oct 2026) — 000. Over plain http, http://www.stats.gov.cn/english/StatisticalCommuniqu/ returned a local
  network-filter "deny" page (200, 389 bytes, iframe to 14.143.143.194/webadmin/deny), so only https was used. GUESSED
  https://www.stats.gov.cn/english/NewsEvents/201102/t20110228_26575.html (2010 communiqué) — 000; GUESSED
  https://www.stats.gov.cn/english/newsandcomingevents/t20070228_402388217.htm — 404. So no 2010 communiqué; 2006 and 2009 used instead. No
  early-2000s communiqué population figures were extracted.
- PBC announcement of 21 July 2005 (exchange-rate reform) and the 11 August 2015 PBC statement itself: https://www.pbc.gov.cn/en/ — 403;
  https://www.pbc.gov.cn/en/3688110/index.html — 404; GUESSED https://www.pbc.gov.cn/english/130721/2831438/index.html and .../2831456/index.html
  — 404. The press-release listing (https://www.pbc.gov.cn/en/3688110/3688172/index.html, 200) shows only recent items; older pages not
  searched. The 2005 terms are from the IMF staff supplement (CN-IMF-2 p. 68); 2015 from the PBC Annual Report (CN-OFF-5).
- 2008 stimulus official text (State Council/NDRC): GUESSED https://www.gov.cn/english/2008-11/09/content_1143689.htm — 404. The stimulus is
  described only through the IMF (CN-IMF-4).
- "Three red lines" (2020): no official Chinese text found (no PBC/MOHURD listing reached); described from CN-IMF-10 p. 9.
- 2026 Government Work Report and the 15th Five-Year Plan text: https://english.www.gov.cn/ (200), /archive/ (200), /policies/latestreleases/
  (200) — no work-report links on current pages; https://english.www.gov.cn/2026special/2026npccppcc/ (GUESSED) — 200 but the home page;
  State Council Gazette listing (200) shows only Aug–Nov 2026, and .../statecouncilgazette/index_1.html and index_2.html (GUESSED) return the
  home page; https://english.www.gov.cn/premier/ — redirect to /institutions; https://www.npc.gov.cn/englishnpc/ — 000. The 4.5–5 percent
  target is taken from the World Bank (CN-OTH-3 p. 20) and is not confirmed from an official text.
- World Bank early China Quarterly Updates: the documents API (https://search.worldbank.org/api/v2/wds?..., 200) lists Feb 2005–Dec 2008 issues,
  but https://documents.worldbank.org/curated/en/378231468221672173/pdf/473910WP0P11191mber020080Box334131B.pdf (Dec 2008) — 403
  (documents.worldbank.org blocks); not pursued further.
- BIS text on China's credit gap (e.g. BIS Quarterly Review): not attempted; data already in the book (CN-OTH-4).
- Phase One outcome (actual purchases 2020–21): no USTR or Chinese assessment fetched.
- Indian official sources: https://dpiit.gov.in/policies-rules-and-acts/press-notes-fdi-circular (200) and https://dpiit.gov.in/ (200) are
  script shells with no Press Note text; https://www.commerce.gov.in/trade-statistics/ (GUESSED) — 404; https://tradestat.commerce.gov.in/eidb/
  (GUESSED) — 404. PIB not attempted (the US agent found no relevant items on its current listings). Press Note 3 (2020) is known here only
  from the Survey (CN-IN-5).
- Survey items not read: ES 2022-23 PLI tables (PDF p. 324) and PN3 repeat (PDF p. 315); ES 2025-26 Chart XVI.5 (China's imports and income,
  p. 648) not read in detail.
