# AI impact assessment — the Companion and the people it affects. v0.1

**30 Aug 2026. DRAFT for clinical review by Lois before any external use.** This is the
single document a health service most wants and the venture does not have. It is also
ISO/IEC 42001's centre of gravity, an input to HREC, and the substance behind the safety
claims already made in the pack.

The hard input already exists — 49 homoglyph probes, 35 parser attacks, the poison-model
proof, the dual-agent architecture. This is the write-up, not new work. **What it must not
be is a marketing document about how safe we are.** Its value comes from naming harms
honestly, including the ones not yet mitigated.

---

## 1. Who is affected

| Group | Relationship |
|---|---|
| **Mothers** | Primary. 20 weeks gestation to 12 months postnatal — a period of heightened vulnerability, sleep deprivation, and elevated incidence of anxiety, depression and family violence |
| **Infants** | Indirect but material. Information acted on affects a non-consenting third party who cannot report harm |
| **Midwives and nurses** | Workforce. Both beneficiaries (reach extended) and bearers of new burden (enrolment, escalations) |
| **The health service** | Carries clinical governance and reputational risk for a tool it did not build |
| **Under-served cohorts** | CALD, First Nations, regional, low digital literacy — the equity case, and the group most exposed to a system that works less well for them |

---

## 2. Harms, mechanisms and current position

### 2.1 Clinical — the Companion misses something serious

**Mechanism.** A mother describes symptoms indicating a genuine emergency — pre-eclampsia,
sepsis, haemorrhage, suicidal ideation — and the system fails to escalate.

**Severity: catastrophic. Likelihood: engineered low.**

**What is built.** Deterministic T1/T2/T3 triggers that do not depend on the model's
judgement. **T3 is unsuppressible.** The poison-model proof demonstrates the safety net
holds with the LLM deliberately corrupted — meaning escalation is not contingent on the
model behaving. 49 Unicode homoglyph probes and 35 parser attacks, zero bypasses.

**This is genuinely strong and most comparable products cannot claim it.**

**Residual risk.** The triggers fire on what she says. **A harm not verbalised is not
caught**, and no architecture fixes that. The trigger set has never met real language at
scale — evidence sprint measurement 6 is its first contact with reality.

### 2.2 Clinical — the Companion says something wrong

**Mechanism.** Confidently incorrect education leading to a harmful decision.

**What is built.** Education-only boundary enforced *architecturally* — symptom
interpretation, triage and diagnosis are not features that were disabled, they were never
reintroduced (Stage 5d). RAG with retrieval provenance: which chunks fed which answer, and
verified by swapping the corpus underneath and confirming the trace was captured rather than
re-queried. Agent B clinical supervision on every turn.

**Residual risk.** **recall@5 and safety-tag triggering are unmeasured** — the gold-standard
eval set does not exist and the Analytics epic is 0 of 12. Until it does, accuracy is
architected for rather than demonstrated. **State it that way in every document.**

### 2.3 Psychological — the warmth trap

**Mechanism.** A companion available at 2am, warm, patient and never irritated, becomes a
substitute for human contact rather than a bridge to it. A mother who would have called the
midwife, or told her partner, tells Elena instead — and Elena cannot visit, examine, or sit
with her.

**This is the harm most specific to this product**, and the one least addressed by
conventional safety engineering. It is already a documented hard gate in the readiness
ladders and it remains **unmeasured**.

**Severity: high. Likelihood: unknown — which is the problem.**

**What is built.** Escalation to human handover. Education-only framing.

**Residual risk.** Substantial and unquantified. **Proposed measurement for the evidence
sprint:** does Companion use correlate with *more* or *fewer* midwife contacts? More is the
good outcome — it means the Companion is a bridge. Fewer is the warning sign, and it will
look like success on every engagement metric.

*That inversion is worth stating explicitly to any buyer: the metric that looks best may be
the harm.*

### 2.4 Equity — it works less well for those who need it most

**Mechanism.** A conversational system trained and tested on dominant-language, high-
literacy interaction serves CALD, First Nations, low-literacy and low-digital-access mothers
worse — while being sold on an equity case.

**Severity: high, and reputationally acute given the framing.**

**What is built.** Cultural avatar packs configured under ACU governance. Multi-modal access
(text, voice) lowers literacy barriers.

**Residual risk. This is the largest documentation gap.** No corpus bias or data quality
assessment has been done. If the equity case is argued to Innovation Victoria or the
Taskforce, someone will ask what was done to verify the Companion serves the mothers the
equity case names. **There is currently no answer.**

Also unaddressed: an app-based channel excludes exactly this cohort — see the open channel
question in the interface doctrine.

### 2.5 Privacy and disclosure

**Mechanism.** Sixteen months of the most sensitive conversation a person may have —
perinatal mental health, pregnancy loss, family violence, infant health — held in one
persistent thread. Exposure harm is severe and non-financial.

**What is built.** Row-level tenant isolation; free-text reads gated to three escalation
roles with researcher and content-SME access removed deliberately; ADR-008 forbids free text
in the analytics store, proven against 18 probe field names; two cross-tenant exposures found
**by review rather than by incident**.

**Residual risk.** Processor path unconfirmed (avatar and STT vendors, Vertex endpoint). No
retention or disposal schedule. No erasure capability. Supplier support access scope unknown.

### 2.6 Autonomy and consent

**Mechanism.** A mother enrolled by her health service may not experience enrolment as a
free choice, and may not understand she is talking to a machine, what it retains, or who can
read it.

**Residual risk.** **No transparency statement exists.** Consent capture is a flow, not an
explanation. This is a small document that closes a real gap.

### 2.7 Workforce

**Mechanism.** Enrolment and escalation handling become unfunded work for midwives already
described by the Taskforce as under strain — the very problem the product claims to address.

**Residual risk.** Unmeasured. **Evidence sprint measurement 8.** A product sold on workforce
relief that adds workload will not be renewed, whatever the mothers think of it.

---

## 3. Summary position

| Harm | Mitigation strength | Evidence | Residual |
|---|---|---|---|
| Missed escalation | **Very strong** | Adversarial testing, poison-model proof | Unverbalised harm; untested at scale |
| Wrong information | Strong architecture | **Unmeasured** — no eval set | High until evals land |
| Warmth trap | Weak | None | **High — and it looks like success** |
| Equity | Partial | **None** | **High** |
| Privacy | Strong engineering | Good | Processor path unknown; no erasure |
| Autonomy | Weak | None | Medium — closable cheaply |
| Workforce | None | None | Unknown |

## 4. What this says about readiness

**Two harms are engineered against to an unusually high standard and two are barely
addressed.** The pattern is consistent: the harms that look like software problems have been
solved well, and the harms that look like human problems — dependence, equity, workforce —
have not been touched.

That is not a criticism of the build. It is the correct thing to say to a health service,
because it is what their clinical governance committee will conclude on their own, and
saying it first is the difference between candour and being caught.

## 5. Actions

1. **Lois to clinically review** before any external use. This must not go out as an
   engineering document.
2. **Corpus bias and data quality assessment** — the largest gap, and it undercuts the
   equity case until closed.
3. **Warmth-trap measurement into the evidence sprint** — midwife contact frequency as the
   indicator, with the inversion stated.
4. **Transparency statement** — small, cheap, closes 2.6.
5. **Re-run after the sprint** with real numbers. An impact assessment with evidence in it is
   a different document from this one.
