# Escalation and clinical resource — doctrine v0.1

**03 Sep 2026 · Kindred Care PM · for Brad, Hector, Lois and the Clinical Governance Group**

*This is a commercial and design position, not legal or clinical advice. Sections 7 and 8
name what must go to a health lawyer and a medical indemnity adviser before anything here
is warranted to a health service or enacted with real mothers.*

---

## 1. The question is three questions

| # | Question | Answer type |
|---|---|---|
| A | What does the Companion do when something looks wrong? | Design |
| B | Who responds, and how fast are we on the hook for it? | Contract and liability |
| C | What clinical resource does Kindred Care itself have to employ? | Cost and org design |

Conflating them produces the worst answer available: a 24/7 clinical roster nobody can
afford, protecting against a risk that was mostly created by our own design choice.

---

## 2. The core move: escalation is mainly a scheduling problem, not a detection problem

Brad's own clinical reference contains the finding that settles this:

> *"Screening tools and education packages do not fix a surveillance gap; scheduled review
> inside the risk window does."*

Read literally, that is not an argument for better detection. It is an argument for
**making reviews happen inside the risk window that would otherwise not happen.**

That reframes the primary clinical function of the Companion:

**Not:** detect deterioration → alert a clinician → clinician responds.
**But:** know the risk window → make the scheduled contact happen, on time, better prepared
→ and hold a narrow exception path for the rare acute event.

This matters enormously, because scheduling adherence:

- is **not** diagnosis, triage or interpretation — the education-only lock survives intact
- needs **no 24/7 roster**, because it is not time-critical
- maps directly onto contacts that already exist and are already funded — MBS 82130 / 82135
  and their telehealth equivalents, and the health service's own postnatal contact schedule
- produces **measurable outcomes** (contact completion rate inside the window) that are
  sellable and publishable
- and is the mechanism that makes the workforce-capacity argument literally true

Detection becomes the exception path. Exception paths can be narrow, rare and conservative.
Primary paths cannot.

---

## 3. The three-lane model

Every signal the Companion generates goes into exactly one of three lanes. There is no
fourth lane and nothing sits between them.

### Lane 1 — NOW
The woman is told, unambiguously and immediately, to contact a service **that is already
staffed 24/7 and already owns this duty of care**: 000, the hospital maternity assessment
line, the ED. Never a Kindred Care queue. Never a callback.

- The Companion's job is to make the call happen, not to make the assessment
- The number is already in her thread, pre-populated at enrolment, not looked up in the moment
- The event is logged with a timestamp, the trigger class, and what was said
- **The unsuppressible T3 trigger belongs here and only here**

### Lane 2 — SOON
An asynchronous flag into the health service's own review queue, with a **contracted,
explicitly non-urgent** service level measured in working hours or days.

- The woman is **also** told what to do herself. Lane 2 never replaces her own agency
- **Lane 2 never carries anything Lane 1 would carry.** If there is doubt, it is Lane 1
- The queue is the customer's, watched by the customer's staff, on the customer's terms

### Lane 3 — SCHEDULED
**The main path, and where the value is.** Adherence support for contacts that should happen
anyway: preparing the woman for the day-5 visit, the 4–8 week check, the mental health
conversation; prompting rebooking when a contact is missed; surfacing to the clinician what
has come up since last time.

Volume expectation: Lane 3 is the overwhelming majority of clinical value. Lane 1 is rare.
Lane 2 is small and deliberately kept small.

---

## 4. The rule that makes it safe

> **Never create a queue that requires a response we do not control.**

Every signal either goes to the woman with an instruction she can act on immediately, or into
a queue whose service level is contracted, non-urgent, and owned by someone with the staff to
meet it.

The corollary, which is the whole safety argument:

> **Over-escalating to a service that already exists is a nuisance. Under-escalating into a
> queue is a death.**

Therefore the bias is always toward Lane 1, and the design accepts a higher false-positive
rate in exchange for never holding a deteriorating woman in a queue.

**The failure mode to design against is not a missed detection. It is a detected signal
sitting unread in an inbox for fourteen hours.** That is a documented failure to respond, it
is worse than never having flagged it, and it is the first thing a health service risk team
will raise.

---

## 5. Where clinicians are actually needed — governance, not operations

Four roles. **None of them is a roster.** All are part-time, named individuals.

