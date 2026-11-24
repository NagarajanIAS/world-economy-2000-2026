# Reading notes: lens 'Other emerging markets' — part A (Brazil, Mexico, Türkiye, South Africa) (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL -o file -w '%{http_code}' URL` (default user-agent, no custom headers, no
cookies), with a 3-second pause between requests; each request and its HTTP status is logged in the scratchpad file `fetchlog_a.txt`.
Listing pages used: the imf.org country pages https://www.imf.org/en/Countries/BRA, /MEX, /TUR, /ZAF (all 200; BRA returned 429 at the
first attempt and 200 on retry; ZAF and TUR also via `index.md` / `index.json`, 200) — each links **only the latest Article IV issue page**,
and those issue pages (200) gave the latest PDF links; the CBRT English home page and its yearly Press Releases pages (200), which list the
interest-rate press releases; the CBRT "1 Week Repo" rates page (200); the National Treasury 2026 budget page (200), which links the Budget
Review; the Banco Central do Brasil (BCB) Copom statement list endpoint (200). **All IMF staff reports before the latest ones come from
GUESSED URLs** built on the IMF file-naming pattern: `/external/pubs/ft/scr/YYYY/crYYNNN.pdf` to 2016; `/-/media/files/publications/cr/
YYYY/crYYNNN.pdf` in 2017–18; and from 2019 `/-/media/files/publications/cr/YYYY/english/1<iso3>eaYYYYnnn.pdf`, **where nnn is a per-country
sequence number (001 = first document of the year), not the CR number** (e.g. 1turea2021001.pdf is CR 21/110; 1mexea2020001.pdf is CR 20/293);
some 2024–26 files need the suffix `-print-pdf` or `-source-pdf`. Candidate report numbers came from citations inside reports already fetched
(e.g. CR 09/126 cited in CR 10/71) or were tried and then checked: for every file the title page and "IMF Country Report No." were read, and
wrong hits (Kuwait, Spain, Cape Verde, Panama, Iceland and others) were deleted and are listed under Not obtained. Downloads are in the
scratchpad folder `lens_em_dl/a/` with subfolders `imf/` (country and issue pages), `imf/g/` (staff reports), `imf/pr/` (old press
releases), `imf/el/` (failed listing attempts), `bcb/`, `cbrt/`, `za/` and `mx/` (empty). PDFs were converted with `pdftotext` (plain and
`-layout`); HTML and JSON were stripped of tags. Python that read downloads was run with `python3 -I` from scripts kept in the scratchpad
root. Economic Survey texts were not refetched: they were read from the Econ Subject folder (`sources/text/es*.txt`, text page = PDF page),
and the printed page was taken from the running header or footer. Quotes are verbatim, under 15 words, and a script checked every one against
the converted text (whitespace-, quote- and dash-normalised): all 14 matched. Everything else is paraphrase. BCB Copom statements are in
Portuguese and are paraphrased in English (no quotes). Outturns come from `data/clean/weo/NGDP_RPCH.json` and `PCPIPCH.json` (WEO October
2026 vintage; PCPIPCH is the **annual average**, so it is not strictly comparable with end-period IMF forecasts — flagged where it matters).

Printed-page offsets (printed = PDF − n; Key Issues pages, title pages and press-release tables are unnumbered or numbered separately and are
cited as "PDF p."): Brazil CR 12/191 and 13/312: −1; CR 16/348: −6; CR 25/194: −5 (the press release is numbered separately, PR p. = PDF − 1).
Mexico CR 09/53 and 09/126: −2; CR 10/71 and 14/319: −1; CR 20/293 and 25/286: −4. Türkiye CR 13/363: −1; CR 18/110 and 21/110: −5;
CR 24/312 and 26/43: −4. South Africa CR 08/348 and 09/273: −2; CR 17/189 and 18/246: −5; CR 23/194 and 26/34: −4. National Treasury Budget
Review 2026: −17 (PDF 18 = printed 1).

Item labels:
- BR-IMF-n, MX-IMF-n, TR-IMF-n, ZA-IMF-n: IMF Article IV staff reports, the Mexico FCL report and IMF press releases.
- BR-BCB-n: Banco Central do Brasil (Selic target series; Copom statements).
- TR-CBRT-n: Central Bank of the Republic of Türkiye (policy-rate table; MPC press releases).
- ZA-GOV-n: National Treasury of South Africa (Budget Review 2026).
- EM-IN-A-n: India links from the Economic Surveys (on disk; not refetched).
- No MX primary document was read (Banxico not attempted; see Not obtained).

Abbreviations: AIV = Article IV; BCB = Banco Central do Brasil; CBRT = Central Bank of the Republic of Türkiye; CR = IMF Country Report;
CAD = current account deficit; eop = end of period; FCL = Flexible Credit Line; IPCA = Brazil's consumer price index; KI = Key Issues page;
MPC = Monetary Policy Committee; NFPS = non-financial public sector; PR = press release; SARB = South African Reserve Bank; SOE = state-owned
enterprise; WEO = IMF World Economic Outlook.

---

## Brazil

### BR-IMF-1. IMF, "IMF Approves US$30.4 Billion Stand-By Credit for Brazil", Press Release No. 02/40, 6 September 2002
URL: https://www.imf.org/external/np/sec/pr/2002/pr0240.htm (GUESSED; 200; accessed 23 Nov 2026). The page is now served in the IMF's
restructured format (summary headings, "Source details"); the number "Press Release No. 02/40, September 6, 2002" appears in the text. No
page numbers (HTML).
- New stand-by of US$30.4 billion replacing the 15-month arrangement of 14 September 2001 (PR 01/38); about US$3 billion available at once,
  another US$3 billion after the first review, the rest in four tranches through 2003.
- Context given: earlier reforms (higher primary surplus, fiscal institutions, float, inflation targeting), then pressure from a weak global
  setting, worries about policies ahead of the presidential election, currency depreciation, a higher debt ratio and slower growth; markets
  under "intense pressure" over the policies of the government taking office in January 2003.
- Program: primary surplus 3.88% of GDP in 2002 and at least 3.75% in 2003–05; inflation to converge to the end-2003 target of 4% ± 2½
  points; floor on net international reserves US$5 billion (US$10 billion below the previous program, to allow room to curb volatility).
- Use: the 2002 confidence crisis box (election, debt, currency), with the Selic path in BR-BCB-1 (25% to 26.5% in December 2002 – February
  2003).

### BR-IMF-2. IMF, *Brazil: 2012 Article IV Consultation—Staff Report; Public Information Notice…; and Statement by the Executive Director*, IMF Country Report No. 12/191, July 2012 (staff report 22 June 2012; Board 9 July 2012)
PDF: https://www.imf.org/external/pubs/ft/scr/2012/cr12191.pdf (GUESSED; 200; 105 PDF pages). Read: title page, KI (PDF p. 2), Staff Appraisal
(pp. 27–28), Table 1 (p. 32).
- KI (PDF p. 2): the economy has cooled after past tightening and global shocks; stimulus since late 2011; growth in 2013–14 back to potential
  of about 4%; medium-term inflation expectations well above the target mid-point. "The staff supports the policy mix of easy money and tight
  fiscal", including the full 3.1% of GDP primary surplus target. Rapid credit growth is creating pockets of vulnerability among consumers.
- p. 27: BNDES balance sheet grew from 7½% of GDP (2007) to 14% (2011); staff suggests a strategic review and a shift away from lending to
  prime corporates.
- pp. 27–28: monetary policy appropriately eased; staff says the authorities should stand ready to unwind stimulus through 2013 as
  expectations have risen; Brazil should rebalance from consumption to investment and net exports; saving below most G-20 EMs.
- Table 1, p. 32 (numbers for the boom): real GDP 6.1 (2007), 5.2 (2008), −0.3 (2009), **7.5 (2010)**, 2.7 (2011); projections **2.5 (2012)**,
  **4.6 (2013)**, 4.1 (2017). IPCA eop 5.9 (2010), 6.5 (2011), proj. 4.8 (2012), 5.0 (2013). NFPS gross debt 65.2% (2010) → 64.9% (2011);
  gross reserves US$288.6 bn (2010) → 352.0 bn (2011); CAD 2.2% of GDP (2010), 2.1% (2011).

### BR-IMF-3. IMF, *Brazil: Staff Report for the 2013 Article IV Consultation*, IMF Country Report No. 13/312, October 2013 (staff report 2 July 2013; Board 26 July 2013)
PDF: https://www.imf.org/external/pubs/ft/scr/2013/cr13312.pdf (GUESSED; 200; 97 PDF pages). Read: KI (PDF p. 2), Staff Appraisal (p. 32),
Table 1 (p. 45).
- KI (PDF p. 2): a gradual, uneven recovery from the slowdown that began in mid-2011, with inflation elevated; output at potential with
  supply constraints; staff sees "excessive fine tuning of fiscal policy" (including through public banks) weakening the fiscal framework's
  credibility; potential growth estimates revised down. Advice: steady fiscal consolidation, wind down policy lending, continued monetary
  tightening; flexible exchange rate as main shock absorber.
