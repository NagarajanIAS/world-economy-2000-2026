# Reading notes: theme chapter "Technology and the productivity puzzle, 2000–2026" (read 23 Nov 2026)

Method: every document was fetched with plain `curl -sL` (default user-agent, no custom headers). URLs were taken from publisher listing
or issue pages (openknowledge.worldbank.org via its search and item APIs, imf.org WEO and Staff Discussion Note listings, nber.org paper
pages, brookings.edu, oxfordmartin.ox.ac.uk, larrysummers.com, bis.org, itu.int, fred.stlouisfed.org, pib.gov.in, trai.gov.in and
rbi.org.in); any guessed URL is flagged. Downloads are in the session scratchpad folder `tech_dl/` (subfolders `wb/`, `imf/`, `oth/`,
`in/`). PDFs were converted with `pdftotext` (plain and `-layout`) and read in the text. Economic Survey texts were not refetched: they were
read from the Econ Subject folder (`sources/text/es*.txt`, page found by counting form feeds) and checked against the PDFs in
`sources/economic-surveys/` for printed page numbers. Quotes are verbatim, under 15 words, copied from the converted text; everything else
is paraphrase. Page numbers are printed page numbers unless stated (PDF page numbers are marked "PDF").

Item labels: TE-WB-n (World Bank), TE-IMF-n (IMF), TE-OTH-n (OECD, BIS, ITU, academic, other), TE-IN-n (India). Indian years are fiscal
or survey years (2022-23, FY25). TFP = total factor productivity; GPT = general-purpose technology; ICT = information and communication
technology; EMDE = emerging market and developing economy; AE = advanced economy; DPI = digital public infrastructure; JAM = Jan Dhan,
Aadhaar, Mobile; GCC = global capability centre; WDR = World Development Report; GEP = Global Economic Prospects; WEO = World Economic
Outlook; SDN = Staff Discussion Note.

Note on a brief title: the brief's "Productivity Revisited (Dieppe ed., 2021)" conflates two World Bank books. *Productivity Revisited*
is Cusolito and Maloney (2018; TE-WB-6); the 2021 volume edited by Alistair Dieppe is *Global Productivity: Trends, Drivers, and
Policies* (TE-WB-4). Both were read.

---

## World Bank

### TE-WB-1. World Bank, *World Development Report 2016: Digital Dividends*, Overview booklet, 2016 (OKR issue date 13 January 2016)
Listing: OKR item https://hdl.handle.net/10986/23347 (found via the OKR search API
https://openknowledge.worldbank.org/server/api/discover/search/objects). Overview PDF ("210671EnSum.pdf" in that item):
https://openknowledge.worldbank.org/bitstreams/5fa7b45d-7986-56f0-a7c2-e172ce198823/download (58 PDF pages; printed p. 2 = PDF 14,
printed = PDF − 12). Read: foreword (PDF 7–8, signed by Jim Yong Kim), overview pp. 2–6, grepped the rest (pp. 21–22).
- Foreword (PDF 7): calls the moment the greatest information and communications revolution in history; more than 40 percent of the
  world's population has internet access; nearly 7 in 10 of the poorest fifth of households have a mobile phone; 2.4 billion people lack
  formal ID; nearly 6 billion lack high-speed internet. Where fundamentals are weak, digital technologies "have not boosted productivity
  or reduced inequality" (paraphrase of the passage).
- p. 2: internet users more than tripled in a decade, from 1 billion (2005) to an estimated 3.2 billion (end-2015). India's Aadhaar is the
  lead example of a digital ID that helps governments include disadvantaged groups. The effect of technology on global productivity has
  been less than expected: firms are more connected than ever, "but global productivity growth has slowed"; labour markets more
  polarised. "So, while digital technologies have been spreading, digital dividends have not." Nearly 60 percent of people still offline.
- p. 3 (figure O.2): the pessimism about the global outlook is "not because of digital technologies, but in spite of them"; panel a is
  median labour-productivity growth per hour in 87 countries.
- p. 6: only 31 percent of people in developing countries had internet access in 2014 vs 80 percent in high-income countries; India in the
  top five by number of users (after China and the United States).
- pp. 21–22: polarisation ("hollowing out") of labour markets is now visible in many developing countries too: high- and low-skill shares
  up, middle-skill share down (figure O.17, circa 1995–2012).

### TE-WB-2. World Bank, *World Development Report 2019: The Changing Nature of Work*, Overview, 2019 (OKR item dated 2019)
Listing: OKR item https://hdl.handle.net/10986/30435 (OKR search API). Overview PDF ("211328ov.pdf"):
https://openknowledge.worldbank.org/bitstreams/ceac2402-00a1-53ef-af36-d8090adef9ed/download (32 PDF pages; printed p. 2 = PDF 12,
printed = PDF − 10; foreword pp. vii–viii = PDF 9–10, signed by Jim Yong Kim). Read: foreword, overview pp. 2–7.
- p. vii: fear that "machines are coming to take our jobs" is centuries old; robots are taking over thousands of routine tasks and will
  eliminate many low-skill jobs, but technology also creates opportunities.
- p. viii: four out of five people in developing countries have never had social protection; 2 billion work informally.
- p. 2: the scenario of mass job loss is "on balance unfounded"; routine "codifiable" jobs are the most vulnerable.
- p. 4: eight in 10 people in developing countries receive no social assistance and 6 in 10 work informally; calls for a "new social
  contract" (investment in human capital plus progressively universal social protection).
- p. 6: "the threat to jobs from technology is exaggerated"; industrial employment share stable at about 10 percent in low-income countries
  (1991–2017) and about 23 percent in upper-middle-income; lower-middle-income rose from 16 to 19 percent; Vietnam 9 → 25 percent. Flipkart
  (India) cited as an example of platform firms.

### TE-WB-3. World Bank, *World Development Report 2026: The Promise of Artificial Intelligence*, Overview booklet, 2026 (title confirmed on the booklet cover and PDF metadata)
Listing: OKR item https://hdl.handle.net/10986/45296. Overview PDF:
https://openknowledge.worldbank.org/bitstreams/2caf7522-b4b1-4733-b086-3e5ae801ba4d/download (68 PDF pages; foreword pp. vii–ix = PDF
9–11, signed by Indermit Gill; overview printed = PDF − 22). Read: foreword; overview pp. 1–15; grepped the rest.
- p. vii (foreword): if handled well, AI could lift global growth "to its strongest pace since the golden years of the 2000s"; even the
  worst-case estimates put developing-economy potential growth above the average of the first half of the 2020s; "development progress
  has dipped to a 75-year low". Risks: call-centre and entry-level software, finance and business-services jobs; electricity and water
  shortages; dependence on foreign technology. Britain was about four times richer per person than India at the start of the Industrial
  Revolution and 10 times by the end of the 20th century.
- p. viii (foreword): less than a tenth of developing-economy jobs are susceptible to AI automation vs more than a third in high-income
  economies; one in six would be enhanced. AI weather forecasts saved up to $560 per small farmer in Telangana. India's UPI and Brazil's
  Pix offered as models of interoperable, multi-provider systems.
- p. 8: adoption lags have shrunk: steam about 80 years between rich and poorer countries, electricity 40, computers and internet 20. At
  ChatGPT's launch (November 2022) over 70 percent of traffic came from the United States; within six months middle-income countries
  accounted for half.
- p. 10: computers did not raise productivity at once because businesses needed years to change workflows (the electricity-factory
  analogy).
- p. 11: the biggest US AI companies are expected to spend more than $750 billion on AI infrastructure in 2026 alone; in 2025 more than
  half the users of ChatGPT, Claude, DeepSeek and Gemini were in developing countries.
- p. 14: in low- and middle-income countries about 4.5 percent of existing jobs are amenable to automation by generative AI vs 14.2
  percent in high-income countries; 16.2 percent amenable to complementing. In India, generative AI reduced monthly job postings for the
  white-collar occupations most amenable to AI, hitting entry-level workers hardest. India's Sarvam AI cited as a model built from scratch
  for local languages (pp. 2, 14).
- p. 15: about one-fifth of small firms (5–19 employees) in India, Jordan, Kenya, Mexico, Nigeria and Thailand use AI chatbots vs
  one-fourth in the United States (Enterprise Survey on AI Adoption; India sample 1,355 firms).
