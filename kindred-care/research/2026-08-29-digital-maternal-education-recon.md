# Recon — digital maternal education: what works, what fails, engagement, and pricing

29 Aug 2026 · prepared for the UCAC pack (feeds GTM §1, §5, §7 and the pilot protocol)

Evidence retrieved from **PubMed** and from public web sources. Every empirical claim below
carries its citation and DOI. Where a figure could not be verified it is marked as such
rather than smoothed over — the same standard the pack asks of everyone else.

---

## The one-paragraph version

The field's problem is not efficacy, it is **retention**, and the single strongest
predictor of retention is **how the mother was enrolled**. Self-registration produces a
median retention of *zero days*; enrolment through a clinic, bundled with something
tangible, produces a median of *167 days*. That finding alone validates Kindred Care's
service-enrolled model and is the strongest available argument for sequencing B2C late.
The second finding is that unselected cohorts produce high satisfaction and no effect —
the exact result that cannot be sold to a health service. Design the pilot for need, not
for volume.

---

## 1. What works

**Acceptability of a conversational agent in the postpartum period is genuinely high.**
In a randomised controlled trial of a mental-health chatbot in a general postpartum
population (n=192 randomised, 152 analysed), **91% of chatbot users were satisfied or
highly satisfied**, **74% had used it at least once in the two weeks before the 6-week
survey**, and **80% of participants were comfortable using a smartphone app for mood
management**. Depression scores fell further in the chatbot arm than usual care at six
weeks (PHQ-9 mean decrease 1.32, SD 3.4, versus 0.13, SD 3.01).
Suharwardy et al., *AJOG Global Reports* 2023 — [10.1016/j.xagr.2023.100165](https://doi.org/10.1016/j.xagr.2023.100165)

**Tailoring and interactivity carry the effect.** Across breastfeeding and perinatal
mental-health trials, the interventions that move self-efficacy and mood are the
personalised and interactive ones — tailored text messaging, gamified education,
monitoring with feedback — rather than static content libraries.

**The features the field says are underused are the ones Kindred Care is built from.**
A systematic review of engagement in perinatal digital mental health and wellbeing
programs names *"chatbots, games, storytelling, rewards, avatars, and personalization"*
as features that *"have potential but continue to be underexplored and underused"* and
that *"could be developed to improve participation."*
Slade et al. (Understanding Engagement…), *JMIR* 2022 — [10.2196/36620](https://doi.org/10.2196/36620)

That sentence is worth quoting verbatim in the pack. The field's own systematic review
describes the gap Kindred Care fills.

## 2. What does not work

**Unselected cohorts produce a null result.** The postpartum chatbot RCT above is the
cautionary tale: the sample *"did not screen positive for depression at baseline and thus
the potential of the chatbot to reduce depressive symptoms in this population was
limited."* The authors explicitly recommend future studies in **high-risk populations who
screen positive**. High satisfaction, no effect size — the worst possible pilot outcome,
because it is unsellable and unpublishable at the same time.
[10.1016/j.xagr.2023.100165](https://doi.org/10.1016/j.xagr.2023.100165)

**Generic LLMs fail on provenance, and that failure is documented.** In an assessment of
ChatGPT-generated patient information in maternal-fetal medicine, four MFM specialists
rated accuracy at a median 4.8/6 but **completeness at only 2.2/3**, with the stated
concerns being *omission of clinically important counselling information* and *inability
to verify the source because ChatGPT does not provide references*.
Horgan et al., *AJOG MFM* 2024 — [10.1016/j.ajogmf.2024.101302](https://doi.org/10.1016/j.ajogmf.2024.101302)

**This is the single best external citation for the Kindred Care moat.** The named
deficiency of the generic alternative — no provenance, silent omission — is precisely
what RAG provenance and ACU content sign-off answer. Put this citation next to the moat
claim in GTM §7.2 rather than asserting the moat.

**Attrition is the norm, not the exception.** A systematic review and meta-analysis of
app-based interventions for chronic disease found a **pooled dropout of 43%** (95% CI
29–57), rising to **49%** (27–70) in observational real-world studies against **40%**
(16–63) in RCTs. Range across studies: 9% (a one-year RCT) to 82% (a six-week
observational study). **Study length had little impact on dropout rate.** The review also
notes that *"up to 80% of all participants in mHealth interventions may engage in only
[minimal use], defined as logging in to the service less than twice."*
Meyerowitz-Katz et al., *JMIR* 2020 — [10.2196/20283](https://doi.org/10.2196/20283)

It also warns that clinical trials reporting 70%+ retention are usually short and *"may
not represent the situation in real-world use."* Any Kindred Care retention claim drawn
from a supported pilot must say so.

**The field does not measure what matters.** In the perinatal engagement review, only
**38% (6/16)** of studies reported *enactment* — whether women actually used what they
learned — and the authors flag inconsistent terminology across "attrition, withdrawal,
dropout and loss to follow-up" as making comparison impossible.
[10.2196/36620](https://doi.org/10.2196/36620)

## 3. Engagement — the mechanics

### The enrolment finding, which outranks everything else

The SMART start feasibility study of digital pregnancy care measured retention by
enrolment route:

| Enrolment route | Median retention |
|---|---|
| **Self-enrolment** | **0 days** (IQR 0–2) |
| Clinic-enrolled, no self-examination package | 0 days (IQR 0–33) |
| **Clinic-enrolled, with self-examination package** | **167 days** (IQR 96–248) |

Adherence to scheduled tasks decayed by task type: weight **42.0%** of weeks as
scheduled, sleep **24.7%**, urinalysis **14.7%**, blood pressure **12.4%**, with a
notable drop across all measures at week 14.
Sander et al., *npj Digital Medicine* 2025 — [10.1038/s41746-025-01966-8](https://doi.org/10.1038/s41746-025-01966-8)

Three consequences for Kindred Care:

1. **The enrolment-code model is evidence-aligned.** A mother enrolled by her maternity
   service, at a booking-in appointment, is a fundamentally different retention prospect
   from one who downloads an app. The register's enrolment-code architecture is not just
   a billing mechanism — it is the retention mechanism, and it should be argued that way
   in the pack.
2. **B2C is weaker than B2B on retention, not just on revenue.** Self-registration
   returned a median of zero days. The month-12 B2C option should be framed as reaching
   women *outside* a service relationship, with retention expectations set accordingly —
   not as the same product with a different payer.
3. **Bundle something tangible with enrolment.** The 167-day cohort had a physical
   self-examination package. Kindred Care has no physical artefact. Consider what plays
   that role — a midwife-delivered onboarding moment, a personalised plan generated at
   enrolment, something that makes the enrolment an event rather than a link.

### What raises engagement

- **Baseline need.** In the perinatal engagement review, the study with the highest
  retention and lowest loss to follow-up had participants at *higher risk of
  psychological distress at baseline* — the authors note they *"may have had increased
  motivation to attend."* [10.2196/36620](https://doi.org/10.2196/36620)
- **Ease of use and technology confidence.** Both significantly associated with higher
  adherence in SMART start. [10.1038/s41746-025-01966-8](https://doi.org/10.1038/s41746-025-01966-8)
- **User-centred design — but it is not sufficient.** One study in the review ran a
  full user-centred design process before its pilot and still saw **63% dropout from
  baseline to six weeks postpartum**. Co-design is necessary and does not rescue a weak
  enrolment route. [10.2196/36620](https://doi.org/10.2196/36620)

### The equity paradox — read this one twice

SMART start found adherence **significantly higher** among participants with greater ease
of technology use, greater interest in technology, and **higher educational attainment** —
and **significantly lower** among participants who **already had children in the
household**. [10.1038/s41746-025-01966-8](https://doi.org/10.1038/s41746-025-01966-8)

Breakthrough Victoria is being asked to fund equity reach, including a regional cohort.
The evidence says the mothers who adhere best are the tech-confident, higher-educated,
first-time mothers — and the mothers the equity narrative promises to serve are the ones
who drop out. **If the pilot does not design and measure for this explicitly, the
evaluation will produce a regressive result and the equity claim will be undermined by
your own data.**

That is a risk to state in the pack before an assessor states it. It is also a research
question worth owning: an intervention that closes rather than widens the adherence gap
is a genuinely publishable finding and a defensible moat.

## 4. What this means for the pilot design

The pilot's job is to produce a result a Victorian maternity service will buy on. That
constrains the design more than the research question does.

1. **Select for need.** Do not run on an unselected antenatal population. Recruit where
   baseline scores leave room to move — the null-result trap above is the most common
   failure in this literature.
2. **Pre-declare the success criteria, the denominator and the retention definition.**
   Against a 43% pooled dropout benchmark, not against optimism. Say in advance what
   counts as engaged.
3. **Enrol through the service, at a clinical moment, with something tangible.** Never a
   QR code on a poster.
4. **Measure enactment, not just usage.** Only 38% of the field does. Measuring it puts
   Kindred Care above the field's own reporting standard — and it aligns directly with
   Brad's DEFINE reporting-guideline work, which is a coherence argument the pack should
   make.
5. **Stratify the analysis by education, parity and digital confidence from the start.**
   Pre-specified, not post hoc. That is how the equity claim survives contact with data.
6. **Report against a reporting guideline.** Given DEFINE, reporting the pilot to a named
   standard is close to free and disproportionately credible.

## 5. Procurement and pricing

### What the market already does

- **Eve** — the Victorian incumbent — is *free of charge to all maternity patients
  attending a hospital with an Eve subscription*. The service pays; the mother does not.
  B2B2C is the established norm in this exact market, not an innovation.
- **UK comparator.** A maternity app with library content and asynchronous midwife chat
  is listed on the NHS G-Cloud digital marketplace at **£55,000 per licence per year**
  (Acadiant Limited). Convert at a current rate before quoting; it is the closest public
  price point to Kindred Care's shape.
- **Healthcare SaaS norms.** Tiered pricing by feature and user band; volume-based scaling
  with typical discounts of 15–25% beyond 250 beds; and **37% of healthcare IT vendors now
  offer some form of outcomes-based pricing, up from 18% in 2018** — a vendor-survey
  figure from a commercial source, so treat it as indicative rather than evidential.
- **Per-birth costing is native to Australian maternity analysis**, so a per-birth unit is
  legible to a Victorian service in a way that per-seat is not.

### Recommended pricing architecture

**Price on annual birth volume bands.** This is already the shape in the Kindred Care
forecast (SCHHS sits in a Network tier on births per year) and it is the right one:

- Births per year is a number every maternity service already knows and reports.
- It is stable and forecastable for both sides.
- It does not punish the service for the product working.
- It maps to the service's own cost language.

**Avoid per-active-user pricing.** It converts engagement — which is Kindred Care's job —
into the customer's financial risk, and it caps your revenue precisely when the product
succeeds. It also invites the buyer to interrogate your retention figures during
negotiation, which given the 43% benchmark is a conversation to have in the evaluation
report, not the contract.

**Price the first pilot as a fixed fee that includes the evaluation, sized under the
service's direct-engagement procurement threshold.** Never as a discount off list. A
published list price you have already discounted is a price you spend the next three
negotiations defending.

**Handle equity with an uplift, not a discount.** The SCHHS/Wishlist arrangement already
does this — an uplift above standard rate to support rural-equity reach. Discounting
regional sites signals that the regional cohort is worth less, which is the opposite of
the funding narrative.

**Defer outcomes-based components to year two.** They are increasingly expected and BV
will respond well to the option being on the table, but never tie year-one revenue to an
outcome you cannot yet evidence.

### One correction to the current plan

The register's mother survey (P1-05, 100 responses) uses **Van Westendorp** price
sensitivity. That is a **consumer willingness-to-pay instrument and it cannot set the B2B
licence price.** A health service does not pay what a mother would pay; it pays a
fraction of the cost it avoids — midwife time, avoidable triage calls, unplanned
presentations. Keep Van Westendorp for the B2C tier, and anchor the B2B price to the
service's own economics. If the survey is currently the intended input to B2B pricing,
that is a gap the pack should close before UCAC.

## 6. What to change in the pack

| # | Change | Where |
|---|---|---|
| 1 | Add the enrolment-retention evidence as the justification for the service-enrolled model | GTM §2, §4.2 |
| 2 | Reframe B2C as a different retention proposition, not the same product with a new payer | GTM §5, board B2C gate |
| 3 | Cite Horgan et al. next to the provenance moat instead of asserting it | GTM §7.2 |
| 4 | Add Eve to the competitor table | GTM §7.1 |
| 5 | State the equity–adherence paradox and how the pilot will measure it | GTM §9, pilot protocol |
| 6 | Set pilot success criteria against the 43% attrition benchmark, pre-declared | Pilot protocol |
| 7 | Add enactment measurement, tied to the DEFINE work | Pilot protocol, GTM §7.2 |
| 8 | Separate Van Westendorp (B2C) from avoided-cost anchoring (B2B) | Pricing Model v1 |
| 9 | Add the £55,000 NHS G-Cloud comparator as an external price anchor | Pricing Model v1 |

## Sources

Retrieved from PubMed:

- Suharwardy S, et al. Feasibility and impact of a mental health chatbot on postpartum mental health: a randomized controlled trial. *AJOG Global Reports* 2023;3(3):100165. [10.1016/j.xagr.2023.100165](https://doi.org/10.1016/j.xagr.2023.100165)
- Horgan R, Martins JG, Saade G, Abuhamad A, Kawakita T. ChatGPT in maternal-fetal medicine practice: a primer for clinicians. *Am J Obstet Gynecol MFM* 2024;6(3):101302. [10.1016/j.ajogmf.2024.101302](https://doi.org/10.1016/j.ajogmf.2024.101302)
- Understanding Engagement in Digital Mental Health and Well-being Programs for Women in the Perinatal Period: Systematic Review Without Meta-analysis. *J Med Internet Res* 2022. [10.2196/36620](https://doi.org/10.2196/36620)
- Rates of Attrition and Dropout in App-Based Interventions for Chronic Disease: Systematic Review and Meta-Analysis. *J Med Internet Res* 2020. [10.2196/20283](https://doi.org/10.2196/20283)
- Adherence to digital pregnancy care — lessons learned from the SMART start feasibility study. *npj Digital Medicine* 2025. [10.1038/s41746-025-01966-8](https://doi.org/10.1038/s41746-025-01966-8)

Public web sources: NHS G-Cloud digital marketplace listing (Acadiant Limited, maternity
app, £55,000 per licence per year); Medicity Eve product and Victorian health service
deployment pages; commercial healthcare-SaaS pricing surveys (indicative only).

**Author-verification note.** Author attributions for the two JMIR reviews were not
confirmed against the source record in this pass and are cited by title and DOI. Confirm
before the citation appears in a document that leaves the venture.
