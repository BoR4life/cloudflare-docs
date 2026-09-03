# CSIRO ON Accelerate — application, final draft v1.0

**03 Sep 2026 · Deadline Sun 06 Sep 2026, 11:59pm AEST · Lead: Brad Chesham**

**Scope assumption stated:** the problem section keeps its focus on the six weeks after
discharge — that is where the acute harm sits and it is the strongest writing in the pack.
The solution section states the product as it is defined everywhere else: **20 weeks of
pregnancy to twelve months after birth.** The two are consistent: the relationship is in
place before discharge so it is there when the window opens.

**Still for Brad to fill:** `[N]` Australian institutions · Russell's mobile · Hector's
surname and title · team members 4–6 · time percentages · the Wishlist meeting date ·
Important Dates check against 16 Sep / 16 Oct / 3 Nov / 28 Nov.

---

## Q1 — Tell us about the problem you are trying to solve

**Who experiences the problem**

In 2023, 281,099 women gave birth in Australia. The problem belongs to them and their families in the six weeks after they leave hospital — most acutely first-time mothers, women discharged early after uncomplicated birth, women from culturally and linguistically diverse and lower socioeconomic backgrounds, and those outside major centres. It is also experienced by the midwives and child and family health nurses expected to cover that window with hours they do not have.

**How it is currently handled**

Postnatal length of stay has collapsed. In 2023, 74% of Australian mothers were discharged within three days, and the average postnatal stay fell from 3.0 days in 2011 to 2.5 days in 2023; for first-time mothers the median is three days (AIHW, National Perinatal Data Collection). The WHO recommends healthy mothers and newborns receive facility care for at least 24 hours after an uncomplicated vaginal birth. A NSW mixed-methods study mapped what happens inside that stay: across an average 70-hour admission, women received a total of three hours of direct care from a health professional — 4.3% of the admission. Of that, 43 minutes went to breastfeeding support and 20 minutes to discharge information. After discharge, most women receive a written handout, a child and family health nurse contact at one to two weeks, and a GP check at six weeks. Between those points they are on their own at 3am, and reduced stays have not been matched by any expansion of home visiting.

**Why it matters**

The gap is where preventable harm sits. Around one in five Australian mothers — roughly 60,000 women a year — experience perinatal depression or anxiety (COPE, National Perinatal Mental Health Guideline). Antenatal depressive symptoms carry a sixfold increase in the odds of postnatal depressive symptoms, so much of the at-risk cohort is identifiable before discharge and still not followed. Feeding outcomes tell the same story: 91% of Australian infants are ever breastfed, but only 38% are exclusively breastfed at six months against a national target of 50% by 2025. Eighteen per cent of mothers cite insufficient milk supply and a further 5% attachment problems as the reason for stopping — both conditions that respond to timely, skilled support delivered in the first fortnight. The costs land on the system as unplanned emergency presentations, neonatal readmissions and later mental health treatment, and on the child through effects on growth, development and immunisation. This is not an edge case. It is the default experience of a universal service.

**What is currently used**

Four things fill the gap, none of them adequate. Hospital handouts and the state child health record, static and generic. Helplines such as PANDA, the Australian Breastfeeding Association and Pregnancy, Birth and Baby, which are excellent but reactive and reach women who already recognise they are struggling. Consumer pregnancy apps and social media parenting groups, which are commercially driven, clinically unvalidated and offer no escalation pathway. And, increasingly, general-purpose conversational AI — women are already taking postnatal questions to ChatGPT at 3am, outside any clinical governance, with no provenance for the advice given, no connection to their treating team, and no mechanism to escalate a bleeding, feeding or mental health red flag. That is happening whether or not health services sanction it.

**The opportunity**

The opportunity is to occupy that window deliberately: continuous, clinically governed, personalised support in place before discharge and through the weeks after it, built on clinically reviewed content with defined escalation pathways back to the treating service — rather than leaving the most vulnerable weeks of maternal care to chatbots and Facebook groups.

---

## Q2 — Tell us about your solution

**What it is**

Kindred Care is the Companion: a midwifery- and nurse-led education Companion a woman uses on her phone, at any hour, in plain language, from 20 weeks of pregnancy through to twelve months after birth. It is deliberately limited to education and signposting. It does not triage, interpret symptoms or diagnose. It teaches, it prepares, and when something needs a clinician it says so and routes her to one.

**The underlying technology**

