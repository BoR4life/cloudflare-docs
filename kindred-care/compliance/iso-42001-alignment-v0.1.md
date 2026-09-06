# ISO/IEC 42001 alignment — the differentiator, mapped

**30 Aug 2026.** The recommendation is **document alignment now, certify when funded.**
Certification is expensive; alignment is not, and Kindred Care already holds most of the
artefacts because the safety architecture was built to be provable rather than asserted.

## Why this one, and why now

ISO/IEC 42001 (published Dec 2023) is the AI management system standard. It has been adopted
in Europe as **EN ISO/IEC 42001:2026** with national adoption due September 2026, and a 2026
Gartner survey reports **83% of Fortune 500 procurement teams plan to require alignment by
2027**. It is built around **accountability, transparency and risk management** — and
carries **38 controls across nine objectives (A.2–A.10)** over an Annex SL management-system
shell (clauses 4–10).

Two reasons it is the right target for Kindred Care specifically:

1. **You can evidence it rather than claim it.** Most vendors seeking 42001 have to build
   governance from scratch. Kindred Care's dual-agent supervision, unsuppressible
   escalation, poison-model proof and deploy gate are *already* the substance of several
   control objectives.
2. **Almost no small Australian health-AI vendor will have it**, and you are selling AI into
   government health during the period procurement starts asking. That is a moat available
   for the cost of documentation.

**Note on Annex A:** it is a reference set, not a checklist. Clause 6.1.3 requires you to
derive controls from your own risk treatment, then compare against Annex A to confirm
nothing relevant was missed. So the Statement of Applicability must be built from the
official standard — the mapping below is the evidence inventory that feeds it, not the SoA.

---

## Evidence inventory, by control domain

| 42001 domain | What Kindred Care already has | Gap |
|---|---|---|
| **AI policy (A.2)** | Education-only boundary enforced *architecturally*, not by policy — Stage 5d never reintroduced across the whole build | The policy itself is not written down. The behaviour is disciplined; the document is absent |
| **Internal organisation (A.3)** | Clear role separation in the console (§3.3 matrix); owner-ruling process for cross-cutting decisions; SA sittings for architectural rulings | No named AI governance owner or accountability statement |
| **Resources (A.4)** | Documented compute, model, data and tooling dependencies; RAG corpus catalogue with ACU approval workflow | Not consolidated into a resource register |
| **AI impact assessment (A.5)** | Safety analysis is genuinely strong: deterministic T1/T2/T3 triggers with T3 unsuppressible; **poison-model proof that the safety net holds with no LLM**; 49 homoglyph probes and 35 parser attacks with zero bypasses | **No formal impact assessment on affected individuals** — the mothers. This is the standard's centre of gravity and the biggest single gap |
| **AI system lifecycle** | Exceptional. Shredded stories with sealed regions, QA-by-mutation, deploy gate, evidence standard (*"a check that cannot go red is documentation, not evidence"*), full audit trail | Needs restating in lifecycle language; the substance is there |
| **Data for AI systems (A.6)** | RAG provenance — which chunks fed which answer, verified by swapping the corpus and confirming the captured trace did not change; ontology coverage analysis; k-anonymity work | Data quality and bias assessment on the corpus is not evidenced. For a maternal cohort spanning CALD and First Nations mothers, this will be asked |
| **Information for interested parties (A.7)** | Safety help-sheet auto-open; consent flow | No AI transparency statement for mothers — what Elena is, what it is not, what it does with what she says, in plain language |
| **Use of AI systems (A.8)** | Supervised architecture with Agent B as clinical supervisor; escalation queue with human handover | Intended-use and misuse documentation not written |
| **Third-party relationships (A.9)** | — | **`processor-map-v0.1.md` is the start of this and it is a draft.** Currently the weakest domain |

---

## The three gaps that matter

1. **The AI impact assessment on mothers.** This is 42001's core and the thing a health
   service most wants. It is also genuinely useful rather than paperwork: who could be
   harmed, how, what mitigates it, what residual risk remains. The safety testing is the
   hard input and it exists — the assessment is the write-up.
2. **The transparency statement for mothers.** Plain language, what Elena is and is not,
   what happens to what she says. Doubles as a consent-flow improvement and as an APP 5
   notification.
3. **Third-party governance.** Close the processor map.

## What this is worth

An ISO 42001 alignment statement, an AI impact assessment and a transparency statement are
**three documents**. With the evidence already in hand, that is perhaps two weeks of work.

The output is the ability to say to a health service, a state programme and an investment
committee: *"our AI governance is documented against the international standard, and here is
the assessment."* Very few vendors in this market can say that in 2026, and the ones who can
are not small.

**Certification target: after the raise, alongside ISO 27001.** Alignment: now.

## Sources
- [ISO 42001 Annex A controls](https://www.isms.online/iso-42001/annex-a-controls/)
- [ISO 42001 and procurement in 2026](https://www.aigovernancetoday.com/news/iso-42001-redefining-ai-governance-2026)
