# Data breach response plan — v0.1

**30 Aug 2026. DRAFT for Brad and Hector to complete and adopt before any pilot.** Required
in substance by the **Notifiable Data Breaches scheme** (Part IIIC, Privacy Act 1988). It
did not exist. A health service will ask for it during procurement, and its absence at a
pilot involving real mothers' health information is not defensible.

**Fill every ⚠ before adoption.** A plan with unnamed roles is not a plan.

---

## 1. Scope

Applies to any actual or suspected unauthorised access to, unauthorised disclosure of, or
loss of personal information held by or on behalf of Kindred Care — including information
held by any processor in the register (`processor-map-v0.1.md`).

Kindred Care holds **health information**, which is *sensitive information* under the
Privacy Act. Assume any breach involving conversation content is likely to cause serious
harm until assessed otherwise, not the reverse.

## 2. Roles

| Role | Who | Responsibility |
|---|---|---|
| **Breach Response Lead** | ⚠ Brad (until a Privacy Officer is appointed) | Owns the assessment clock, decides on notification, single point of external contact |
| **Technical Lead** | ⚠ Hector | Containment, forensic scope, evidence preservation |
| **Clinical Lead** | ⚠ unassigned — likely Lois | Assesses harm to mothers specifically, and whether any escalation pathway was affected |
| **Health-service liaison** | ⚠ per tenant | Every institutional customer must be notified; their own obligations run in parallel |

**Gap to close:** no Privacy Officer is appointed. For a venture holding maternal health
conversation this should be a named person before the pilot.

## 3. The five steps

### Step 1 — Contain (immediately)
Stop the exposure. Revoke credentials, disable the affected path, isolate the tenant.
**Preserve evidence before remediating** — logs, database state, the request path. Do not
delete to tidy.

### Step 2 — Assess (within 30 days, and far faster in practice)
The NDB scheme requires assessment within **30 days** of becoming aware of grounds to
suspect. Treat 30 days as the legal ceiling and **72 hours as the working target** — a
health service partner will expect to hear within days, not weeks.

Assess: what information, whose, how many, who accessed it, is it recoverable, what harm is
likely. For this cohort, harm includes **disclosure of perinatal mental health content,
pregnancy loss, family violence disclosure, and infant health** — categories where harm is
severe and not financial.

### Step 3 — Notify, if it is an eligible data breach
An eligible breach is one likely to result in **serious harm** and not remediated. If so:
- **OAIC** — notify as soon as practicable via the online form.
- **Affected individuals** — mothers directly, in plain language, with what happened, what
  information, what they should do, and how to contact us.
- **The health service tenant** — always, immediately, regardless of eligibility. They have
  their own obligations under **Health Records Act 2001 (Vic)** or **Information Privacy Act
  2009 (Qld)**, and finding out from the regulator would end the relationship.
- ⚠ **Consider whether ACU must be notified** under the JV or any research/HREC arrangement.
  If transcripts touched by the breach are within the PhD research scope, the HREC pathway
  is engaged and the supervisor must be told.

### Step 4 — Review
Written post-incident review within 14 days. Root cause, not proximate cause. Feed into the
risk register and, where relevant, into an ADR.

### Step 5 — Record
Maintain a breach register including breaches assessed as **not** notifiable and why. A
regulator asks for this, and "we had none" is less credible than a register showing
judgement was applied.

## 4. Notification content for mothers — draft principles

Written for a woman who may be sleep-deprived, anxious, and holding a baby:
- Plain language, no legal throat-clearing, no "we take your privacy seriously".
- Say what happened in the first sentence.
- Say exactly what information was involved. Do not generalise to avoid alarm — being vague
  compounds distrust.
- Say what she should do, if anything. If nothing, say that plainly.
- Give a real contact, staffed, and say when she will hear next.
- ⚠ Consider whether a clinical support pathway should be offered alongside — for this
  cohort a privacy breach can itself be distressing.

## 5. Testing

⚠ **Run one tabletop exercise before the pilot.** Scenario: a support engineer's access is
compromised and free-text conversation content for 40 mothers at one tenant is exposed. Time
the assessment. A plan never tested is documentation, not evidence — the standard the build
already holds itself to.

## 6. Open items

- Appoint a Privacy Officer.
- Confirm whether each processor's contract obliges them to notify us of a breach, and
  within what time. Most standard SaaS terms are weaker than an Australian health service
  will accept.
- Align tenant notification timelines with what will be written into the pilot agreement.
