# EXAM-BRIEF — PR000340 Professional Agentic Architect (beta)

Verified 2026-09-15 against the official guide and FAQ. Markers: `(v)` fetched and checked that
day, with source; `⚠` not yet verified — Prompt 1 owes it a fetch. Recheck any `(v)` older than
two weeks; this product family renames fast.

Sources (v):
- Guide (PDF): <https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf>
- Cert page: <https://cloud.google.com/learn/certification/agentic-architect>
- FAQ: <https://support.google.com/cloud-certification/answer/18080541>
- Learning path: <https://www.skills.google/paths/4525>

## Facts that drive the plan (v)

- Hybrid certification: proctored multiple-choice exam (Pearson) **and** hands-on labs in Google
  Skills. Both must pass. Passing the MCQ alone does not certify.
- MCQ: 3 hours, English only, window **Sept 8 – Sept 30, 2026**, registration closes Sept 30.
  Beta price $120 (40% off the $200 GA price). Beta exams can be up to twice as long as GA.
- Labs: released only to candidates who pass the MCQ; email when available (**late October**);
  window late October – December; estimated **< 5 hours** to complete; run in an active cloud
  environment hosted by Google Skills.
- Results for the MCQ: late October. Beta participants notified 4–6 weeks after both windows close.
- GA of the exam: mid-November 2026. Credential valid **1 year** (not 2), continuous-education path.
- Recommended experience: 3+ years cloud, 1+ year building agentic solutions on Google Cloud.
- No official practice exam for the beta was found on the cert page (v, 2026-09-15). Sample
  questions: none listed. The bank in `questions/` is the substitute.

## Cost plan

| Item | Amount | Status |
|---|---|---|
| Beta exam fee | $120 + tax | committed |
| Travel to test centre | own budget | committed |
| Google Cloud, before Sept 30 | $0 target; free tier + new-customer credits only; **hard ceiling $25** | opt-in, gated |
| Google Cloud, lab block (after results) | credits first; ceiling set then | later |
| Paid courses / question banks | none by default; Prompt 1 ranks candidates by value and refund policy | decide D1 |

Console time before Sept 30 is for *recognising* products (names, screens, decision points), not
for drills. Anything that provisions a billable resource needs an explicit human go-ahead.

## The guide as a checklist

Tick when the lesson is done, the case runs, and the section's quiz is ≥ 85% on `just quiz --weak`.

### Section 1 — Building agents using low-code tools (~13%)
**1.1 Configuring agentic workflows and behavior using low-code tools**
- [ ] State-based workflows (pages, transition routes, event handlers) with Gemini Enterprise tools (Agent Designer, CX Agent Studio)
- [ ] System instructions and in-console prompt templates (few-shot, chain-of-thought) in Agent Designer / CX Agent Studio

**1.2 Connecting enterprise data to Gemini Enterprise**
- [ ] Securely connect and query enterprise proprietary data (Gemini Enterprise, Agent Search)
- [ ] Ingest and process unstructured multimodal data (video, audio, images) into the workflow

### Section 2 — Using coding agents for application development (~17%)
**2.1 Using coding agents effectively**
- [ ] Configure coding agents with MCP servers, custom skills, tool access (Antigravity, Claude Code on Google Cloud)
- [ ] Coding agents in secure sandboxes (GKE, Cloud Workstations, Antigravity)
- [ ] Refactor source, optimise runtimes, patch application-layer vulnerabilities with coding agents

**2.2 Customizing coding agents for enterprise workflows**
- [ ] Skills, plugins, extension hooks, rules, subagents in Antigravity
- [ ] Augment Antigravity with Agents CLI to build, scale, govern, optimise deployed agents

### Section 3 — Developing custom agents (~33%)
**3.1 Designing and building agentic workflows in code**
- [ ] Model selection: LLM vs SLM, self-hosted vs SaaS, OSS vs proprietary — cost, security, architecture
- [ ] Build custom agents with open-source libraries (ADK)
- [ ] Sessions and memory (Agent Platform Memory Bank, managed sessions)
- [ ] Skills via Agents CLI (plugins; agent vs human mode)

**3.2 Integrating enterprise domain knowledge**
- [ ] RAG pipelines and vector retrieval: embedding models, similarity scoring, reranking; Vector Search, Agent Retrieval
- [ ] Agent permissions (Agent Identity)
- [ ] Agent Registry and Google Cloud MCP Servers for prebuilt/custom capabilities (managed DB integration layers, API integrations, MCP to third-party SaaS and remote servers)

