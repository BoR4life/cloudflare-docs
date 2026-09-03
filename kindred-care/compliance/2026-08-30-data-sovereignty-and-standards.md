# Australian data protection, sovereignty and standards — what applies and what to do

**30 Aug 2026.** Written to Brad's question. Verified against current sources rather than
recalled; every claim that turns on a moving target is marked and sourced. **This is a
commercial and architectural read, not legal advice** — the Privacy Act positions here need
an Australian privacy lawyer before anything is warranted to a health service.

---

## 1. The law that applies

### Commonwealth

**Privacy Act 1988 (Cth)** and the 13 **Australian Privacy Principles**. Two things make
Kindred Care's position stricter than a general SaaS:

- **Health information is "sensitive information"** — a higher bar for collection, use and
  disclosure, and consent is generally required to collect it.
- **All private sector health service providers are covered regardless of turnover** —
  there is no small-business exemption to shelter behind.

**Notifiable Data Breaches scheme** (Part IIIC) — mandatory notification to the OAIC and to
affected individuals for an eligible breach. **You need a written incident response plan
before a pilot, not after.** I have not seen one in the data room.

**Reform is live but unlanded.** Tranche 1 is legislated and progressively taking effect.
Tranche 2 remains a government commitment — the Attorney-General confirmed in February 2026
that it is being progressed, with **no timetable announced and no bill passed**. Proposed
scope that would bite directly on a conversational agent holding 16 months of maternal
health dialogue: a **"fair and reasonable" test applying regardless of consent**, a **right
to erasure**, and an **expanded definition of personal information**. Design as though these
are coming — retrofitting erasure into a persistent conversational thread is expensive.

### State — and this is the layer people miss

State health-records law sits *on top of* the Commonwealth regime and **differs by state**:

| Jurisdiction | Instruments |
|---|---|
| **Victoria** | Privacy and Data Protection Act 2014 (Vic) · **Health Records Act 2001 (Vic)** (Health Privacy Principles) |
| **Queensland** | **Information Privacy Act 2009 (Qld)** — applies to HHSs as Qld public sector agencies |

Kindred Care is pursuing both Victoria and Queensland. **That means two compliance postures,
not one**, and a Victorian service and SCHHS will ask different questions. The pack treats
privacy as a single undifferentiated obligation.

### One thing to purge

Hector's original cost sheet prices *"HIPAA-compliant environment setup"* for the oncology
use case. HIPAA is US law and **irrelevant here**. If that language has leaked into any
Kindred Care document, it reads to an Australian health buyer as a team applying US
frameworks to an Australian context — a credibility problem out of proportion to the error.
Grep the pack.

---

## 2. Data sovereignty — the actual finding

**APP 8** governs cross-border disclosure: you remain accountable for what an overseas
recipient does with the information. Many state health services then impose **contractual**
onshore requirements stricter than the law alone requires.

### The good part

GCP **australia-southeast1 (Sydney)** is the right choice, and ML processing for the Gemini
2.5 family **is** supported in that region.

### The gap you must disclose rather than have found

**Google's formal AI/ML data residency (DRZ) commitment is only offered in US and EU
locations.** ML processing *can* occur in Sydney; there is **no contractual data-residency
guarantee for the ML layer in Australia**. That is a real gap, it is not fatal, and it is
far better raised by you in a procurement conversation than discovered by their security
team. ([Google Cloud data residency](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency))

### A concrete technical check for Hector, testable today