- Booklet front matter carries an AI disclosure statement: several AI models (named there, including Claude models) were used for coding
  and labelling data, and an internal ChatGPT/Copilot interface to edit earlier drafts.
- Inconsistency to note: the foreword's "less than a tenth" vs "more than a third" and the overview's 4.5 vs 14.2 percent describe job
  exposure on apparently different measures; the booklet does not reconcile them.

### TE-WB-4. Alistair Dieppe (ed.), *Global Productivity: Trends, Drivers, and Policies*, World Bank, 2021 (OKR issue date 4 June 2021)
Listing: OKR item https://hdl.handle.net/10986/34015 (OKR search API, query "Global Productivity" Dieppe). PDF ("9781464816086.pdf"):
https://openknowledge.worldbank.org/bitstreams/2281cca1-9ae3-5550-9ab0-e09bc4004096/download (463 PDF pages; foreword p. xv = PDF 17,
signed by Ceyla Pazarbasioglu; introduction printed = PDF − 26). Read: foreword; introduction pp. 3–7.
- p. xv: COVID-19 caused the deepest recession since World War II; per capita incomes fell in more than 90 percent of countries in 2020,
  the largest share since 1870. The pandemic followed "a steep, broad-based slowdown" in productivity growth after 2007–09, affecting
  about 70 percent of advanced economies and EMDEs and more than 80 percent of the world's extreme poor.
- p. 3: the top quarter of EMDEs by labour-productivity growth cut extreme poverty by more than 1 point a year (1981–2015); poverty rose
  in the bottom quarter. Digital technologies are among innovations that had promised large gains.
- p. 4 (figure 1): EMDE productivity levels are below 20 percent of the advanced-economy average.
- p. 6: global labour-productivity growth fell from a peak of 2.8 percent (2007) to a trough of 1.4 percent (2016), and stayed below 2.0
  percent in 2017–18.
- p. 7: EMDE productivity growth fell from 6.6 percent (2007) to 3.1 percent (2015), the steepest, longest and most synchronised multiyear
  slowdown in recent decades; LIC labour productivity just 2 percent of the AE average (2010–18); the slowdown came from weaker investment
  and slower TFP growth "in approximately equal measures"; fundamental drivers (working-age population, education, global value chains)
  weakened.
- Vintage note: GEP January 2020 (TE-WB-5) gave 2.7 → 1.5 percent and an EMDE trough of 3.2 percent; this 2021 book gives 2.8 → 1.4 and
  3.1. Same authors, revised data.

### TE-WB-5. World Bank, *Global Economic Prospects, January 2020: Slow Growth, Policy Challenges*, Chapter 3 "Fading Promise: How to Rekindle Productivity Growth" (OKR issue date 8 January 2020)
Listing: OKR item https://hdl.handle.net/10986/33044 (OKR search API). Full-report PDF ("9781464814693.pdf"):
https://openknowledge.worldbank.org/bitstreams/b202130d-78f2-5b2c-91b0-becd457dbe05/download (334 PDF pages; chapter 3 starts p. 191 =
PDF 213; printed = PDF − 22; executive summary p. xvii = PDF 19). Read: executive summary paragraph; chapter 3 pp. 193–194.
- p. xvii and p. 193: a broad-based slowdown in labour-productivity growth has been under way since the global financial crisis; in EMDEs it
  reflects weak investment, moderating efficiency gains and dwindling reallocation between sectors; key drivers (education,
  urbanisation, institutions) have slowed or stagnated. Chapter prepared by Alistair Dieppe and Gene Kindberg-Hanlon; data for 29 AEs and
  74 EMDEs, 1981–2018.
- p. 193: the average EMDE worker produces less than one-fifth of the output of an AE worker.
- p. 194: global labour-productivity growth fell from 2.7 percent (2007) to 1.5 percent (2016) and was 1.9 percent in 2018; the slowdown
  hit nearly 70 percent of AEs and EMDEs and over 80 percent of the extreme poor. In AEs it continues a trend under way "since the late
  1990s"; in EMDEs the fall from 6.6 percent (2007) to 3.2 percent (2015) was "the steepest, longest, and broadest yet". At current rates,
  halving the EMDE–AE productivity gap would take over a century. In AEs slower capital deepening explains most of the 2013–18 slowdown
  relative to 2003–08.

### TE-WB-6. Ana Paula Cusolito and William F. Maloney, *Productivity Revisited: Shifting Paradigms in Analysis and Policy*, Overview, World Bank, 2018 (OKR issue date 25 October 2018)
Listing: OKR item https://hdl.handle.net/10986/30588 (OKR search API, query "Productivity Revisited"). Overview PDF ("211334ov.pdf"):
https://openknowledge.worldbank.org/bitstreams/9c698cc1-dfb3-5dc5-bccf-252894f62186/download (37 PDF pages; overview p. 4 = PDF 19).
Read: preface (PDF 9) and overview pp. 1–7 (PDF 16–22).
- Preface (PDF 9): productivity accounts for half of cross-country differences in GDP per capita, yet productivity growth has slowed
  globally.
- PDF 16 and p. 4: "There is little consensus" on what slowed the productivity engine (declining dynamism is one school); the book calls
  the global slowdown the "first puzzle" and slow catch-up by followers the second.
- p. 5 (PDF 20): in a decomposition of manufacturing productivity growth, reallocation between firms is marginally the dominant
  contributor in India. PDF 22: Chile and India evidence shows trade liberalisation's productivity effect depends on market structure.

---

## IMF

### TE-IMF-1. Mauro Cazzaniga, Florence Jaumotte, Longji Li, Giovanni Melina, Augustus J. Panton, Carlo Pizzinelli, Emma Rockall and Marina M. Tavares, "Gen-AI: Artificial Intelligence and the Future of Work", IMF Staff Discussion Note SDN/2024/001, January 2024
Listing: SDN listing https://www.imf.org/en/Publications/SPROLLs/Staff-Discussion-Notes → issue page
https://www.imf.org/en/publications/staff-discussion-notes/issues/2024/01/14/gen-ai-artificial-intelligence-and-the-future-of-work-542379.
PDF: https://www.imf.org/-/media/files/publications/sdn/2024/english/sdnea2024001.pdf (42 PDF pages; executive summary p. 2 = PDF 4;
printed = PDF − 2). Read: abstract, executive summary, section II.
- Abstract (PDF 2): AEs will feel AI's benefits and pitfalls sooner than EMDEs because their jobs are cognitive-intensive; women and
  college-educated workers are more exposed but better placed to benefit; if productivity gains are large enough, "income levels could
  surge for most workers"; EMDEs should prioritise digital infrastructure and skills. An editor's note (1 March 2024) records a correction
  to Annex Table 5.1 (AI Preparedness Index).
- p. 2: "Almost 40 percent of global employment is exposed to AI"; about 60 percent in AEs, of which roughly half may be hurt and half
  helped; 40 percent in emerging markets, 26 percent in low-income countries. Unlike earlier automation, which hit middle-skill workers
  hardest, AI's displacement risk reaches high earners; with high complementarity labour-income inequality rises; capital returns raise
  wealth inequality.
- p. 8 (PDF 10): high-exposure employment ranges from 41 percent in Brazil to 26 percent in India; most Indian workers are craftspeople,
  farm workers or elementary workers, mostly low exposure (India data from the Periodic Labour Force Survey).

### TE-IMF-2. IMF, *World Economic Outlook, April 2024*, Chapter 3 "Slowdown in Global Medium-Term Growth: What Will It Take to Turn the Tide?" (authors Nan Li and Diaa Noureldin, co-leads, and others)
Listing: WEO listing https://www.imf.org/en/Publications/WEO → issue page
https://www.imf.org/en/publications/weo/issues/2024/04/16/world-economic-outlook-april-2024 (describes ch. 3 as "Medium-term growth
slowdown and drivers"). PDF: https://www.imf.org/-/media/files/publications/weo/2024/april/english/ch3.pdf (22 PDF pages; p. 65 = PDF 1).
Read: summary, introduction, pp. 65–68, 75–77.
- p. 65: medium-term growth prospects have been revised down consistently since 2008–09; the slowdown started in the early 2000s in AEs and
  after the crisis in EMDEs; "a significant and broad-based slowdown in total factor productivity growth" explains more than half of the
  decline; misallocation of capital and labour across firms rose. Without policy or new technology, global growth will be only 2.8 percent
  by 2030, about 1 point below the 2000–19 average.
