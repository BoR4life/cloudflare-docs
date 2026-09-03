# The eight-week evidence sprint — protocol v1.0

**30 Aug 2026. Supersedes `pilot-protocol-v0.1.md`,** which predates the interface doctrine,
the D-23 finding, the corrected unit economics and the compliance stack.

## Why this is the keystone

The build is 97 of 148 stories. The three questions that decide whether any of it is worth
doing — **does a mother engage, will a service pay, does it work** — are all at zero.

Almost everything else in the programme is downstream of numbers we could hold in eight
weeks. **The build is not the bottleneck. Evidence is.**

---

## 1. Site

**Sunshine Coast.** Not Victoria, and the reasoning should be stated openly rather than
finessed:

- **Michelle Schmidt has signed** for SCHHS Maternity Services (23 July).
- **Wishlist provides a funding pathway** — Brendan Hogan signed the same day.
- A **national simulation research centre** sits alongside.
- Victoria has **zero sites past step 1** after four months, and the named channel has said
  in writing that her connections are in South Australia.

**The answer to "but Innovation Victoria needs Victorian benefit":** a Queensland pilot
producing real evidence is worth more to a Victorian funder than three Victorian meetings
that have not happened. Evidence travels; meetings do not. Run the sprint where the signed
partner is, and take the results to Victoria.

*Route via rung 0 — record the introduction, the interest and the pathway before the
approach, per the early-adopter doctrine.*

## 2. Cohort

**150 mothers.** Deliberately matched to the proposed $18,000 entry tier so the pilot is a
real commercial engagement at list price rather than a discounted favour — which protects
the reference price and keeps it clear of the contract-splitting line.

**Honest limitation, stated up front and in every output:** the cohort spans 20 weeks
gestation to 12 months postnatal — about 16.6 months. **Eight weeks measures early-phase
engagement only.** It cannot measure 16-month retention, and any claim that it does will be
taken apart. What it *can* do is establish the engagement rate, the modality split and the
cost base, which is what the decisions need.

Recruit across the span — antenatal, early postnatal, later postnatal — rather than a single
phase, so the modality and engagement data is not an artefact of one life stage.

## 3. What we measure

### Primary — these three decide open questions

| # | Measurement | Model assumes | Decides |
|---|---|---|---|
| 1 | **Engagement rate** — % of enrolled active in a month | **40%** | Every margin, every tier, the whole forecast. The model says in bold it *"must be tracked from Day 1"* |
| 2 | **Avatar minutes per active mother per month** | **40** | **D-23.** 69–80% of variable cost rides on this number, and Hector hedged it himself |
| 3 | **Modality choice** — text vs voice vs video, when all three are available and none is the default | untested | The interface doctrine. Whether Call or Chat is the front door |

### Secondary — these matter almost as much

| # | Measurement | Why |
|---|---|---|
| 4 | **Enrolment conversion** — of mothers offered, how many enrol | The hidden operational risk. A service buys 150 places; midwives must enrol 150 women during appointments with no incentive. **Nobody has planned this and nobody is measuring it** |
| 5 | **Thread continuity** — return rate, gaps, re-entry triggers | The retention mechanism the persistent-thread design rests on |
| 6 | **Safety trigger rate** — T1/T2/T3 frequency, escalation outcomes, false-positive rate | The safety architecture's first contact with reality. Also the number a clinical governance committee will ask for |
| 7 | **Question taxonomy** — what mothers actually ask | Feeds corpus development and the bias assessment |
| 8 | **Midwife burden** — time cost per enrolment and per escalation | Determines whether a service renews |

### The TRL measurements — dependent, see section 5

| # | Measurement | Threshold |
|---|---|---|
| 9 | **recall@5** against the gold-standard eval set | **≥ 0.85** |
| 10 | **Safety-tag triggering** against the same set | **≥ 0.95** |

## 4. Instrumentation requirements

Per-mother, per-session, from day one — not reconstructed afterwards:

- Modality per turn, and every switch, with duration
- Avatar minutes metered per mother, reported weekly
- Time-of-day distribution — **this is how we prove or disprove the 2am hypothesis**
- Session length and inter-session interval
- Trigger events with tier and outcome
- Enrolment funnel: offered → consented → enrolled → first session → second session

**k-anonymity and the ADR-008 constraint apply.** No free text into the analytics store —
the closed-vocabulary allowlist already enforces this and must not be relaxed for the pilot.
Qualitative data comes through the consented research pathway, not the telemetry pipeline.

## 5. The dependency nobody has costed

**Measurements 9 and 10 require the gold-standard eval set, and the Analytics & evals epic
is 0 of 12.** FIX-DB-001 sits in that epic's own table, with every one of those stories
downstream of it.

So: **the TRL 4 claim is gated by an epic that has not started.** Two consequences —

1. **The sprint can run without it.** Measurements 1–8 need no eval set and answer D-23, the
   engagement assumption and the interface question. **Do not delay the sprint waiting for
   evals.**
2. **But TRL 4 by UCAC requires the evals epic to clear**, and that should be stated as a
   dated dependency on Track A rather than assumed.

## 6. Prerequisites — what must be true before mother one

| # | Prerequisite | Owner | Status |
|---|---|---|---|
| 1 | HREC / ethics pathway confirmed, and the **PhD firewall check run** | Brad + Lois | ⚠ Not done |
| 2 | Vertex regional endpoint confirmed | Hector | ⚠ `endpoint-check-for-hector.md` |
| 3 | Processor map ⚠ rows closed | Hector | ⚠ Draft |
| 4 | Incident response plan adopted, Privacy Officer named | Brad | ⚠ Draft, role unfilled |
| 5 | Transparency statement for mothers, plain language | Brad | ⚠ Not written |
| 6 | D-23 interim decision, so avatar exposure is known | Hector + Brad | ⚠ Brief written |
| 7 | Two cross-tenant exposures built and merged (owner-ruled, in Ready) | Hector | In flight |
| 8 | Pilot agreement with SCHHS, at list price, externally funded | Brad | ⚠ Not drafted |

**Items 1–5 are non-negotiable.** A pilot holding real maternal health conversation without
an ethics pathway, a known data path, a breach plan and a transparency statement is not a
pilot, it is an exposure.

## 7. What it produces

**For UCAC (16 Oct):** first real engagement numbers; a validated or corrected unit cost;
D-23 resolved on evidence; a named reference site with a signed agreement; the safety
architecture's first real-world performance data.

**For the raise:** the difference between "we believe mothers will engage" and "here is what
150 mothers did."

**For the product:** the modality answer, which sets the interface and the cost base.

**For the JV:** the first co-authored output with ACU — the academic value exchange the
early-adopter doctrine identifies as underused.

## 8. Timeline

| Week | Activity |
|---|---|
| −4 to −1 | Prerequisites 1–8. Ethics is the long pole — start it now |
| 1–2 | Enrolment. Measure conversion from the first offer |
| 3–8 | Running. Weekly measurement report, every week, no exceptions |
| 9 | Analysis, write-up, UCAC input |

**Starting the ethics pathway is this week's action.** Everything else can compress; that
cannot.