| Role | What it does | Cadence | Status |
|---|---|---|---|
| **Clinical content reviewers** | Approve corpus items — the RAG gate | Per release | **NAMED** — Wallace, Simpson, Byatt |
| **Clinical Safety Officer** (named, accountable) | Owns trigger design, the education-only boundary, the hazard log, sign-off before each release | Per release + on change | **OPEN — the critical gap** |
| **Escalation incident reviewer** | Retrospectively reads every Lane 1 event: was it right, did it convert, what changes | Weekly to monthly, hours not days | **OPEN** |
| **Clinical face for procurement** | A health service buys clinical safety from a clinician, not from a founder with a deck | Ad hoc | Partially Brad; needs a second |

**The Clinical Safety Officer is the single highest-value clinical hire and it is not full
time.** The UK's NHS clinical-risk standards formalise exactly this role for health IT. There
is no directly equivalent Australian mandate, and the absence of a mandate is not the absence
of an expectation — a health service's own clinical governance process will look for a named
accountable clinician whether or not a standard compels one. Borrowing the structure
voluntarily is cheap and it answers a question we will otherwise be asked cold.

### What Kindred Care must NOT staff
- A 24/7 clinical response line. It duplicates infrastructure that exists, is the largest
  cost in any model, collapses gross margin, competes with the customer, and almost certainly
  changes the regulatory classification
- Anyone who reviews signals in real time. That is the queue we said we would never create

---

## 6. What this means commercially

| Model | Effect |
|---|---|
| **Lane 1 + Lane 3 only** (no Lane 2) | Supports the current price schedule. Cleanest position. Weakest closed-loop evidence |
| **Lanes 1–3 with customer-owned queue** | The recommended shape. No clinicians on our payroll. Evidence of conversion. Requires the queue clause in every contract |
| **Kindred Care provides clinical response** | A different company. Different margins, different registration, different indemnity, different regulator. Do not drift into it accidentally |

The path from the recommended shape to the third one is a slope, not a step. It gets walked
one reasonable-sounding customer request at a time. The defence is that the doctrine is
written down and the Clinical Safety Officer owns the boundary.

---

## 7. The liability line — and where the lawyer goes

The governing principle, stated commercially:

> **The moment we create an expectation of a response, we own the response.**

Which makes the transparency statement to mothers a safety control, not a disclaimer:
**"Nobody is watching this in real time. If you are worried, call."** It belongs in the
interaction, repeated at the moment of escalation — not buried in terms of service where it
protects nobody and warns nobody.

**Questions for a health lawyer and a medical indemnity adviser, before anything is
warranted to a health service:**

1. Does a contracted non-urgent SLA on a Lane 2 queue transfer the duty of care to the health
   service, or is it shared?
2. Does logging a Lane 1 event without confirming the woman acted create a duty to follow up?
3. What is our exposure where a Lane 1 trigger fires correctly and the woman does not act?
4. Where a trigger does **not** fire and harm follows, does the existence of the trigger
   system itself create a higher standard than having no system at all?
5. Does the Clinical Safety Officer carry personal professional liability, and does our cover
   respond?
6. What must the transparency statement say, in what words, at what moments?

---

## 8. What must be true in the pilot

If the pilot does not measure this, the surveillance argument cannot be sold at all:

- **Escalation conversion rate** — of Lane 1 events, how many resulted in an actual clinical
  contact within a defined window. **This is the single most important number the pilot can
  produce**
- **Lane 3 adherence** — completion rate of scheduled contacts inside the risk window,
  against baseline
- **False positive rate and its cost** — nuisance calls to a maternity line are a real cost
  to the customer and must be quantified honestly, not hidden
- **Time-of-day distribution** — the 2am case is the whole thesis and it either shows up in
  the data or the doctrine is wrong
- **Zero tolerance metric** — any Lane 2 item that should have been Lane 1. Target zero,
  reported whether or not it is zero

---

## 9. The permanent tension, stated plainly

**The strongest version of this product is the one closest to being a medical device.**

Every improvement to detection sensitivity moves toward TGA regulation. This tension does not
resolve and it does not go away with a better form of words. The discipline is:

> **Improve routing and adherence. Do not improve detection.**

Get better at making the right contact happen at the right time, with the right preparation.
Do not get better at working out what is wrong with her. The first is a workforce product.
The second is a regulated device.

---

## 10. The decision to take now

**Adopt the three-lane model as design doctrine, and appoint a named Clinical Safety Officer
before the pilot protocol is finalised.**

Everything else follows from those two. The lanes bound what the build does; the Safety
Officer owns the boundary and signs off against it. Neither requires money we do not have,
and both are prerequisites to a conversation with a health service's clinical governance
committee.

---

*Status: DRAFT doctrine v0.1. Not approved. Requires Clinical Governance Group review, and
legal and indemnity advice per §7 before enactment.*