- p. 67: five-year-ahead WEO forecasts have fallen for nearly 82 percent of economies since 2008; Brazil, China, India, Indonesia and Russia
  account for about 0.8 point of the 1.8-point drop in projected world growth; no pessimism bias in the forecasts.
- p. 68: AE TFP growth fell from 1.3 percent (1995–2000) to 0.2 percent after the pandemic, about half the GDP-growth reduction; EM and
  low-income TFP growth fell from 2.5 and 2 percent (2001–07) to 0.7 percent and nearly zero. Footnote: GDP mismeasurement from the digital
  economy is an open question; cites Syverson (2017) against it.
- p. 72 (PDF 8): within-firm TFP slowdown causes cited include waning gains from ICT (Fernald 2015) and declining business dynamism.
- pp. 75–77: by 2030 labour's contribution to world growth is expected to be 0.2 point (a quarter of the 2000–19 average) and TFP's 0.9
  point (vs 1.0). AI could add 10 to 80 basis points to medium-term global growth depending on adoption and whether it replaces or augments
  workers (box 3.3); public debt overhang could subtract 5–15 basis points; nearly two in three new labour-force entrants over the medium
  term will come from India and sub-Saharan Africa (p. 69).

### TE-IMF-3. IMF, *World Economic Outlook, April 2026: Global Economy in the Shadow of War*, Chapter 1 "Global Prospects and Policies"
Listing: issue page https://www.imf.org/en/publications/weo/issues/2026/04/14/world-economic-outlook-april-2026 (lists "a reassessment
of expectations surrounding artificial-intelligence-driven productivity" among risks; data through 1 April 2026). PDF:
https://www.imf.org/-/media/files/publications/weo/2026/april/english/ch1.pdf (46 PDF pages; printed = PDF). Read: AI-related passages
on pp. 1–2, 15–16, 21–28.
- p. 1: tailwinds might carry the economy through the war "to a higher growth path paved by productivity gains" from AI.
- p. 2: semiconductor and AI-related equipment exports buoyed Asian economies in 2025.
- p. 15 (downside risk): if AI-driven profitability projections prove "overly optimistic", technology investment could drop sharply and
  tech-heavy equity markets could reprice.
- p. 16 (upside risk): "The reference forecast does not include direct effects of AI on productivity"; adoption still modest in many
  sectors (figure 1.14, US Census Business Trends and Outlook Survey). A faster payoff, "possibly foretold by the above-trend US
  productivity growth since 2020", could add up to 0.3 point to world growth near term and 0.1–0.8 point medium term (citing box 1.3 of the
  October 2025 WEO, not read here).
- p. 22 (box 1.1): AI-related technology investment added an estimated 0.5 percentage point to US GDP growth in 2025; it was import-
  intensive, with large spillovers to Asia.
- pp. 25–26 (box 1.3, scenario B): a reversal of the AI boom with a risk-off episode; in it US equities fall 20 percent in 2026, "about half
  the size" of the post-dot-com correction.

### TE-IMF-4. Florence Jaumotte and others, "Bridging Skill Gaps for the Future: New Jobs Creation in the AI Age", IMF Staff Discussion Note SDN/2026/001, January 2026
Listing: SDN listing (as TE-IMF-1) → issue page
https://www.imf.org/en/publications/staff-discussion-notes/issues/2026/01/09/bridging-skill-gaps-for-the-future-new-jobs-creation-in-the-ai-age-572136.
PDF: https://www.imf.org/-/media/files/publications/sdn/2026/english/sdnea2026001.pdf (49 PDF pages). Read: abstract (PDF 2) only.
- Abstract: about 1 in 10 AE job vacancies demands at least one new skill (often first in the United States), about half that in emerging
  markets; new skills raise average wages and employment but deepen polarisation, possibly shrinking the middle class; AI-skill vacancies
  pay more, but AI-skill diffusion is linked to lower employment in high-exposure, low-complementarity occupations, "posing challenges for
  the youth". India appears only in data annexes.

### TE-IMF-5. Cristian Alonso, Tanuj Bhojwani, Emine Hanedar, Dinar Prihardini, Gerardo Una and Kateryna Zhabska, "Stacking up the Benefits: Lessons from India's Digital Journey", IMF Working Paper WP/23/78, March 2023
Listing: issue page (URL guessed from the standard IMF pattern, then confirmed by the page's own title and canonical URL; the IMF Working
Papers SPROLL listing returned 404):
https://www.imf.org/en/Publications/WP/Issues/2023/03/31/Stacking-up-the-Benefits-Lessons-from-Indias-Digital-Journey-531692.
PDF: https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023078-print-pdf.pdf (51 PDF pages; page numbers given as PDF).
Read: abstract, executive summary, sections on UPI, DBT savings, cost of Aadhaar, financial inclusion.
- Abstract (PDF 2): foundational DPI (digital ID, payments, data exchange), the "India Stack", has fostered innovation and competition,
  closed financial-inclusion gaps, raised revenue and improved spending efficiency.
- PDF 7 (executive summary) and PDF 26 (table 2): the Government of India estimates about 1.1 percent of GDP was saved in expenditure up to
  March 2021 from DBT and related governance reforms (table total ₹2,230 billion, 1.14 percent of GDP; PDS ₹1,016 billion, PAHAL LPG ₹729
  billion), mostly by removing duplicate and ineligible beneficiaries. The paper cautions that DBT's effect "is difficult to disentangle"
  from other developments (PDF 26).
- PDF 13: UPI monthly volume about 8 billion in December 2022 (NPCI); box 1 says over 7.82 billion transactions a month by over 260 million
  unique users (December 2022). UPI itself is not used by government for service delivery.
- PDF 21–22: payment-card ownership rose from 9 to 34 percent of adults (2011–17); female account ownership from 26 to 77 percent.
- PDF 24: cites a UNDP (2022) estimate that DPI could add 1–1.4 points to GDP growth in low- and middle-income countries by 2030.
- PDF 25: Aadhaar cost over US$1 billion, about US$1 per enrolment, among the cheapest ID projects in the world.

---

## OECD, BIS, ITU, academic and other

### TE-OTH-1. Robert J. Gordon, "Is U.S. Economic Growth Over? Faltering Innovation Confronts the Six Headwinds", NBER Working Paper 18315, August 2012 (issue date 23 August 2012 on the NBER page)
Listing: https://www.nber.org/papers/w18315. PDF: https://www.nber.org/system/files/working_papers/w18315/w18315.pdf (25 PDF pages;
pages given as PDF). Read: abstract, introduction, pp. 1–7, grepped the rest.
- PDF 2 (abstract): rapid growth since 1750 "could well turn out to be a unique episode in human history". Three industrial revolutions:
  IR #1 (steam, railways, 1750–1830), IR #2 (electricity, internal combustion, running water and more, 1870–1900), IR #3 (computers, web,
  mobile phones, 1960 to present). IR #2 drove 80 years of fast productivity growth (1890–1972); IR #3 produced only a short-lived revival
  (1996–2004). Six headwinds (demography, education, inequality, globalisation, energy/environment, debt) could drag long-run growth to half
  or less of the 1.9 percent a year of 1860–2007; consumption per capita for the bottom 99 percent could grow below 0.5 percent a year for
  decades.
- PDF 3–4: argues the outlook was "already dismal" in 2007 but unnoticed amid ICT euphoria; IR #3's main productivity effect "has withered
  away in the past eight years"; analysis deliberately pretends the financial crisis did not happen.
- PDF 7: his illustrative path has growth falling to 0.2 percent a year by 2100 (a self-described "fantasy forecast") and 1.4 percent for
  2007–27 before headwinds.

