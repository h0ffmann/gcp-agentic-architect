# interviews — system-design questions for agentic / RAG roles

Whiteboard-style questions of the kind consulting firms and enterprise AI teams ask in a 45–60
minute round: a system that exists and is wrong, a regulated domain, and three follow-ups —
fix it in place, fix it with new infrastructure, and choose a stack. The MCQ bank in
`questions/` teaches product recognition; this folder teaches the conversation.

**Off the study calendar.** Nothing here is on [`STUDY-CALENDAR.md`](../STUDY-CALENDAR.md) and
nothing here should displace a lesson before Sept 30. Use it the week after the MCQ, or when an
interview lands.

## The questions

| # | File | Domain | Constraint that drives the design | Lessons |
|---|---|---|---|---|
| 01 | [`01-healthcare-rag-refactor.md`](01-healthcare-rag-refactor.md) | Healthcare consulting | PHI, per-user access, unbounded agent loop | 04 · 05 · 10 |
| 02 | [`02-bank-fraud-kyc-agent.md`](02-bank-fraud-kyc-agent.md) | Retail bank | PCI + LGPD, sub-second decisions, analyst HITL | 06 · 07 · 10 |
| 03 | [`03-insurer-claims-documents.md`](03-insurer-claims-documents.md) | Insurer | Document extraction, adjuster HITL, audit trail | 04 · 07 · 10 |
| 04 | [`04-retail-multitenant-support.md`](04-retail-multitenant-support.md) | Retail marketplace | Tenant isolation, A2A to vendor agents, unit cost | 05 · 06 · 08 |
| 05 | [`05-pharma-clinical-search.md`](05-pharma-clinical-search.md) | Pharma / clinical | GxP validation, citation faithfulness, immutable audit | 04 · 07 · 09 |

Every file has the same skeleton: **Setting · The system as found · Constraints · Part A · Part B ·
Part C · Related lessons**. There is no answer section anywhere in this folder — on purpose.

## How to run one

1. Start a 45-minute timer. Read the question once; do not open the lessons.
2. Write your answer in `interviews/answers/NN-YYYYMMDD.md`. Headings `## Part A`, `## Part B`,
   `## Part C` (the Part C table filled in). Prose, bullet lists, ASCII diagrams — whatever you
   would say out loud. Answers are tracked; commit them or not.
3. Ask for a review:

   ```
   use the design-reviewer agent on interviews/answers/01-20260922.md
   ```

   The agent scores seven axes 1–5, names three strengths, three gaps *as the follow-up question
   an interviewer would ask*, and a verdict. It holds the rubrics and shows you only what you
   missed. It never writes files.
4. Redo the gaps in a second file the next day. Compare.

## Sources

Every Part C table is answered from these. Google Cloud names change; the exam and an interviewer
both want the current one. Fetched 2026-09-22 unless marked.

| Side | Product | One line | Mark |
|---|---|---|---|
| GCP | [Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime) | formerly Agent Engine; managed runtime with sessions, memory bank, code/computer-use sandboxes; API resource still `ReasoningEngine` | (v) |
| GCP | [Agent Retrieval](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview) | formerly Vector Search 2.0; vector + payload filtering in one store; usage-based or resource-based pricing | (v) |
| GCP | [Model Armor](https://docs.cloud.google.com/model-armor/overview) | screens prompts and responses: injection/jailbreak, responsible-AI categories, Sensitive Data Protection for PII; skips files over the size cap | (v) |
| GCP | [Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) | ingress (Client-to-Agent) and egress (Agent-to-Anywhere) policy point; SPIFFE identity, IAM, Model Armor callouts, tool-combination rules | (v) |
| GCP | [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) | per-agent SPIFFE identity; PAB policies cap access regardless of other grants; end-user credentials encrypted at the auth manager | (v) |
| GCP | [Agent Registry](https://docs.cloud.google.com/agent-registry/automatic-registration) | catalog of agents, tools, MCP servers; auto-registration from Agent Runtime | (v) 2026-09-15, lesson 05 |
| GCP | RAG Engine · Agent Search (ex Vertex AI Search) · Cloud Run · GKE · Sensitive Data Protection (own doc) | in scope, not fetched for this folder | ⚠ |
| FOSS | [ADK](https://github.com/google/adk-python) | agent framework; local runner, eval, `adk deploy`; Ollama via LiteLLM | (v) 2026-09-15, lesson 02 |
| FOSS | [Qdrant](https://github.com/qdrant/qdrant) | vector DB; JSON payload filters (`must`/`should`/`must_not`) combined with vector search | (v) |
| FOSS | [pgvector](https://github.com/pgvector/pgvector) | vectors in Postgres; `WHERE` + `ORDER BY embedding <->`; partitioning for tenants; RLS applies | (v) |
| FOSS | [Presidio](https://github.com/microsoft/presidio) | PII detection/redaction/anonymisation; pluggable custom recognizers | (v) |
| FOSS | [OPA](https://github.com/open-policy-agent/opa) | general policy engine, Rego; authorization decisions outside app code | (v) |
| FOSS | [vLLM](https://github.com/vllm-project/vllm) | self-hosted inference; OpenAI-compatible and Anthropic Messages API servers | (v) |
| FOSS | [Langfuse](https://github.com/langfuse/langfuse) | MIT, self-hostable; tracing + evals | (v) |
| FOSS | [Phoenix](https://github.com/Arize-ai/phoenix) | OpenTelemetry-based LLM tracing, evals, datasets; self-hosted | (v) |
| FOSS | [Ragas](https://github.com/explodinggradients/ragas) | RAG/LLM-app evaluation metrics and test-set generation | (v) |
| FOSS | [MCP](https://modelcontextprotocol.io) · [A2A](https://a2a-protocol.org/latest/) | tool and agent-to-agent protocols | (v) 2026-09-15, lessons 05–06 |

## Ground rules

- Same source rule as the rest of the repo: a product claim in a question is `(v)` with a fetched
  URL and date, or `⚠`. FOSS entries link to their repo.
- No real interview content beyond what a candidate volunteered about their own round, and never
  a name, a firm, or a client. 01 is anonymised from a friend's debrief; 02–05 are written.
- Nothing here is copied from a paid course or an interview-prep site.
