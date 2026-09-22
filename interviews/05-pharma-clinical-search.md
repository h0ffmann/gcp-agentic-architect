# 05 — Literature and protocol search for a pharma clinical-operations team

Time box: 45 min. Deliverable: `interviews/answers/05-YYYYMMDD.md` with `## Part A`, `## Part B`,
`## Part C`. Review: `use the design-reviewer agent on <that file>`.

## Setting

A mid-size pharmaceutical company runs ~60 clinical trials at a time. Clinical-operations staff
write and amend trial protocols, answer site questions, and prepare regulatory submissions. They
spend hours a week searching internal SOPs, past protocols, investigator brochures, and published
literature. An innovation team built a "research assistant" chatbot over that corpus; it is
popular and it is not validated. Quality Assurance has now classified it as a GxP-relevant
system because its answers have been pasted into protocol amendments. The interviewer is the
head of clinical systems. They need a design that QA will validate, or a reason to withdraw the
tool.

## The system as found

- A vector index over ~400 000 chunks from SOPs, protocols, brochures and PubMed abstracts,
  rebuilt weekly from a shared drive. No document version is recorded; superseded SOPs are in
  the index alongside current ones.
- Top-8 chunks are pasted into a prompt with "answer with citations". Citations are whatever the
  model writes; a QA spot check found 1 in 6 citations pointing to a chunk that did not say that.
- Everyone with a company login sees everything, including protocols for unblinded studies.
- No record of questions and answers is kept; staff paste answers into documents by hand.
- Model: hosted, API, no fine-tuning. Prompt edited in a config file, no history.

## Constraints

- GxP: a validated system needs a defined intended use, documented requirements, evidence that
  it meets them, change control, and an audit trail. 21 CFR Part 11-style records: attributable,
  legible, contemporaneous, original, accurate.
- Blinded-study material must be visible only to the roles the study's blinding plan lists.
- A wrong answer that reaches a protocol is a deviation; a wrong citation is a finding.
- The corpus changes daily; an SOP revision must be searchable within the day and its
  predecessor must stop being served.
- Company policy: no proprietary document text may be used to train any model.

## Part A — improve it without changing infrastructure

Same index, same model, same chat UI. What do you change so that the 1-in-6 bad-citation rate
is measured, then driven down, and so that superseded SOPs stop being served? Say what evidence
you would hand QA at the end of the month.

## Part B — you may change infrastructure

Design the validated system. Show how an answer is traceable to the exact document version and
passage; show how blinding is enforced at retrieval time, not in the prompt; show the change
control path for a prompt or model change. Say what the intended-use statement is and what the
tool must refuse to do.

## Part C — FOSS stack vs Google Cloud Agent Runtime stack

| Concern | FOSS option | Google Cloud option | What tips it |
|---|---|---|---|
| Ingestion with document versioning and supersession | | | |
| Retrieval filtered by role, study, blinding status | | | |
| Reranking and citation-grounded generation | | | |
| Faithfulness / citation-accuracy evaluation, run on every change | | | |
| Immutable Q&A audit record, attributable to a user | | | |
| Change control: prompt and model versions, approvals, rollback | | | |
| Data residency and "no training on our documents" guarantees | | | |
| Screening for leaked blinded data in responses | | | |
| Validation evidence package: what the platform gives you for free | | | |
| Cost at 800 users × 15 queries/day | | | |

Products you may name on either side are listed with their sources in
[README — Sources](README.md#sources). Anything not on that list is `⚠` in your answer until you
fetch it.

## Related lessons

[04 RAG](../course/04-rag-vector-search.md) · [07 Evaluation](../course/07-evaluation.md) ·
[09 Troubleshooting & observability](../course/09-troubleshooting-observability.md).
Objectives 3.2 · 4.1 · 4.2 · 5.2.