### TE-OTH-2. Lawrence H. Summers, "Why stagnation might prove to be the new normal", 15 December 2013 (reposted on larrysummers.com, tagged "Washington Post")
Listing: https://larrysummers.com/category/secular-stagnation/page/2/ → https://larrysummers.com/news-item/why-stagnation-might-prove-to-be-the-new-normal/
(HTML). Read: whole text. Caution: the site tags it "Washington Post" but the text uses "per cent" and ends "The writer is Charles W Eliot
university professor", a newspaper sign-off style; the original outlet is not confirmed from what was read.
- He raised "secular stagnation" in "a talk hosted by the International Monetary Fund" (November 2013 per the site's secular-stagnation
  page). Evidence: recovery only matched population and normal productivity growth; mid-2000s bubbles and easy credit produced only
  moderate growth; the zero lower bound may stop real rates falling enough; US GDP more than 10 percent below pre-crisis forecasts.
- Lists reasons equilibrium real rates may have fallen, including slower labour-force and "perhaps slower productivity growth", rising
  inequality, and cheaper IT capital goods (the same saving buys more capital).
- "secular stagnation should be viewed as a contingency to be insured against".

### TE-OTH-3. Łukasz Rachel and Lawrence H. Summers, "On Secular Stagnation in the Industrialized World", NBER Working Paper 26198, August 2019 (prepared for Brookings Papers on Economic Activity, Spring 2019)
Listing: https://larrysummers.com/research/ (link "Secular-Stagnation.pdf"). PDF:
https://larrysummers.com/wp-content/uploads/2025/04/Secular-Stagnation.pdf (46 PDF pages). Read: abstract only. (The brief asked for the
2014 *Business Economics* paper or the 2013 IMF speech text; neither was obtained, see Not obtained. This later paper is the substitute.)
- PDF 2 (abstract): the industrial world as a whole is "highly prone to secular stagnation"; neutral real rates fell by at least 300 basis
  points over a generation, and the "private sector neutral real rate" by as much as 700 basis points since the 1970s once fiscal support
  is netted out.

### TE-OTH-4. Erik Brynjolfsson, Daniel Rock and Chad Syverson, "Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics", NBER Working Paper 24001, November 2017
Listing: https://www.nber.org/papers/w24001 (issue date 2 November 2017). PDF:
https://www.nber.org/system/files/working_papers/w24001/w24001.pdf (46 PDF pages; pages given as PDF). Read: abstract, introduction,
sections on lags and past GPTs.
- PDF 2 (abstract): "measured productivity growth has declined by half over the past decade" despite AI's advances; four explanations:
  false hopes, mismeasurement, redistribution, implementation lags; lags likely the biggest. Complementary investments behave like
  intangible capital; national statistics may miss the benefits, "some may even have the wrong sign".
- PDF 3: "we see transformative new technologies everywhere but in the productivity statistics", a redux of the Solow (1987) paradox.
- PDF 6: US labour productivity grew 1.3 percent a year 2005–16, under half the 2.8 percent of 1995–2004; 28 of 29 other OECD countries
  slowed; unweighted average 2.3 percent (1995–2004) vs 1.1 percent (2005–15).
- PDF 25 and 28: computer capital reached its plateau (about 5 percent of nonresidential equipment) just as Solow made his remark; the late-
  1990s acceleration was the partial resolution of the Solow paradox, as 1915–24 was for electrification. PDF 32: the "J-curve" (suggested
  by Larry Summers, PDF 1): intangible build-up first depresses, then raises measured productivity.
- Reference list: Solow, Robert (1987), "We'd Better Watch Out", *New York Times Book Review*, July 12, p. 36. This is the only fetched
  source for the Solow citation; the NYT original was not obtained (see Not obtained).

### TE-OTH-5. David M. Byrne, John G. Fernald and Marshall B. Reinsdorf, "Does the United States Have a Productivity Slowdown or a Measurement Problem?", *Brookings Papers on Economic Activity*, Spring 2016, pp. 109–182
Listing: https://www.brookings.edu/articles/does-the-united-states-have-a-productivity-slowdown-or-a-measurement-problem/ (links to the
final text and conference drafts). PDF: https://www.brookings.edu/wp-content/uploads/2016/03/byrnetextspring16bpea.pdf (74 PDF pages;
printed p. 109 = PDF 1). Read: abstract, introduction, section II summary.
- p. 109: after 2004 measured labour productivity and TFP growth slowed; "We find little evidence that this slowdown arises from growing
  mismeasurement" of IT gains. IT hardware mismeasurement was larger in 1995–2004 (when more was produced domestically), so correcting it
  makes the slowdown worse; free services such as Google searches and Facebook are conceptually nonmarket and their estimated gains are too
  small to offset the loss from slower market productivity; globalisation and fracking effects are small.
- p. 130 (PDF 22): the slowdown in average annual labour-productivity growth was about 1¾ points, of which TFP about 1¼.
- pp. 131–132: alternative IT deflators add just under 0.3 point to 1995–2004 growth and about 0.2 point to 2004–14, so the slowdown grows
  by about 0.3 point.

### TE-OTH-6. Chad Syverson, "Challenges to Mismeasurement Explanations for the U.S. Productivity Slowdown", NBER Working Paper 21974, February 2016 (published version: *Journal of Economic Perspectives* 31(2), 2017, not obtained)
Listing: https://www.nber.org/papers/w21974 (issue date 4 February 2016); AEA article page https://www.aeaweb.org/articles?id=10.1257/jep.31.2.165
(title confirmed; its PDF link returned 403). PDF read: https://www.nber.org/system/files/working_papers/w21974/w21974.pdf (28 PDF pages).
Read: abstract.
- PDF 2 (abstract): four challenges to the mismeasurement hypothesis: (1) the slowdown occurred in dozens of countries and its size is
  unrelated to ICT intensity; (2) estimates of consumer surplus from internet-linked technologies fall far short of the $2.7 trillion or
  more of "missing output", the largest under one-third of it; (3) if mismeasurement explained even a modest share, true output and
  productivity growth in ICT-producing industries would have had to be multiples of the measured rates; (4) GDI has exceeded GDP on average
  since 2004, but that began before the slowdown and reflects unusually high capital income (profits), not labour income. Caveat: the JEP
  version may differ in detail.

### TE-OTH-7. Daron Acemoglu, "The Simple Macroeconomics of AI", NBER Working Paper 32487, May 2024
Listing: https://www.nber.org/papers/w32487 (issue date 23 May 2024). PDF: https://www.nber.org/system/files/working_papers/w32487/w32487.pdf
(58 PDF pages; pages given as PDF). Read: abstract, introduction, section on the estimates.
- PDF 2: using a task-based model and Hulten's theorem, AI's macro effects look "nontrivial but modest": no more than a 0.66 percent rise
  in TFP over 10 years; because early evidence comes from easy-to-learn tasks, under 0.53 percent; AI likely to widen the capital–labour
  income gap; some new AI tasks may have negative social value.
- PDF 3: contrasts Goldman Sachs (2023): 7 percent higher global GDP ($7 trillion) and 1.5 percentage points a year faster US productivity
  growth over 10 years; McKinsey $17.1–25.6 trillion.
- PDF 6–7 and 31: 0.66 percent over 10 years is about 0.064 percent a year of extra TFP growth; upper bounds 0.53 percent TFP and 0.90
  percent GDP over 10 years. Inputs: about 4.6 percent of tasks affected, average cost savings 14.4 percent.

### TE-OTH-8. Carl Benedikt Frey and Michael A. Osborne, "The Future of Employment: How Susceptible Are Jobs to Computerisation?", Oxford Martin Programme on Technology and Employment working paper, dated 17 September 2013
Listing: https://www.oxfordmartin.ox.ac.uk/publications/the-future-of-employment. PDF:
https://www.oxfordmartin.ox.ac.uk/downloads/academic/future-of-employment.pdf (79 PDF pages). Read: abstract, introduction, data section.
(The 2017 journal version was not fetched.)
- PDF 2 (abstract): probability of computerisation estimated for 702 US occupations with a Gaussian process classifier; "about 47 percent
  of total us employment is at risk"; wages and education strongly negatively related to that probability.
- PDF 32: the 702 occupations cover 138.44 million US jobs; 4.628 million (3 percent) excluded.
- Caution: the paper sets no firm date for the risk; robotic perception and manipulation challenges are "unlikely to be fully resolved in
  the next decade or two" (PDF 29), and "at risk" is a technical-feasibility probability, not a forecast of job losses.