- p. 32 (paras 36–37): the fiscal responsibility law, inflation targeting and the float preserved stability and underpinned a large fall in
  poverty in the 2000s; the sharp slowdown since mid-2011 reflects supply constraints and policy uncertainty; a front-loaded monetary
  tightening is advised.
- Table 1, p. 45: real GDP 7.5 (2010), 2.7 (2011), **0.9 (2012)**; projections **2.5 (2013)**, **3.2 (2014)**, 3.5 (2018). IPCA eop 5.8
  (2012), proj. 5.8 (2013, 2014). NFPS gross debt 68.0% (2012); CAD 2.4% (2012) → 3.2% (2013 proj.); reserves US$373.1 bn (2012).
- Note: the 2012 report's 4.6% for 2013 had already been cut to 2.5% a year later.

### BR-IMF-4. IMF, *Brazil: 2016 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director for Brazil*, IMF Country Report No. 16/348, November 2016 (staff report 14 October 2016; Board 31 October 2016)
PDF: https://www.imf.org/external/pubs/ft/scr/2016/cr16348.pdf (GUESSED; 200; 96 PDF pages). Read: title page, KI (PDF p. 7), Staff Appraisal
(pp. 28–29), Table 1 (p. 30).
- KI (PDF p. 7): "The economy is still in its deepest recession in decades", partly from past policy failures, aggravated by a political
  crisis; President Rousseff impeached on 31 August 2016; growth to resume gradually but stay weak; the Petrobras corruption probe noted;
  failure to implement the structural fiscal reforms is the main risk to debt sustainability; gross debt stabilises only after the 5-year
  horizon in the baseline.
- KI and pp. 28–29: the strategy of holding non-interest spending constant in real terms (the spending cap) plus social security reform is
  welcome but will bear fruit slowly; staff favours a more front-loaded consolidation once growth firms; monetary policy on hold until
  expectations converge to the centre of the band; reduce the stock of FX swaps gradually; intervene only against market dysfunction.
- Table 1, p. 30: real GDP 0.1 (2014), **−3.8 (2015)**, **−3.3 (2016 proj.)**, **0.5 (2017)**, 1.5 (2018), 2.0 (2019–21). IPCA eop **10.7 (2015)**,
  7.2 (2016), 5.0 (2017). NFPS primary balance −1.9% (2015), −2.7% (2016); NFPS overall balance incl. policy lending −10.4% (2015); NFPS gross
  debt 63.3% (2014) → 73.7% (2015) → 93.5% (2021 proj.); CAD 4.3% (2014) → 0.8% (2016); reserves US$356.5 bn (2015).

### BR-IMF-5. IMF, *Brazil: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director for Brazil*, IMF Country Report No. 25/194, July 2025 (staff report 27 June 2025; Board 14 July 2025; PR 25/252, 17 July 2025)
Issue page: https://www.imf.org/en/publications/cr/issues/2025/07/16/brazil-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-568678
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1braea2025001-source-pdf.pdf (from issue page;
200; 118 PDF pages). The latest Brazil Article IV listed on the IMF Brazil page (no 2026 report listed). Read: PR (PR pp. 1–3, PDF pp. 2–4),
PR Table 1 (PR p. 4, PDF p. 5), KI (PDF p. 6), pp. 6, 13, 15, Staff Appraisal (pp. 34–35).
- PR p. 1: growth to moderate from 3.4% (2024) to 2.3% (2025), then 2.5% over the medium term; inflation rebounded in 2024 above the tolerance
  interval; the September 2024 pivot to tightening was appropriate. PR p. 2: inflation 5.2% by end-2025, back to the 3% target by end-2027;
  growth risks tilted down.
- KI (PDF p. 6): growth "remarkably resilient" for three years, driven by consumption with fiscal support; elevated debt and spending
  rigidities; general government gross debt to stabilise at 99% of GDP.
- p. 6: interest bill about 6.3% of GDP in 2024. p. 13: after 450 bp of hikes to **15% in June 2025**, real rates close to 10% against a staff
  neutral estimate of about 5%. p. 15: policy rate to peak at 15% in 2025; federal primary deficit 0.6% of GDP in 2025, surplus 1.4% by 2030;
  CAD to narrow to 1.9% of GDP. pp. 34–35: IOF-FX tax on financial transactions is a multiple currency practice, being phased out; Pix and the
  Drex CBDC pilot noted.
- PR Table 1 (PDF p. 5): real GDP 3.2 (2023), 3.4 (2024), **2.3 (2025)**, **2.1 (2026)**, 2.5 (2030); IPCA average 4.4 (2024), 5.3 (2025), 4.2
  (2026); general government gross debt 84.0% (2023), 87.3% (2024), 91.6% (2025), 99.0% (2029); CAD 2.8% of GDP (2024); reserves US$330 bn
  (2024); unemployment 6.9% (2024); GDP US$2,171 bn, per capita US$10,214 (2024).

### BR-BCB-1. Banco Central do Brasil, SGS series 432 "Meta Selic definida pelo Copom" (daily), 1 January 2000 – 23 November 2026
URLs (GUESSED; the API caps daily series at 10-year windows, so three requests):
https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial=01/01/2000&dataFinal=31/12/2009 (200),
…dataInicial=01/01/2010&dataFinal=31/12/2019 (502, then 200 on retry), …dataInicial=01/01/2020&dataFinal=23/11/2026 (200). A first request
for the whole period returned 406 (window too long). Dates below are the dates from which the new target applies (own reading of the series).
- Peaks and troughs (own reading): 19% (Jan 2000) → 15.25% (Jan 2001) → **26.5% from 20 Feb 2003** (after rises from 18% in October 2002) →
  16% (Apr 2004) → 19.75% (May 2005) → 11.25% (Sep 2007) → 13.75% (Sep 2008) → 8.75% (Jul 2009) → 12.5% (Jul 2011) → **7.25% from 11 Oct
  2012** → **14.25% from 30 Jul 2015** (held until 20 Oct 2016) → 6.5% (Mar 2018) → **2.0% from 6 Aug 2020** → **13.75% from 4 Aug 2022**
  (held to 3 Aug 2023) → 10.5% (May 2024) → **15.0% from 19 Jun 2025** → first cut to 14.75% from 19 Mar 2026 → **13.75% from 17 Sep 2026**.

### BR-BCB-2. Banco Central do Brasil, Copom statements (comunicados), meetings 202, 271, 277 and 282
List: https://www.bcb.gov.br/api/servico/sitebcb/copom/comunicados?quantidade=300 (GUESSED; 200; lists meetings 202–282, 19 Oct 2016 – 4 Nov
2026). Statements: https://www.bcb.gov.br/api/servico/sitebcb/copom/comunicados_detalhes?nro_reuniao=N (GUESSED; 200 for N = 202, 271, 277,
282). In Portuguese; paraphrased. No page numbers (JSON/HTML).
- Meeting 202, 19 Oct 2016: unanimous cut from 14.25% to 14.00%, the first of the cycle; activity a little weaker than expected but
  stabilising; high slack; Focus expectations for 2017 down to about 5.0% against the 4.5% target.
- Meeting 271, 18 Jun 2025: rise to **15.00%**; external environment adverse and uncertain because of US trade and fiscal policy; Focus
  expectations 5.2% (2025) and 4.5% (2026), above target; Copom projection 3.6% for 2026; expectations described as unanchored.
- Meeting 277, 18 Mar 2026: **cut to 14.75%**, while noting heightened uncertainty from the Middle East conflicts and that risks to inflation
  had intensified; Focus 4.1% (2026), 3.8% (2027); projection 3.3% for 2027 Q3.
- Meeting 282, 4 Nov 2026 (latest): **hold at 13.75%** (after cuts to 14.25% in June, 14.00% in August and 13.75% in September 2026); the
  prolonged Middle East conflicts pushed up oil prices; headline and core inflation accelerated above the upper limit of the tolerance
  interval; Focus 5.2% (2026), 4.8% (2027); projection 3.5% for 2028 Q2, risks skewed up.

---

## Mexico

