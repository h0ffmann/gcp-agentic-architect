# 04 — RAG: embeddings, Agent Retrieval / Vector Search, RAG Engine, reranking

**Exam objectives:** 3.2 · section weight 33%. Quiz: `just quiz --lesson 04`. Case: `just case 04`.

## On the exam

- Names: **Agent Retrieval = formerly Vector Search 2.0** — collections of JSON objects, filter by vector *and* payload, built-in embedding population or bring-your-own embeddings, usage-based or resource-based pricing. **Vector Search 1.0** = the earlier ANN index (still listed). **RAG Engine** = managed end-to-end RAG pipeline. **Agent Search** (formerly Vertex AI Search) = enterprise search/grounding over connected data (Section 1).
- Pipeline questions test where quality is lost: chunking → embedding model choice → similarity scoring (cosine/dot) → top-k → **reranking** → prompt assembly. "Right docs retrieved but wrong ones used" → reranker. "Relevant docs never retrieved" → embeddings/chunking/hybrid search.
- Evaluation of retrieval is separate from evaluation of the answer (lesson 07).
- Cost tells: small workload → usage-based pricing; tuned performance → resource-based.

## Read (fetched 2026-09-15)

- [Agent Retrieval (formerly Vector Search 2.0)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview) (v).
- [Google-Cloud-AI/agent-platform samples](https://github.com/Google-Cloud-AI/agent-platform) — names RAG Engine, Agent Search, Vector Search 2.0 side by side (v).

## Verified today

| Product | What it does | Limits / notes | Mark |
|---|---|---|---|
| Agent Retrieval | Unified vector + payload storage and filtering; collections; BYOE or built-in embeddings; indexes for scale | two pricing models | (v) |
| Vector Search 1.0 | Earlier ANN index product; Agent Retrieval keeps its performance | still in scope | (v) named in AR overview |
| RAG Engine | Managed RAG over enterprise datasets | ⚠ details | ⚠ |
| Agent Search | Semantic search engines over your data (ex Vertex AI Search) | Section 1 | ⚠ |

## Case — `cases/04-rag-rerank`

Runs with no Google Cloud account and no dependencies beyond Python. Read the source; it is the concept reduced to 40 lines.

## marola port

marola's `knowledge/` store (MIP-0055) is the local Agent Retrieval; add a `Reranker` step to `KnowledgeStore.query` with a deterministic lexical reranker and record retrieval@k in the benchmark ledger. Cloud impl: Agent Retrieval collection as a `KnowledgeStore`.

## Quiz

`just quiz --lesson 04` — questions tagged `lesson: "04"` in `questions/bank.jsonl`.

## Flashcards

`questions/cards/04.tsv` (front TAB back). Import into Anki as basic cards.
