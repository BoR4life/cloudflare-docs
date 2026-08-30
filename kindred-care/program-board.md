# Kindred Care — program board

**Readiness: TRL 3 / CRL 3 / IRL 3** · Last updated: 29 Aug 2026
**Cadence:** full review Monday, midweek check Thursday.

Baselined 29 Aug 2026 against the MVP Board snapshot of 28 Aug 2026 — see
`reviews/2026-08-29.md` for the gate review. Standing position: **the build is no
longer the constraint.** 97 of 148 MVP stories shipped and ~193 hours of loop time
remaining, against no named buyer, no written regulatory position, no HREC approval and
no verified entity. Six of the eight live blockers are Brad's, not Hector's.

Status vocabulary — use these and no others:
`NOT STARTED` · `IN PROGRESS` · `BLOCKED (on: …)` · `DONE (evidence: …)` · `SLIPPED (was DD MMM YYYY)` · `UNKNOWN (as at DD MMM YYYY)`

## Hard external dates
| Date | What | Consequence if missed |
|---|---|---|
| **31 Aug / 1 Sep 2026** | Brad ↔ Marie Gentile-Andrit one-to-one | Role clarity, prior-app IP and affiliation must be settled at or before this |
| **4 Sep 2026** | WS-PROP1 — Enterprise Proposal Draft-1 | Stage 1→2 bridge; all three input workshops unrun. Proceed compressed or re-baseline — do not let it pass silently |
| **11 Sep 2026, 10–11am** | SCHHS SPARK — Jake Penrose (CDO), Hayley Farry (ED Workforce) | **Different BoR product (occupational violence).** Executive door; do not turn it into a Kindred Care pitch |
| **16 Sep 2026, 3:00–3:45pm** | **ACU Enterprise (Clinic) Steering Committee** | Socialising and advice-seeking, not a funding gate. **No deck exists** |
| **16 Oct 2026** | UCAC assessment sitting | The gate. Pack assembly begins 2 Oct |
| **23 Oct / 30 Oct 2026** | VC endorsement / IC submission | Programme end-point |
| **Feb–Apr 2027** | Proposal window for interstate health-service funding in FY2027–28 | Secondary to the Victorian beachhead; relevant to SCHHS |
| May–Jun 2027 | End-of-FY underspend window — occasionally funds a small pilot quickly | Opportunistic only; not a plan |
| UNKNOWN | Grant rounds in play (TRGS, district innovation funds, CEQ, MRFF, Industry Growth Program) | — |
| UNKNOWN | ACU JV / reporting deadlines | — |
| Y2.5 of PhD | Paper 5 data window (Kindred Care transcripts) | Transcript collection must be consented and HREC-covered before this, not after |
| **Late Sep – Oct 2026 (est.)** | MVP build complete, from ~193h of loop time at 2 tracks | Product finished ~5 months before the next district funding window — that gap is where entity, HREC, regulatory position, assurance pack and beachhead must be closed |

## Product track (TRL)
**TRL 3, climbing** — corrected 29 Aug 2026 from the Business Plan's deliberate position. TRL 4 requires recall@5 ≥ 0.85 and safety-tag triggering ≥ 0.95 against a gold-standard evaluation set that does not yet exist (P4-04, P3-06, due 2 Oct). Shipped build volume is not the test, and claiming TRL 4 removes the R&D the POC exists to fund.