Google's own guidance: **avoid the global endpoint where data cannot leave a continent —
pin a regional endpoint explicitly.** There is a known defect class in which Vertex AI with
an API key **ignores `GOOGLE_CLOUD_LOCATION` and silently uses the global endpoint**
([gemini-cli #27984](https://github.com/google-gemini/gemini-cli/issues/27984)).

**If that is happening in `bor-iridia`, mothers' conversations are egressing and nobody
knows.** This is free to check and it either confirms a claim you are already making or
destroys it. Do it this week.

### The bigger sovereignty problem is the avatar

**HeyGen / LiveAvatar is a US SaaS vendor.** If any part of a mother's conversation is sent
to it to generate speech or video, that is a **cross-border disclosure of health information
to a US processor** under APP 8. The same question applies to the STT/TTS vendors the MVP
Board lists as out-of-loop pending "real vendor credentialing".

**For a Victorian public health service this may be a hard blocker independent of cost.**

So **D-23 is now three decisions converging on one call**: a cost decision (69–80% of
variable cost), a product decision (video for demonstration, not conversation), and a
sovereignty decision (a US processor in the conversational path). Three independent lines
pointing the same way is the strongest form of argument available — use it with Hector.

---

## 3. The standards a buyer will actually ask for

### VPDSS — the one that will appear in a Victorian contract

The **Victorian Protective Data Security Standards** (12 mandatory standards, issued by OVIC
under Part 4 of the Privacy and Data Protection Act 2014). **Contracted service providers
with direct or indirect access to public sector information must adhere where the engaging
agency requires it, and may be asked to demonstrate assurance.**
([OVIC — contracted service providers](https://ovic.vic.gov.au/information-security/contracted-service-providers/))

Treat this as a **contractual requirement, not an optional extra**, for any Victorian public
health service. A VPDSS self-assessment completed *before* the first procurement
conversation is cheap and makes a small vendor look serious in a way little else does.

### ISO/IEC 27001 — the baseline

Not law. Effectively a commercial requirement for government health sales, and it will
appear in any tender. This is the funded certification target.

### ISO/IEC 27701 — the privacy extension

Extends 27001 to privacy information management. Increasingly asked alongside it. Sequence
it after 27001, not instead.

### ISO/IEC 42001 — the differentiator, and the recommendation

The AI management system standard (published Dec 2023). Adopted in Europe as
**EN ISO/IEC 42001:2026 with national adoption due September 2026**, and a 2026 Gartner
survey reports **83% of Fortune 500 procurement teams plan to require alignment by 2027**.
([ISO 42001 in 2026](https://www.aigovernancetoday.com/news/iso-42001-redefining-ai-governance-2026))

**This is the opening.** Kindred Care is an AI vendor selling into government health with a
genuinely unusual safety architecture, and 42001's three pillars — accountability,
transparency, risk management — are things you can already evidence rather than assert:
dual-agent supervision, deterministic unsuppressible triggers, the poison-model proof, the
deploy gate, the audit trail, the evidence standard on the build itself.

**Certification is expensive; documented alignment is not**, and you already hold most of
the artefacts. Almost no small Australian health-AI vendor will have either. Do the
alignment mapping now, certify when funded.

### IRAP and the Essential Eight

Commonwealth-oriented, but state health procurement sometimes references them. GCP Sydney
carries IRAP assessment, so **some controls are inherited** — know which you inherit and
which you own, because a buyer will ask and "Google has IRAP" is not an answer.

### ISO 13485 and ISO 14971 — do not pursue

Medical device quality management and risk management. **You have deliberately positioned
outside SaMD, and the education-only boundary is what holds that position.** Pursuing device
standards would signal you think you might be a device, which undercuts the whole regulatory
posture. Revisit only if the TGA classification changes.

---

## 4. What I would actually do, in order

1. **Check the endpoint pinning in `bor-iridia` this week.** Free, and binary.
2. **Build the processor map** — one page: every third-party processor, what data reaches
   it, which jurisdiction, what the legal basis is. This is simultaneously a diligence
   artefact, a procurement artefact and a VPDSS input, and it does not exist.
3. **Write the incident response plan.** Required by the NDB scheme, absent from the room.
4. **VPDSS self-assessment** before the first Victorian procurement conversation.
5. **Decide D-23 knowing it is a sovereignty decision**, not only a cost one.
6. **ISO 27001 as the funded target; ISO 42001 alignment documented now** as the
   differentiator.
7. **Purge HIPAA language** from anything Kindred Care.
8. **Design for erasure now**, ahead of Tranche 2. Retrofitting a right to erasure into a
   16-month persistent conversational thread is a rebuild, not a feature.

## Sources

- [Vertex AI data residency — Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/data-residency)
- [Google Cloud Platform Services Data Residency](https://cloud.google.com/terms/data-residency)
- [Vertex AI global endpoint / GOOGLE_CLOUD_LOCATION defect](https://github.com/google-gemini/gemini-cli/issues/27984)
- [OVIC — Victorian Protective Data Security Standards](https://ovic.vic.gov.au/information-security/standards/)
- [OVIC — contracted service providers](https://ovic.vic.gov.au/information-security/contracted-service-providers/)
- [Privacy Act second tranche — status and scope](https://rulesmate.com.au/insights/privacy-act-second-tranche-reforms-2026-outlook)
- [ISO 42001 and procurement in 2026](https://www.aigovernancetoday.com/news/iso-42001-redefining-ai-governance-2026)
