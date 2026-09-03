# Third-party processor map — v0.1

**30 Aug 2026.** The single artefact that serves three purposes at once: investor diligence,
health-service procurement, and the VPDSS third-party requirement. It did not exist.

**Status: DRAFT — every row marked ⚠ needs Hector to confirm before this goes anywhere.**
Do not send externally until the ⚠ rows are resolved; an incorrect processor map is worse
than none, because a buyer will treat it as a warranty.

## How to read this

**"Data reaching it"** is the test that matters, not what the vendor is nominally for. A
vendor that never sees conversation content is a different risk class from one that does.
Under **APP 8** you remain accountable for what an overseas recipient does with personal
information, and health information is *sensitive information*, so the bar is higher again.

## The register

| # | Processor | Purpose | Data reaching it | Jurisdiction | Class | Status |
|---|---|---|---|---|---|---|
| 1 | **Google Cloud Platform** | Compute, storage, database, hosting | All platform data incl. conversation content at rest | **australia-southeast1 (Sydney)** | Onshore | ✅ Correct choice. IRAP-assessed region — confirm which controls are inherited vs owned |
| 2 | **Vertex AI / Gemini** | LLM inference — Agent A and Agent B | **Conversation content in full** | ⚠ **UNCONFIRMED** — Sydney ML processing is supported, but the global endpoint may be in use | **The critical row.** See `endpoint-check-for-hector.md`. Google's formal AI/ML data-residency commitment covers **US and EU only** — no contractual guarantee for the ML layer in Australia |
| 3 | **Vertex AI Search (RAG)** | Corpus retrieval | Query text derived from conversation | ⚠ Same question as row 2 | Same check applies |
| 4 | **HeyGen / LiveAvatar** | Avatar video generation | ⚠ **What exactly?** Full utterance text? Rendered audio only? A pre-approved script? | **United States** | **Highest risk row.** If conversation content reaches it, that is a cross-border disclosure of health information. May be a hard blocker for a Victorian public health service **independent of cost** — see the D-23 brief |
| 5 | **STT vendor** | Speech to text | Mother's spoken words — raw audio and/or transcript | ⚠ **Unselected.** MVP Board lists "real STT/TTS vendor credentialing" as out-of-loop | Choose with sovereignty as a selection criterion, not after |
| 6 | **TTS vendor** | Text to speech | Companion's output text | ⚠ Unselected, as above | Lower risk than STT — output rather than disclosure — but still a processor |
| 7 | **Cloud Build / GitHub** | CI and source control | Source code; **no production personal information** | US (GitHub) | Low risk. Confirm no production data in CI fixtures — the test-DB hygiene work suggests this is already disciplined |
| 8 | **ClinOps** | 8×5 platform support | ⚠ **Support access scope?** Can support staff see conversation content or mothers' free text? | ⚠ Confirm entity domicile and staff location | **Related party — Hector's company.** Disclosable, normal, and an investor will ask. Also a VPDSS *personnel security* question: who is vetted, to what level |
| 9 | **Email / notification provider** | Enrolment codes, re-engagement notifications | Contact details; **must carry no clinical content** | ⚠ Unconfirmed | Notification bodies are a classic leak path. Confirm they carry no health information |

## The three questions this map has to answer, and currently cannot

1. **Does conversation content leave Australia at any point?** Rows 2, 3, 4 and 5 are all
   unconfirmed. Until they are, the pack cannot claim onshore processing, and it should not.
2. **Can a human at a supplier read what a mother wrote?** Row 8. The console work already
   gated free-text ticket reads to three escalation roles — good — but supplier support
   access is a separate path.
3. **What is the legal basis for each disclosure?** Consent alone is a weak basis under the
   proposed Tranche 2 "fair and reasonable" test. Where a processor is genuinely necessary
   to deliver the service, say so and document why.

## What to do with it

- Hector fills the ⚠ rows. Nothing else in the compliance stack can be finished first.
- Add a column for each contract: is there a written data processing agreement? For most of
  these there will not be, and a health service will ask.
- Once complete, this becomes an appendix to the data room, a VPDSS input, and the answer to
  the sovereignty section of any security questionnaire.