| Milestone | Owner | Due | Status | Evidence | As at |
|---|---|---|---|---|---|
| MVP build complete | Hector | UNKNOWN — ~193h loop time, ~2–2½ weeks of continuous sessions at 2 tracks | IN PROGRESS | 97/148 shipped; suites green 1354/578/668/267 | 28 Aug 2026 |
| Safety gate (TRL 5) | Hector | — | DONE (evidence: MVP Board — deterministic T1/T2/T3, T3 unsuppressible, no-LLM net proven with a poison model, non-degradable supervisor, 000 guard, staffed escalation queue, break-glass audit, non_diagnostic structurally mandatory) | MVP Board 28 Aug 2026 | 28 Aug 2026 |
| Safety gate residuals — live incident log and review process; escalation directory pointed at real services | Hector + Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Privacy gate (TRL 5) — architecture | Hector | — | DONE (evidence: transcripts-only CI-enforced no-recording gate, 41 fixture tests; retention on access_ends_at; tiered re-consent; k-floor; AU data residency Sydney/Melbourne) | MVP Board 28 Aug 2026 | 28 Aug 2026 |
| **Privacy gate (TRL 5) — legal sign-off on privacy notice and S11 ToS** | Brad | — | BLOCKED (on: lawyer not instructed) | — | 29 Aug 2026 |
| Close Q1 cross-tenant exposure — outreach gate identity-reveal across any institution | Hector | — | IN PROGRESS | Owner-ruled, sits in Ready | 28 Aug 2026 |
| Close Q2 cross-tenant exposure — all six roles can read mothers' free text | Hector | — | IN PROGRESS | Owner-ruled, sits in Ready | 28 Aug 2026 |
| FIX-DB-001 — identity-sequence defect, migration 0082, HIGH | Hector | — | IN PROGRESS | In loop, Track A round 1 | 28 Aug 2026 |
| **Warmth-trap measurement design (TRL 6 gate)** | Brad | — | NOT STARTED | Analytics & evals epic 0 of 12 | 29 Aug 2026 |
| **Analytics & evals epic — the evidence engine (Director, HREC and platform views)** | Hector | — | NOT STARTED | 0 of 12; downstream of FIX-DB-001 | 28 Aug 2026 |
| **Written TGA classification position — gates TRL 5 in this channel** | Brad, with advice | — | NOT STARTED | — | 29 Aug 2026 |
| Admin console deployed (shell merged, deploy story pending) | Hector | — | IN PROGRESS | Track B | 28 Aug 2026 |
| Knowledge / RAG epic closed | Hector | — | IN PROGRESS | 8 of 10; 038 opening, 039 next | 28 Aug 2026 |
| LiveAvatar vendor decision (D-23) | Brad | — | NOT STARTED | Named out-of-loop on the board | 28 Aug 2026 |
| STT/TTS vendor credentialing | Brad + Hector | — | NOT STARTED | Named out-of-loop on the board | 28 Aug 2026 |
| First consented real user — **do not cross before HREC coverage and consent wording are settled** | Brad | — | NOT STARTED | — | 29 Aug 2026 |

## Market track (CRL)
Lead motion: **Victorian public maternity services** (BVUIP is Victorian money), ACU midwifery network as channel, **SCHHS as Evaluation Partner / non-Victorian reference**. VIC = Trial Partners, QLD = Evaluation Partners. See `strategy/gtm-v3-2026-08-29.md`.

| Milestone | Owner | Due | Status | Evidence | As at |
|---|---|---|---|---|---|
| **Reply to Michelle Schmidt and book the SCHHS Maternity leadership session** | Brad | Mon 31 Aug 2026 | BLOCKED (on: Brad to send — draft ready in `drafts/2026-08-30-emails-to-send.md`) | — | 30 Aug 2026 |
| **Competitor analysis — standing ask from Russell, 26 Aug** | Brad | Tue 1 Sep 2026 | IN PROGRESS | Draft ready to circulate: GTM v3 §2 + research recon | 30 Aug 2026 |
| **16 Sept Steering Committee deck — Brad's sections** | Brad | 16 Sep 2026 | IN PROGRESS | Full slide-by-slide content drafted: `drafts/steering-committee-deck-16sep-outline.md`. Lock content 9 Sep; Elena clip 12 Sep; Russell sights 14 Sep | 30 Aug 2026 |
| Confirm whether the Elena persona can deliver the Steering Committee intro | Brad + Hector | 16 Sep 2026 | NOT STARTED | Russell asked 12 Aug | 29 Aug 2026 |
| Two named Victorian pilot sites (metro + regional) | Lois | — | NOT STARTED | Everything downstream assumes them | 29 Aug 2026 |
| **Safer Care Victoria — reconnect via Elisa McDonald** | Brad + Russell | This week | NOT STARTED | Raised 20 Aug, endorsed by Russell same day, not in any document | 29 Aug 2026 |
| Content Advisory Panel seated — Wallace, Simpson, Byatt + the Monash educator | Lois | 14 Aug 2026 | SLIPPED (was 14 Aug 2026) | Nominees supplied 12 Aug | 29 Aug 2026 |
| Decide Eve: compete / partner / acquire — test the Cabrini relationship via ACU's Catholic-sector network | Brad + Russell | Before 16 Oct 2026 | NOT STARTED | — | 29 Aug 2026 |
| Mother survey closes (100 responses) + analysis | Brad | 4 Sep 2026 | NOT STARTED | Van Westendorp — B2C only, not B2B | 29 Aug 2026 |
| Pricing shape — birth-volume bands, external anchor (£55k NHS G-Cloud comparator) | Brad + Hector | 11 Sep 2026 | NOT STARTED | — | 29 Aug 2026 |
| Pilot protocol — pre-declared criteria, service enrolment, enrolment artefact, stratification | Brad + Lois | Before any site approach | NOT STARTED | Evidence base in `research/` | 29 Aug 2026 |
| Comrade NDAs executed (early adopters) | Brad | 28 Aug 2026 | SLIPPED (was 28 Aug 2026) | — | 29 Aug 2026 |
| B2C gate — **moved to FY29**, resourced separately | Brad | FY29 | NOT STARTED | Self-enrolment median retention 0 days | 29 Aug 2026 |
