# VPDSS readiness self-assessment — v0.1

**30 Aug 2026.** For any Victorian public health service, the **Victorian Protective Data
Security Standards** (12 mandatory standards issued by OVIC under Part 4, Privacy and Data
Protection Act 2014) will be a contractual matter, not an optional extra. Contracted service
providers with direct or indirect access to public sector information must adhere where the
engaging agency requires it, and may be asked to demonstrate assurance.

**Doing this before the first procurement conversation is cheap, and it makes a small vendor
look serious in a way little else does.**

## A gap in this draft, stated plainly

`ovic.vic.gov.au` is blocked from this environment, so I could not retrieve the **exact
numbered titles of the 12 standards**. I have not guessed them — a document going to a
health service with invented standard numbers would do more damage than having none.

**Action: Brad or Lois to download the VPDSS V2.0 Standards and the Implementation Guidance
from https://ovic.vic.gov.au/information-security/standards/ and map the evidence below onto
the numbered standards.** The evidence-gathering is the hard part and it is done here; the
mapping is an hour's work.

What is verified: the standards number **12**, and they span **five security areas —
governance, information, personnel, ICT, and physical security**.

---

## Evidence we already hold, by security area

This is the useful part. Most small vendors have nothing here; Kindred Care has a lot,
because the build was run to an evidence standard from the start.

### Governance security
| Have | Evidence |
|---|---|
| ✅ Architectural decision records | ADR series, incl. ADR-008 on analytics and k-anonymity |
| ✅ Change control with an approval gate | Deploy gate; QA/owner-approval loop; nothing merges unapproved |
| ✅ Risk register | `kindred-care/risks.md`, 130 entries, owned and dated |
| ✅ Audit trail | Console audit posture; alerts inbox |
| ⚠ **Missing** | Named Privacy Officer; information security policy set; **third-party processor register is v0.1 draft** |

### Information security
| Have | Evidence |
|---|---|
| ✅ Tenant isolation | Postgres row-level security; two cross-tenant exposures found by QA reading code and ruled by the owner — *found by review, not by incident* |
| ✅ Access control by role | §3.3 role matrix; free-text ticket reads gated to three escalation roles, with researcher and content-SME access removed deliberately |
| ✅ Data minimisation in analytics | ADR-008 §5 forbids free text in the analytics store; closed-vocabulary allowlist proven against 18 probe field names |
| ✅ Consent capture | Consent flow in the enrolment journey; `withdrawConsent` exists |
| ⚠ **Missing** | Information classification scheme; **retention and disposal schedule**; erasure capability ahead of Privacy Act Tranche 2 |

### Personnel security
| Have | Evidence |
|---|---|
| ⚠ **Largely missing** | Who is vetted, to what level, and by whom. **ClinOps support staff can potentially access production** — scope unconfirmed (processor map row 8) |
| ⚠ | Confidentiality deeds exist for ACU (Hector's CDA); no equivalent evidenced for support personnel |
| Note | A health service will ask about **National Police Check** and possibly **Working with Children Check** for anyone with access to information about mothers and infants. Decide the position before being asked |

### ICT security
| Have | Evidence |
|---|---|
| ✅ Segregated environments | dev/prod separation; per-track databases (IAC-008) |
| ✅ CI/CD with gated deployment | Cloud Build → Cloud Run; deploy gate |
| ✅ Test discipline as a control | Hygiene guard promoted WARN→FAIL, proven by re-planted mutation rather than asserted; leak class closed on a measured run-over-run delta of zero |
| ✅ Authenticated service boundaries | Token-gated agent service; upload-gate as a separate service |
| ⚠ **Missing** | **Vertex regional endpoint pinning unconfirmed** (see `endpoint-check-for-hector.md`); penetration test; vulnerability management process; Essential Eight self-assessment; backup and restore testing |

### Physical security
| Have | Evidence |
|---|---|
| ✅ Inherited | GCP australia-southeast1 data centre controls; region is IRAP-assessed |
| ⚠ **Missing** | Own posture — where staff and contractors work, device management, whether any production access happens from personal or offshore devices. **Given a distributed team this is a real question, not a formality** |

---

## The honest summary for a buyer

**Strong:** the technical controls are unusually good for a pre-revenue venture, and they are
*evidenced* rather than asserted — which is the exact thing VPDSS assurance asks for.

**Weak:** the paperwork layer. Policies, classification, retention, vetting, and the third-
party register. None of it is hard; none of it is done.

**That asymmetry is worth naming in a procurement conversation before they find it.** "Our
engineering controls are ahead of our documentation, here is the documentation plan and its
dates" reads far better than being walked through the gaps.

## Sequence

1. Retrieve the official 12 standards and map this evidence onto them.
2. Close the processor map ⚠ rows — several standards depend on it.
3. Write the missing policy set. It is a week of work, not a project.
4. Appoint a Privacy Officer and settle the vetting position.
5. Then complete a formal self-assessment and keep it current.
