# Diligence question bank

**30 Aug 2026 · v1 · Confidential — ACU & BoR**

Forty questions Kindred Care will be asked, with the answer as it stands **today** and, where
today's answer is weak, the work that fixes it. Written to be read aloud.

**The discipline:** an answer marked ⚠ is one we cannot yet give well. Those are the
preparation list. An honest ⚠ that names its own fix beats a confident evasion every time —
and a venture that hands over its own weak-answer list is read as unusually well run.

**Rules for using this.** Never improve an answer by improving the claim. Where a number is
quoted, it comes from `canonical-numbers.md`. If a document in the pack disagrees with an
answer here, the document is stale.

---

## A. Structure, ownership and the entity

**1. What exactly am I investing in?**
Kindred Care Pty Ltd, to be incorporated at the POC gate. Bundle of Rays and ACU as
founding shareholders; background IP licensed in from both parents, never assigned; the
company owns all foreground IP. Innovation Victoria comes in post-completion as an
investor with no IP contribution. Today the venture runs as an unincorporated arrangement
between BoR and ACU under a scoping agreement, which is the normal pre-POC posture.

**2. What's the equity split? ⚠**
Not yet agreed. It will be set by contribution-based valuation across cash, in-kind and IP
— the model that informs it is being restated now, and the cap table is a 2 October
deliverable. *Fix: cap table v1 (P2-06), which depends on the IP register (18 Sep).* We are
deliberately not quoting a split we have not negotiated.

**3. Your documents say 70/30, "to be agreed", and "held by Bundle of Rays". Which is it? ⚠**
"To be agreed" is correct; the other two are stale wording being removed this cycle. The
target structure is the founding-shareholder model in answer 1. *Fix: consistency sweep,
this week.*

**4. Does ACU's holding dilute on a future round?**
To be settled in the shareholders agreement. Our position going in is standard pro-rata
dilution with pre-emptive rights, not anti-dilution — but it is ACU's call as much as ours
and it is on the Heads of Agreement list.

**5. Who controls the company?**
Board composition is a start-up-suite item. Our proposal: founding shareholders
proportionate, an independent chair, and investor rights appropriate to holding. A
recruited lead becomes CEO or MD at incorporation with the founder moving to the board.

**6. Bundle of Rays has existing investors. How do their rights affect this? ⚠**
BoR carries prior investor arrangements. Kindred Care Pty Ltd is a separate entity, so
those rights attach to BoR's shareholding rather than to the company — but the terms need
to be on the table before signature. *Fix: locate and index the BoR investor terms; first
diligence item, this week.*

---

## B. The money

**7. How much are you raising and on what terms?**
$300,000 at the POC round, then $1,000,000 at commercialisation — $1.3M in total under
BVUIP, each round matched 50/50 between ACU and Innovation Victoria. POC is a SAFE with a
side letter and a binding agreement for post-incorporation shares; the commercialisation
round is a full subscription into the incorporated company.

**8. Where is ACU's half coming from? ⚠**
ACU's cash obligation is $650,000 across both rounds — $150,000 at POC and $500,000 at
commercialisation. ACU has flagged that no standing cash pool exists for it, and the
Enterprise Office is progressing a syndicator pathway. **This is the venture's single
largest open item and we are not going to pretend otherwise.** *Fix: dated position
requested from ACU Enterprise Office; open since July.*

**9. What does the POC money buy?**
The TRL 3→4 climb: a curated 40-document ACU corpus, a gold-standard evaluation set
co-built with ACU, and the first formal retrieval evaluation against declared thresholds —
recall@5 ≥ 0.85 and safety-tag triggering ≥ 0.95. It converts a working system into an
evidenced one.

**10. Your model shows negative cash in year one. ⚠**
It did, and it was wrong to leave it that way. The model is being restated: BVUIP moved
out of income and into financing where it belongs as a SAFE, the FY27 equity line re-sized
to hold a three-month operating buffer, and international revenue moved to a labelled
upside case. Restated, FY27 requires roughly $720,000 beyond the POC. *That number is the
reason answer 8 matters.*

**11. Your unit economics claim peak burn of $0.15M. Your model says $770,000. ⚠**
The $0.15M figure is being withdrawn. The model figure is correct and, at roughly $770,000
peak cumulative burn to a repeating-revenue business, still a genuinely capital-efficient
profile — we would rather say the true number.

**12. What's your gross margin? ⚠**
Between 35% and 80%, depending on a unit-cost figure we are settling this week. Three
internal documents carry different variable costs per active mother — approximately
$14.70, $44.60 and $70.44 a year — driven by an unresolved decision on avatar-video plan
economics. **We are not quoting a margin until that lands.** *Fix: CTO decision on the
HeyGen plan basis and GCP cost per active user at three scale points, this week.*

