# Strategy analysis to investment — 31 Aug 2026

Written at Brad's request for a full pause and analysis. Integrates the 28 Aug MVP Board
with the relationship position established 30–31 Aug. Five conclusions, in order of how much
they change what we do.

---

## 1. The build lands *before* the gate, and nobody has said so

193 hours of orchestrated loop time across two parallel tracks — **roughly 2–2½ working
weeks of continuous sessions.** From 28 Aug that puts a complete MVP in **mid-to-late
September**, ahead of UCAC on 16 October.

Every plan in the pack still reads as though the build is the thing being funded. It isn't.
By the gate we will have a finished product, and the question in the room will be *does it
work and will anyone pay* — not *can you build it*.

**This is the strongest argument yet for starting the evidence sprint now rather than after
the build.** The build and the pilot should overlap, not queue.

## 2. The engineering governance is an unsold investment asset

The board records, in the last week alone:

- QA refusing a passing grade because waving the first vehicle through under a new rule
  *"would hollow the rule out immediately"*
- QA proving a fix weaker than claimed, then **declining to fail the builder** because the
  weak control was QA's own round-1 prescription implemented literally — *"failing someone
  for building what the reviewer specified would be a new goalpost"*
- A builder planting a defect, getting zero failures, and concluding **the test was blind
  rather than the fix fine** — then writing the missing test and re-running with the plant
  still in
- The leak class **retired, not reduced**, ruled on a run-over-run delta rather than a
  flattering after-count, with both numbers required to appear together *"so the flattering
  one could never be quoted alone"*
- A second oracle obtained for a predicate QA declined to trust
- Two cross-tenant exposures found **by reading code, not by incident**
- A guard-on-the-guard catching QA's own planted mutation

**That is not "1354 tests passing", which is how the pack describes it.** It is a
demonstrated culture of adversarial verification, and it is rare in a pre-revenue company.

Three places it converts directly into value:

- **ISO 42001.** Accountability, transparency and risk management are the standard's three
  pillars, and this is *evidence* of all three rather than an assertion. Most applicants
  build governance from scratch; this is already the substance.
- **Health-service clinical governance.** A committee assessing an AI product asks how you
  know it works. "We found two cross-tenant exposures by reading our own code before anyone
  was exposed" is a better answer than any certificate.
- **The investment case.** It is the credible foundation for the safety claims. Without it
  the poison-model proof is a slide; with it, it is a habit.

**Action: write the engineering governance section of the pack.** It does not exist. It is
free. It is possibly the most differentiated thing the venture owns.

## 3. Evals last is the sequencing error

**Analytics & evals: 0 of 12.** At the board's own loop times that is roughly **24–30 hours**
— days, not months. And it gates:

- The gold-standard eval set → **recall@5 ≥ 0.85 and safety-tag ≥ 0.95** → **the TRL 4 claim**
- The Director, HREC and platform views → **the pilot's measurement layer**

So a fortnight of work sits behind the single most valuable claim in the raise, scheduled
last, behind features nobody has asked for. FIX-DB-001 — in loop now on Track A — is its
first blocker, in the eval framework's own table.

**Action: promote the evals epic ahead of the remaining app modalities.** Thirteen app
modality stories can wait; the thing that proves the product works cannot. This is the
highest-value scheduling decision available and it costs nothing.

## 4. The real critical path is not Hector's

The board lists what it does not count: **legal sign-off (privacy notice, S11 ToS), ACU/HREC
approvals (ADR-008 k-values, S9e copy), the LiveAvatar decision D-23, STT/TTS vendor
credentialing, manual Stitch cleanup.**

**Every one of those is a Brad item or an ACU item. Not one is a Hector item.**

The build finishes and then waits. This is the throughput diagnosis confirmed from the
engineering side: the constrained lane is the one with a single person in it, and the build
board has been telling us for a week.

Note also that **HREC already appears as an out-of-loop blocker on the build board**. The
ethics pathway is not only a pilot prerequisite — it is already gating shipped-story
closure.

## 5. Two exposures are pilot prerequisites and are not built

Q1 (outreach-gate identity reveal across any institution) and Q2 (all six roles reading
mothers' free text) are **owner-ruled and sitting in Ready.** One SA sitting plus one build
loop.

**Neither may remain open when an external environment exists.** They are cheap, they are
specified, and they are a hard gate on enrolling a single mother.

---

## What this means for the raise

**16 October is a POC case, and a strong one:** a finished product, demonstrated pull from
the profession at every level, an unusually rigorous engineering governance story, a live
pilot enrolling, and candour about what is not yet measured.

**It is not a commercialisation case**, because the engagement and efficacy evidence will
not exist by then. That is what POC funding is for. The failure mode is presenting
commercialisation-grade certainty at POC stage.

**Two things can still stop it, and both sit with ACU:** the $650,000 with no identified
source, and the Heads of Agreement. Both 61 days open. Their continued absence is itself
information.

## Sequence

**This week** — ethics started; evals epic promoted ahead of app modalities; Q1 and Q2
scheduled; D-23 answered; pricing decided; Marie's scope agreed; Russell pressed for dated
positions.

**By 16 Sept** — engineering governance section written; relationship set in the deck;
Wishlist met; SCHHS presentation dated.

**By 2 Oct** — build complete or near; evals shipping; pilot enrolling; sweep done; impact
assessment reviewed by Lois.

**16 Oct** — a finished product, a live pilot, a governance story nobody else has, and an
honest account of what is still unknown.