The platform runs on Google Cloud's Vertex AI in Australian regions, with the security and audit controls a health service requires. That is the foundation, not the product. On top of it sits a governed retrieval layer over a corpus authored and reviewed by midwives and nurses, and a personalisation layer that holds a woman's stage of pregnancy or postnatal week and shapes what she is taught accordingly.

The safety architecture is the part we would ask an assessor to look at first. Two agents, not one: a generating agent and an independent supervising agent that checks every response against clinical rules before it reaches her. Escalation is deterministic — defined in code, not left to the model — with three tiers, the highest of which cannot be suppressed by anything the model or the user does. The design has been tested against a deliberately poisoned model and adversarial inputs, with no bypass found.

The research foundation is the Andragogical Agent Framework, developed through doctoral research at Australian Catholic University: how a conversational agent should teach an adult — reading readiness, respecting what she already knows, answering the question she actually asked, and recognising the point at which teaching must stop and a clinician must be brought in.

**Who it is for**

The end user is the woman, and by extension her partner and family. The customer is the health service responsible for her — public maternity services and private maternity units — for whom the postnatal window generates avoidable presentations, readmissions and complaints, and whose workforce cannot extend its reach any further.

**How it solves the problem**

At present a woman leaves hospital with a handout and a phone number she is reluctant to ring. Kindred Care replaces that silence with something continuous. At 3am, when her baby will not latch or she cannot tell whether her bleeding is normal, she gets an answer grounded in her own stage, in language she can act on. Where the answer is reassurance, she gets it and goes back to sleep. Where it is not, she is told clearly to contact her service or emergency care, the number is already in front of her, and the event is recorded. Between contacts, it prepares her for the scheduled reviews that should happen anyway — the early home visit, the six-week check — so the midwife's time is spent where it matters rather than on repeating discharge information forty times a week.

**Why it is better than what exists**

A handout cannot answer a question. A helpline needs her to already know she is in trouble. A consumer app knows nothing about her birth. A general-purpose chatbot — which women are already using at 3am — has no clinical governance and no escalation pathway; it will answer a postpartum haemorrhage question with the same confidence it answers a recipe. Kindred Care is that same behaviour done properly: governed by clinicians, bounded to education, engineered so that escalation cannot be talked out of, built by nurses and midwives on university research, on infrastructure a hospital will accept.

---

## Q3 — What traction does your idea have in the market?

**Where we are**

Kindred Care is pre-revenue and has not run a clinical trial. What exists is a working build, a defined evaluation design, health services in early discussion in two states, and a founding team that has closed institutional health-education contracts before.

**Health service engagement**

*Queensland.* Sunshine Coast Hospital and Health Service provided a written letter of clinical support in July 2026, and a meeting with Wishlist, the Sunshine Coast health foundation, is scheduled for the week of [7 September] to discuss evaluation funding. We applied in July to Queensland's Private Sector Pathways challenge to fund a postnatal evaluation; that application was not shortlisted, and the evaluation design it defined carries forward. Initial contact with UnitingCare's Buderim Private Hospital on 2 September drew an immediate positive response and an introductory meeting is being arranged. Exploratory discussions were held with Townsville Hospital and Health Service in June and July.

*Victoria.* We met the Victorian Chief Midwifery Officer in June 2026. Regional and metropolitan health services have been introduced through our clinical network and those conversations are at introduction stage.

*The profession.* The Australian College of Midwives met us in April 2026 and raised three areas of possible involvement — clinical oversight, professional education and conference engagement — which we are now progressing with them. The profession most exposed to an AI tool here has engaged with it as an extension of midwifery care rather than a threat.

The letters we hold are letters of clinical support for an evaluation, not procurement commitments.

**Track record of the founding team**

Bundle of Rays has two Indian state government contracts at execution stage — Maharashtra (10,000 student seats, five-year term, USD $900,000) and Uttar Pradesh (approximately 5,000 users, five-year term, USD $450,000), distributed through our partner Jaypee across state medical colleges, both expected to execute in late September 2026. Domestically, Bundle of Rays holds active engagements with [N] Australian universities and health services. This is a different product line to Kindred Care, but it demonstrates that this team can navigate institutional procurement, security review and clinical governance, and deliver at scale once a contract is signed.

**Engagement strategy**

