# Prompt series — `gcp-agentic-architect` (Google Cloud Professional Agentic Architect, beta)

> Plan of record, formerly `gt.md`. The prompts are kept as written; where the repo outgrew one
> (Prompt 5's nix-config lab, Prompt 6's publications pipeline), a "Status" note under that
> prompt says what was actually built.

Not one prompt. Seven sessions, one deliverable each, in the same "one feature, one session"
discipline marola already enforces (`/clear`, `/rename` to the branch, `just pr`). Prompt 0 is the
skeleton every later prompt pushes into; Prompts 1–6 are independent enough to run in any order
after 0, but the order below is the study order.

## What I verified before writing this (read first — it changes the plan)

- The exam guide is public: five sections, weighted **13 / 17 / 33 / 22 / 15**. The prompts
  below hard-code those weights. Section 3 (custom agents: ADK, sessions/memory, RAG, MCP, A2A,
  Agent Identity/Registry/Runtime) is a third of the exam and gets a third of the course.
- **The certification has two components**: a proctored multiple-choice exam (Pearson) **and
  hands-on labs in Google Skills**. Verified 2026-09-15 (FAQ): the labs unlock **only for
  candidates who pass the MCQ**, by email in late October, window late Oct–Dec, < 5 h. So the
  15 days are MCQ-only; lab prep is a separate block after results. GCP stays opt-in and gated.
- **The beta window closes September 30** — your exam day. Beta exams have no official practice
  test and results arrive weeks after the window closes. Plan for that, don't be surprised by it.
- The in-scope tool list is full of names newer than any model's memory — Antigravity, Agents
  CLI, Agent Runtime (formerly Agent Engine), Agent Search (formerly Vertex AI Search), Vector
  Search 1.0, Agent Gateway, Agent Identity, Skill Registry, Model Armor. Every prompt says: fetch
  the current docs, never write from memory, mark every claim `(v)` or `⚠` the ww3-gpu way.
- GitHub blocks automated browser fetches. Run these in **Claude Code with the three repos cloned
  side by side** (`marola/`, `ww3-gpu/`, `nix-config/`), or attach repomix packs in a browser
  session (you already have `marola-context-full.md`; make `ww3-gpu` and `nix-config/labs`
  packs the same way).

---

## Block A — paste at the top of every session

```text
CONTEXT (identical in every session of this lab)

Who: one candidate, full-time on this for 15 days, exam on 2026-09-30 (beta window closes that
day). Pass on the first attempt without overspending. Treat me as a senior engineer — no
hand-holding, no filler.

Exam: PR000340, Google Cloud Certified – Professional Agentic Architect (beta, English).
Official guide: https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf
Cert page:      https://cloud.google.com/learn/certification/agentic-architect
Two components: Pearson proctored MCQ + hands-on labs in Google Skills.
Sections and weights: 1 low-code (Gemini Enterprise, Agent Designer, CX Agent Studio) 13% ·
2 coding agents (Antigravity, Claude Code on GCP, MCP, sandboxes, Agents CLI) 17% ·
3 custom agents (ADK, LLM/SLM selection, sessions & Memory Bank, RAG/Vector Search/Agent
Retrieval, Agent Identity/Registry/Runtime, MCP + A2A, multi-agent workflows) 33% ·
4 evaluation & deployment (evalsets, Gen AI evaluation service, autoraters, Agent Runtime vs
Cloud Run vs GKE, troubleshooting loops/drift/latency, observability) 22% ·
5 security & governance (OAuth 2.0 via Auth Manager, PAB policies, Agent Gateway, Model Armor,
Sensitive Data Protection, HITL, identity propagation) 15%.

Repos on disk (read before writing anything):
- ./marola        — Scala 3/Kyo/Ollama ocean-intelligence product; local-first, cloud opt-in per
                    integration; MIP process (.claude/skills/mip), docs/AI-103-MAPPING.md and
                    docs/AI-500-MAPPING.md are the exam-mapping precedent; AGENTS.md is law.
- ./ww3-gpu       — the BASELINE for this lab's shape: course/NN-*.md lessons, runnable cases,
                    AWESOME-*_YYYYMM.md curated list, AGENTS_*.md, Nix-pinned toolchain,
                    one-command regression tests, markdown→PDF publications in CI (EN source,
                    PT generated), (v)/⚠ verification markers.
- ./nix-config    — my NixOS/Home Manager flake; labs/<name> holds per-lab devShells/checks
                    (labs/pratico, labs/agentic) and the ai-jail recipes; ww-lab and marola
                    consume it as a flake input. New Nix tooling goes HERE, not in the lab repo.

Target repo: ./gcp-agentic-architect (personal, public). Same house rules as marola's AGENTS.md:
few comments, no attribution banners, Tested:/Cost: trailers, verify-then-claim, no paid cloud
resource without explicit human go-ahead (adapt guard-azure.sh → guard-gcloud.sh: deny
`gcloud ... create|deploy`, `terraform apply`, `adk deploy` unless GCP_ALLOW_DEPLOY=1).

Rules for this session:
1. Fetch, don't recall. Every product claim links its source and carries (v) or ⚠. Product
   names in the exam guide are newer than your training; assume renames and check.
2. Weighted effort: 13/17/33/22/15. Don't give Section 1 the same depth as Section 3.
3. Local-first: anything runnable runs with Ollama/ADK-local/no GCP by default; GCP is a flag.
4. Scenario-style questions ("An architect must… which option…") with a rationale per option,
   not trivia. That is how Google Professional exams are written.
5. Output goes in the repo as files; end with `git status` and the commands you ran.
6. Stop and ask before anything that costs money or takes >30 min of compute.
```

