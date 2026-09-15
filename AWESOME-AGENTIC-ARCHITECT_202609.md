# Awesome Agentic Architect (2026-09)

Curated resources for **Google Cloud Certified · Professional Agentic Architect** (PR000340, beta).
Every entry was fetched on 2026-09-15 unless marked `⚠` (found but not opened, or only a
secondary source). Dead links are dropped, not kept. Ranked within sections by value for a
15-day, full-time candidate preparing for the multiple-choice part.

## 1. Official

- (v) [Exam guide (PDF)](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf) — the syllabus; five sections at 13/17/33/22/15 and the 28-tool in-scope list. Read it twice; `EXAM-BRIEF.md` is this file as a checklist.
- (v) [Certification page](https://cloud.google.com/learn/certification/agentic-architect) — registration, both components, beta notes.
- (v) [FAQ](https://support.google.com/cloud-certification/answer/18080541) — the dates: MCQ Sept 8–30, labs late Oct–Dec only after passing, $120 beta, 3 h, 1-year validity, GA mid-November.
- (v) [How beta exams work](https://support.google.com/cloud-certification/answer/9750304) — up to 2× GA length, no practice test, results after the window.
- (v) [Google Skills learning path (13 activities)](https://www.skills.google/paths/4525) — login-gated; Google's own note: *it does not cover all topics in the exam guide*. Partners: [path 4531](https://partner.skills.google/paths/4531).
- (v) [Agentic AI on Google Cloud path](https://www.skills.google/paths/3273) — Gemini Enterprise intro + ADK multi-agent build/secure; the older, broader path.
- Sample questions: **none published for the beta** (checked cert page 2026-09-15). `questions/` is the substitute.

## 2. Google Skills labs and codelabs, by exam section

The 13 path activities need a login to enumerate; do that on D1 and fill this table. Lab credits
are needed for most labs; the free monthly credits on Google Skills are the first budget.

| Section | Activity | Covers | Minutes | Credits |
|---|---|---|---|---|
| 2.2 | (v) [Codelab: Authoring Google Antigravity Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills) | SKILL.md structure, rules vs skills vs workflows | ~60 | none |
| 3.1/4.1 | (v) [ADK eval starter (workshop repo)](https://github.com/cuppibla/adk_eval_starter) | `adk web`, `adk eval`, Cloud Run deploy | ~90 | GCP project |
| 3.1 | (v) [Memory Bank quickstart with ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank/adk-quickstart) | Sessions + Memory Bank, local then Runtime | ~45 | Runtime instance |
| 3.2 | ⚠ [Vector Search 2.0 quickstart notebook](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview) | collections, embeddings, BYOE | ~45 | usage-based |
| all | ⚠ path 4525 activities 1–13 | fill on D1 | | |

## 3. Docs per in-scope tool

Root: [Gemini Enterprise Agent Platform docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview) (v) — four pillars Build / Scale / Govern / Optimize; read the overview first, it names every product on the exam.

| Tool | Canonical doc | Note |
|---|---|---|
| ADK | (v) [adk-docs](https://google.github.io/adk-docs/) · [adk-python](https://github.com/google/adk-python) | `adk web`, `adk eval <agent> <evalset>`, `adk conformance`, `adk deploy docker|cloud_run|agent_engine` |
| Agent evaluation | (v) [ADK evaluate](https://google.github.io/adk-docs/evaluate/) · [criteria](https://google.github.io/adk-docs/evaluate/criteria/) | tool-trajectory match, `response_match_score` (default 0.8), rubric-based *_v1, `safety_v1` delegates to Agent Platform Eval SDK and needs a GCP project |
| Agent Gateway | (v) [overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) · [set up](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway) · [troubleshoot](https://docs.cloud.google.com/gemini-enterprise-agent-platform/troubleshooting/troubleshoot-agent-gateway) | egress (Agent-to-Anywhere) vs ingress (Client-to-Agent); IAP dry-run first; registry lookups |
| Agent Identity | (v) [overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) | SPIFFE ID, mTLS+DPoP, auth manager, no legacy bucket roles |
| Agent Registry | (v) [automatic registration](https://docs.cloud.google.com/agent-registry/automatic-registration) · manual registration linked from it | Runtime = automatic, A2A skills extracted |
| Agent Retrieval / Vector Search | (v) [Agent Retrieval (formerly Vector Search 2.0)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/overview) | collections of JSON, built-in or BYO embeddings, usage- or resource-based pricing; **Vector Search 1.0** is the older index product the guide also lists |
| Agent Runtime | (v) [runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/runtime) · [scale](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) | formerly Agent Engine; API `client.agent_engines.*`; Sessions, Memory Bank, code execution, Example Store (preview) |
| Sessions / Memory Bank | (v) [Memory Bank](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/memory-bank) · [sessions with ADK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions/manage-with-adk) | CreateSession → AppendEvent → GenerateMemories; scope by user id |
| Agent Search | ⚠ formerly Vertex AI Search / Gen AI App Builder — find the current landing page | named in [samples repo](https://github.com/Google-Cloud-AI/agent-platform) |
| A2A / MCP | (v) [a2a-protocol.org](https://a2a-protocol.org/latest/) (linked from Registry docs) · ⚠ [modelcontextprotocol.io](https://modelcontextprotocol.io) | A2A = agent↔agent, MCP = agent↔tool |
| Agents CLI | ⚠ official doc not surfaced by search; (v) [community tutorial](https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d) | `agents-cli` binary, manifest, skills to `~/.agents/skills` |
| Antigravity | (v) [antigravity.google/docs/cli](https://antigravity.google/docs/cli) (URL from a tracked issue) · (v) [Gemini CLI → Antigravity CLI transition post](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) | `agy`; keeps Agent Skills, Hooks, Subagents, Extensions; reads AGENTS.md/GEMINI.md as rules; `.agents/skills` project scope |
| Model Armor | (v) [overview](https://docs.cloud.google.com/model-armor/overview) · [Agent Gateway integration](https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration) · [Agent Platform integration](https://docs.cloud.google.com/model-armor/model-armor-vertex-integration) | floor settings vs templates; inspect-only vs INSPECT_AND_BLOCK; 4 MB limit; document screening only in Gemini Enterprise; fails open if unreachable |
| Sensitive Data Protection | ⚠ | invoked through Model Armor filters |
| Skill Registry | ⚠ official doc not surfaced | reachable via Agents CLI skill `agent-platform-skill-registry` |
| Gemini Enterprise / Agent Designer / CX Agent Studio | ⚠ | Section 1; console-only |
| Cloud Run · GKE · BigQuery · Cloud SQL · Firestore · Cloud Storage · Memorystore · Observability | known products; agent-specific: ADK deploy targets, Runtime logs under `aiplatform.googleapis.com/ReasoningEngine` (v) | |

## 4. Open source you can run without GCP

- (v) [google/adk-python](https://github.com/google/adk-python) — `pip install google-adk`; local runner, eval, docker deploy. Point it at Ollama/open weights via LiteLLM for a zero-cloud loop.
- (v) [Google-Cloud-AI/agent-platform](https://github.com/Google-Cloud-AI/agent-platform) — official sample index; also names A2UI and AP2 (possible distractors).
- (v) [a2a-protocol.org](https://a2a-protocol.org/latest/) — spec and samples; two local agents exchanging agent cards is `cases/06`.
- ⚠ [modelcontextprotocol.io](https://modelcontextprotocol.io) — spec + reference servers (Node); `cases/05` is a stdio MCP-shaped server in stdlib Python.
- Model Garden open weights via Ollama — the model-selection lesson runs on them.

## 5. Courses with exam questions — ranked

1. (v) [Udemy: [Practice Test] Google Cloud Professional Agentic Architect (Sayyam)](https://www.udemy.com/course/gcp-google-cloud-professional-agentic-architect-practice-test-exam/) — the only one found that targets **this** exam; two weeks old; claims reference links per answer. Unknown question count; Udemy has a 30-day refund. Buy on sale only; use as a second mock source after your own bank, and cross-check every answer against docs (it is not Google's material).
2. Everything else in search is a different exam relabelled — Microsoft AB-100, NVIDIA NCP-AAI, Claude Certified Architect. Useful only for question *style* practice on generic agent topics (RAG, HITL, orchestration); their product answers are wrong for Google.
3. No Whizlabs / official practice exam found for this beta.

## 6. Architecture reading

- (v) Agent Platform overview (above) — the taxonomy the exam uses.
- (v) [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) — the clearest single page on how Identity, Registry, Gateway, Model Armor and IAM compose.
- (v) [ADK evaluate: why evaluate agents](https://google.github.io/adk-docs/evaluate/) — trajectory vs response evaluation, golden baselines, conformance.
- ⚠ Google's agent whitepapers and the well-architected generative-AI pillar — locate on D1.

## 7. Community

- (v) [Model Armor release notes](https://docs.cloud.google.com/model-armor/release-notes) — the pattern for every product: read release notes for renames and GA dates.
- (v) [google/adk-python issues/discussions](https://github.com/google/adk-python/discussions) — real eval and deploy failure modes.
- ⚠ Google Cloud blog "agentic" tag, Google Developers Blog.

## 8. Similar labs

- (v) [dnacenta/claude-certified-architect](https://github.com/dnacenta/claude-certified-architect) — a public, runnable exam-prep repo with a study plan and PDF built from markdown in CI; closest in spirit to this one.
- (v) [iamaanahmad/everything-antigravity](https://github.com/iamaanahmad/everything-antigravity) — agents, skills, hooks, rules, MCP configs for Antigravity 2.0; useful to *see* the customisation types Section 2.2 names.
- (v) [eyupece/adk-workshop-guide](https://github.com/eyupece/adk-workshop-guide) — a runnable ADK eval workshop (Turkish/English commands).

## Digest

`scripts/awesome_digest.py` proposes GitHub candidates for this list from its cached search
queries; it never edits this file. Run `just quality` to refresh the cache when network exists.