### TE-OTH-9. Bank for International Settlements, *Annual Economic Report 2024*, Chapter III "Artificial intelligence and the economy: implications for central banks", June 2024
Listing: https://www.bis.org/publ/arpdf/ar2024e.htm (title "BIS Annual Economic Report 2024") → chapter page
https://www.bis.org/publications/aer-2024/artificial-intelligence-economy-implications-central-banks. PDF:
https://www.bis.org/publications/artificial-intelligence-economy-implications-central-banks.pdf (37 PDF pages; p. 123 = PDF 34,
printed = PDF + 89). Read: key takeaways, introduction, adoption and productivity sections.
- p. 91 (PDF 2): AI adoption outpaces earlier technology waves; ChatGPT reached one million users in under a week; nearly half of US
  households used gen AI tools in the past 12 months.
- p. 96 (PDF 7): GPT adoption typically follows a J-curve; electricity and the telephone took decades, smartphones under a decade; AI's
  ease of use and negligible cost suggest "an even steeper J-curve".
- p. 109 (PDF 20): cited experiments: LLM access raised coders' output (lines of code) 55 percent; footnote 32: a gen-AI assistant raised
  customer-support agents' productivity 14 percent (Brynjolfsson et al 2023).
- p. 112 (PDF 23, graph 9): AI raises output in the short and long run but could be inflationary or disinflationary in the short run.