### MX-IMF-1. IMF, *Mexico: 2008 Article IV Consultation—Staff Report; Staff Supplement; and Public Information Notice…*, IMF Country Report No. 09/53, February 2009 (staff report 15 January 2009; Board 6 February 2009)
PDF: https://www.imf.org/external/pubs/ft/scr/2009/cr0953.pdf (GUESSED; 200; 62 PDF pages). Read: title page, Executive Summary (PDF p. 3),
p. 16, Staff Appraisal (pp. 33–34), Table 1 (p. 36).
- Exec. Summary (PDF p. 3): a significant drop in growth expected amid tight financial conditions and a US recession; strong frameworks
  and balance sheets mean "a countercyclical policy response is not only desirable but also possible", the first time for Mexico. Advice:
  ease monetary policy, consider more fiscal stimulus if needed, keep supporting markets through development banks, think about a structural
  fiscal rule.
- pp. 33–34: Mexico faces the crisis from greater strength than in the past (flexible exchange rate, stronger public, corporate and bank
  balance sheets); the October 2008 peso depreciation helped clear markets; the Fed swap line helped sentiment; the PEMEX oil-price hedge
  should pay off in 2009, but stimulus would largely be withdrawn in 2010.
- Table 1, p. 36: real GDP 3.2 (2007), 1.8 (2008), **−0.3 (2009 proj.)**, 2.1 (2010); CPI eop 6.5 (2008), 3.6 (2009); gross public debt 39.3%
  (2008); net international reserves US$85.6 bn (2008).

### MX-IMF-2. IMF, *Mexico: Arrangement Under the Flexible Credit Line—Staff Report; Staff Supplement; and Press Release…*, IMF Country Report No. 09/126, April 2009 (staff report 7 April 2009; Board 17 April 2009)
PDF: https://www.imf.org/external/pubs/ft/scr/2009/cr09126.pdf (GUESSED from the citation in CR 10/71 p. 7; 200; 41 PDF pages). Read: title
page, summary (PDF p. 3), pp. 6, 9, press release (PDF p. 40).
- PDF p. 3: Mexico qualifies for the FCL; access SDR 31.528 billion (1,000% of quota); the authorities intend to treat it as precautionary;
  very large impact on Fund liquidity.
- p. 6: GDP now expected to fall about 3¾% in 2009, after about 1.3% growth in 2008; footnote: revised from −0.3% in the January 2009 WEO
  because Q4 2008 GDP fell 10.3% (saar) and US demand was revised down.
- p. 9: access is some US$47 billion for one year; Mexico's reserves lower than key EM peers; non-residents held about US$180 bn of Mexican
  assets at end-2008; 2009 gross external financing needs about US$80 bn.
- PR (PDF p. 40): Board approves the one-year SDR 31.5 bn (about US$47 bn) FCL on 17 April 2009.

### MX-IMF-3. IMF, *Mexico: 2010 Article IV Consultation—Staff Report and Public Information Notice…*, IMF Country Report No. 10/71, March 2010 (staff report 1 March 2010; Board 10 March 2010)
PDF: https://www.imf.org/external/pubs/ft/scr/2010/cr1071.pdf (GUESSED; 200; 54 PDF pages). Read: summary box (PDF p. 2), contents (p. 2),
Table 1 (p. 34).
- PDF p. 2: the FCL (SDR 31.528 bn) approved 17 April 2009 is treated as precautionary; 2010 consultation centred on exiting the recession.
- p. 7 (by search): the FCL helped sentiment when approved; FCL developments in CR 09/126 and 09/302. p. 29: Fed swap line plus FCL amounted
  to about US$80 billion of insurance.
- Table 1, p. 34: real GDP 1.5 (2008), **−6.5 (2009 est.)**, **4.0 (2010 proj.)**, 4.5 (2011); CPI eop 3.6 (2009), 5.3 (2010); gross public debt
  44.6% (2009); net international reserves US$90.8 bn (2009).

### MX-IMF-4. IMF, *Mexico: 2014 Article IV Consultation—Staff Report; and Press Release*, IMF Country Report No. 14/319, November 2014 (staff report 24 October 2014; Board 7 November 2014)
PDF: https://www.imf.org/external/pubs/ft/scr/2014/cr14319.pdf (GUESSED; 200; 72 PDF pages). Read: KI (PDF p. 2), Staff Appraisal
(pp. 14–15).
- KI (PDF p. 2): growth 2.4% projected for 2014; major reforms approved in energy, education, anti-trust, telecoms and finance; secondary
  legislation for energy and telecoms completed; staff estimates the reforms raise potential growth by ¾ point to 3½–4% a year; main external
  risk is capital-flow volatility from US monetary normalisation.
- p. 14: Mexico is one of very few countries to reach political consensus on long-standing problems; the energy reform opens oil, gas and
  electricity to private investment. p. 15: real GDP 2½% (2014) and **3½% (2015)**; the FCL is valuable tail-risk insurance; staff supports
  cutting the PSBR to 2.5% of GDP by 2018 under the new Fiscal Responsibility Law.

### MX-IMF-5. IMF, *Mexico: 2020 Article IV Consultation—Press Release and Staff Report*, IMF Country Report No. 20/293, November 2020 (staff report 19 October 2020; Board 2 November 2020)
PDF: https://www.imf.org/-/media/files/publications/cr/2020/english/1mexea2020001.pdf (GUESSED; 200; 88 PDF pages). Read: KI (PDF p. 5),
pp. 9–10, Staff Appraisal (pp. 25–26).
- KI (PDF p. 5): over 85,000 deaths; 12 million lost jobs; working poverty rate 48%; output to shrink 9% in 2020; fiscal response muted;
  staff urges extra support of 2½–3½% of GDP and a credible medium-term tax reform; reforms needed "to reap the gains from USMCA".
- p. 9: USMCA took effect in July 2020 and positions Mexico to benefit from on-shoring of supply chains to North America, but reversals of
  the energy reform (cancelled auctions, airport, pipeline renegotiations, CFE rules favouring public generators, a cancelled brewery) raise
  uncertainty. p. 10: staff projects **−9.0% (2020)** and **3.5% (2021)** (table also gives Finance Ministry −8.0/4.6, consensus −9.8/3.3);
  output back to pre-crisis level by 2024; per-capita income below pre-pandemic for a decade.
- pp. 25–26: policy response "very conservative"; tax reform could raise 3–4% of GDP; Pemex strategy crowding out essential spending.

### MX-IMF-6. IMF, *Mexico: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 25/286, October 2025 (staff report 8 October 2025; Board 23 October 2025)
Issue page: https://www.imf.org/en/publications/cr/issues/2025/10/27/mexico-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-571378
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2025/english/1mexea2025001-source-pdf.pdf (from issue page;
200; 115 PDF pages). Latest Mexico AIV on the IMF Mexico page. Read: PR and PR table (PDF pp. 2–4), KI (PDF p. 5), p. 5 (Box 1), Staff
Appraisal (pp. 23–24), Annex VI (p. 67).
- KI (PDF p. 5): activity soft since mid-2024 (capacity limits, fiscal consolidation, tight money); US tariffs added to headwinds mainly via
  uncertainty; growth to pick up somewhat in 2026; main near-term risk is the trade relationship with the US. "Open trade is essential to
  ensure Mexico remains an attractive destination for investment".
- p. 5: as of July 2025 the applied effective US tariff on Mexico was closer to 5% because of rising USMCA-preference use. Box 1 (p. 5): with
  an assumed ~9% effective tariff, GIMF gives about −0.6% of GDP from tariffs and −0.4% from uncertainty: cumulative loss about 1% over three
  years.
- Annex VI, p. 67: dutiable share of US imports from Mexico rose from 8.6% to 18%; effective tariff 0.3% (January) → about 5% (July 2025)
  against a 13% statutory estimate; USMCA-preference use about 85% of exports to the US in July; the USMCA review is scheduled for 2026.
- pp. 23–24: debt-to-GDP drifting up to 61.5% by 2030 on authorities' plans; about 1½% of GDP of measures needed; Box 4 (p. 23) the 2024
  energy reform reverses parts of the 2013 reform (Pemex reclassified as a "public" SOE); further rate cuts should wait for clear evidence on
  core inflation.
- PR table (PR p. 3, PDF p. 4): real GDP 1.4 (2024), **1.0 (2025)**, **1.5 (2026)**; CPI eop 4.2/3.7/3.0, average 4.7/3.9/3.3; gross public
  debt 58.3/58.9/59.9% of GDP; CA −0.9/−0.2/−0.3% of GDP; reserves US$232.1/249.7/259.0 bn; GDP per capita US$14,034 (2024).

---

## Türkiye

### TR-IMF-1. IMF, "IMF Managing Director Sees Impressive Commitment by Turkey to Economic Reforms; Executive Board Approves US$16 Billion Stand-By Credit", press release, 4 February 2002
URL: https://www.imf.org/external/np/sec/pr/2002/pr0207.htm (GUESSED; 200). The press-release number is not shown in the fetched
(restructured) page text. No page numbers.
- Three-year SDR 12.8 bn (about US$16 bn) stand-by for 2002–04 replacing the December 1999 arrangement; SDR 7.3 bn (about US$9 bn) available
  at once.