---

## Prompt 0 — Skeleton, calendar, and the honest brief (run first, ~1 session)

```text
[Block A]

TASK: bootstrap ./gcp-agentic-architect as a git repo, modelled on ww3-gpu's layout, empty of
course content but with every file the later sessions will fill.

Deliver:
1. README.md — what this is (a public exam lab: my research, my agentic dev-loop, marola ports),
   the two exam components, the 15-day calendar below, how to run (`nix develop`, `just`).
2. EXAM-BRIEF.md — the exam guide re-typed as a checklist: every 1.1–5.2 bullet as a checkbox,
   the in-scope tool list with one verified line each (what it is TODAY, formerly-called-what,
   doc URL, (v)/⚠). Also: registration facts, beta caveats (no practice exam, delayed results),
   what the Google Skills labs half requires, and a cost plan (free tier, credits, hard ceiling).
3. AGENTS.md — marola's rules ported: phase discipline replaced by "cheap before paid", the
   gcloud guard, commit trailers, (v)/⚠ markers, "fetch don't recall".
4. Layout (empty files with a one-line header each):
   course/00-orientation.md … course/14-mock-exam-2.md (filenames from Prompt 2's outline)
   cases/            runnable local exercises, one dir per lesson
   questions/        JSONL banks + scripts/quiz.py (Prompt 3)
   marola/           the MIP drafts and mapping doc that get upstreamed (Prompt 4)
   publications/     course book + post-exam writeup, EN source, PT generated (Prompt 6)
   AWESOME-AGENTIC-ARCHITECT_202609.md (Prompt 1)
   flake.nix         thin: inputs.nix-config, devShell = nix-config.labs.agentic (Prompt 5)
   justfile          build, quiz, pdf, smoke, jail-claude, guard test
   .github/workflows/ci.yml  flake check + scripts self-tests + pdf build, ubuntu-latest only
5. STUDY-CALENDAR.md — 15 days, full time, in this order and weight:
   D1 orientation + EXAM-BRIEF + AWESOME list (Prompt 1) · D2–3 Section 3a (ADK, LLM selection,
   sessions/memory) · D4–5 Section 3b (RAG, Vector Search, MCP, A2A, multi-agent) · D6 Section 4a
   (evaluation) · D7 Section 4b (deploy, troubleshoot, observability) + read-only console recon ·
   D8 Section 5 · D9 Section 2 · D10 Section 1 · D11 mock exam 1 + weak-spot review · D12
   Sections 3–4 second pass, every ⚠ resolved · D13 marola port session (Prompt 4) as active
   recall · D14 mock exam 2 + flashcards · D15 travel: flashcards only, no new material.
   The Google Skills labs are NOT in this window: they unlock only after passing the MCQ
   (late October) — the calendar gets an "After the MCQ" block for them.
   Each day: reading block, runnable case, 30-question quiz, 20-min spaced-repetition review.
Acceptance: `nix develop -c just smoke` passes on the empty skeleton; CI green; `git log` has
one commit with Tested:/Cost: trailers. Do NOT write lesson content in this session.
```