We sell to the health service, not to the mother; the mother pays nothing. The buyer is a maternity service carrying avoidable presentations and readmissions after discharge, with a workforce that cannot stretch further. The route is a funded evaluation at a single Queensland site against defined outcomes, then procurement through the Victorian public system once outcome data exists, then expansion. Private hospital groups run standardised operations, so a proven private site is a template rather than a one-off.

**Proof this is what users want**

The strongest evidence is behavioural. Women are already taking postnatal questions to general-purpose AI at 3am, unprompted and unsafeguarded, because nothing else is open. Demand for round-the-clock conversational support is demonstrated; what does not exist is a safe, clinically governed version of it. The clinical data point the same way: 18% of Australian mothers stop breastfeeding citing insufficient supply and 5% citing attachment, both problems that resolve with timely skilled support; one in five experiences perinatal depression or anxiety, most identifiable before discharge yet not followed.

What we have not yet done is ask parents directly and systematically. A structured needs-and-preferences study — recalled moments of unmet need, forced trade-offs between forms of help, and modality in context — is designed and begins this month. We would rather arrive at ON Accelerate with that in hand than with assumptions.

---

## Q4 — Technology Readiness Level

**Select: TRL 3** (experimental proof of concept).

*If a justification field exists:* A working build exists with a dual-agent safety architecture, deterministic three-tier escalation and an unsuppressible top tier, tested against a poisoned model and adversarial inputs with no bypass found. TRL 4 requires validation against a gold-standard evaluation set (retrieval recall and safety-trigger performance at pre-declared thresholds), which is in construction. We hold ourselves to the level we can evidence.

---

## Q5 — Challenge alignment

Supporting healthy and thriving communities.

## Q6 — Sectors

Idea / target market: Medical science; Enabling capabilities. Team's project: Health and medical; Technology.

---

## Q7 — Investment or grant funding received

Kindred Care has not received investment or grant funding. It has been self-funded by Bundle of Rays Pty Ltd, with in-kind research contribution from Australian Catholic University. No company has yet been incorporated for the venture and no shares have been issued. The intended ownership structure is being formalised through ACU's commercialisation office; details are commercially confidential and available under NDA.

## Q8 — Investment Readiness Level

IRL 3.

---

## Q9 — IP

**How have you (or will you) protect your IP?** Yes. *(If a field exists:)* Background platform IP — the agent deployment platform, safety architecture and tooling — is held by Bundle of Rays Pty Ltd and will be licensed to the venture, not assigned. Clinical content is held under authorship and review records. The venture's IP plan is in draft.

**Is the IP encumbered?** **Yes.** The Andragogical Agent Framework arises from doctoral research at Australian Catholic University, and the allocation of IP between Bundle of Rays and ACU is being finalised through ACU's commercialisation office as part of the venture's formation.

**Documents to support current IP status?** No formal registrations. A draft IP plan (v0.3) exists and is available on request.

**Incorporated a company?** No. Bundle of Rays Pty Ltd is the existing operating company. Kindred Care is intended to be incorporated on completion of the structuring work with ACU.

---

## Q10 — Why a startup venture is the most appropriate pathway

**Pathways considered.** Licensing the framework and content to an existing digital health vendor was considered and rejected: no incumbent holds the midwifery governance, the deterministic escalation architecture or the university research base together, and a licence would separate the clinical governance from the product it is meant to govern. A research-only partnership was considered and rejected because it produces papers rather than a deployed service inside the window where the harm occurs. Delivery as a feature of Bundle of Rays' existing education platform was considered and rejected because a health service buys clinical safety from an entity that can be procured, hold indemnity and be held accountable, not from a training company's product line.

**Why a venture, and how it creates impact.** The value is in the integrated whole — governed content, escalation that cannot be talked out of, a persistent presence across the risk window — sold to health services as workforce capacity. That requires an entity that can contract with public and private health services, hold clinical governance in its own right, and be evaluated and published on. Impact is measured in scheduled postnatal reviews that actually happen, escalations that convert to care, and midwife hours returned to clinical work.

**Evidence of viability.** The buyer is engaging without a formal sales approach: written clinical support from a Queensland health service, an immediate positive response from a private maternity operator, a foundation meeting on evaluation funding, exploratory discussions with a second Queensland service, and a meeting with the Victorian Chief Midwifery Officer. The Australian College of Midwives has proposed forms of involvement rather than objection. The founding team has closed institutional health-education contracts before, including two Indian state government contracts at execution stage.

