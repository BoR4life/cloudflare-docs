# Readiness ladders — TRL / CRL / IRL

Three ladders, one board. The headline of every report is `TRL n / CRL n / IRL n`.

**The rule that makes these worth having: a level is evidenced, not claimed.** Each
level below lists the artefact that proves it. No artefact, no advance. Levels can
also go *down* — if the evidence for a claimed level turns out not to exist, drop it
and say so. TRL is the language grant assessors, ACU commercialisation, and
government programs speak in; inflating it in an application is a much larger
problem than a slipped date.

A venture is only as strong as its **lowest** ladder. TRL 7 with CRL 2 is a science
project. CRL 6 with TRL 3 is a promise you cannot keep.

---

## Technology Readiness Level (TRL)

Standard 1–9 scale, with Kindred Care's exit evidence. "Relevant environment" means
a supervised care setting with proxy or consented pilot users. "Operational
environment" means a real care service delivering to real clients at real volume.

| TRL | Standard meaning | Exit evidence for Kindred Care |
|---|---|---|
| 1 | Basic principles observed | Written problem statement; the andragogical/care literature it rests on |
| 2 | Technology concept formulated | Concept note: who it speaks to, what it does, why conversational AI is the right form |
| 3 | Experimental proof of concept | A working conversation with a real transcript, reviewed by a domain expert |
| 4 | Validated in lab | Scripted scenario suite passing; failure modes catalogued; a transcript corpus you can point at |
| 5 | Validated in relevant environment | **Gated — see below.** Consented users in a supervised setting; safety and escalation live; data handling signed off |
| 6 | Demonstrated in relevant environment | A cohort over a defined period with pre-declared success measures and results, good or bad |
| 7 | Prototype in operational environment | A district service running it with their own patients or clients; health service staff, not the build team, in the loop |
| 8 | System complete and qualified | Security review passed; uptime, support and incident process defined; regulatory position formally settled |
| 9 | Proven in operational environment | Running in service beyond the pilot, with outcome data over time |

### Hard gates — these block TRL advance regardless of build progress

**Safety gate (blocks TRL 5).** Kindred Care speaks to people who may be isolated,
unwell, cognitively impaired, or in crisis. Before *any* non-team user, all four must
exist and be documented: (a) crisis and risk detection, with the specific triggers
written down; (b) an escalation path to a named human, tested end to end; (c) explicit
scope limits — what the agent will not discuss or advise on; (d) an incident log and
who reviews it. A demo is not a defence.

**Privacy and data gate (blocks TRL 5).** Lawful basis for collection, consent
wording, where transcripts are stored and under whose control, retention and deletion,
sub-processors (including model providers), and whether any of it is health
information under the Privacy Act. If transcripts feed PhD Paper 5, the consent must
cover research use *at the point of collection* — retrofitted consent is a finding.

**Warmth-trap gate (blocks TRL 6).** The dependence risk Brad's own research names.
Before a cohort study: what is measured to detect it, what threshold triggers a design
change, and what the product does to interrupt it. Kindred Care cannot ship the exact
failure mode its founder publishes on.

**Regulatory classification gate (blocks TRL 5 in the LHD/HHS channel).** Get a written position on whether
Kindred Care is a TGA-regulated medical device. It turns on *claims and intended
purpose*, not on technology. Wellbeing, companionship, and education framings are
generally outside; anything that diagnoses, monitors a condition, triages, or informs
clinical decisions is generally inside, and Software as a Medical Device brings
conformity assessment, a quality system, and a very different timeline and cost. Settle
this **before the first LHD/HHS conversation** — not before the pilot, because what is
said in the first meeting becomes the intended purpose — and before any deck claims a
clinical outcome. Deploying inside a health service raises this risk materially compared
with a consumer product. Take advice; do not settle it from this file.

---

## Commercial Readiness Level (CRL)