**3.3 Orchestrating and coordinating agentic workflows**
- [ ] Agentic protocols: MCP and A2A
- [ ] Multi-agent handoffs: parallel, sequential, graph workflows — with Agent Identity, Agent Registry, Agent Runtime, agent policies

### Section 4 — Evaluating and deploying agentic workflows (~22%)
**4.1 Evaluating agents in development and production**
- [ ] Test sets: golden data, prompts, edge cases
- [ ] Continuous evaluation pipelines for tool execution against success criteria
- [ ] Choosing the framework: ADK evalset, Agent Platform Gen AI evaluation service, custom autoraters
- [ ] Evaluate against a golden dataset for response and retrieval quality (ADK)

**4.2 Deploying and scaling production workloads**
- [ ] Runtime selection by use case, requirements, cost: Agent Runtime vs Cloud Run vs GKE
- [ ] Troubleshoot: drift, tool-invocation latency, reasoning loops, system failures
- [ ] Monitor and optimise: logic errors, latency bottlenecks, hallucinations, cost

### Section 5 — Securing and governing agentic workflows (~15%)
**5.1 Configuring agent security and governance**
- [ ] Authentication and secure tool execution (agent-to-tool OAuth 2.0)
- [ ] Principal access boundary (PAB) policies via Agent Identity
- [ ] Agent Gateway to monitor traffic and track agents
- [ ] Governance and policy enforcement (Agent Registry, Model Armor)

**5.2 Implementing secure agent behavior and execution**
- [ ] Safety frameworks and guardrails (Agent Gateway, Model Armor, HITL)
- [ ] Secure data access and identity propagation (Agent Gateway, Agent Registry)

## In-scope tools — one line each

The guide lists 28 tools. Umbrella product: **Gemini Enterprise Agent Platform**, organised as
Build / Scale / Govern / Optimize (v — docs.cloud.google.com/gemini-enterprise-agent-platform/overview).
Doc root: `https://docs.cloud.google.com/gemini-enterprise-agent-platform/`.