### TE-OTH-10. International Telecommunication Union, *Measuring Digital Development: Facts and Figures 2026* (pages dated 13 October 2026)
Listing: https://www.itu.int/itu-d/reports/statistics/facts-figures-2026/ (index https://www.itu.int/itu-d/reports/statistics/facts-figures-2026/index/).
Page read: "Internet use" https://www.itu.int/itu-d/reports/statistics/2026/10/13/ff26-internet-use/ (HTML; no PDF link found on the
pages). The 2025 edition page (https://www.itu.int/itu-d/reports/statistics/facts-figures-2025/) was also read for its summary.
- 2026: 76 percent of the world (6.3 billion people) online, up from 74 percent (6.1 billion) in 2025; about 2 billion offline; growth 3
  percent year on year (2.5 percent previously).
- High-income countries 93 percent online, low-income 32 percent; Africa 42 percent; Asia-Pacific 80 percent; LDCs 41 percent, LLDCs 43
  percent; universality conventionally means at least 95 percent.
- 2025 edition summary: "almost three-quarters" online, 2.2 billion offline, "progress is slowing".
- Compare WDR 2016 (TE-WB-1): 3.2 billion users end-2015 and nearly 60 percent offline.

### TE-OTH-11. US Bureau of Labor Statistics series "Nonfarm Business Sector: Labor Productivity (Output per Hour) for All Workers" (OPHNFB), as republished by FRED, Federal Reserve Bank of St. Louis (last observation 2026 Q3)
Listing: https://fred.stlouisfed.org/series/OPHNFB (index 2017 = 100, seasonally adjusted; source BLS). Data:
https://fred.stlouisfed.org/graph/fredgraph.csv?id=OPHNFB (CSV, 1947 Q1 to 2026 Q3). BLS's own productivity pages returned 403 (see Not
obtained), so this is a third-party copy of the BLS series, not a BLS publication.
- Own calculation (compound annual growth of annual-average index, for the book's chart; not a published BLS figure): 1948–73 2.8 percent;
  1973–95 1.4 percent; 1995–2004 3.1 percent; 2004–19 1.5 percent; 2007–19 1.5 percent; 2019–25 2.3 percent; 1948–2025 2.2 percent.
- Caution: BRS (TE-OTH-4) give 2.8 percent for 1995–2004 and 1.3 percent for 2005–16 on 2017 data; the difference reflects data
  revisions and endpoint choice. Use one source per chart.

---

## India

### TE-IN-1. Government of India, Ministry of Finance, *Economic Survey 2001-02*, Chapter 7 (Industry), paras 7.52–7.59 (on disk; not refetched)
Files: `sources/text/es2001-02.txt`; PDF `sources/economic-surveys/Economic Survey 2001-02 (English).pdf` (no printed page numbers found in
the extracted text; PDF 141–143). Read: paras 7.52–7.60 and the box on services exports.
- PDF 142 (para 7.54): software and IT-enabled services "has emerged as a niche opportunity for India"; the software industry grew at a CAGR
  above 50 percent over the decade, with turnover of US$8.3 billion and exports of US$6.2 billion in 2000-01; more than 260 of the Fortune
  1,000 outsource software to India; cost advantage the main driver.
- PDF 142 (services exports): software exports rose from ₹17,150 crore (1999-2000) to ₹28,350 crore (2000-01), up 65 percent, and were
  expected at ₹40,000 crore in 2001-02.
- PDF 143 (paras 7.56–7.59): ITES employed 70,000 and was 10.6 percent of IT revenues; R&D rose from 2.5 to over 4 percent of spending;
  62 percent of software exports went to North America, 24 percent to Europe; offshore work about 44 percent of exports. PDF 152: worry
  that the September 2001 attacks might hurt IT exports.
- Inconsistency to note: para 7.52 (PDF 141) gives "electronics hardware and computer software exports" of ₹33,138 crore in 2000-01
  (₹48,500 crore expected 2001-02), a different aggregate from the ₹28,350 crore software-only figure.

### TE-IN-2. *Economic Survey 2002-03*, Chapter 9 (Infrastructure), para 9.23, telecommunications (on disk)
Files: `sources/text/es2002-03.txt`; PDF `Economic Survey 2002-03 (English).pdf` (PDF 221; no printed page number extracted). Read: paras
9.23–9.32 and table 9.7.
- Teledensity (phone lines per 100 people) improved from 3.6 (March 2001) to 4.9 (December 2002), still well behind other developing
  countries (table 9.7, international comparison). Reforms listed: opening long distance, internet telephony, a Universal Service
  Obligation mechanism, a fourth mobile operator.
- Also in *Economic Survey 2003-04* (PDF 361, note to the teledensity table): India's teledensity was 7.02 on 31 March 2004.

### TE-IN-3. *Economic Survey 2007-08*, Chapter 8 (Industry), paras 8.42–8.43, IT-ITES (on disk)
Files: `sources/text/es2007-08.txt`; PDF `Economic Survey 2007-08 (English).pdf` (p. 193 = PDF 194; p. 195 = PDF 196).
- p. 193 (para 8.42): IT-ITES export revenues grew from US$23.6 billion (2005-06) to US$31.3 billion (2006-07), up 32.6 percent; double-
  digit revenue growth and an unprecedented rise in MNC investment.
- p. 193 (para 8.43): 90 Indian IT firms certified at SEI CMM Level 5 by December 2006; most Fortune 500 and Global 2000 firms source IT-
  ITES from India.
- p. 195: IT-ITES employment rose from an estimated 12,87,000 (2005-06) to 16,21,000 (2006-07), plus about 60 lakh indirect and induced
  jobs.

### TE-IN-4. *Economic Survey 2014-15*, Volume 1, Chapter 3 "'Wiping Every Tear From Every Eye': The JAM Number Trinity Solution" (on disk)
Files: `sources/text/es2014-15.txt`; PDF `Economic Survey 2014-15 (English).pdf` (chapter opens p. 52; p. 63 = PDF 69; p. 64 = PDF 70).
Read: introduction (p. 52) and section 3.5 (p. 64).
- p. 52: the direct fiscal cost of an illustrative subset of subsidies is about ₹378,000 crore, 4.24 percent of GDP.
- p. 64: the JAM Number Trinity (Jan Dhan Yojana, Aadhaar, mobile numbers) lets the state support poor households in a targeted, less
  distortive way. Over 720 million had an Aadhaar by December 2014, rising by 20 million a month and expected to exceed 1 billion by
  December 2015; over 100 million bank accounts seeded with Aadhaar by December 2014; rural mobile users rising 2.82 million a month.
- Context (from the same Survey, PDF 441): PM Jan Dhan Yojana launched 28 August 2014, with 1063.9 lakh new accounts by 3 January 2015.

### TE-IN-5. *Economic Survey 2022-23*, Chapter 12 "Physical and Digital Infrastructure: Lifting Potential Growth", Box XII.6 "Unified Payments Interface - The game changer in real-time payments!" (on disk)
Files: `sources/text/es2022-23.txt`; PDF `Economic Survey 2022-23 (English).pdf` (p. 369 = PDF 412).
- p. 369: UPI introduced in 2016; participating banks rose from 35 (December 2017) to more than 380 (December 2022). UPI was 17 percent of
  3,100 crore digital transactions in FY19, over 27 percent (1,250 of 4,600 crore) in FY20, 52 percent of 8,840 crore in FY22; average
  growth FY19–22 121 percent (value) and 115 percent (volume). In December 2022 "UPI touched its highest-ever mark": 782 crore transactions
  worth ₹12.8 lakh crore.
- p. 370 (PDF 413): over 23 crore UPI QR codes deployed in five years, from 25 lakh merchant devices before.

### TE-IN-6. *Economic Survey 2025-26*, Statistical Appendix, Table 3.6 "Rupay cards & UPI Payments" (on disk), with the 2024-25 Appendix for comparison
Files: `sources/text/es2025-26_statistical_appendix.txt` (p. 80 = PDF 87; source NPCI); 2024-25 Appendix in `Economic Survey 2024-25
(English).pdf` (p. 80 = PDF 569).
- UPI volume (million) / value (₹ billion): 2016-17 18 / 70; 2017-18 915 / 1,098; 2018-19 5,392 / 8,770; 2019-20 12,519 / 21,317;
  2020-21 22,331 / 41,037; 2021-22 45,968 / 84,176; 2022-23 83,714 / 139,149; 2023-24 131,129 / 199,951; 2024-25 185,866 / 260,570;
  2025-26 to 31 December 2025: 176,878 / 229,530.
- Vintage note: the 2024-25 Appendix gave 2018-19 volume as 5,353 and 2022-23 as 83,751 million (value 139,207); small revisions.
- Related (ES 2025-26 ch. 12, p. 490 = PDF 541): gig workers rose from 77 lakh (FY21) to 120 lakh (FY25), helped by over 80 crore
  smartphone users and "15 billion UPI transactions per month".

### TE-IN-7. *Economic Survey 2025-26*, Chapter 1 "State of the Economy: Pushing the Growth Frontier", growth-accounting section and Table I.7 (on disk)
Files: `sources/text/es2025-26.txt`; PDF `Economic Survey 2025-26 (English).pdf` (p. 33 = PDF 84; p. 34 = PDF 85).
- p. 33: capital stock grew about 8.6 percent a year in FY03–FY12 and 7.6 percent in FY13–FY20; capital share 0.49 from RBI's KLEMS
  database; labour input grew about 2.3 percent (FY13–FY20, KLEMS); estimated trend TFP growth averaged about 1.9 percent pre-pandemic
  (FY13–FY20) and appears lower (1.7 percent) in FY23–FY25. Adoption of Aadhaar, UPI and GSTN has cut transaction and compliance costs.
- p. 34: "deeper productivity effects tend to materialise with a lag"; assumes trend TFP returns to 1.9 percent in FY26–FY30; with capital
  growth 7.6 percent and labour 2.6 percent this lifts potential growth from 6.5 to about 7 percent (Table I.7).
- Caution: TFP here is a residual from the Survey's own assumptions, not a published KLEMS estimate; the KLEMS data files themselves were
  not obtained (see Not obtained).

### TE-IN-8. *Economic Survey 2025-26*, IT services and GCCs: Chapter 4 para 4.59 and Chapter 7 para 7.33 (on disk)
PDF pages: p. 171 = PDF 222; p. 279 = PDF 330.
- p. 171 (para 4.59, RBI survey): software services exports rose 7.3 percent in FY25 after 2.3 percent in FY24; computer services over
  two-thirds of software exports; US share fell from 54.1 to 52.9 percent, Europe's rose from 30.8 to 32.8 percent (FY24 to FY25).
- p. 279 (para 7.33): India hosts over 1,700 GCCs employing over 19 lakh professionals (FY24), the largest global hub for captive centres;
  GCCs have driven much incremental IT hiring.

### TE-IN-9. *Economic Survey 2024-25*, Chapter 13 "Labour in the AI Era: Crisis or Catalyst?" (on disk)
Files: `sources/text/es2024-25.txt`; PDF `Economic Survey 2024-25 (English).pdf` (chapter opens p. 411; pp. 412–415 = PDF 457–460).
Read: paras 13.1–13.12.
- p. 412 (para 13.3): AI research concentrated in a few large firms risks concentrating automation's benefits; cites Korinek and Stiglitz
  on a "winner-takes-all" outcome hurting labour-rich developing countries.
- p. 413 (para 13.5): AI patents up 62.7 percent to just over 62,000 (2021–22); private gen-AI investment from about US$3 billion (2022) to
  US$25.2 billion (2023); corporate AI investment US$761 billion (2021–23) (Stanford AI Index).
- p. 414 (paras 13.9–13.10): summarises outside estimates: IMF (TE-IMF-1), ILO (about 75 million jobs at complete risk), Goldman Sachs
  (nearly 300 million full-time jobs exposed), McKinsey (up to 30 percent of hours automatable by 2030 in Europe and the US).
- p. 415 (para 13.11): an IIM Ahmedabad survey found 68 percent of white-collar employees expect partial or full automation of their jobs
  within five years and 40 percent expect their skills to become redundant; AI-skill jobs pay a 13–17 percent premium; NASSCOM expects the
  Indian AI market to grow 25–35 percent a year to 2027.
- Framing: India has time to build institutions because scaling AI is hard (para 13.8).

### TE-IN-10. *Economic Survey 2025-26*, Chapter 14 "Evolution of the AI Ecosystem in India: The Way Forward" (on disk)
PDF pages: chapter opens p. 549 = PDF 600; pp. 549–552 read in full, rest grepped (pp. 560–565 on data-centre and GPU constraints;
pp. 567–568 and 583 on IndiaAI Mission).
- p. 549 (chapter summary): India's AI strategy should be bottom-up, sector-specific, open and interoperable, grounded in its own
  constraints (capital, compute, energy) rather than copying "unsustainable models" of advanced economies; government as enabler.
- p. 550 (paras 14.2–14.3): McKinsey survey: 88 percent of organisations used AI in at least one function in 2025; high-income countries
  58.4 percent of AI usage (April 2025, World Bank), upper- and lower-middle-income 22.5 and 18.7 percent.
- p. 551 (paras 14.5–14.6): early evidence (Yale Budget Lab; Brynjolfsson, Chandar and Chen 2025) tempers extreme labour-impact predictions,
  some reassurance for labour-abundant India; but "productivity gains from augmentation have a ceiling".
- pp. 551–552 (box XIV.1): in the US professional, business and information services sector, after December 2022 employment responds less
  to output growth (framed as structural change, not causal).
- pp. 560–563: simulation of Indian data-centre operators finds financing, then GPU supply, then grid capacity as successive bottlenecks.

### TE-IN-11. Press Information Bureau (Cabinet), "Cabinet Approves Ambitious IndiaAI Mission to Strengthen the AI Innovation Ecosystem", 7 March 2024 (PIB Delhi, 7:46 PM)
URL: https://pib.gov.in/PressReleasePage.aspx?PRID=2012355 (HTML; PRID taken from PIB's release numbering, page title and text confirmed on
fetch). Read: whole release.
- Outlay ₹10,371.92 crore; implemented by the IndiaAI Independent Business Division under Digital India Corporation.
- Components: IndiaAI Compute (10,000 or more GPUs via public-private partnership, plus an AI marketplace); Innovation Centre (indigenous
  large multimodal and domain models); Datasets Platform (non-personal data); Application Development; FutureSkills (Data and AI Labs in
  Tier 2 and 3 cities); startup financing; safe and trusted AI.

### TE-IN-12. Telecom Regulatory Authority of India, "Highlights of Telecom Subscription Data at the end of September 2026", Press Release No. 140/2026, 27 October 2026
Listing: https://www.trai.gov.in/release-publication/reports/telecom-subscriptions-reports. PDF:
https://www.trai.gov.in/sites/default/files/2026-10/PR_No140of2026_0.pdf (25 PDF pages). Read: highlights table and broadband section
(pp. 1–2).
- Total telephone subscribers 1,367.93 million (wireless 1,319.19); urban 807.78, rural 560.16 million.
- Tele-density 95.52 percent with M2M connections, 85.41 percent without; urban 155.85 percent, rural 61.30 percent (with M2M).
- Broadband subscribers 1,107.68 million with M2M (1,013.87 without); 1,596 operators reporting; 1,212.80 million active wireless
  subscribers on peak VLR date.
