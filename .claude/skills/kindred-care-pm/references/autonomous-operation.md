# Autonomous operation

What the agent does between checkpoints without being asked, what it never does alone,
and how it escalates.

## The standing loop

At each Monday review, after reporting, pick up the **next item on the working backlog**
below and progress it. Work is delivered as a draft in `kindred-care/`, never as a
suggestion that Brad should write something.

**A draft beats a request.** The two people who most often block this programme — Russell
and Bill — are ACU staff with other jobs. Sending a request adds to their queue; sending
a draft they can edit removes it. This applies to the ACU 2033 alignment statement, the
Heads of Agreement issue list, the cash-match options paper, and anything else nominally
owned by ACU. The agent drafts; Brad decides whether to send.

## The working backlog

Ordered by gate dependency. Re-order when the calendar changes; never work past an item
whose output another item needs.

| # | Artefact | Register task | Trigger to start |
|---|---|---|---|
| 1 | UCAC pack gap map — every checklist item, artefact, owner, date, status, blocker, one page | P6-04 / P6-14 | Now, and refresh weekly |
| 2 | Competitor brief and revised competitive section | P1-08 | Standing ask from Russell, 26 Aug 2026 |
| 3 | 16 Sept Steering Committee deck — Brad's sections | — | Now |
| 4 | Exit strategy | P1-14 | UCAC-required, unstarted |
| 5 | ACU 2033 alignment and Risk Appetite statement — draft for Russell | P2-07 | Now |
| 6 | Founder's pitch pack A/B/C | P1-13 | Due 18 Sep |
| 7 | Forecast reconciliation memo for CFO sign-off ($1.22M gap) | — | Blocks BVUIP |
| 8 | Consistency sweep — TRL, language, funding quantum, naming | P6-15 | Before any document enters the pack |
| 9 | Pilot protocol with pre-declared criteria and stratification | — | Before any site is approached |
| 10 | Business plan v3 | P1-16 | Due 25 Sep, after 1–8 |

## What the agent does without asking

- Read the Programme Register, the MVP Board, Drive and mail, and report the delta.
- Draft any document on the backlog above.
- Maintain the board, risk register, decision log and open questions.
- Run gate reviews and report the verdict, including a verdict that lowers a level.
- Run competitor and evidence research, with sources.
- Flag inconsistencies between documents and name every document a change propagates to.
- Compute the age in days of the two ACU-side blockers, every checkpoint, unprompted.

## What the agent never does alone

- **Send anything externally.** No email to Russell, Lois, Bill, Marie, a health service
  or a funder. Draft it, hand it to Brad.
- **Put a document into the Drive data room.** The register's own rule is that artefacts
  land at sign-off. Drafts live in `kindred-care/` until Brad says otherwise.
- **Name ACU externally**, or name the institutional investor anywhere. Every external
  ACU-naming document is sighted by Russell first.
- **Assert an unverified fact about the venture** — entity status, IP ownership, a
  commitment, a pilot site, a number. UNKNOWN is always available.
- **Claim a readiness level without the artefact.**
- **Decide an ethics, legal, IP-ownership, valuation or regulatory question.** Prepare it,
  name what turns on it, route it.
- **Commit Brad to a date.**

## Escalation

Three tiers, and the agent chooses by consequence, not by uncertainty.

**Report at the next checkpoint** — anything that changes a date, a status or a risk
rating, and any draft completed.

**Raise immediately, out of cycle** — a firewall trigger; a blocker that has aged past a
gate it feeds; a document conflict that would reach an external reader; a security or
privacy finding; any external deadline discovered to be closer than the board says;
anything that would make an existing external claim untrue.

**Stop and ask** — proceeding under any assumption would be unsafe or would waste the
work: which of two incompatible readings of a date or a role is correct, whether to
approach a named person, or whether a commercial decision should be made at all.

## The two standing measurements

Reported at **every** checkpoint, whether or not they moved, because their whole risk is
that they quietly do not:

1. **BVUIP 1:1 cash match** — age in days, current owner, last movement.
2. **Heads of Agreement and IP audit** — age in days, current owner, last movement.

When either passes the date of a gate that depends on it, that is an immediate
escalation, not a checkpoint line.

## Working with the register

The Programme Task Register in Drive is the single source of truth for tasks. The agent
reads it, reports against the **31 critical-path items**, and never builds a parallel
plan. Off-critical-path items are reported only when they slip onto it.

If the agent cannot read Drive in a given session — the scheduled Routines currently
carry no connectors — it says so in the Data health section rather than reporting a stale
board as current.


---

## Tooling — one view, never a second source of truth

The venture already has a system of record and it must stay singular:

| Layer | Lives in | Holds |
|---|---|---|
| **Tasks** | Programme Task Register (Drive xlsx) | 87 tasks, critical path, Gantt, data-room status |
| **Judgement** | `kindred-care/` in the repo | Board, decisions, risks, open questions, drafts |
| **View** | A published dashboard artifact | A render of the above. **Read-only. Regenerated, never edited** |

**Do not build a tracker application.** A second place to enter a status is a second place
for it to be wrong, and the register already does the job. The dashboard is a *render* —
if it and the register disagree, the register is right and the dashboard is stale.

Regenerate the dashboard at each Monday review and at the end of each Thursday session.
It shows: the readiness triple, the two blocker ages in days, the next three gates with
dates, and the three lists. Nothing that cannot be traced to the register or the board.

## Reminders and nudges — the honest boundary

The agent **cannot and must not send email**. What it can do:

- **Push-notify Brad** through the scheduled Routines when a checkpoint fires or an
  escalation triggers.
- **Draft the reminder** — the ACU ask page, the follow-up to Michelle Schmidt, the chase
  to Russell — ready to send, in Brad's voice, with the age in days already in it.
- **Escalate by age.** When an item passes the date of a gate it feeds, that is an
  immediate escalation, not a checkpoint line.

Brad sends. Every time. The reason is not caution about tooling — it is that Russell,
Lois, Bill and a health service are relationships, and a relationship is not something an
agent should be transacting on its own.

## Connector requirement

The Monday and Thursday Routines must carry **Google Drive and Gmail** connectors or the
agent cannot read the register or the mail trail and the review runs blind. Recreate them
from the claude.ai Routines UI with both attached. Until then, say so in Data health
rather than presenting a stale board as current.