**13. Why is your forecast mostly offshore revenue? ⚠**
It was, and it shouldn't have been. India and UK/USA are being moved into a clearly
labelled upside scenario, leaving a base case that is Victorian and Australian. The
international relationships are real, but they are optionality, not thesis — and for
Victorian co-investment the base case should be defensible without them.

**14. What are your revenue assumptions on churn?**
10% institutional churn, a ten-year customer life, consistent with the venture's own unit
economics. The earlier forecast carried zero churn across five years; that is corrected.

**15. When do you need the next round?**
The commercialisation round follows the POC gate, targeted FY28. It is deliberately
sequenced to follow pilot evaluation, so the round is priced against evidence rather than
promise.

---

## C. Technology and readiness

**16. What TRL are you at?**
TRL 3, climbing to 4. We hold that line deliberately. A working, deployed, multimodal
Companion exists — but retrieval accuracy is not yet validated against a gold-standard
evaluation set, and until it is we will not claim TRL 4. The POC funds exactly that climb.

**17. But you've shipped a lot of software. Isn't that TRL 4 or 5?**
Volume of build is not the test. Our own instrumented definition of TRL 4 is recall@5
≥ 0.85 and safety-tag triggering ≥ 0.95 measured against an evaluation set that does not
yet exist. We would rather be at 3 with a measured path to 7 than claim 4 and be unable to
show the measurement.

**18. How do I know the safety controls actually work?**
Because they are proven by planted mutation, not asserted. The deterministic safety net is
demonstrated to work with no LLM in the path at all — using a poison model that fails the
build if it is ever invoked in the safety path. Tier-3 triggers are unsuppressible and
proven so from both directions. The parser survived 49 Unicode homoglyph attacks and 35
adversarial probes with zero bypasses. We can show the tests.

**19. What happens if a mother discloses something dangerous at 2am?**
Deterministic keyword triggers fire before any model involvement and deliver emergency
contact protocols. A dual-agent architecture has a clinical supervisor intercepting every
response before it reaches her. Escalation is autonomy-first: she nominates her own care
team and the Companion prompts her to reach them — it does not contact anyone on her
behalf unless a service has enabled consented outreach, which is off by default.

**20. You depend on a third-party model. What if pricing or behaviour changes?**
Vendor seams exist and a multi-vendor roster is in the architecture. Our defensibility was
never the model — frontier performance will be matched within eighteen months and RAG
architectures are already commodity. The moat is the governed corpus and the evidence.

**21. Is this a medical device? ⚠**
Our position is no: it is education-only, cannot diagnose, triage, interpret symptoms or
advise on treatment, and that boundary is enforced architecturally rather than by policy,
with documented boundary tests. **What we do not yet have is that position in writing from
a regulatory adviser.** *Fix: written TGA classification position — required before the
first health-service pilot conversation.*

**22. Where is the data?**
Australian-resident infrastructure on Google Cloud, inference in Sydney. Transcripts only
— no recording, and that commitment is enforced in continuous integration against the
whole artefact class, with 41 fixture tests. Tenant isolation at the database level.

---

## D. Market and customers

**23. Who is the buyer?**
Victorian public maternity services first, through the ACU midwifery network. Executive
sponsor is a Director of Nursing and Midwifery or equivalent; the budget conversation is
framed on workforce and equity, not patient education.

**24. Show me a customer. ⚠**
We cannot yet. We have an invitation to present to Sunshine Coast HHS maternity
leadership, ACU-routed introductions into Victorian services in progress, and a target of
three to four Victorian letters of intent by October–November. **No LOI exists today.**
*Fix: this is the market track's whole focus for September.*

**25. What's the competitive landscape?**
The incumbent in our exact beachhead is Eve, built by Cabrini Health, launched 2020,
national Not-for-Profit Solution of the Year in 2021, 50,000+ women, deployed across
Victorian services. It has advantages we do not: antenatal record integration, a human
midwife in the chat, and incumbency. We are a different product — education delivered
conversationally at the moment of need, university-governed, with an evidence pipeline.

**26. Six years and 50,000 women. Why haven't they won?**
The clinicians we speak to describe Eve as difficult to use and not focused on education.
That reads to us as a market occupied rather than served. We would rather compete on the
job that is not being done than on the one that is.

**27. Should you be partnering with them instead?**
It is a live option we have deliberately considered rather than dismissed. Cabrini is a
Catholic health service; ACU is a Catholic university; Eve is records-and-tools and we are
education-only. On paper those are complements. Our posture is compete-first, partner-open.

**28. What's your pricing? ⚠**
Tiered by annual birth volume — the unit every maternity service already reports.
Indicative list runs from $25,000 for the smallest services to $95,000 at enterprise
scale, with pilot sites at an explicit, time-limited discount. **Our own documents
currently carry more than one schedule and we are consolidating to a single list this
cycle.** *Fix: canonical price list, pending final sign-off.*