- Compare ES 2002-03 (TE-IN-2): teledensity 4.9 in December 2002.

---

## Synthesis

1. **The productivity slowdown was real, early and broad.** In the United States the ICT boom gave a short burst: labour productivity grew
   2.8 percent a year in 1995–2004 and 1.3 percent in 2005–16 (TE-OTH-4 PDF 6); on FRED's copy of the BLS series 3.1 percent in
   1995–2004 and 1.5 percent in 2004–19 (TE-OTH-11, own calculation). Gordon saw IR #3's effect as "short-lived" (1996–2004) and already
   fading in 2012 (TE-OTH-1). The World Bank found the post-2008 slowdown in about 70 percent of economies, covering over 80 percent of the
   extreme poor; global labour-productivity growth 2.7 → 1.5 percent (2007–16; GEP 2020, TE-WB-5 p. 194) or 2.8 → 1.4 percent (2021 book,
   TE-WB-4 p. 6); in EMDEs 6.6 → 3.2 or 3.1 percent. The IMF in 2024 said a TFP slowdown explained more than half of the fall in world
   growth, with AE TFP growth 1.3 percent (1995–2000) → 0.2 percent post-pandemic (TE-IMF-2 pp. 65, 68).
2. **Why? Four contested explanations.** (a) *Exhausted big ideas*: Gordon's one-time inventions and six headwinds (TE-OTH-1). (b) *Demand
   and low real rates*: Summers' secular stagnation; real neutral rates down 300 bp or more (TE-OTH-2, TE-OTH-3). (c) *Mismeasurement*:
   rejected by Byrne–Fernald–Reinsdorf (correcting IT prices makes the slowdown worse; free digital services are nonmarket; TE-OTH-5) and
   Syverson (surplus estimates fall far short of the $2.7 trillion gap; TE-OTH-6); the IMF in 2024 called it "an open question" but cited
   Syverson (TE-IMF-2 p. 68). (d) *Lags and intangibles*: Brynjolfsson–Rock–Syverson's J-curve; electrification and computers both took
   years (TE-OTH-4; repeated by WDR 2026 p. 10 and BIS p. 96). Also: misallocation and weaker dynamism (TE-IMF-2; TE-WB-6 says "little
   consensus").
3. **Digital spread ran ahead of digital dividends.** Internet users went from 1 billion (2005) to 3.2 billion (2015) while productivity
   slowed: "while digital technologies have been spreading, digital dividends have not" (WDR 2016, TE-WB-1 p. 2). By 2026, 6.3 billion
   (76 percent) are online, but 2 billion are not, and low-income countries are at 32 percent (TE-OTH-10).
4. **Jobs fear, three waves.** Frey–Osborne: 47 percent of US jobs "at risk" (2013; TE-OTH-8). WDR 2019: the threat "is exaggerated"
   (TE-WB-2 p. 6). IMF 2024: almost 40 percent of world jobs exposed to AI, 60 percent in AEs, 26 percent in India (TE-IMF-1). WDR 2026:
   4.5 percent of jobs in developing countries amenable to gen-AI automation vs 14.2 percent in rich ones, with early signs of fewer entry-
   level white-collar postings, including in India (TE-WB-3 p. 14). IMF 2026: AI-skill diffusion linked to lower youth-relevant employment
   in exposed occupations (TE-IMF-4). ES 2025-26 cites US studies finding no discernible disruption yet (TE-IN-10 p. 551).
5. **How big will AI's payoff be? A wide range.** Goldman Sachs: +1.5 points a year to US productivity growth for a decade (as cited by
   TE-OTH-7 PDF 3); IMF 2024: +0.1 to +0.8 point to world medium-term growth (TE-IMF-2 p. 77); IMF 2026: up to 0.3 point near term, 0.1–0.8
   medium term, none of it in the baseline (TE-IMF-3 p. 16); Acemoglu: under 0.66 percent on the TFP level over 10 years, about 0.06 point a
   year (TE-OTH-7). Meanwhile AI investment itself added about 0.5 point to US GDP growth in 2025 (TE-IMF-3 p. 22), and the IMF modelled a
   bust with US equities down 20 percent (pp. 25–26). WDR 2026 says even the worst case lifts developing-country potential growth (p. vii).
6. **India, part 1: services exports before the digital state.** In 2001-02 software was "a niche opportunity" with exports of ₹28,350
   crore (US$6.2 billion) and turnover US$8.3 billion (TE-IN-1); by 2006-07 IT-ITES exports were US$31.3 billion and direct employment
   16.2 lakh (TE-IN-3); by FY24 over 1,700 GCCs employed over 19 lakh (TE-IN-8). Teledensity rose from 3.6 (March 2001) to 85.41 percent
   without M2M (September 2026; TE-IN-2, TE-IN-12).
7. **India, part 2: digital public infrastructure.** The JAM trinity (2015 Survey; 720 million Aadhaar holders by December 2014; TE-IN-4)
   became the "India Stack" (TE-IMF-5). UPI volumes went from 18 million (2016-17) to 185,866 million (2024-25) (TE-IN-6); IMF staff
   cite government estimates of about 1.1 percent of GDP saved by DBT and related reforms to March 2021, while noting attribution is hard
   (TE-IMF-5 PDF 26). WDR 2026 holds up UPI as a model for interoperable AI procurement (TE-WB-3 p. viii). The Survey assumes DPI will lift
   trend TFP back to 1.9 percent, but with a lag (TE-IN-7 pp. 33–34).
8. **India, part 3: AI.** IndiaAI Mission approved March 2024, ₹10,371.92 crore, 10,000+ GPUs (TE-IN-11). The 2025 Survey worried about
   white-collar anxiety (68 percent of surveyed employees expect automation; TE-IN-9 p. 415); the 2026 Survey argues for a bottom-up,
   sector-specific, open-model path and flags GPU and grid bottlenecks (TE-IN-10). The IMF rates India's exposure low because most work is
   manual (26 percent high exposure; TE-IMF-1 p. 8).

### What the reports said at the time vs what happened

| Year | Source | What was said | What the later record shows |
|---|---|---|---|
| 2001-02 | ES 2001-02 (TE-IN-1) | Software exports expected at ₹40,000 crore in 2001-02; India as a "niche" software player | By 2006-07 IT-ITES exports were US$31.3 bn and still growing 32.6 percent a year (TE-IN-3); by FY24, 1,700+ GCCs (TE-IN-8) |
| 2002-03 | ES 2002-03 (TE-IN-2) | Teledensity 4.9, far behind other developing countries | 7.02 by March 2004 (ES 2003-04); 85.41 percent without M2M by September 2026 (TE-IN-12) |
| 2012 | Gordon (TE-OTH-1) | US growth headed to half or less of the 1.9 percent 1860–2007 rate; IR #3 already spent | US productivity growth 1.5 percent a year 2004–19; 2.3 percent 2019–25 on FRED/BLS data (TE-OTH-11); IMF 2026 sees above-trend US productivity since 2020 (TE-IMF-3) |
| 2013 | Summers (TE-OTH-2) | Secular stagnation a contingency; real rates may be unable to fall far enough | Rachel–Summers (2019) estimate neutral rates down 300+ bp (TE-OTH-3); post-2021 rates not covered in these notes |
| 2013 | Frey–Osborne (TE-OTH-8) | About 47 percent of US jobs at risk of computerisation | WDR 2019: threat "exaggerated" (TE-WB-2); ES 2025-26 cites US studies finding no discernible AI disruption yet (TE-IN-10) |
| 2014-15 | ES 2014-15 (TE-IN-4) | Aadhaar expected to exceed 1 billion by December 2015; JAM to enable cash transfers | IMF 2023: Aadhaar enrolled over a billion; DBT savings about 1.1 percent of GDP to March 2021, attribution uncertain (TE-IMF-5) |
| 2016 | WDR 2016 (TE-WB-1) | Digital dividends lag; nearly 60 percent offline | 76 percent online in 2026, 2 billion still offline (TE-OTH-10); productivity slowdown continued (TE-IMF-2) |
| 2016 | BFR; Syverson (TE-OTH-5, 6) | Slowdown is real, not mismeasurement | IMF 2024 still calls mismeasurement "an open question" but treats the slowdown as real (TE-IMF-2 p. 68) |
| 2017 | BRS (TE-OTH-4) | Lags explain the paradox; AI's effects will come with complementary investment | IMF 2026: AI's productivity effects still not in the baseline; adoption modest (TE-IMF-3 p. 16) |
| 2020 | GEP Jan 2020 (TE-WB-5) | Broad productivity slowdown, steepest yet in EMDEs; expected to stay subdued | IMF 2024: TFP slowdown explains over half the growth decline; world growth 2.8 percent by 2030 without new tech (TE-IMF-2) |
| 2022-23 | ES 2022-23 (TE-IN-5) | UPI record 782 crore transactions in December 2022 | 185,866 million in 2024-25, about 15 billion a month (TE-IN-6) |
| 2024 | IMF SDN (TE-IMF-1); Acemoglu (TE-OTH-7) | 40 percent of world jobs exposed; macro gains "nontrivial but modest" | AI investment added 0.5 point to US 2025 growth; productivity payoff still uncertain (TE-IMF-3); WDR 2026 sees early falls in entry-level postings (TE-WB-3) |