- Achievements cited: move to a floating exchange rate, better fiscal position, bank restructuring. Priorities: restructure and privatise
  state banks, recapitalise private banks, cut public employment, base-money targets and preparation for formal inflation targeting.
- Numbers: after 11 September the 2002 external financing gap was US$10 bn by November 2001; lira up more than 20% since mid-October 2001;
  benchmark bond rate down more than 20 points to about 70%; program: **GNP growth 3% in 2002**, **CPI target 35% for 2002 from 68.5% in
  December 2001**, primary surplus 6.5% of GNP.

### TR-IMF-2. IMF, *Turkey: 2013 Article IV Consultation*, IMF Country Report No. 13/363, December 2013 (staff report 1 November 2013; Board 20 November 2013)
PDF: https://www.imf.org/external/pubs/ft/scr/2013/cr13363.pdf (GUESSED; 200; 71 PDF pages). Read: KI (PDF p. 2), Staff Appraisal
(pp. 28–29).
- KI (PDF p. 2): growth accelerating partly from pro-cyclical policies; CAD widening from a high level; inflation well above target; policies
  should cut external vulnerabilities "so Turkey can break free of its boom and bust cycles". Re-establish a nominal anchor; tighten fiscal
  (0.7% of GDP structural improvement in 2014).
- p. 28: 2013 growth expected 3.8%, **2014 forecast 3½%**; CAD above 7% of GDP in 2013 (gold imports); inflation above the 5% target this year
  and next. The CBRT framework is "complex" with too many objectives; positive real policy rates needed; FX sales only against excessive
  volatility. p. 29: banks sound but watch FX credit to corporates.

### TR-IMF-3. IMF, *Turkey: 2018 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 18/110, April 2018 (staff report 16 March 2018; Board 30 March 2018)
PDF: https://www.imf.org/-/media/files/publications/cr/2018/cr18110.pdf (GUESSED; 200; 82 PDF pages). Read: KI (PDF p. 6), p. 7, Staff
Appraisal (pp. 16–17), Table 1 (p. 25).
- KI (PDF p. 6): sharp 2017 rebound on stimulus after the 2016 coup-attempt slump; clear signs of overheating; monetary policy too loose with
  low credibility; on- and off-budget stimulus (credit guarantees, PPPs); CAD above 5% of GDP. Advice: front-loaded monetary tightening,
  contain quasi-fiscal stimulus, address highly leveraged corporates.
- p. 7: medium-term growth to fall to potential of 3½–4%; inflation in double digits in 2018; risks from large gross external financing needs,
  low reserves, short-term inflows, corporate FX exposure; bank loan-to-deposit ratio 123%. pp. 16–17: the input-intensive growth model is
  ripe for a reset.
- Table 1, p. 25: real GDP 3.2 (2016), 7.0 (2017), **4.4 (2018)**, **4.0 (2019)**; inflation average 11.1 (2017), **11.4 (2018)**, **10.5 (2019)**;
  end-year 11.9 (2017), 10.9 (2018); CAD 5.5% (2017); gross reserves US$107.7 bn; gross external debt 53.2% of GDP (2017); general government
  debt 28.5% (2017). (The forecasts were made five months before the August 2018 currency crisis.)

### TR-IMF-4. IMF, *Turkey: 2021 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 21/110, June 2021 (staff report 13 May 2021; Board 27 May 2021)
PDF: https://www.imf.org/-/media/files/publications/cr/2021/english/1turea2021001.pdf (GUESSED; 200; 95 PDF pages). Read: PR table (PDF
p. 5), KI (PDF p. 6), Staff Appraisal (pp. 30–31).
- KI (PDF p. 6): the initial pandemic response "set Turkey apart from its peers": rapid monetary and credit expansion gave positive 2020
  growth but raised inflation, dollarisation and the CAD and drained reserves; the late-2020 shift to tighter policy was undermined after the
  March 2021 change of central bank governor (lira weakened, spreads widened). Advice: no premature easing.
- pp. 30–31: net international reserves negative once FX swaps are subtracted; growth about **5¾% in 2021**, then about 3¼% a year from 2022;
  risk of premature relaxation.
- PR table (PDF p. 5): real GDP 0.9 (2019), 1.8 (2020), 5.8 (2021), 3.3 (2022); inflation average 12.3 (2020), **16.9 (2021)**, **14.9 (2022)**;
  end-year 14.6 (2020), 16.5 (2021); general government debt 39.5% (2020). (Report predates the September–December 2021 rate cuts, TR-CBRT-2.)

### TR-IMF-5. IMF, *Republic of Türkiye: 2024 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 24/312, October 2024 (staff report 12 September 2024; Board 27 September 2024)
PDF: https://www.imf.org/-/media/files/publications/cr/2024/english/1turea2024001-print-pdf.pdf (GUESSED; 200; 99 PDF pages; plain `.pdf`
and `-source-pdf` variants 404). Read: PR table (PDF p. 4), KI (PDF p. 5), Staff Appraisal (p. 29).
- KI (PDF p. 5): significant tightening since mid-2023 has cut crisis risks; ratings upgraded, risk premia halved; inflation to 43% end-2024;
  growth **3.0% (2024)** and **2.7% (2025)**, inflation 24% end-2025; staff wants a tighter stance for faster disinflation.
- p. 29: "A bold policy shift since mid-2023 has reduced economic imbalances and crisis risks"; inflation peaked at 75% y/y in May 2024; CAD
  4.0% of GDP (2023) → 2.2% (2024); minimum wage now indexed once a year.
- PR table (PDF p. 4): real GDP 11.4 (2021), 5.5 (2022), 5.1 (2023), 3.0 (2024), 2.7 (2025); inflation average 19.6 (2021), **72.3 (2022)**,
  53.9 (2023), 60.9 (2024), **33.0 (2025)**; end-year 64.3 (2022), 64.8 (2023); general government debt 30.8% (2022), 25.2% (2024).

### TR-IMF-6. IMF, *Republic of Türkiye: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 26/43, February 2026 (staff report 26 January 2026; Board 6 February 2026)
Issue page: https://www.imf.org/en/publications/cr/issues/2026/02/13/republic-of-trkiye-2025-article-iv-consultation-press-release-staff-report-and-statement-573962
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2026/english/1turea2026001-source-pdf.pdf (from issue page;
200; 115 PDF pages). Latest Türkiye AIV. Read: PR table (PDF p. 4), KI (PDF p. 5), Staff Appraisal (pp. 28–29).
- KI (PDF p. 5): deficit cut substantially in 2025 after the 2024 fiscal expansion; real rates still high despite cuts; inflation 31% y/y in
  December 2025, falling slowly; growth 4.0% y/y in 2025 Q1–Q3; on current policies inflation stays in double digits; staff recommends a
  decisive tightening that would bring inflation to single digits in 2027 (returning rates to end-2024 levels, phasing out credit-growth
  targets and scaling back FX intervention).
- p. 28: reserves reached US$184 bn; high inflation hurts financial deepening and widens wealth gaps.
- PR table (PDF p. 4): real GDP 3.3 (2024), 4.1 (2025), **4.2 (2026)**, 4.0 (2028–31); inflation average 58.5 (2024), 34.9 (2025), **25.9 (2026)**;
  end-year 44.4 (2024), 30.9 (2025), 23.0 (2026); general government debt 23.1% (2025); CAD 1.4% of GDP (2025–26).

### TR-CBRT-1. CBRT, "1 Week Repo" (Central Bank Interest Rates) table, accessed 23 Nov 2026
URL: https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Core+Functions/Monetary+Policy/Central+Bank+Interest+Rates/1+Week+Repo
(GUESSED; 200). Lending rate by effective date (own reading of the table, which starts 20 May 2010).
- 7.00% (May 2010) → 4.50% (May 2013) → **10.00% (29 Jan 2014, emergency hike)** → 7.50% (Feb 2015) → 8.00% (Nov 2016) → 17.75% (8 Jun 2018)
  → **24.00% (14 Sep 2018)** → 8.25% (May 2020) → 19.00% (19 Mar 2021) → cuts to 18 (24 Sep 2021), 16, 15, **14.00% (17 Dec 2021)** → 13, 12,
  10.5, 9.00% (25 Nov 2022) → 8.50% (24 Feb 2023) → **15.00% (23 Jun 2023)** → 17.5, 25, 30, 35, 40, 42.5, 45 → **50.00% (22 Mar 2024)** →
  first cut 47.50% (27 Dec 2024) → 42.50% (Mar 2025) → **46.00% (18 Apr 2025)** → 43, 40.5, 39.5, 38 (Dec 2025) → 37.00% (23 Jan 2026) →
  **36.00% (23 Oct 2026)**.

