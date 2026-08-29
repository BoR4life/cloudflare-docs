# Kindred Care — canonical facts and UNKNOWN register

**As at 29 Aug 2026. Read this before answering anything factual about Kindred Care.**

**Section A** is verified — every line carries a source. **Section B** is the UNKNOWN
register — the things this agent must not guess. If a live document contradicts
Section A, flag the conflict to Brad rather than silently picking one.

When Brad confirms an UNKNOWN, move the line from B to A **with its source and the
date he confirmed it**, and remove it from `kindred-care/open-questions.md`.

Principal source for the product facts below: the **Kindred MVP Board**, snapshot
28 Aug 2026 (evening), supplied by Brad 29 Aug 2026. Cited as *MVP Board 28 Aug 2026*.

---

## Section A — verified

### The venture

| Fact | Detail | Source |
|---|---|---|
| Venture structure | Kindred Care is a **70/30 joint venture, Bundle of Rays / ACU** | `phd-define-writing` canonical facts, Jul 2026 |
| Brad's role | CEO, Bundle of Rays Academy; carries the Kindred Care venture | same |
| ACU | Australian Catholic University — 30% JV partner, partner on the raise and go-to-market, **and an approval role inside the product itself** (see below) | same + Brad, 29 Aug 2026 + MVP Board |
| Hector | Leads product/technology build | Brad, 29 Aug 2026 |
| PhD interface | Kindred Care **transcripts** are the data source for PhD Paper 5 (pedagogical discourse analysis, "warmth trap" markers), timed Y2.5 | `phd-define-writing` canonical facts |
| Declared COI | Brad's Kindred Care commercial relationship is a declared conflict on the ACU HREC application | same |
| Lead go-to-market motion | **Working direction, not locked:** B2B contracts into NSW Local Health Districts and QLD Hospital and Health Services. Multi-year public health contracts judged better collateral for a raise than early consumer revenue | Brad, 29 Aug 2026 |
| B2C | A real option from roughly **month 12**, conditional on **dedicated resourcing** | Brad, 29 Aug 2026 |
| Review cadence | Twice weekly — full review Monday, midweek check Thursday | Brad, 29 Aug 2026 |

### The product

| Fact | Detail | Source |
|---|---|---|
| What it is | A supervised conversational AI agent named **Elena**. User journey: sign in → consent → enrol with a code → **Call or Chat** with Elena. Modalities: avatar / audio / text | MVP Board 28 Aug 2026 |
| Domain | **Maternal / perinatal.** Evidenced by the Top-Ten ontology of "ten maternal-issue codes" (VS-032), EDD/DOB capture with life stage derived on read (VS-026), and support tickets containing "free text mothers wrote about themselves" | MVP Board 28 Aug 2026 |
| Commercial model | **B2B2C, already built in** — multi-tenant by institution, with plans, sponsorships, seat caps, enrolment codes, usage ledger and entitlement. The institution enrols; the mother uses it | MVP Board 28 Aug 2026 |
| Second persona | A non-clinical **Support Assistant** (VS-024) on the shared agent image — own config, corpus and eval suite, no avatar, text chat, health-topic router | MVP Board 28 Aug 2026 |
| Codename | Platform/repo codename is **Iridia** (`bor-iridia`, `iridia-dev`). Relationship between the Iridia codename and the Kindred Care brand is not stated on the board | MVP Board 28 Aug 2026 |
| Surface | Flutter web app at `iridia-dev.bundleofrays.app` (dev) | MVP Board 28 Aug 2026 |

### Architecture and stack

| Fact | Detail | Source |
|---|---|---|
| Services | **Four platform services** — app (Flutter), api (Nest.js), agent (Python/ADK), upload-gate. First three live in dev at `*.bundleofrays.app` | MVP Board 28 Aug 2026 |
| Admin console | Next.js — Workbench, deploy gate, templates/clone/export, alerts inbox, tenant management all merged (VS-067→097). **Shell merged, not yet deployed**; deploy story pending on Track B | MVP Board 28 Aug 2026 |
| Repository | `github.com/BundleOfRays/bor-iridia`, branch `develop`. CI: Cloud Build → Cloud Run on every push | MVP Board 28 Aug 2026 |
| Model | **Gemini via Vertex AI** (`LLM_PROVIDER=vertex` in dev). Multi-vendor roster and vendor seams exist | MVP Board 28 Aug 2026 |
| Data residency | **Inference in Sydney (AU), data in Melbourne (AU)** | MVP Board 28 Aug 2026 |
| Identity | Google sign-in via GCIP; token planes; MFA on the console | MVP Board 28 Aug 2026 |
| Data layer | Postgres with RLS tenant isolation; migrations at least through 0082 | MVP Board 28 Aug 2026 |
| RAG | Chunk → safety-tag → embed → index. Local deterministic embedder + Postgres index in dev, Vertex slots for later | MVP Board 28 Aug 2026 |

