# Kindred Care — program manager

This directory is the **live state** of the Kindred Care venture. The agent that reads
and maintains it is the skill at `.claude/skills/kindred-care-pm/`.

## What it does

Runs **twice weekly** — a full review on Monday, a short midweek check on Thursday —
and holds one board across three tracks that would otherwise drift apart:

- **Product (TRL 1–9)** — Hector's build, and whether each readiness claim is evidenced
- **Market (CRL 1–9)** — who signs, out of which budget, for how much
- **Investment (IRL 1–9)** — entity, IP, non-dilutive funding, data room, the raise

Lead motion is **B2B into NSW Local Health Districts and QLD Hospital and Health
Services**, with B2C as a resourced option from around month 12.

Every report leads with the triple — `TRL n / CRL n / IRL n` — and a level only moves
on evidence you can point at. It also runs a **firewall check** on any commercial
decision that touches research data, participants, publication, or ACU, because Brad is
simultaneously the venture's CEO and a Student Investigator on the ACU HREC application
that governs Paper 5.

## Files

| File | What it is |
|---|---|
| `program-board.md` | The board. Readiness triple, milestones, owners, dates, status, evidence |
| `open-questions.md` | Everything UNKNOWN, ordered by what it unblocks. Work this list first |
| `risks.md` | Risk register |
| `decisions.md` | Append-only decision log |
| `reviews/` | Saved weekly reviews, `YYYY-MM-DD.md` |

## Using it

Say any of these in a session where the skill is available:

- *"Kindred Care weekly review"* — the Monday ritual: what moved, what's blocked, the
  three tracks, timeline risk, one decision
- *"Midweek check"* — the Thursday short form: did Monday's decision move, what's still blocked
- *"Gate review: are we at TRL 5?"* — evidence audit against the ladder, pass or fail
- *"Draft the monthly investor update"*
- *"We're thinking about a pilot with X"* — runs the firewall check and the pilot rules
- *"Update the board: Hector shipped the escalation path on 3 Sep"*

Anything Kindred Care-shaped should pull the skill in on its own.

## Installing the skill elsewhere

It currently lives at `.claude/skills/kindred-care-pm/`, so it loads automatically in
Claude Code sessions on this repo. To use it everywhere:

- **Claude Code, all projects** — copy the folder to `~/.claude/skills/kindred-care-pm/`
- **Claude apps and web** — zip the `kindred-care-pm` folder and upload it in Settings →
  Capabilities → Skills. It will then sync to every surface, alongside
  `phd-define-writing` and `financial-checkpoint`

If you install it in the apps, keep this state directory somewhere the agent can reach
in whichever workspace you run the reviews from — the skill is portable, the state is not.

## Ground rule

The skill never invents a Kindred Care fact. Anything not confirmed sits in
`open-questions.md` and prints as UNKNOWN in reports, with staleness on the face of the
report rather than buried. Confirmed facts move into
`.claude/skills/kindred-care-pm/references/canonical-facts.md` with their source and date.

## Scheduled reviews

Two Routines fire fresh sessions in this environment, push-notify Brad, and commit
their output back to this branch:

| Routine | Fires | ID |
|---|---|---|
| Kindred Care — Monday full review | Mondays 08:05 (cron `5 22 * * 0` UTC) | `trig_018F7yLw4xUFcS9MiTuCehMK` |
| Kindred Care — Thursday midweek check | Thursdays 08:05 (cron `5 22 * * 3` UTC) | `trig_0186ew9847ETUWr8MuTP5rUp` |

Times assume **AEST (UTC+10)**. When daylight saving starts they shift to 09:05 AEDT —
confirm the city and the crons can be pinned. Manage them from the Routines list on
claude.ai, or ask in a session to change the schedule.

**Connector limitation:** these Routines carry no connectors, so the sessions they fire
cannot read Gmail, Calendar or Drive to refresh the board — they work from the repo and
from what Brad supplies. To give them connector access, recreate them from the claude.ai
Routines UI with the connectors attached.