---

## Prompt 1 — The AWESOME list (D1, ~1 session)

```text
[Block A]

TASK: write AWESOME-AGENTIC-ARCHITECT_202609.md in the sindresorhus/awesome convention, the way
ww3-gpu's AWESOME-WW3_202609.md and marola's MIP-0043 did it: every entry fetched live this
session, one line of why-it-matters, (v) or ⚠, dated. Nothing from memory.

Sections, in this order:
1. Official — exam guide, cert page, FAQ, registration, Google Skills learning path(s) for this
   cert, the official sample/diagnostic questions if any exist for the beta (check; say if not).
2. Google Skills labs and codelabs mapped to exam sections — for each: which 1.1–5.2 bullet it
   covers, minutes, whether it needs credits. This is the labs-half study plan.
3. Docs per in-scope tool (the 27-item list in the guide) — the canonical doc, the quickstart,
   the pricing page. Note every rename (Agent Engine→Runtime, Vertex AI Search→Agent Search).
4. Open-source you can run without GCP — ADK (Python/Java) local run, A2A spec + samples, MCP
   spec + reference servers, ADK evaluation, Model Garden open weights via Ollama.
5. Courses with exam questions — Udemy/Whizlabs/ExamTopics-style/YouTube; for each: does it
   actually target THIS exam or PCA/PMLE relabelled, question count, price, refund policy.
   Rank by value for a 15-day full-time candidate. Flag dump sites as dump sites.
6. Architecture reading — Google's agent whitepapers, ADK design docs, well-architected AI
   pillar, A2A/MCP comparisons, the agent-security papers behind PAB/Agent Gateway.
7. Community — release notes feeds, the ADK GitHub discussions, blogs that track renames.
8. "Similar labs" — 5–10 public repos of people prepping Google AI certs the runnable way.
Also: a `scripts/awesome_digest.py` copying marola's awesome_agentic_digest.py shape (stdlib
only, .tmp cache, --self-test, --json, never edits the doc) pointed at GitHub Search for
"agentic architect" / "adk" / "a2a" candidates. Wire into `just quality`.
Acceptance: every link fetched (list the ones that 404'd and dropped), self-test green.
```

---

## Prompt 2 — The course (D1 outline, then one session per 2–3 lessons)