### TR-CBRT-2. CBRT, "Press Release on Interest Rates", No. 2021-42 (23 September 2021), 2023-22 (22 June 2023), 2026-12 (12 March 2026) and 2026-45 (22 October 2026); also 2021-33, 2023-25, 2026-17
Listing pages: https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2021 (and /2023, /2026) (GUESSED year
paths; 200). Each release URL taken from the listing, e.g. …/Press+Releases/2021/ANO2021-42 (200). HTML, no page numbers.
- 2021-33 (12 Aug 2021): policy rate held at 19%. **2021-42 (23 Sep 2021): cut from 19% to 18%**, with inflation rising; the MPC judged the
  recent rise to stem from supply-side factors (food and import prices, supply constraints, administered prices) and called them transitory.
- **2023-22 (22 Jun 2023): rise from 8.5% to 15%** under new Governor Erkan, to begin tightening, anchor expectations and stop the
  deterioration in pricing behaviour. 2023-25 (20 Jul 2023): 15% → 17.5%.
- 2026-12 (12 Mar 2026) and 2026-17 (22 Apr 2026): held at 37% (overnight lending 40%, borrowing 35.5%) amid geopolitical shock and higher
  energy prices, with coordinated fiscal measures. **2026-45 (22 Oct 2026): cut from 37% to 36%**; underlying inflation decelerating, domestic
  demand weak, energy prices an upside risk.

---

## South Africa

### ZA-IMF-1. IMF, *South Africa: 2008 Article IV Consultation—Staff Report; Staff Statement; Public Information Notice…*, IMF Country Report No. 08/348, October 2008 (staff report 15 August 2008; Board 8 September 2008)
PDF: https://www.imf.org/external/pubs/ft/scr/2008/cr08348.pdf (GUESSED; 200; 64 PDF pages). Read: title page, Executive Summary (PDF p. 3),
Table 1 (p. 26).
- Exec. Summary (PDF p. 3): after several years of high growth, shocks are slowing growth while food and fuel prices push inflation into double
  digits; strong investment, including a large public investment programme, widens the CAD worryingly; further tightening may be needed; the
  authorities more relaxed about financing the CAD.
- Table 1, p. 26: real GDP 5.0 (2005), 5.4 (2006), 5.1 (2007), **3.8 (2008 proj.)**, **3.7 (2009 proj.)**; CPI average 7.1 (2007), 11.3 (2008);
  CAD 7.3% (2007), 9.0% (2008), 9.6% (2009); national government debt 28.6% (2007) → 22.8% (2009). (Written before the Lehman collapse.)

### ZA-IMF-2. IMF, *South Africa: 2009 Article IV Consultation—Staff Report; Staff Statement and Supplement…*, IMF Country Report No. 09/273, September 2009 (staff report 20 July 2009)
PDF: https://www.imf.org/external/pubs/ft/scr/2009/cr09273.pdf (GUESSED; 200; 68 PDF pages). Read: Executive Summary (PDF p. 3), Staff
Appraisal (p. 24), Table 1 (p. 32).
- Exec. Summary: the global crisis pushed an already-slowing economy into recession (capital outflows late 2008, commodity slump);
  countercyclical policies (investment-led fiscal stimulus, monetary easing in H1 2009) appropriate; authorities aim to act well before net
  debt plus guarantees reaches their 50% of GDP limit.
- p. 24: robust expansion until recently, "an impressive achievement considering the challenges faced following the end of apartheid"; inflation
  targeting made policy focused and credible.
- Table 1, p. 32: real GDP 3.1 (2008), **−2.1 (2009 proj.)**, **1.9 (2010)**, 3.8 (2011), 4.5 (2013–14); CPI average 11.5 (2008), 7.4 (2009);
  CAD 7.4% (2008), 6.0% (2009); national government debt 27.3% (2008) → 33.6% (2014).

### ZA-IMF-3. IMF, *South Africa: 2017 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 17/189, July 2017 (staff report 9 June 2017)
PDF: https://www.imf.org/-/media/files/publications/cr/2017/cr17189.pdf (GUESSED; 200; 106 PDF pages). Read: PR table (PDF p. 5), KI (PDF p. 6).
- KI (PDF p. 6): improvements in living conditions since democracy have slowed; public debate questions whether the policy paradigm delivers
  for all; growth 1.0% (2017) and **1.2% (2018)** after a near-standstill in 2016; vulnerabilities rising from government debt, SOE contingent
  liabilities and perceptions of weakening governance; debt to reach 56% of GDP in 2020.
- PR table (PDF p. 5): real GDP 2.5 (2013), 1.7 (2014), 1.3 (2015), 0.3 (2016); gross government debt 44.1% (2013) → 51.7% (2016).

### ZA-IMF-4. IMF, *South Africa: 2018 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 18/246, July 2018 (staff report 29 June 2018; Board 25 July 2018)
PDF: https://www.imf.org/-/media/files/publications/cr/2018/cr18246.pdf (GUESSED; 200; 117 PDF pages). Read: PR table (PDF p. 5), KI (PDF
p. 6), p. 7, Staff Appraisal (p. 37), Annex II on Eskom (p. 53).
- KI (PDF p. 6): slow reforms, weakened governance and policy uncertainty keep growth subdued; public debt doubled in a decade; growth slightly
  below 2% over the medium term; advice: tackle corruption, restructure weak SOEs, labour-market and education reform.
- p. 7: the new administration's priorities are combating "state capture" (defined in footnote 3 as connected individuals influencing
  government decisions to benefit from public resources) and jobs; the FY17/18 consolidated deficit overshot the 3.1% target by more than 1
  point; Eskom's governance and liquidity problems needed bridge financing.
- p. 37: over five years "the South African economy has decoupled from the global growth recovery"; per-capita growth negative.
- Annex II, p. 53: Eskom's rising costs raised its debt and the risk to the sovereign; it needs R60–80 bn (about 1½% of GDP) a year.
- PR table (PDF p. 5): real GDP 1.8 (2014), 1.3 (2015), 0.6 (2016), 1.3 (2017), 1.5 (2018), **1.7 (2019)**; gross government debt 47.0% (2014)
  → 53.0% (2017) → 56.0% (2019); repo rate 7.0% (end-2016), 6.5% (end-2018 proj.).

### ZA-IMF-5. IMF, *South Africa: 2023 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 23/194, June 2023 (staff report 5 May 2023; Board 22 May 2023)
PDF: https://www.imf.org/-/media/files/publications/cr/2023/english/1zafea2023001.pdf (GUESSED; 200; 175 PDF pages). Read: PR table (PDF
p. 4), KI (PDF p. 5), Staff Appraisal (p. 29), Annex III (p. 64), ED statement (PDF p. 171).
- KI (PDF p. 5): the post-COVID recovery is "petering out": growth 4.9% (2021) → 2.0% (2022) amid the war in Ukraine, global tightening, floods
  and an unprecedented energy crisis; inflation above the band; urgent consolidation and reforms needed; FATF grey list exit to be pursued.
- p. 29: authorities pledge a clean break with the state-capture era; risk of long-term stagnation.
- Annex III, p. 64: rolling outages ("loadshedding") on almost 160 days in 2022, more than triple the fewer than 50 days of 2021; worse
  expected in 2023; firms with self-generation nearly tripled 2007–20.
- ED statement (PDF p. 171): SARB view that load-shedding cut 0.7% off real output in 2022.
- PR table (PDF p. 4): real GDP −6.3 (2020), 4.9 (2021), 2.0 (2022), **0.1 (2023)**, **1.8 (2024)**; CPI average 6.9 (2022); gross government
  debt 71.0% (2022) → 76.9% (2025); repo 7.0% (end-2022); reserves US$61.0 bn (2022).

### ZA-IMF-6. IMF, *South Africa: 2025 Article IV Consultation—Press Release; Staff Report; and Statement by the Executive Director*, IMF Country Report No. 26/34, February 2026 (staff report 22 January 2026; Board 9 February 2026)
Issue page: https://www.imf.org/en/publications/cr/issues/2026/02/10/south-africa-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-573842
(from country page; 200). PDF: https://www.imf.org/-/media/files/publications/cr/2026/english/1zafea2026001-source-pdf.pdf (from issue page;
000 timeout at first, 200 on retry; 109 PDF pages). Latest SA AIV. Read: PR table (PDF p. 4), KI (PDF p. 5), p. 26, Staff Appraisal (p. 31).
- KI (PDF p. 5): resilient to 2025 protectionism and uncertainty thanks to endowments, independent institutions and a strong monetary
  framework, but structural rigidities, infrastructure gaps, governance and rising debt constrain growth; growth 1.3–1.4% in 2025–26, 1.8%
  medium term; inflation to the **new lower 3% target** by end-2027; debt still rising.