| Tool (guide name) | What it is today | Formerly / note | Mark |
|---|---|---|---|
| Agent Development Kit (ADK) | Open-source, code-first framework (Python, Java) for agents, tools, runners, multi-agent orchestration; runs locally (`adk web` on :8000) | — | (v) via Memory Bank quickstart |
| Agent evaluation | ADK: `adk eval` on `.evalset.json`, criteria incl. tool-trajectory match, `response_match_score` (default 0.8), rubric-based *_v1; `safety_v1` and trajectory-quality delegate to Agent Platform Eval SDK (needs project); `adk conformance` for golden-baseline regression | Optimize pillar | (v) adk-docs/evaluate |
| Agent Gateway | Central policy-enforcement point for agent traffic; egress (Agent-to-Anywhere) and ingress (Client-to-Agent) modes; IAP/IAM authorization policies; delegates content checks to Model Armor; looks up Agent Registry | Agent Runtime and Gemini Enterprise route through it automatically | (v) govern/gateways/agent-gateway-overview |
| Agent Identity | Managed per-agent identity (SPIFFE ID) replacing shared service accounts; mTLS + DPoP bound tokens; PAB policies; audit logs show agent and user; auth manager encrypts end-user credentials | cannot hold legacy bucket roles | (v) govern/agent-identity-overview |
| Agent Registry | Central catalog of agents, tools, MCP servers; automatic registration from Agent Runtime; A2A skills extracted; manual registration for external hosts | doc root also docs.cloud.google.com/agent-registry | (v) agent-registry/automatic-registration |
| Agent Retrieval and Vector Search 1.0 | **Agent Retrieval = formerly Vector Search 2.0**: collections of JSON objects, filter by payload + vector, built-in embedding population or BYOE, usage-based or resource-based pricing. **Vector Search 1.0** = the earlier ANN index product, still in scope | know both names | (v) build/vector-search-2/overview |
| Agent Runtime | Fully managed runtime to deploy/scale agents; provides Sessions, Memory Bank, code execution sandbox, Example Store (preview); API still `client.agent_engines.*`, resource type `reasoningEngines` | **formerly Agent Engine** (v) | (v) scale/, build/runtime |
| Agent Search | Enterprise search/grounding over connected data for Gemini Enterprise | **formerly Vertex AI Search** (v, guide) | ⚠ fetch product page |
| Agentic protocols (A2A, MCP) | A2A: agents declare capabilities/skills (a2a-protocol.org); MCP: tool/server protocol | — | (v) A2A ref in Registry docs; ⚠ MCP spec version |
| Agents CLI in Agent Platform | `agents-cli` binary: scaffolds projects (pyproject + `agents-cli-manifest.yaml`), installs skills to `~/.agents/skills` (visible to Antigravity), skills for scaffold/eval/deploy and `agent-platform-skill-registry` | needs Python 3.11+, Node, uv | (v) community tutorial — ⚠ official doc |
| Antigravity (CLI, SDK, App) | Agent-first dev platform: desktop app, CLI `agy`, SDK. CLI is Gemini CLI's successor (consumer Gemini CLI ended 2026-06-18) and keeps Agent Skills, Hooks, Subagents, Extensions; reads AGENTS.md/GEMINI.md as rules; skills = SKILL.md dirs (`.agents/skills` project, global under `~/.gemini/…`); terminal auto-execution modes Request Review / Always Proceed | official docs antigravity.google/docs/cli | (v) Google transition post + codelab |
| Auth Manager (OAuth 2.0) | Manages OAuth flows/credentials for agent-to-tool calls; encrypts end-user creds, decrypted at Gateway | part of Agent Identity story | (v) mention only — ⚠ dedicated doc |
| BigQuery | Data warehouse; tool target / data source | — | known, ⚠ agent-specific features |
| Cloud Run | Serverless containers; ADK deploy target | — | known, ⚠ ADK deploy doc |
| Cloud SQL | Managed relational DB; tool/data source | — | known |
| Cloud Storage | Object storage; ingestion source | — | known |
| Firestore | Document DB; session/state store in samples | — | known |
| Gemini Enterprise | Enterprise agent workspace; low-code Agent Designer, connectors, Agent Search | umbrella for Section 1 | ⚠ |
| Gemini LLMs | Gemini model family | — | ⚠ current versions/pricing |
| Google Cloud Observability | Cloud Logging + Cloud Trace; Runtime logs under `aiplatform.googleapis.com/ReasoningEngine` | + Topology view | (v) troubleshooting page |
| Google Kubernetes Engine (GKE) | Managed Kubernetes; ADK deploy target; coding-agent sandbox | — | known, ⚠ ADK deploy doc |
| Memorystore for Redis | Managed Redis; cache/short-term state | — | known |
| Model Armor | Screens prompts and responses: prompt injection/jailbreak, responsible-AI filters, Sensitive Data Protection, images. **Floor settings** (project-level) vs **templates** (per request); inspect-only vs INSPECT_AND_BLOCK; 4 MB input cap; document screening only in the Gemini Enterprise integration; if unreachable the request continues unscreened; Gateway needs `roles/modelarmor.calloutUser` + `modelarmor.user` | — | (v) model-armor/overview + integrations |
| MCP servers | Google Cloud MCP Servers (managed) + custom/third-party, registered in Agent Registry | — | ⚠ |
| Model Garden | 200+ foundation models, incl. open weights | Build pillar | (v) agents overview |
| RAG Engine | Managed RAG pipeline service | ⚠ relation to Agent Retrieval | ⚠ |
| Sensitive Data Protection | DLP: detect/de-identify sensitive data; used as a filter inside Model Armor templates | — | (v) via Model Armor docs — ⚠ own doc |
| Skill Registry | Agent Platform registry of reusable skills; accessible via Agents CLI skill `agent-platform-skill-registry` | — | (v) community tutorial — ⚠ official doc |

Also seen in docs and likely to appear as distractors: **Agent Studio** (low-code, Build pillar),
**Agent Garden** (prebuilt samples), **Example Store** (preview, few-shot retrieval),
**Agent Platform Workbench**, **Semantic Governance policies**, **Context-Aware Access**, **IAP**,
**A2UI** (agent-to-UI protocol), **AP2** (Agent Payments Protocol), **Agent Simulation**.

## Prompt 1 owes this file

Fetch and mark `(v)` every `⚠` row above; add the pricing unit and the canonical doc URL per row;
record the learning path's course/lab list against section ids.
