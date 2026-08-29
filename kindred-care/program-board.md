# Kindred Care — program board

**Readiness: TRL 4 / CRL 2 / IRL 1** · Last updated: 29 Aug 2026
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
| **Feb–Apr 2027** | Proposal window for LHD/HHS funding in FY2027–28 (Australian FY starts 1 Jul) | A proposal not drafted by Jan 2027 misses a full year of district budget |
| May–Jun 2027 | End-of-FY underspend window — occasionally funds a small pilot quickly | Opportunistic only; not a plan |
| UNKNOWN | Grant rounds in play (TRGS, district innovation funds, CEQ, MRFF, Industry Growth Program) | — |
| UNKNOWN | ACU JV / reporting deadlines | — |
| Y2.5 of PhD | Paper 5 data window (Kindred Care transcripts) | Transcript collection must be consented and HREC-covered before this, not after |
| **Late Sep – Oct 2026 (est.)** | MVP build complete, from ~193h of loop time at 2 tracks | Product finished ~5 months before the next district funding window — that gap is where entity, HREC, regulatory position, assurance pack and beachhead must be closed |

## Product track (TRL)
**TRL 4.** Build is ahead of both other tracks. TRL 5 fails on four gates, three of which are not build work.

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
Lead motion: **B2B into NSW Local Health Districts and QLD Hospital and Health Services** (working direction, 29 Aug 2026). B2C is a month-12 option conditional on dedicated resourcing.

| Milestone | Owner | Due | Status | Evidence | As at |
|---|---|---|---|---|---|
| One-sentence product statement | Brad | — | UNKNOWN | — | 29 Aug 2026 |
| Get the ACU clinical placement partnership map — districts, services, named academic per relationship | Brad + ACU | — | NOT STARTED | — | 29 Aug 2026 |
| Pick the beachhead: one district, one service line, one measurable problem | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Name the executive sponsor role and the budget line at the beachhead | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Build the assurance pack (privacy, security, AI assurance, clinical, regulatory, insurance) — gate between CRL 3 and 4 | Brad + Hector | — | NOT STARTED | — | 29 Aug 2026 |
| Confirm the district's direct-engagement procurement threshold and size pilot one beneath it | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Assess co-applying with a district for external pilot funding (TRGS / district innovation fund / CEQ) | Brad + ACU | — | NOT STARTED | — | 29 Aug 2026 |
| Pilot protocol template with pre-declared success criteria and a named data collector | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Pricing shape decided, anchored to district economics (before any number) | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Competitor list | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Named pipeline of three or more districts (concentration-risk answer) | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Prequalification assessment — NSW ICT purchasing arrangements, QLD QITC | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| B2C gate: dated decision point ~month 12, with the resourcing precondition written into it | Brad | — | NOT STARTED | — | 29 Aug 2026 |

## Investment track (IRL)
| Milestone | Owner | Due | Status | Evidence | As at |
|---|---|---|---|---|---|
| **Resolve entity question — incorporated Pty Ltd with 70/30 on a cap table, or contractual JV?** | Brad + ACU + lawyer | — | NOT STARTED | — | 29 Aug 2026 |
| IP ownership schedule — code, prompts, brand, transcripts | Brad + lawyer | — | NOT STARTED | — | 29 Aug 2026 |
| Confirm what ACU is contributing, in writing (cash / in-kind / staff / introductions) | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Hector's agreement — role, IP assignment, equity or compensation | Brad | — | UNKNOWN | — | 29 Aug 2026 |
| R&D Tax Incentive position and contemporaneous record-keeping started | Brad + accountant | — | NOT STARTED | — | 29 Aug 2026 |
| Grant shortlist — applied / in progress / explicitly ruled out | Brad + ACU | — | NOT STARTED | — | 29 Aug 2026 |
| Financial model, burn, runway on the Kindred Care line | Brad | — | UNKNOWN | — | 29 Aug 2026 |
| Milestone-to-raise map and use of funds | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| Data room index with gaps visible | Brad | — | NOT STARTED | — | 29 Aug 2026 |
| First monthly investor update written (no investors required) | Brad | — | NOT STARTED | — | 29 Aug 2026 |

## Governance / firewall
| Milestone | Owner | Due | Status | Evidence | As at |
|---|---|---|---|---|---|
| **Confirm consent wording at point of collection covers Paper 5 research use — before the first consented user, not before the first pilot** | Brad + CI | — | BLOCKED (on: HREC approval, listed out-of-loop) | — | 29 Aug 2026 |
| Resolve ACU / HREC approvals — ADR-008 k-values, S9e copy. Establish who is waiting on whom | Brad + ACU | — | BLOCKED (on: unclear ownership) | — | 29 Aug 2026 |
| Name who staffs the ACU approval seat (content_sme_acu) in production, and the turnaround | Brad + ACU | — | NOT STARTED | ACU approval inbox VS-090 shipped; seat unstaffed as far as evidenced | 29 Aug 2026 |
| Named ACU counterpart for commercial matters, distinct from supervisory panel | Brad | — | UNKNOWN | — | 29 Aug 2026 |
| Agree publication rule — negative findings are never withheld | Brad + ACU | — | NOT STARTED | — | 29 Aug 2026 |
| JV steering group / decision rights when Brad and ACU disagree | Brad + ACU | — | UNKNOWN | — | 29 Aug 2026 |

## Milestone-to-raise map
Raising to: **UNKNOWN** — cannot be built until the entity question is answered and the beachhead is picked.

**Standing constraint from the B2B choice:** an LHD/HHS sales cycle runs 9–18 months
plus security and privacy review, so the round must fund roughly **24 months, not 12**.
Revenue arrives after the raise, not during it. State this in the raise narrative
rather than letting an investor discover it.

| Milestone | Cost (AUD) | Date |
|---|---|---|
| — | — | — |

## Gate review history
| Date | Level claimed | Result | Missing evidence |
|---|---|---|---|
| 29 Aug 2026 | TRL 5 | **FAIL** — assessed TRL 4 | Legal sign-off; warmth-trap measurement; written TGA position; two unfixed cross-tenant exposures; no consented users |
| 29 Aug 2026 | CRL 3 | **FAIL** — assessed CRL 2 | No named district, sponsor, budget line, pricing hypothesis, competitor list or assurance pack |
| 29 Aug 2026 | IRL 2 | **FAIL** — assessed IRL 1 | Entity status unresolved; IP ownership unverified |