| CRL | Meaning | Exit evidence |
|---|---|---|
| 1 | Market hypothesis | Written statement of who pays and why |
| 2 | Problem validated | Interviews with people in the buying role, not just end users; notes exist |
| 3 | ICP defined and reachable | Named segment, named organisations, a route to reach them |
| 4 | Value proposition tested | Buyers can restate the value unprompted; a pricing hypothesis with a signal behind it |
| 5 | Pilot agreement | A signed pilot agreement with a real organisation, with success criteria in it |
| 6 | Paid pilot delivered | Money changed hands; results measured against the criteria that were set beforehand |
| 7 | First standard-terms customer | A contract that is not a favour, on terms you would offer the next buyer |
| 8 | Repeatable | Three or more customers through the same motion; CAC, cycle length and unit economics known |
| 9 | Scaling | Predictable pipeline; channel producing without founder involvement |

**Careful with pilots.** Unpaid pilots are easy to get in Australian health and prove
almost nothing — a free pilot tests curiosity, not budget. CRL 5 requires a signed
agreement with success criteria; CRL 6 requires money. See `gtm-playbook.md`.

### What each CRL means in the LHD/HHS channel

The lead motion is B2B into NSW Local Health Districts and Queensland Hospital and
Health Services. Read the rungs this way:

| CRL | In this channel |
|---|---|
| 3 | A named district, a named service line, a named executive sponsor role, and the relationship source (usually an ACU placement partnership) |
| 4 | The **assurance pack** exists — privacy, security, AI assurance, clinical, regulatory position. Without it, nothing advances past a first meeting |
| 5 | A pilot agreement executed under the district's own procurement instrument, with success criteria in the document — ideally sized under the direct-engagement threshold |
| 6 | Money moved, or an external funding body funded the pilot with the district as co-applicant, and the pre-declared criteria were measured |
| 7 | A contract on standard terms, with the termination-for-convenience clause read and the IP position settled |
| 8 | Three or more districts through the same motion — this is what earns a statewide pathway, which is never sold cold |

An executive sponsor with a budget line is the gate between CRL 3 and 4. A delighted
clinical champion with neither is still CRL 3, however good the meeting felt.

---

## Investment Readiness Level (IRL)

| IRL | Meaning | Exit evidence |
|---|---|---|
| 1 | Intent to raise | Nothing but a plan |
| 2 | **Investable entity exists** | Incorporated company, clean cap table, IP assigned in, founders/JV terms documented |
| 3 | Numbers exist | Financial model, burn, runway, use of funds tied to milestones |
| 4 | Non-dilutive path worked | R&D Tax Incentive position, grants applied for or explicitly ruled out, ACU contribution documented |
| 5 | Data room assembled | Index complete, gaps listed rather than hidden |
| 6 | Narrative validated | Deck tested on people who will not invest, and rebuilt on what they said |
| 7 | Live conversations | Named investors in process; diligence questions arriving |
| 8 | Term sheet | Signed term sheet |
| 9 | Closed | Funds received and deployed against the stated milestones |

**IRL 2 is the one that traps joint ventures.** A JV documented as an agreement
rather than as shares in a company is not something external capital can enter. If
Kindred Care is not incorporated with the JV reflected on a cap table and IP assigned
in, IRL is capped at 1 no matter how good the deck is. This currently sits in the
UNKNOWN register — resolving it is the highest-leverage item on the investment track.

---

## How to run a gate review

Triggered whenever a level is claimed, and at every quarterly reset.

1. State the level being claimed and read its exit-evidence row aloud in the output.
2. For each item, name the artefact and where it lives. Not "we've done that" — a link.
3. Check the hard gates that sit at or below that level. Any gate unmet fails the review.
4. **Pass or fail. There is no partial.** A fail is normal and useful; it names exactly
   what is missing.
5. Write the result into `kindred-care/program-board.md` with the date, and log any
   resulting decision to `kindred-care/decisions.md`.
6. If the review moves a level *down*, say so plainly in the next weekly review and
   list every external document that now states the old level — deck, grant
   application, website, ACU reporting.