**29. Why won't a health service just use ChatGPT?**
Because they cannot govern it. No content provenance, no clinical sign-off, no audit
trail, no escalation architecture, and no way to answer a coroner. The documented failure
of general models on maternal patient information is omission of clinically important
content and no verifiable references — which is precisely what retrieval provenance and
academic sign-off answer.

**30. How long is the sales cycle?**
Nine to eighteen months in public health services, plus security and privacy review. That
is why the round is sized to fund roughly 24 months and why the pilot exists — the
evaluation converts the conversation from a demonstration to an outcomes discussion.

---

## E. Evidence, ethics and the founder

**31. Your evidence comes from research your founder runs. How is that independent? ⚠**
It is a real conflict and we declare it rather than manage it quietly. ACU's own structure
separates Kindred Care-aligned PhD outcomes from non-aligned ones; the HREC application
names the founder as Student Investigator with the commercial relationship declared; and
the publication protocol prevents the company suppressing negative findings. *Fix:
publication-protection protocol to survive change of control — drafted into the exit
strategy.*

**32. The founder runs another company, is doing a PhD, and holds an overseas fellowship.
How much time does Kindred Care get? ⚠**
Founder-led through diligence, with a recruited lead becoming CEO or MD at incorporation
and the founder moving to the board. That transition is deliberate and in the plan rather
than a concession. **The recruited lead is not yet appointed.** *Fix: co-CEO process
active; candidate met, one-to-one this week.*

**33. What does your own research say about the risks of this product category?**
That warmth in a conversational agent can produce dependence rather than confidence — we
call it the warmth trap. It is the founder's published research interest and it is
designed against: the Companion is engineered to scaffold self-efficacy rather than solve
on the mother's behalf. We would rather name our own failure mode than have an investor
find it in a paper.

**34. Has the pilot got ethics approval? ⚠**
HREC submission is coordinated by ACU and remains an open item, along with legal sign-off
on the privacy notice and terms. **No consented user data should be collected until both
land** — and consent wording must cover research use at the point of collection, because
it cannot be retrofitted.

**35. What are your evidence thresholds?**
Declared in advance: recall@5 ≥ 0.85 and safety-tag triggering ≥ 0.95 at UAT, rising to
recall@5 ≥ 0.90 with faithfulness ≥ 0.95 at pilot. Pilot success criteria are pre-declared
with the service before enrolment opens, and the analysis is stratified by education,
parity and digital confidence so an equity claim can be tested rather than assumed.

---

## F. The hard ones

**36. What's the single biggest risk to this venture?**
ACU's $650,000 cash obligation, unresolved since July. Everything else on our list is work;
that one is a dependency we do not control.

**37. What would make you walk away?**
If the education-only boundary could not hold — if the product could only be useful by
becoming clinical — the regulatory and safety profile would change fundamentally and this
would be a different company requiring different investors.

**38. Why should Victoria fund this rather than someone else?**
Because the asset is Victorian: ACU midwifery in Fitzroy, Victorian pilot sites, Victorian
data residency, and a Victorian maternity system that carries the workforce pressure this
addresses. The international upside is real but it is upside; the base case is built here.

**39. What have you got wrong so far?**
Our financial model booked co-investment as income, carried no churn, and let
international revenue dominate a case for Victorian money. Our IP plan misattributed our
own platform. Our documents carried more than one price list. We found those ourselves,
before submission, and they are being corrected — which is the reason we are confident
about what remains.

**40. What do you need from us beyond money?**
A route to the ACU-side match. Introductions in the Catholic health sector, including to
Cabrini. And a hard read on what kills ventures at your investment committee, early enough
to fix it.

---

## The ⚠ list — the preparation queue

| # | Question | Fix | Owner | By |
|---|---|---|---|---|
| 12 | Gross margin unquotable | Settle unit cost | Hector | This week |
| 8 | ACU's $650k | Dated position | Russell / Bill | Requested |
| 21 | TGA position | Written regulatory advice | Brad | Before first pilot conversation |
| 24 | No customer | LOIs from Victorian sites | Brad / Lois | Oct–Nov |
| 2, 3 | Cap table and ownership wording | Cap table v1 + consistency sweep | Russell / Brad | 2 Oct |
| 28 | Multiple price lists | Canonical list sign-off | Brad | This week |
| 6 | BoR investor terms | Locate and index | Brad | This week |
| 34 | HREC and legal sign-off | ACU + lawyer | Brad | Before any consented user |
| 32 | Recruited lead | Co-CEO process | Brad / Lois | September |
| 10, 11 | Restated model | Apply restatement workbook | CFO | Before 2 Oct |