### Build state as at 28 Aug 2026

| Fact | Detail | Source |
|---|---|---|
| MVP progress | **97 of 148 MVP stories shipped.** Board columns: Done 97, In build 1, Ready 37 (column header shows 39), Staged 58 | MVP Board 28 Aug 2026 |
| Test suites | All green on `develop`: Backend 1354/1354 · Console 578 · Flutter 668 · Agent 267 | MVP Board 28 Aug 2026 |
| Remaining effort | **≈193 hours** of orchestrated loop time for "the 94 remaining stories (±30%)"; roughly **2–2½ working weeks** of continuous sessions at two parallel tracks, throttled by Brad's verify-gate turnaround | MVP Board 28 Aug 2026 |
| Parallel tracks | Track A customer app · Track B admin console (opened 26 Aug) · Track C subscription manager (worktree open, BE-111 queued, session not yet opened) | MVP Board 28 Aug 2026 |
| Epic at zero | **Analytics & evals: 0 of 12 shipped** — Director, HREC and platform views, k-anonymity, A/B evals. Untouched | MVP Board 28 Aug 2026 |
| Knowledge / RAG | 8 of 10 shipped; 038 opening, 039 next, then the epic closes | MVP Board 28 Aug 2026 |

### Safety design — substantially built and evidenced

| Control | Detail | Source |
|---|---|---|
| Deterministic triggers | T1/T2/T3 safety triggers; **T3 unsuppressible**, proven from both directions and across all three layers | MVP Board 28 Aug 2026 |
| No-LLM safety net | The deterministic safety net "works with no LLM at all — proven with a poison model that fails the test suite if it is ever invoked" | MVP Board 28 Aug 2026 |
| Dual-agent supervisor | Agent B vets every turn, **non-degradable**; echo-attack-proof parser; 49 Unicode homoglyph probes, zero bypasses; 35 QA parser attacks all fail closed | MVP Board 28 Aug 2026 |
| Escalation | BoR-staffed clinical worklist with atomic leases, 3-factor PII gate, break-glass audit; per-institution escalation directory with tiers and a **000 reserved-number guard** (0/31 adversarial escapes) | MVP Board 28 Aug 2026 |
| Help sheet | S9e safety help sheet auto-opens | MVP Board 28 Aug 2026 |
| Scope limits | `non_diagnostic` structurally mandatory — "no third outcome exists (unwritable or refuses boot)"; clinical-content guard at TS/Python parity; Support Assistant non-clinical by construction | MVP Board 28 Aug 2026 |
| Not balance-gated | Safety proven never gated on account balance | MVP Board 28 Aug 2026 |
| Safety gate | Board states **"Safety gate: SATISFIED"** — strict-shape parsing and per-turn nonce landed before Vertex was enabled | MVP Board 28 Aug 2026 |

### Privacy and data handling

| Control | Detail | Source |
|---|---|---|
| No recording | **Transcripts only** — the no-recording commitment is CI-enforced against the whole artifact class (41 fixture tests, 3 QA rounds of adversarial plants) | MVP Board 28 Aug 2026 |
| Retention | Retention on `access_ends_at`; stamped retention sweep; offline cache account-scoped with purge on owner change | MVP Board 28 Aug 2026 |
| Consent | Global consent gate; tiered re-consent enforcement on every real client path; `withdrawConsent` exists; Privacy Notice and ToS versioned with publication requiring a full materiality affirmation | MVP Board 28 Aug 2026 |
| Analytics privacy | ADR-008 §5 forbids free text in the analytics store; k-anonymity floor on every export | MVP Board 28 Aug 2026 |
| Australian Privacy Principles | Tracked explicitly — an open item names "stateless-DSAR vs APP 11.2/12 obligations" | MVP Board 28 Aug 2026 |

### ACU's role inside the product

ACU is not only the 30% owner, the ethics approver and a potential channel. It is also
a **governance role inside the running system**: there is a `content_sme_acu` console
role, an **ACU approval inbox** (VS-090) with a reviewer worklist, diff and eval
scorecard, and the Knowledge/RAG epic includes "ACU approval" as a stage. Corpus
documents cannot reach the live index without approval.