```text
[Block A]

TASK: write the self-paced course under course/, ww3-gpu style — each lesson a markdown file
with a runnable case under cases/NN-*/ and a `just case NN` recipe. Do the OUTLINE first, stop,
let me approve, then write lessons in the study-calendar order (Section 3 first, not 1).

Outline (fixed; weights drive length — 33% ≈ 5 lessons, 22% ≈ 3, 17% ≈ 2–3, 15% ≈ 2, 13% ≈ 2):
00 orientation — exam mechanics, how to read a Google scenario question, elimination technique
01 LLM/SLM selection: self-hosted vs SaaS, OSS vs proprietary, cost/security/latency matrix (3.1)
02 ADK fundamentals: agents, tools, runners, local run, ADK vs raw SDK (3.1)
03 sessions, state, Memory Bank, managed sessions (3.1) + Agents CLI skills/plugins/human mode
04 RAG on GCP: embeddings, Vector Search 1.0, Agent Retrieval, RAG Engine, reranking (3.2)
05 MCP + Agent Registry + Google Cloud MCP servers + Agent Identity for tools (3.2)
06 multi-agent: sequential/parallel/graph, A2A, handoffs, Agent Runtime, agent policies (3.3)
07 evaluation: evalsets, golden data, Gen AI evaluation service, autoraters, CI eval (4.1)
08 deployment: Agent Runtime vs Cloud Run vs GKE decision table, scaling, cost (4.2)
09 troubleshooting + observability: loops, drift, tool latency, Cloud Trace/Logging (4.2)
10 security: OAuth 2.0/Auth Manager, PAB via Agent Identity, Agent Gateway, Model Armor, SDP (5.1/5.2)
11 coding agents: Antigravity, Claude Code on GCP, MCP config, sandboxes (GKE/Workstations) (2.1/2.2)
12 low-code: Gemini Enterprise, Agent Designer, CX Agent Studio pages/routes/handlers, data connectors, multimodal ingestion (1.1/1.2)
13 mock exam 1 (60 q, timed) — questions/mock-1.jsonl
14 mock exam 2 (60 q, timed) + final review sheet

Every lesson has the same skeleton:
- "On the exam" — the exact 1.x–5.x bullets, weight, and the 5 decisions Google most likely
  tests here (each with the tell-tale phrasing that points to the right product).
- "Read" — 3–6 fetched links from the AWESOME list, with what to skip.
- "Verified today" — a table: product · what it does · limits/quotas · pricing unit · (v)/⚠.
- "Case" — runnable WITHOUT GCP by default (ADK local + Ollama/Gemma via Model Garden weights,
  local vector index, local MCP server, local A2A between two ADK agents); a `--gcp` flag path
  documented but gated. One command, one expected output block, one regression assertion.
- "marola port" — 5–10 lines: which marola trait/MIP this maps to (feeds Prompt 4).
- "Quiz" — 20 scenario questions, 4 options, answer + a rationale per option, tagged with the
  objective id; appended to questions/bank.jsonl (Prompt 3's schema).
- "Flashcards" — 15 one-liners, Anki-importable (tab-separated) under questions/cards/.
Acceptance per session: `just case NN` runs, `just quiz --lesson NN` loads, links fetched.
```

---

## Prompt 3 — Question bank and quiz runner (D1 schema, then grows with each lesson)

```text
[Block A]

TASK: build the question infrastructure marola-style (stdlib-only Python, --self-test, wired
into `just quality`), then seed it.

1. questions/schema.md — JSONL, one object per line: id, section (1.1…5.2), lesson, stem,
   options {A–D}, answer, rationale {A–D} (why each is right/wrong), difficulty, source_url,
   verified (v|⚠), tags. Multi-select allowed (answer as list).
2. scripts/quiz.py — modes: `--lesson NN`, `--section 3`, `--mock N --minutes 120`, `--weak`
   (spaced repetition over .tmp/quiz-history.jsonl, Leitner boxes), `--export-anki`,
   `--stats` (accuracy per objective vs the 13/17/33/22/15 weights → a "predicted score" line
   and the three weakest objectives). No deps beyond the stdlib. --self-test covers scoring,
   Leitner, and malformed lines.
3. Seed 150 questions now across all sections at the exam weights, before lessons exist —
   from the exam guide bullets + fetched docs only; style = Google Professional scenario
   items (a company, a constraint, "what should you do?", one best answer, distractors that
   are real products used wrongly). Mark each with source_url. No copied questions from any
   paid or dump site.
4. questions/mock-1.jsonl and mock-2.jsonl — 60 each, weighted, disjoint from bank.jsonl,
   assembled last (Prompt 2, lessons 13/14) not now; leave a generator `--build-mock N`.
Acceptance: `just quiz --self-test`, `just quiz --section 3` runs a session and writes history,
`just quiz --stats` prints the weighted predicted score. Fail loudly on unknown objective ids.
```

---

## Prompt 4 — Porting to marola, still runnable with no cloud (D13, one MIP session + one tasks session)