**Current status.** Pre-incorporation. A working build with the safety architecture in place. Evaluation design defined. A parent needs-and-preferences study beginning this month. Venture structure, IP allocation and commercial terms being formalised with ACU's commercialisation office, with ACU executive meetings on the venture in mid-September 2026.

**Company structure.** Bundle of Rays Pty Ltd holds background IP and has funded development to date. Australian Catholic University is research partner and prospective venture party. The intended shareholding structure is to be set out in the agreement currently in preparation with ACU; details are commercially confidential and available under NDA.

---

## Q11 — Commercialisation Manager

Dr Russell Carrington · Commercialisation Manager, Enterprise Office (ODVCRE), Australian Catholic University · russell.carrington@acu.edu.au · [mobile]

Proof of endorsement to follow within one week of submission.

---

## Q12 — Engagement with the Commercialisation Office and the commercialisation plan

**Engagement to date**

Kindred Care has been developed in direct engagement with ACU's commercialisation team rather than presented to it after the fact. Russell Carrington and Bill Russell have been the commercial contacts throughout; Professor Lois McKellar, Head of Discipline (Midwifery), leads the research relationship. The current work with the office concerns the IP position between the university and the venture, the commercial terms of ACU's participation, and a state government co-investment pathway being prepared with the office. ACU executive meetings on the venture are scheduled for mid-September 2026. A director of Bundle of Rays with senior nursing executive experience was re-introduced to the team on 27 August as the structuring work moved into its final stage. That work is in train, not hypothetical.

**Commercialisation plan**

The business model is business-to-business software sold to health services on an annual per-site licence banded by births per year. The mother pays nothing. The buyer is the maternity service responsible for her, for whom the postnatal window generates avoidable presentations, readmissions and complaints it currently has no tool to address, framed and priced as workforce capacity rather than patient education.

Go-to-market runs in three stages. First, a funded evaluation at a single Queensland maternity service against pre-declared clinical and service outcomes, with a published protocol. Second, procurement into the Victorian public system once outcome data exists, supported by the system-level engagement already begun with the Victorian Chief Midwifery Officer and the Australian College of Midwives, and by ACU's Melbourne base. Third, expansion — private hospital groups run standardised operations, so a proven site is a template, and public services follow evidence.

**Team transition**

Bundle of Rays is an operating company with revenue, so the team moves into venture roles from paid positions rather than from unfunded research. Brad Chesham (RN, MSc; CEO, Bundle of Rays) leads the venture at [x]% of time. [Hector surname] leads the build at [x]%. Professor Lois McKellar leads the research and clinical governance relationship within ACU. ACU's continuing role is research partner and venture party, with academic supervision of the underlying framework remaining in the university.

**What we need from the program**

Our gaps are validation discipline and access to investors who understand clinical software. We have a defensible research base, a working build with an unusual safety architecture, an engaged buyer and a team that has delivered institutional health contracts. What we have not done is stress-test the business model in front of people whose job is to find the holes, or build the investor relationships needed to fund national scale.

---

## Team

| # | Name | Organisation | Role in the team | Core (attends all sessions)? |
|---|---|---|---|---|
| 1 | Brad Chesham | Bundle of Rays | Lead; clinical and commercial | **Yes** |
| 2 | Hector [surname] | Bundle of Rays / ClinOps | Technical lead | **Yes** |
| 3 | Prof Lois McKellar | ACU | Research and clinical governance lead | **Yes — confirm with her** |
| 4 | [Marie — if her 90-day engagement is confirmed] | — | Clinical partnerships | — |
| 5 | Bill Russell | ACU | Enterprise / grants | Supporting |
| 6 | — | — | — | — |

**Three core members must have agreed to attend every session before submission.**

---

## FoR / SEO (ANZSRC 2020) — verified 03 Sep 2026

**Correction to earlier advice: Midwifery is its own four-digit group, 4204. It does not sit
under Nursing.** Division 42 Health Sciences comprises 4201 Allied health and rehabilitation
science, 4202 Epidemiology, 4203 Health services and systems, **4204 Midwifery**, 4205
Nursing, 4206 Public health, 4207 Sports science and exercise, 4208 Traditional,
complementary and integrative medicine, 4299 Other health sciences.

**Primary FoR Division: 39 EDUCATION.** The question asks for the research underpinning the
technology. The application's own Q2 names the Andragogical Agent Framework, doctoral
research supervised in ACU's Faculty of Education and Arts. Health is the application, and
SEO carries it. *Defensible alternative: 42 Health Sciences, if being read by clinical
assessors matters more; then 4204 Midwifery is the primary group.*