- p. 26: under Operation Vulindlela electricity generation has stabilised (better Eskom performance, private and renewable generation);
  private participation in freight rail and the Durban port approved, but Transnet's balance sheet strained. "The current state-led
  development model appears to have reached its limits".
- p. 31: additional adjustment of ¾ point of GDP next year and ½ point in each of the following two years needed; a fiscal rule with a debt
  ceiling suggested; the lower target is an important achievement.
- PR table (PDF p. 4): real GDP 0.5 (2024), 1.3 (2025), **1.4 (2026)**, 1.7 (2028); CPI average 4.4 (2024), 3.2 (2025), **3.6 (2026)**; repo 7.8%
  (end-2024), 6.8% (end-2025); gross government debt 76.0% (2024) → 81.1% (2028); CAD 0.9% of GDP (2025).

### ZA-GOV-1. National Treasury (Republic of South Africa), *Budget Review 2026*, 25 February 2026 (RP05/2026)
Listing: https://www.treasury.gov.za/documents/national%20budget/2026/default.aspx (GUESSED; 200). PDF:
https://www.treasury.gov.za/documents/national%20budget/2026/review/FullBR.pdf (from listing; 200; 269 PDF pages). Read: Ch. 1 (pp. 1, 6),
Ch. 2 (pp. 11–12), Ch. 3 (p. 23).
- p. 1: growth estimated at 1.4% in 2025 (0.5% in 2024), rising to 2% in 2028; the debt ratio stabilises this fiscal year and declines
  thereafter. p. 6: gross loan debt stabilises at **78.9% of GDP in 2025/26**; consolidated deficit from 4.5% of GDP (2025/26) to 3.1%
  (2028/29); debt-service costs R420.6 bn (2025/26).
- p. 11: in November 2025 the Finance Minister announced a **3% inflation target with a ±1 point band**; growth 1.6% forecast for 2026.
  p. 12: **load-shedding suspended since May 2025**; freight rail volumes stabilised.
- p. 23: the 2026 Budget "marks a turning point for the public finances"; the gross debt ratio is stabilising for the first time since 2008.

---

## India links (Economic Surveys, on disk; not refetched)

### EM-IN-A-1. *Economic Survey 2013-14*, Ch. 2 (running footer "Issues and Priorities"), para 2.22–2.23, p. 33
- After the May 2013 US taper signal, capital left emerging markets and their currencies came under pressure; the rupee too (Figure 2.8).
  India, Brazil and Turkey responded by raising interest rates (Figure 2.9), keeping the cost of capital high. Pairs with BR-BCB-1 (Selic up
  from 7.25% in April 2013) and TR-CBRT-1 (Turkey's emergency rise to 10% in January 2014).

### EM-IN-A-2. *Economic Survey 2021-22*, Ch. 3 "External Sector", para 3.49 p. 105 and box text p. 111
- p. 105: the rupee depreciated 3.4% (December 2021 over March 2021), modest compared with EM peers such as the Turkish lira and Argentine
  peso. p. 111: in 2013 India was among the Fragile Five (footnote 7 lists Indonesia, South Africa, Brazil, Turkey and India); the Survey
  stresses India's "transformation from being among the Fragile Five countries" to the fourth-largest reserve holder.

### EM-IN-A-3. *Economic Survey 2022-23*, Ch. 2 "India's Medium-Term Growth Outlook: With Optimism and Hope", para 2.29, p. 36
- Capital flows and optimism about BRICS "triggered a domestic credit and investment boom that eventually proved unsustainable", as the twin
  deficit crisis of 2013 showed; private non-financial debt peaked at 113.6% of GDP (December 2010) and fell to 83.8% by December 2018.

### EM-IN-A-4. *Economic Survey 2022-23*, Ch. 5 "Prices and Inflation: Successful Tight-rope Walking", p. 118
- Among EMs Brazil's prices moderated in 2022, while Turkey's inflation was above 80% from August to November 2022 and 64.3% in December (cf.
  TR-IMF-5: 72.3% average for 2022).

### EM-IN-A-5. *Economic Survey 2023-24*, Ch. 3 "Prices and Inflation", para 3.6 and Charts III.3–III.4, p. 87
- India was within its 2–6% band in 2023 and had one of the lowest average deviations from target in 2021–23. Chart III.4 labels (own reading
  of the chart): South Africa 1.3, India 1.8, France 2.6, Mexico 3.4, USA 3.6, Brazil 3.9, Germany 4.0, UK 4.3, Russia 4.8 points. Notes: South
  Africa's target taken as the 4.5% midpoint of 3–6%; Brazil's target 3.75% (2021), 3.5% (2022), 3.25% (2023).

### EM-IN-A-6. *Economic Survey 2024-25*, Ch. 3 (external sector), para 3.66, p. 114
- In April 2024 – 6 January 2025 the rupee fell 2.9%, less than the Canadian dollar (5.4%), Korean won (8.2%) and **Brazilian real (17.4%)**;
  the Survey attributes rupee weakness mainly to broad dollar strength.

### EM-IN-A-7. *Economic Survey 2010-11*, Ch. 6 "Balance of Payments", Box 6.1 "BRIC Study Report", p. 135
- Explains the BRIC term (Goldman Sachs, 2001); BRIC finance ministers and central bank governors (London, 4 September 2009) commissioned a
  study of the BRIC role in the post-crisis world, noting that EMs helped the world economy absorb the crisis; India to anchor the study.

### EM-IN-A-8. *Economic Survey 2011-12*, Ch. 6, para 6.56–6.57, p. 144
- In the 2011 euro-area flight to the dollar, the Brazilian real (11.9%), Russian rouble (9.3%), Korean won (6.2%) and South African rand
  (17.63%) fell against the dollar between July and November 2011, as did the Mexican peso (no figure given): the rupee's fall was part of a
  wider EM move.

### EM-IN-A-9. *Economic Survey 2025-26*, Ch. 5 (inflation), para 5.6, p. 206
- EMDE growth averaged 4.2% with inflation outcomes varying widely; Brazil's headline inflation rose from 4.4% (2024) to 5.2% (2025) before
  easing as services inflation moderated (consistent with BR-IMF-5 and BR-BCB-2).

---

## Forecast vs outturn pairs (own arithmetic; outturns from WEO October 2026, `NGDP_RPCH.json` / `PCPIPCH.json`; 2025 values are
estimates and 2026 values are still WEO projections; WEO inflation is the annual average)