Candidate quotes (all verified in the converted text, under 15 words):
- "So, while digital technologies have been spreading, digital dividends have not." (WDR 2016, TE-WB-1 p. 2)
- "the threat to jobs from technology is exaggerated" (WDR 2019, TE-WB-2 p. 6)
- "development progress has dipped to a 75-year low" (WDR 2026 foreword, TE-WB-3 p. vii)
- "the steepest, longest, and broadest yet" (GEP January 2020, TE-WB-5 p. 194)
- "Almost 40 percent of global employment is exposed to AI" (IMF SDN 2024, TE-IMF-1 p. 2)
- "a significant and broad-based slowdown in total factor productivity growth" (WEO April 2024, TE-IMF-2 p. 65)
- "The reference forecast does not include direct effects of AI on productivity" (WEO April 2026, TE-IMF-3 p. 16)
- "could well turn out to be a unique episode in human history" (Gordon 2012, TE-OTH-1 PDF 2)
- "secular stagnation should be viewed as a contingency to be insured against" (Summers 2013, TE-OTH-2)
- "we see transformative new technologies everywhere but in the productivity statistics" (BRS 2017, TE-OTH-4 PDF 3)
- "measured productivity growth has declined by half over the past decade" (BRS 2017, TE-OTH-4 PDF 2)
- "We find little evidence that this slowdown arises from growing mismeasurement" (BFR 2016, TE-OTH-5 p. 109)
- "nontrivial but modest" (Acemoglu 2024, TE-OTH-7 PDF 2)
- "about 47 percent of total us employment is at risk" (Frey and Osborne 2013, TE-OTH-8 PDF 2)
- "an even steeper J-curve" (BIS AER 2024, TE-OTH-9 p. 96)
- "has emerged as a niche opportunity for India" (ES 2001-02 on software, TE-IN-1 PDF 142)
- "UPI touched its highest-ever mark" (ES 2022-23, TE-IN-5 p. 369)
- "deeper productivity effects tend to materialise with a lag" (ES 2025-26, TE-IN-7 p. 34)
- "productivity gains from augmentation have a ceiling" (ES 2025-26, TE-IN-10 p. 551)

## Not obtained

- IMF *WEO October 2001: The Information Technology Revolution*, Chapter III (listed on the index page
  http://www.imf.org/external/pubs/ft/weo/2001/02/index.htm, HTTP 200, as "Past All-Purpose Technological Revolutions"): chapter PDF
  https://www.imf.org/-/media/websites/imf/imported-flagship-issues/external/pubs/ft/weo/2001/02/pdf/_chapter3pdf.pdf — 404; guessed
  variants http://www.imf.org/external/pubs/ft/weo/2001/02/pdf/chapter3.pdf and .../_chapter3pdf.ashx — 404. Only the table of contents
  was read; no 2001 IMF view of IT productivity is in these notes.
- IMF Working Papers listing https://www.imf.org/en/Publications/SPROLLs/Working-Papers — 404 (TE-IMF-5's issue page was reached by a
  guessed URL that returned 200).
- IMF WEO chapter on technology and the labour share (April 2017 ch. 3): issue page
  https://www.imf.org/en/publications/weo/issues/2019/08/30/world-economic-outlook-april-2017-gaining-momentum-44510 (200) lists only the
  full-text PDF /-/media/files/publications/weo/2017/april/pdf/text.pdf; not downloaded or read. October 2025 WEO box 1.3 on AI (cited by
  TE-IMF-3) not read; the October 2025 issue page (200) lists chapters on EM resilience and industrial policy only.
- IMF SDN/2024/006 "Broadening the Gains from Generative AI: The Role of Fiscal Policies" (listed on the SDN page): not read.
- Summers: 2014 *Business Economics* paper — guessed URL
  https://larrysummers.com/2014/02/17/u-s-economic-prospects-secular-stagnation-hysteresis-and-the-zero-lower-bound/ — 404; not found on
  larrysummers.com/research/ (200) or the secular-stagnation category pages (200). The November 2013 IMF speech text was not found; only
  his December 2013 article referring to it (TE-OTH-2).
- Syverson, *Journal of Economic Perspectives* 2017: article page https://www.aeaweb.org/articles?id=10.1257/jep.31.2.165 (200), PDF
  https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.31.2.165 — 403. NBER working-paper version used (TE-OTH-6).
- Solow's 1987 remark, *New York Times Book Review*, 12 July 1987, p. 36 ("We'd Better Watch Out"): NYT search
  https://www.nytimes.com/search?query=%22We%27d+Better+Watch+Out%22+Solow&startDate=19870712&endDate=19870712 — 403; no direct article
  URL found. The citation is verified only through BRS's reference list (TE-OTH-4); the exact wording of the remark was not read in any
  fetched source and should not be quoted from memory.
- US BLS productivity pages: https://www.bls.gov/productivity/ — 403 ("Access Denied"); https://www.bls.gov/news.release/pdf/prod2.pdf —
  403. BLS data used only via FRED (TE-OTH-11).
- OECD Compendium of Productivity Indicators: https://www.oecd.org/en/publications/oecd-compendium-of-productivity-indicators-2025_b024d9e1-en.html
  (guessed) — 403. OECD Employment Outlook 2023: https://www.oecd.org/en/publications/oecd-employment-outlook-2023_08785bba-en.html
  (guessed) — 403; https://www.oecd-ilibrary.org/employment/oecd-employment-outlook-2023_08785bba-en — 403 (Cloudflare "Just a
  moment..."). No OECD source is in these notes.
- Frey and Osborne 2017 journal version (*Technological Forecasting and Social Change*): not tried; 2013 working paper used.
- NPCI UPI product statistics: https://www.npci.org.in/what-we-do/upi/product-statistics — 403 (Akamai "Access Denied"). UPI figures
  taken from the Economic Survey Statistical Appendix, which cites NPCI (TE-IN-6).
- RBI India KLEMS database: listing https://www.rbi.org.in/Scripts/KLEMS.aspx (200; latest release listed "July 2024", earlier releases
  January 2024, September 2023, October 2022 with an India Productivity Report, back to June 2014); data file
  https://rbidocs.rbi.org.in/rdocs/content/docs/INDIAKLEMS08072024.xlsx — no connection (curl HTTP 000). No KLEMS TFP-by-period figures
  in these notes; India TFP comes only via ES 2025-26 (TE-IN-7).
- NASSCOM IT-BPM revenue: https://nasscom.in/knowledge-center/publications (guessed) — 404. Not otherwise tried; IT figures come from the
  Economic Surveys.
- ITU Facts and Figures PDF: no PDF link found on the 2025 or 2026 pages (HTML read instead, TE-OTH-10).
- Economic Survey 2023-24 (DPI and AI passages): grepped counts only (DPI 8, AI 20 mentions); not read for these notes.