This is a **fifth hat** on top of the four in `acu-jv-and-phd-firewall.md`, and it is
the one with an operational dependency: if the ACU approval seat is unstaffed or slow,
the knowledge pipeline stalls in production, not just in governance.

### Known blockers sitting outside the build loop

Named on the board as "not counted: out-of-loop items":

1. **Legal sign-off** — privacy notice, S11 ToS
2. **ACU / HREC approvals** — ADR-008 k-values, S9e copy
3. Manual Stitch cleanup
4. **LiveAvatar vendor decision (D-23)**
5. **Real STT/TTS vendor credentialing**

### Open security findings, ruled but not yet fixed

Both found by QA reading code; the board states neither is a known incident. Both sat
in **Ready**, not Done, as at 28 Aug 2026:

- **Q1 — outreach gate.** Any console user, including the research-only account, could
  switch on identity-reveal for **any** institution.
- **Q2 — ticket reads.** All six console roles could read the free text mothers wrote
  about themselves. Now to be gated to the three escalation roles.

Also in flight: **FIX-DB-001**, an identity-sequence defect in shipped migration 0082
(`governance.eval_suite.id`) rated HIGH, in the build loop on Track A. Every one of the
twelve unstarted analytics/evals stories is downstream of that table.

---

## Section B — UNKNOWN register

Do not fill any of these from inference. Ask Brad, or leave it UNKNOWN in the output.

### Entity, legal and IP — unchanged and still the binding constraint
- [ ] **Is Kindred Care an incorporated entity (Pty Ltd), or a contractual JV inside Bundle of Rays?** Highest-leverage open question for the raise
- [ ] Where the 70/30 is documented, and whether it is equity, revenue share, or an MOU
- [ ] Who owns the IP — code, prompts, brand, transcript data. The `bor-iridia` repo sits under the BundleOfRays org, which is evidence of custody, not of ownership
- [ ] Whether ACU staff or student contributions create an ACU IP claim — sharpened by ACU holding an approval role inside the product
- [ ] Does ACU's 30% dilute on an external round
- [ ] Hector's formal role, agreement, IP assignment and equity or compensation
- [ ] Relationship between the Iridia codename and the Kindred Care brand — one product or two

### Market
- [ ] Which LHD / HHS is the beachhead, and who is the executive sponsor and budget owner
- [ ] The ACU clinical placement partnership map — districts, services, named academic per relationship
- [ ] Which maternity or child-and-family service line the beachhead pilot addresses
- [ ] Any named prospect, LOI, paid pilot or revenue to date
- [ ] Pricing hypothesis — nothing on the board states one, though plans, seat caps and metering are built
- [ ] **Regulatory classification: is Elena a TGA-regulated medical device?** No written position exists on the board
- [ ] Whether the National Safety and Quality Digital Mental Health Standards apply, and whether accreditation is being pursued

### Users and evidence
- [ ] Are there any consented real users yet, or is everything still dev-only
- [ ] Do transcripts exist from real users, and under what consent
- [ ] **Does the consent given at point of collection cover PhD Paper 5 research use** — HREC approval is listed as an out-of-loop blocker, so this is live
- [ ] What "ACU/HREC approvals (ADR-008 k-values, S9e copy)" specifically requires and who is waiting on whom

### Money and timeline
- [ ] Raise target, instrument, and use of funds
- [ ] Kindred Care's own burn and runway, separate from Bundle of Rays
- [ ] What ACU has actually committed — cash, in-kind, staff time, introductions
- [ ] Grants applied for, in progress, or ruled out
- [ ] Hard external dates — grant rounds, ACU deadlines, pilot windows
- [ ] Target date for MVP complete, and what "MVP complete" is being held to mean commercially
- [ ] Where the entity is based, for state grant eligibility

### Governance
- [ ] Does the JV have a steering group, and who decides when Brad and ACU disagree
- [ ] Who staffs the ACU approval seat in production, and against what turnaround

### Board arithmetic to reconcile — do not silently pick a number
The MVP Board carries three counts that do not reconcile, and the agent must quote them
as they are until Brad resolves them:
- "97 of 148 shipped" against a runway line costing "the 94 remaining stories" — 97 + 94 = 191, not 148
- Done 97 + Building 1 + Ready 37 + Staged 58 = 193
- The Ready chip says 37; the Ready column header says 39

The likely explanation is that 148 counts MVP-scoped stories while 191–193 includes FIX
and debt items, but that is a guess and is recorded here as one.
