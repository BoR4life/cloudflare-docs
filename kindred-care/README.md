# Kindred Care — program manager

This directory is the **live state** of the Kindred Care venture. The agent that reads
and maintains it is the skill at `.claude/skills/kindred-care-pm/`.

## What it does

Holds one board across three tracks that would otherwise drift apart:

- **Product (TRL 1–9)** — Hector's build, and whether each readiness claim is evidenced
- **Market (CRL 1–9)** — who signs, out of which budget, for how much
- **Investment (IRL 1–9)** — entity, IP, non-dilutive funding, data room, the raise

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