| Country | Report (date) | Forecast | Outturn (WEO Oct 2026) | Gap |
|---|---|---|---|---|
| Brazil | CR 12/191 (Jun 2012), Table 1 p. 32 | growth 2.5 for 2012; 4.6 for 2013 | 1.9 (2012); 3.0 (2013) | −0.6; −1.6 |
| Brazil | CR 13/312 (Jul 2013), Table 1 p. 45 | growth 3.2 for 2014 | 0.5 | −2.7 |
| Brazil | CR 16/348 (Oct 2016), Table 1 p. 30 | growth 0.5 for 2017; IPCA eop 5.0 for 2017 | 1.3; 3.4 (average) | +0.8; n/c |
| Brazil | CR 25/194 (Jun 2025), PR Table 1 PDF p. 5 | growth 2.3 (2025), 2.1 (2026); IPCA avg 5.3 (2025), 4.2 (2026) | 2.3, 2.2 (proj.); 5.0, 4.4 (proj.) | 0.0, +0.1; −0.3, +0.2 |
| Mexico | CR 09/53 (Jan 2009), Table 1 p. 36 | growth −0.3 for 2009 | −6.3 | −6.0 |
| Mexico | CR 09/126 (Apr 2009), p. 6 | growth about −3¾ for 2009 | −6.3 | about −2.5 |
| Mexico | CR 10/71 (Mar 2010), Table 1 p. 34 | growth 4.0 for 2010 | 5.0 | +1.0 |
| Mexico | CR 14/319 (Oct 2014), p. 15 | growth 3½ for 2015 | 2.7 | −0.8 |
| Mexico | CR 20/293 (Oct 2020), p. 10 | growth −9.0 (2020); 3.5 (2021) | −8.4; 6.0 | +0.6; +2.5 |
| Mexico | CR 25/286 (Oct 2025), PR table PDF p. 4 | growth 1.0 (2025); 1.5 (2026); CPI avg 3.9 (2025), 3.3 (2026) | 0.5; 1.5 (proj.); 3.8; 3.8 (proj.) | −0.5; 0.0; −0.1; +0.5 |
| Türkiye | PR 4 Feb 2002 (TR-IMF-1) | GNP growth 3 (2002); CPI target 35 (end-2002) | GDP 6.4; CPI avg 45.1 | +3.4 (GNP vs GDP); n/c |
| Türkiye | CR 13/363 (Nov 2013), p. 28 | growth 3½ for 2014 | 4.6 (current GDP series) | +1.1 |
| Türkiye | CR 18/110 (Mar 2018), Table 1 p. 25 | growth 4.4 (2018), 4.0 (2019); inflation avg 11.4 (2018), 10.5 (2019) | 3.5, 1.3; 16.3, 15.2 | −0.9, −2.7; +4.9, +4.7 |
| Türkiye | CR 21/110 (May 2021), p. 31 / PR table PDF p. 5 | growth 5¾ (2021); inflation avg 16.9 (2021), 14.9 (2022) | 11.8; 19.6, 72.3 | +6.1; +2.7, **+57.4** |
| Türkiye | CR 24/312 (Sep 2024), KI PDF p. 5 / PR table PDF p. 4 | growth 2.7 (2025); inflation avg 33.0 (2025) | 3.7; 34.9 | +1.0; +1.9 |
| Türkiye | CR 26/43 (Jan 2026), PR table PDF p. 4 | growth 4.2 (2026); inflation avg 25.9 (2026) | 2.7 (proj.); 31.2 (proj.) | −1.5; +5.3 |
| South Africa | CR 08/348 (Aug 2008), Table 1 p. 26 | growth 3.7 for 2009 | −1.5 | −5.2 |
| South Africa | CR 09/273 (Jul 2009), Table 1 p. 32 | growth −2.1 (2009); 1.9 (2010) | −1.5; 3.0 | +0.6; +1.1 |
| South Africa | CR 17/189 (Jun 2017), KI PDF p. 6 | growth 1.2 for 2018 | 1.6 | +0.4 |
| South Africa | CR 18/246 (Jun 2018), PR table PDF p. 5 | growth 1.7 for 2019 | 0.3 | −1.4 |
| South Africa | CR 23/194 (May 2023), PR table PDF p. 4 | growth 0.1 (2023); 1.8 (2024) | 0.8; 0.5 | +0.7; −1.3 |
| South Africa | CR 26/34 (Jan 2026), PR table PDF p. 4 | growth 1.4 (2026); CPI avg 3.6 (2026) | 1.0 (proj.); 4.4 (proj.) | −0.4; +0.8 |

n/c = not comparable (end-period forecast or target against an annual average). Strongest boxes: Mexico 2009 (January forecast −0.3, outturn
−6.3); South Africa 2009 (3.7 vs −1.5); Türkiye 2022 inflation (14.9 vs 72.3); Brazil 2014 (3.2 vs 0.5).

---

## Already in the book (cite; not refetched)
- `IMF_2000-2002.md`, IEO evaluation of the IMF in Argentina, p. 3: after Brazil's early-1999 devaluation staff began to doubt the
  Argentine peg.
- `IMF_2010-2014.md`, WEO October 2013 Ch. 1 figure (p. 10): Brazilian real, rupee and rand fell 8–16% against the dollar in 2013.
- `IMF_2014-2019.md`, WEO October 2019 Ch. 1 p. 9: distress in Argentina, Iran, Turkey and Venezuela explains about half the fall in world
  growth from 3.8% (2017) to 3.0% (2019).
- `IMF_2020-2021.md`, WEO April 2020: Exec. Summary p. vii (South Africa among EMs giving significant fiscal support); Ch. 1 p. 3 (rate cuts
  by Brazil, Mexico, South Africa and others).
- `IMF_2022-2023.md`, WEO April 2022 Ch. 1 p. 5: Brazil had raised rates 975 bp over the past year.
- `IMF_2024-2025.md`: WEO April 2024 Ch. 1 p. 6 (Brazil and Chile raised early and already cut); WEO April 2025 Exec. Summary p. xv and
  Ch. 1 p. 11, Box 1.2 p. 32 (2025 US tariffs on Mexico with USMCA carve-out; effective tariff up about 15 points for Mexico); WEO Update July
  2025 p. 6 (large deficits in Brazil, France, US may raise term premiums).
- `IMF_2026.md`: WEO April 2026 Ch. 1 p. 12 (Brazil +0.2 point in 2026 as net energy exporter; Türkiye cut 0.8 point to 3.4%); WEO October
  2026 CSF p. 31 (Brazil among suppliers replacing Gulf oil).
- `Theme_debt.md` DF-IMF-1 p. 16 (Brazil, India, South Africa need reforms to budget rigidities); DF-IMF-2 Table p. 3 (Brazil gross debt
  87.1 / 93.3 / 106.5) and p. 13 (India, Mexico and Türkiye restrained primary spending); DF-IMF-6 p. 76 (Mexico 2016 SOE transfers).
- `Theme_markets.md` MK-OTH-2 (Bernanke 2005: Mexico 1994, Brazil 1999 crises behind reserve build-up); **MK-OTH-7 (BIS 84th Annual Report,
  pp. 28–29: in the 2013 taper episode Brazil, India, Indonesia, South Africa and Turkey currencies fell more than 10%; Brazil, India,
  Indonesia and Russia each lost more than $10 bn of reserves)**; MK-IN-4 p. 47, MK-IN-6, MK-IN-7 (valuation and market-cap comparisons with
  Brazil).
- `Theme_money.md` MO-IMF-4 pp. 41, 49 (Brazil, Chile, Mexico hiked early in the "Great Tightening"); MO-IMF-5; MO-IN-4 para 46 (Brazil
  lowered its target from 8% to 2.5% — check context there).
- `Theme_growth.md` GR-WB-1 pp. 19–20 (Brazil among the 13 high-growth economies; its growth faded after the second oil shock); GR-IMF-4
  p. 67 (five big EMs incl. Brazil drove much of the medium-term downgrade).
- `Theme_trade.md` TR-IMF-3 p. 99 (Brazil among the most FDI-vulnerable large EMs); TR-IMF-4 (2025–26 tariffs on Mexico); TR-IN-3 (export
  concentration: Brazil, Mexico vs India).
- `Theme_demography.md` DL-WB-1 (South African youth unemployment), DL-WB-3 (Mexico fertility), DL-OTH-4 (Mexico second remittance recipient,
  US$67.64 bn in 2024). `Theme_development.md` DV-WB-9 (WDR 2006 South African children example), DV-OTH-3 (Brazil very unequal).
  `Theme_energy.md` EN-WB-8 (Brazil and Türkiye preparing carbon pricing). `Theme_technology.md` TE-WB-3 (Pix), TE-IMF-1 p. 8 (AI exposure
  41% in Brazil).

---

## Not obtained
- IMF eLibrary search https://www.elibrary.imf.org/search?q=Brazil+Article+IV… — **403** (CloudFront "Request blocked"); not retried.
- IMF CR listings: https://www.imf.org/external/pubs/cat/scr1.cfm?country=Brazil — **403**; https://www.imf.org/en/publications/cr/index.md —
  404; https://www.imf.org/en/publications/search?series=IMF+Staff+Country+Reports&country=Brazil — 404. Old country page
  /external/country/BRA/index.htm (200) only redirects to the new page; /external/country/BRA/rr/index.htm (200, 392 bytes, empty).
- Country page variants: BRA, MEX `index.md`/`index.json` — 429 (rate limit) at first pass; BRA HTML and JSON later 200; MEX variants not
  retried (HTML page sufficed).
- **Brazil early-2000s Article IV** (2002–05): not found. Tried CR 03/001 (404) and 05/366 (Iceland Selected Issues, deleted). Replaced by
  BR-IMF-1 (PR 02/40).
- **Brazil 2011 Article IV**: tried 11/216 (Spain), 11/217, 11/218, 11/219 (Kuwait), 10/217 (an EFM review, other country), 10/218 (Cape
  Verde) — all wrong, deleted. 2012 report (BR-IMF-2) used instead. Brazil 2024 AIV: 1braea2024001-source-pdf.pdf — 404 (not pursued).
- **Türkiye 2019 Article IV** (after the 2018 crisis): cr19395 tried on the wrong-era pattern (404), 1turea2019001.pdf (404),
  1turea2019001-print-pdf.pdf (404), 1turea2019002.pdf (404). Türkiye 2022: 1turea2022001.pdf (404). Not obtained.
- Türkiye 2024: 1turea2024001.pdf and -source-pdf.pdf — 404 (the -print-pdf file worked). South Africa 2024: 1zafea2024001.pdf and
  -source-pdf.pdf — 404 (not needed).
- Mexico 2018–19: cr18307.pdf (404), 1mexea2019001.pdf (404); USMCA-period coverage taken from CR 20/293 instead.
- South Africa CR 10/314 — Panama 2010 AIV (wrong; deleted). Wrong-sequence probes 1turea2021110 / 1mexea2019336 (404) before the sequence
  rule was understood.