```text
[Block A]
Use marola's `mip` skill, then `mip-tasks`. Read docs/AI-103-MAPPING.md, docs/AI-500-MAPPING.md,
docs/ARCHITECTURE.md §5, MIP-0011, MIP-0017, MIP-0039, MIP-0040, MIP-0043, MIP-0055 first.

TASK 4a (MIP session): write MIP-0057 "Google Cloud Agentic Architect coverage: mapping doc,
a `gcp/` opt-in module, and local shapes for the five exam sections". Deliver:
- docs/AGENTIC-ARCHITECT-MAPPING.md, same shape as AI-103-MAPPING.md: every 1.1–5.2 bullet →
  what marola already has (verified, file:line) / what a local-only shape would be / what only
  a real GCP resource can cover (honest gap). Draft mapping to seed from, verify each:
    ADK sequential/parallel/graph agents  → Kyo Recommender pipeline + Reviewer (a 2-agent chain)
    A2A                                    → local JSON-RPC between marola's MCP server and a
                                             second ADK-local agent (case in cases/06)
    MCP servers / Agent Registry           → cli/ MCP tool server + docs/AGENT-SKILLS.md
    Sessions / Memory Bank                 → SightingStore + FileKnowledgeStore; a Session trait
    RAG / Vector Search / reranking        → knowledge/ (MIP-0055), benchmark ledger
    Evaluation, evalsets, autoraters       → MIP-0040 reviewer-judge validation + `just benchmark`
    Model Armor / guardrails / HITL        → MIP-0039 deterministic fact guard, MIP-0022 safety
                                             footer, the water-quality veto in code
    Agent Identity / PAB / Agent Gateway   → ai-jail, .claude/settings.json deny rules,
                                             guard-*.sh hooks, .env masking — the local analogue
    Agent Runtime / Cloud Run / GKE        → MIP-0008 Docker images + smoke test
    Coding agents (Antigravity, Claude Code)→ MIP-0011, MIP-0013, MIP-0017 (already done; cite)
    Low-code (Agent Designer)              → honest gap; nothing local; console-only study
    Observability (Trace/Logging)          → Telemetry trait; local OTLP collector case
- Design of `gcp/` as a fifth sbt module mirroring `azure/`: traits from core, opt-in via
  AppConfig env vars, zero GCP SDK in core/local, `.claude/rules/gcp.md` with the cost gate,
  guard-gcloud.sh alongside guard-azure.sh. Candidates: Gemini via Vertex as an LlmClient,
  Vector Search as a KnowledgeStore, Agent Runtime deploy manifest, Cloud Trace as Telemetry.
  Written-not-run status stated plainly (no GCP account provisioned).
- §10 exam-coverage mapping now cites three exams. Fill the six triage fields. Cost: ≤ S/M.
TASK 4b (tasks session): `mip-tasks` on MIP-0057 → stacked PRs: (1) mapping doc, (2) gcp/
module skeleton + guard, (3) Session trait + local impl, (4) A2A local case wired to `just`,
(5) docs/README index + AGENTS.md "Before implementing a feature" now lists three mappings.
Acceptance: `just build && just test && just quality` green with NO GCP env vars set; the
local path still carries zero cloud SDK (assert it in build.sbt the way azure/ is asserted).
```

---

## Prompt 5 — Nix tooling lives in nix-config (D1, one session; revisit after Prompt 2)