**Four-digit FoR spread:** 3901 Curriculum and pedagogy · **4204 Midwifery** · 4203 Health
services and systems · 4602 Artificial intelligence.

**SEO Division 20 Health** (confirmed groups): 2001 Clinical health · **2002 Evaluation of
health and support services** · 2003 Provision of health and support services · 2005 exists
with six-digit sub-codes.

**2002 is the strongest SEO fit** — its sub-codes include *health education and promotion*,
*telehealth*, *health inequalities* and *health system performance*. That is Kindred Care
described in ANZSRC's own words, and it reinforces the workforce-and-equity framing rather
than the patient-education framing.

**Authoritative sources:** ABS ANZSRC 2020 (https://www.abs.gov.au/statistics/classifications/australian-and-new-zealand-standard-research-classification-anzsrc/latest-release).
ACU hosts a browsable FoR 2020 list at https://orion.acu.edu.au/ACU/res/FOR20-list.html —
use that with Russell and Bill so the codes match what ACU reports.

---

## Pre-submission checklist

- [ ] Bill sights it today (2pm)
- [ ] Russell sights it by email before Sunday — it names ACU
- [ ] Important Dates checked against 16 Sep / 16 Oct / 3 Nov / 28 Nov
- [ ] Three core team members confirmed by name
- [ ] Lead Organisation settled
- [ ] Every placeholder filled or the sentence removed
- [ ] Every statistic in Q1 has a citation ready for interview
- [ ] No "joint venture", no "70/30", no investor named, no "CLARA", no "clinical reasoning"

---

## Team Q — What does your team want to achieve through this program? (225 words)

Three outputs, in priority order.

First, a pricing and business model that survives a hostile read. Our schedule is built from a cost model, not from what an Australian maternity service will actually pay for it. We want it broken in front of people who have sold into this system.

Second, evidence discipline. We hold TRL 3 because the evaluation set that would make it TRL 4 does not yet exist, and we have never systematically asked an Australian parent what she wants. A structured needs-and-preferences study begins this month. We want the rigour to design what follows it, and to publish whichever way it falls.

Third, investor relationships. We have not raised, and we do not know the people who fund clinical software in this country.

Our coverage. Clinical and research are strong: a registered nurse founder, and ACU's Head of Discipline (Midwifery) leading research and clinical governance. Technical is strong: a working build with a dual-agent safety architecture. Commercially, we have closed institutional health-education contracts internationally.

Our gaps. We have never closed an Australian health service. We have no named clinical safety officer accountable for the escalation boundary, and no consumer voice in content governance. Both are appointments we intend to make, and we would value the program's challenge on how.

We would rather these were found now than at diligence.

### Team member — Russell Carrington (ACU), contribution (100 words)

Russell is ACU's Commercialisation Manager and the university's commercial lead on Kindred Care. He is structuring the venture: the IP position between ACU and the company, the terms of ACU's participation, and the state co-investment pathway being prepared with his office. He carries the venture through ACU's internal approvals, and is the route to the university's clinical and research networks in Victoria.

In the program he brings institutional commercialisation experience, and tests our structure and terms against ACU's requirements as they are set. He is the person who converts what we design into something the university can sign.

### Team member — Marie Gentile-Andrit, contribution (96 words)

**DO NOT SUBMIT until the four flags below are cleared.**

Marie leads clinical partnerships for Kindred Care under a defined engagement from September 2026. Her contribution is access and judgement: mapping which Australian maternity services can be opened, which cannot, and why. That assessment is the one nobody else on the team can make. She leads engagement with clinical teams and shapes the evaluation design with them, rather than presenting it to them.

In the program she is the counterweight to founder optimism. She tests our commercial assumptions against what a maternity unit will actually adopt, and carries the buyer conversations we are asked to run.

**Flags.** (1) Organisation "ACU" and category "Researcher" are unverified — the 30 Aug brief records that she writes from a personal address and that where she works was an open question for the one-to-one. (2) COI status is **PENDING DISCLOSURE** — prior-application IP (the COVID education app) and current affiliations unresolved; if she is currently inside a Victorian health service, naming her as a team member while that service is a prospective buyer is the probity problem the brief identified. (3) Email blank, and consent plus the CSIRO Privacy Notice is required before listing her. (4) Attendance — Bootcamp and Immersion for all members, 75% to graduate, against a 90-day engagement.
