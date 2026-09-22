# 03 — Claims intake from documents, at a property insurer

Time box: 45 min. Deliverable: `interviews/answers/03-YYYYMMDD.md` with `## Part A`, `## Part B`,
`## Part C`. Review: `use the design-reviewer agent on <that file>`.

## Setting

A property-and-casualty insurer receives ~3 000 claims a day as email attachments: scanned
forms, photos, PDF invoices, police reports, occasionally a 40-page engineering assessment. An
intake team of 25 people keys the relevant fields into the claims system and routes each claim to
an adjuster. A vendor sold the insurer a "document AI agent" a year ago; it handles about half
the volume and the intake team fixes the rest. The interviewer is the claims-technology director.
The vendor contract is up for renewal in three months and they want an in-house design to compare
against it.

## The system as found

- A nightly batch: attachments → OCR → one long prompt per claim ("extract the following 31
  fields as JSON") → fields written straight into the claims system with `source = "AI"`.
- No confidence per field. A claim is either fully written or the whole claim is dropped to the
  manual queue when the JSON fails to parse.
- The prompt contains six worked examples. Nobody knows which lines of business they cover.
- Adjusters have found claims where the AI-written policy number belonged to a different
  customer with a similar name. Three of those were paid.
- There is no record of what the model saw; the attachments are kept, the OCR text is not.

## Constraints

- Every field that reaches a payment decision needs a provenance trail the auditor can follow
  back to a page and a region of a document.
- Intake staff are the reviewers; their queue must not grow. Adjusters' time is the most
  expensive resource in the building.
- Lines of business differ: motor, home, commercial; the same field name means different things.
- Some documents contain third-party personal data (the other driver, a tenant) that the insurer
  may store but must not use for anything else.
- The insurer runs one cloud and has a data-platform team; no ML team.

## Part A — improve it without changing infrastructure

Same batch, same OCR, same model, same claims system. What do you change in how the model is
asked and how its output is trusted so that the wrong-customer payments stop this month? Say
what you would measure before and after.

## Part B — you may change infrastructure

Design the target intake pipeline. Show where a human looks and at what, per field or per claim;
show how a paid claim is traced back to a document region; show how motor and commercial stay
separate. Say what would make you keep the vendor instead.

## Part C — FOSS stack vs Google Cloud Agent Runtime stack

| Concern | FOSS option | Google Cloud option | What tips it |
|---|---|---|---|
| Orchestration: classify → extract → validate → route, per line of business | | | |
| Structured output with per-field confidence and provenance | | | |
| Retrieval of policy and prior-claim context to validate a field | | | |
| Human review queue: per-field, ordered by risk × confidence | | | |
| Third-party PII: detect, tag, restrict | | | |
| Evaluation set built from the intake team's corrections | | | |
| Traces and the "what did the model see" record | | | |
| Batch vs event-driven; what a 10× storm day does | | | |
| Cost per claim vs the vendor's price | | | |

Products you may name on either side are listed with their sources in
[README — Sources](README.md#sources). Anything not on that list is `⚠` in your answer until you
fetch it.

## Related lessons

[04 RAG](../course/04-rag-vector-search.md) · [07 Evaluation](../course/07-evaluation.md) ·
[10 Security & governance](../course/10-security-governance.md). Objectives 3.2 · 4.1 · 5.1.