```text
[Block A]
Read nix-config/labs/pratico and labs/agentic first; match their shape exactly (flake with
devShells + checks, nixpkgs-fmt/statix/deadnix clean, ci.yml matrix entry).

TASK: add nix-config/labs/agentic-architect (or extend labs/agentic if that is the intended
home — say which and why) providing:
- devShell: python3 (stdlib is enough for scripts/), uv, google-adk pinned (Python) or the
  Java ADK via coursier (decide from Prompt 2's cases; both if cheap), ollama, just, pandoc +
  the same md→PDF toolchain ww3-gpu uses (reuse its derivation, don't fork it), gcloud CLI,
  nodejs (for MCP reference servers), shellcheck, jq, the ai-jail recipes (jco/jcf/jcs).
- checks: the lab's `scripts/*.py --self-test` and a quiz smoke (`quiz.py --self-test`), the
  PDF build of one lesson, flake evaluation.
- The lab repo's flake.nix stays thin: `inputs.nix-config`, `devShells.default =
  nix-config.labs.agentic-architect.devShells.${system}.default`, exactly the way marola and
  ww-lab consume it. If marola's flake needs a `gcp` addition (gcloud, adk) for Prompt 4, put
  it in nix-config too and bump marola's input.
Acceptance: `nix flake check` green in nix-config CI matrix; `nix develop -c just smoke` green
in the lab repo from a clean clone; `just toolchain` prints exact versions (for the book's
methods section, as in labs/pratico).
```

**Status (2026-09-15).** No `labs/agentic-architect` was added. nix-config's labs became generic
and reusable (`lint`, `agentic`, `publisher`, `pratico`, `cuda`), and its consumers follow
marola's shape: the project's own tools (python, uv, gcloud, ollama, node) in the repo's
`flake.nix`, the shared labs appended as flake inputs — `lint.lib.tools`, `agentic.lib.tools`
(ai-jail, `jail-run`, gh), and `publisher.lib.mkPdf` for the book. The drop-in under `contrib/`
was deleted. The flake is locked, so `nix develop` works from a clean clone.

---

## Prompt 6 — Publications, zip, first push (D14 evening / D15 morning)

```text
[Block A]

TASK: package the lab for its first public push and produce the zip.
1. publications/book/ — the course as one book, ww3-gpu pipeline: EN source, PT generated,
   PDF built in CI to pdf/ on main. Front matter states the date, the exam version (beta,
   2026-09), and that every (v) was checked on the date shown.
2. publications/post-exam.md — a template I fill after 2026-09-30: what the exam actually
   emphasised vs the guide, which lessons paid off, what the labs half looked like (within
   the NDA — no question content), the score when it arrives.
3. STUDY-LOG.md — one line per day from STUDY-CALENDAR.md with actual hours, quiz score,
   predicted score from `just quiz --stats`.
4. Push checklist in README: secrets scan (no .env, no tokens, no GCP project ids), LICENSE
   (MIT, matching marola/ww3-gpu), CI green, first release tag `v0.1-beta-exam`.
5. `just zip` → gcp-agentic-architect-<date>.zip of the repo (git-clean tree, no .tmp, no
   node_modules, no pdf binaries larger than 20 MB) plus the two marola PR bundles from Prompt
   4 (`git bundle`) so the marola side can be pushed separately.
Acceptance: zip unpacks, `nix develop -c just smoke` green from the unpacked tree, `git log`
trailers present, nothing in the zip that the secrets scan flags.
```

**Status (2026-09-15).** The book uses ww3-gpu's pipeline as ported: `scripts/book_prep.py` +
`scripts/build_pdf.sh` + `publications/book/{defaults.yaml,template.tex,filters/}`, built in the
Nix sandbox by `publisher.lib.mkPdf` (`nix build .#book`), and `.github/workflows/pubs.yml`
commits `pdf/` back to `main` through the `h0ffmann/nix-config/labs/publisher` action. PT
generation is still open: ww3-gpu's `translate_md.py` targets its proposal, not a book.

---

## Sequencing cheat-sheet

| Day | Session(s) | Output |
|---|---|---|
| D1 | Prompt 0 → 5 → 1 → 3 (schema + seed) → 2 (outline only) | skeleton, shell, AWESOME, 150 q, approved outline |
| D2–D10 | Prompt 2, two lessons per session, Section 3 first | 13 lessons, cases, 260 more questions, flashcards |
| D7 | read-only console recon inside lesson 08 | product recognition, no drills |
| D12 | targeted `--weak` sessions, resolve every ⚠ | Sections 3–4 second pass |
| D11, D14 | Prompt 2 lessons 13/14 (`--build-mock`) | two timed mocks |
| D13 | Prompt 4a then 4b | MIP-0057 + 5 stacked marola PRs |
| D14–15 | Prompt 6 | book PDFs, zip, first push, tag |

Two things I would change in your original ask, stated once: the certification is not "no
cloud" end-to-end — its hands-on-labs half runs in Google Skills after you pass the MCQ, so plan
a lab block and a credit ceiling for late October; and "use ww3-gpu as a baseline" is about the repo's
*shape* (lessons + runnable cases + verified awesome list + Nix + PDF pipeline), not its content,
so Prompt 0 copies the skeleton and nothing else.
