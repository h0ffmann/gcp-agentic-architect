# 01 — Refactor a healthcare RAG assistant

Time box: 45 min. Deliverable: `interviews/answers/01-YYYYMMDD.md` with `## Part A`, `## Part B`,
`## Part C`. Review: `use the design-reviewer agent on <that file>`.

## Setting

You are the senior engineer a consulting firm has put on a healthcare client. The client runs a
network of outpatient clinics. Six months ago a contractor built an internal assistant that lets
clinic staff ask questions over patient records, discharge summaries and internal care
protocols. It works — people use it daily — and it is about to be audited. The interviewer plays
the client's engineering lead. They give you the code below and ask you to walk them through
what you would change, in what order, and why.

## The system as found

```python
import os, requests

SYSTEM = """You are a helpful clinical assistant. Answer the user's question using the
documents below. Documents:
{docs}
"""

def fetch_documents(question: str) -> list[str]:
    rows = db.execute("SELECT body FROM documents")           # every document, every time
    return [r.body for r in rows if any(w in r.body for w in question.split())]

def call_llm(prompt: str) -> str:
    r = requests.post(LLM_URL, json={"prompt": prompt, "max_tokens": 1024},
                      headers={"Authorization": f"Bearer {os.environ['LLM_KEY']}"})
    return r.json()["text"]

def answer(question: str) -> str:
    docs = fetch_documents(question)
    prompt = SYSTEM.format(docs="\n---\n".join(docs)) + "\nQuestion: " + question
    while True:
        out = call_llm(prompt)
        if "FINAL:" in out:
            return out.split("FINAL:")[1]
        prompt += "\n" + out + "\nContinue."
```

Things the interviewer will confirm if you ask: the caller is a web form behind the clinic's
SSO; `answer()` receives only the question string; `documents` has ~2 M rows across all clinics
with columns `clinic_id`, `patient_id`, `doc_type`, `created_at`, `body`; the LLM is a hosted
model reached over HTTPS; there are no tests, no traces, no eval set; the spec the contractor
worked from said "must handle PHI appropriately" and nothing else.

## Constraints

- Patient data is protected health information (PHI) under the client's jurisdiction; the
  auditor will ask who can see what, and whether the model provider ever receives PHI.
- A nurse must only see records from their own clinic; a physician may see their own patients
  across clinics; protocol documents are visible to everyone.
- Median answer today is ~9 s; staff tolerate 5 s.
- No new hires. The client's team is three backend engineers who know Python and Postgres.
- The audit is in eight weeks. The client will pay for infrastructure it can justify, not for a
  platform migration.

## Part A — improve it without changing infrastructure

Same Postgres, same hosted LLM endpoint, same web form. What do you change in the code and the
prompt, and in what order? Say what each change buys and what it costs. Name the first thing
you would ship in week one.

## Part B — you may change infrastructure

You may add services, replace the retrieval layer, put something between the app and the model,
change where the model runs. Draw the target system. Say what moves the client from "passes the
audit" to "would pass it again in a year". Be explicit about what you would *not* add.

## Part C — FOSS stack vs Google Cloud Agent Runtime stack

Fill the table. One line per concern; add rows you think are missing. The last column is the
one that matters: what fact about the client tips the choice.

| Concern | FOSS option | Google Cloud option | What tips it |
|---|---|---|---|
| Orchestration / agent loop | | | |
| Retrieval store, filtered by clinic and patient | | | |
| Reranking | | | |
| PHI detection and redaction before the model | | | |
| Per-user authorization, propagated to retrieval | | | |
| Agent identity / credentials to downstream tools | | | |
| Prompt/response screening (injection, leaks) | | | |
| Traces, evals, regression set | | | |
| Where the model runs, and who sees PHI | | | |
| Cost model at 400 staff × 30 questions/day | | | |

Products you may name on either side are listed with their sources in
[README — Sources](README.md#sources). Anything not on that list is `⚠` in your answer until you
fetch it.

## Related lessons

[04 RAG](../course/04-rag-vector-search.md) · [05 MCP, Registry, Identity](../course/05-mcp-registry-identity.md) ·
[10 Security & governance](../course/10-security-governance.md). Objectives 3.2 · 5.1 · 5.2.