- Turkey 2002 press release search: pr0203 (Chad), pr0204 (Cambodia), pr0205 (IMF–World Bank conference), pr0206 (Peru) — wrong, deleted;
  pr0130 and pr0108 — 404.
- BCB: whole-period SGS request — 406 (10-year window limit); 2010–19 window — 502 once, then 200. Copom detail endpoints
  `copom/comunicadoDetalhes?nro_reuniao=277` and `copom/comunicados?nro_reuniao=277` — 500. Copom list starts only at meeting 202
  (October 2016), so 2003 and 2015 statements were not obtained (rates from the SGS series instead).
- SARB MPC statements page https://www.resbank.co.za/en/home/publications/statements/mpc-statements — 200, but statement links are not in
  the static HTML (script-rendered); no SARB statement obtained.
- Banxico (Mexico) primary documents: not attempted (time); folder `mx/` empty.
- Fetched and title-checked but not read in depth: South Africa CR 16/217 (2016 AIV) and CR 20/33 (2019 AIV, January 2020).

---

## Bibliography rows

| Key | Title | Publisher | Year | Edition / report no. | URL |
|---|---|---|---|---|---|
| imf-pr-bra-2002 | IMF Approves US$30.4 Billion Stand-By Credit for Brazil | IMF | 2002 | PR 02/40 | https://www.imf.org/external/np/sec/pr/2002/pr0240.htm |
| imf-bra-2012 | Brazil: 2012 Article IV Consultation | IMF | 2012 | CR 12/191 | https://www.imf.org/external/pubs/ft/scr/2012/cr12191.pdf |
| imf-bra-2013 | Brazil: Staff Report for the 2013 Article IV Consultation | IMF | 2013 | CR 13/312 | https://www.imf.org/external/pubs/ft/scr/2013/cr13312.pdf |
| imf-bra-2016 | Brazil: 2016 Article IV Consultation | IMF | 2016 | CR 16/348 | https://www.imf.org/external/pubs/ft/scr/2016/cr16348.pdf |
| imf-bra-2025 | Brazil: 2025 Article IV Consultation | IMF | 2025 | CR 25/194 | https://www.imf.org/-/media/files/publications/cr/2025/english/1braea2025001-source-pdf.pdf |
| bcb-selic | Meta Selic definida pelo Copom (SGS 432) | Banco Central do Brasil | 2026 | series 432 | https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json |
| bcb-copom | Copom statements, meetings 202, 271, 277, 282 | Banco Central do Brasil | 2016–2026 | comunicados | https://www.bcb.gov.br/api/servico/sitebcb/copom/comunicados_detalhes?nro_reuniao=282 |
| imf-mex-2009a | Mexico: 2008 Article IV Consultation | IMF | 2009 | CR 09/53 | https://www.imf.org/external/pubs/ft/scr/2009/cr0953.pdf |
| imf-mex-fcl-2009 | Mexico: Arrangement Under the Flexible Credit Line | IMF | 2009 | CR 09/126 | https://www.imf.org/external/pubs/ft/scr/2009/cr09126.pdf |
| imf-mex-2010 | Mexico: 2010 Article IV Consultation | IMF | 2010 | CR 10/71 | https://www.imf.org/external/pubs/ft/scr/2010/cr1071.pdf |
| imf-mex-2014 | Mexico: 2014 Article IV Consultation | IMF | 2014 | CR 14/319 | https://www.imf.org/external/pubs/ft/scr/2014/cr14319.pdf |
| imf-mex-2020 | Mexico: 2020 Article IV Consultation | IMF | 2020 | CR 20/293 | https://www.imf.org/-/media/files/publications/cr/2020/english/1mexea2020001.pdf |
| imf-mex-2025 | Mexico: 2025 Article IV Consultation | IMF | 2025 | CR 25/286 | https://www.imf.org/-/media/files/publications/cr/2025/english/1mexea2025001-source-pdf.pdf |
| imf-pr-tur-2002 | Executive Board Approves US$16 Billion Stand-By Credit (Turkey) | IMF | 2002 | press release, 4 Feb 2002 | https://www.imf.org/external/np/sec/pr/2002/pr0207.htm |
| imf-tur-2013 | Turkey: 2013 Article IV Consultation | IMF | 2013 | CR 13/363 | https://www.imf.org/external/pubs/ft/scr/2013/cr13363.pdf |
| imf-tur-2018 | Turkey: 2018 Article IV Consultation | IMF | 2018 | CR 18/110 | https://www.imf.org/-/media/files/publications/cr/2018/cr18110.pdf |
| imf-tur-2021 | Turkey: 2021 Article IV Consultation | IMF | 2021 | CR 21/110 | https://www.imf.org/-/media/files/publications/cr/2021/english/1turea2021001.pdf |
| imf-tur-2024 | Republic of Türkiye: 2024 Article IV Consultation | IMF | 2024 | CR 24/312 | https://www.imf.org/-/media/files/publications/cr/2024/english/1turea2024001-print-pdf.pdf |
| imf-tur-2026 | Republic of Türkiye: 2025 Article IV Consultation | IMF | 2026 | CR 26/43 | https://www.imf.org/-/media/files/publications/cr/2026/english/1turea2026001-source-pdf.pdf |
| cbrt-repo | 1 Week Repo (Central Bank Interest Rates) | CBRT | 2026 | web table | https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Core+Functions/Monetary+Policy/Central+Bank+Interest+Rates/1+Week+Repo |
| cbrt-pr-2021-42 | Press Release on Interest Rates | CBRT | 2021 | No. 2021-42 | https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2021/ANO2021-42 |
| cbrt-pr-2023-22 | Press Release on Interest Rates | CBRT | 2023 | No. 2023-22 | https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2023/ANO2023-22 |
| cbrt-pr-2026-45 | Press Release on Interest Rates | CBRT | 2026 | No. 2026-45 | https://www.tcmb.gov.tr/wps/wcm/connect/EN/TCMB+EN/Main+Menu/Announcements/Press+Releases/2026/ANO2026-45 |
| imf-zaf-2008 | South Africa: 2008 Article IV Consultation | IMF | 2008 | CR 08/348 | https://www.imf.org/external/pubs/ft/scr/2008/cr08348.pdf |
| imf-zaf-2009 | South Africa: 2009 Article IV Consultation | IMF | 2009 | CR 09/273 | https://www.imf.org/external/pubs/ft/scr/2009/cr09273.pdf |
| imf-zaf-2017 | South Africa: 2017 Article IV Consultation | IMF | 2017 | CR 17/189 | https://www.imf.org/-/media/files/publications/cr/2017/cr17189.pdf |
| imf-zaf-2018 | South Africa: 2018 Article IV Consultation | IMF | 2018 | CR 18/246 | https://www.imf.org/-/media/files/publications/cr/2018/cr18246.pdf |
| imf-zaf-2023 | South Africa: 2023 Article IV Consultation | IMF | 2023 | CR 23/194 | https://www.imf.org/-/media/files/publications/cr/2023/english/1zafea2023001.pdf |
| imf-zaf-2026 | South Africa: 2025 Article IV Consultation | IMF | 2026 | CR 26/34 | https://www.imf.org/-/media/files/publications/cr/2026/english/1zafea2026001-source-pdf.pdf |
| nt-zaf-br-2026 | Budget Review 2026 | National Treasury, South Africa | 2026 | RP05/2026 | https://www.treasury.gov.za/documents/national%20budget/2026/review/FullBR.pdf |
| es-2013-14 | Economic Survey 2013-14 | Ministry of Finance, India | 2014 | Ch. 2 | on disk (es2013-14.txt) |
| es-2021-22 | Economic Survey 2021-22 | Ministry of Finance, India | 2022 | Ch. 3 | on disk (es2021-22.txt) |
| es-2022-23 | Economic Survey 2022-23 | Ministry of Finance, India | 2023 | Chs. 2, 5 | on disk (es2022-23.txt) |
| es-2023-24 | Economic Survey 2023-24 | Ministry of Finance, India | 2024 | Ch. 3 | on disk (es2023-24.txt) |
| es-2024-25 | Economic Survey 2024-25 | Ministry of Finance, India | 2025 | Ch. 3 | on disk (es2024-25.txt) |
| es-2010-11 | Economic Survey 2010-11 | Ministry of Finance, India | 2011 | Ch. 6, Box 6.1 | on disk (es2010-11.txt) |
| es-2011-12 | Economic Survey 2011-12 | Ministry of Finance, India | 2012 | Ch. 6 | on disk (es2011-12.txt) |
| es-2025-26 | Economic Survey 2025-26 | Ministry of Finance, India | 2026 | Ch. 5 | on disk (es2025-26.txt) |
