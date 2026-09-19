<div align="center">

# ☁️ gcp-agentic-architect

**Google Cloud Professional Agentic Architect, hands on — without a cloud bill.**

[![ci](https://github.com/h0ffmann/gcp-agentic-architect/actions/workflows/ci.yml/badge.svg)](https://github.com/h0ffmann/gcp-agentic-architect/actions/workflows/ci.yml)
[![pubs](https://github.com/h0ffmann/gcp-agentic-architect/actions/workflows/pubs.yml/badge.svg)](https://github.com/h0ffmann/gcp-agentic-architect/actions/workflows/pubs.yml)
[![Built with nix](https://img.shields.io/static/v1?label=Built%20with&message=nix&color=blue&style=flat&logo=nixos&link=https://nixos.org&labelColor=111212)](https://nixos.org)
[![GCP](https://img.shields.io/badge/GCP-PR000340_beta-4285F4?style=flat&logo=googlecloud&logoColor=white)](https://cloud.google.com/learn/certification/agentic-architect)
[![license: MIT](https://img.shields.io/badge/license-MIT-2EA043?style=flat)](LICENSE)

</div>

An open exam lab for **PR000340 — Google Cloud Certified · Professional Agentic Architect
(beta)**: a self-paced course weighted like the exam guide, runnable agent cases that need no
Google Cloud account, a scenario-style question bank with spaced repetition, a verified
awesome-list, and the design notes for porting what the exam teaches into
[marola](https://github.com/h0ffmann/marola) without breaking its no-cloud default.

Shape borrowed from [ww3-gpu](https://github.com/h0ffmann/ww3-gpu) (lessons + cases + AWESOME
list + Nix + PDF pipeline, every claim marked `(v)` or `⚠`); toolchain from
[nix-config](https://github.com/h0ffmann/nix-config)'s labs.

---

## The exam in one screen (verified 2026-09-15 — see [`EXAM-BRIEF.md`](EXAM-BRIEF.md))

| | |
|---|---|
| Sections · weights | 1 low-code 13% · 2 coding agents 17% · **3 custom agents 33%** · 4 eval & deploy 22% · 5 security & governance 15% |
| Part 1 | Proctored multiple-choice, 3 h, Pearson, window **Sept 8–30, 2026**, $120 beta |
| Part 2 | Hands-on labs in Google Skills (< 5 h), **only after passing Part 1**, delivered late Oct–Dec |
| Results | Part 1 late October; both parts required; credential valid 1 year |
| Guide | <https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf> |

Everything before Sept 30 is Part 1. Lab prep is a separate block after results.

## What's in here

| Path | What it is |
|---|---|
| [`course/`](course/) | 15 lessons, Section 3 first: model selection, ADK, sessions & memory, RAG, MCP, A2A, evaluation, deployment, troubleshooting, security, coding agents, low-code, two mock-exam procedures |
| [`cases/`](cases/) | 12 runnable cases, one per lesson, stdlib Python, one command and one assertion each |
| [`questions/`](questions/) | `bank.jsonl` (316 scenario questions, rationale per option), two built 60-question mocks, Anki decks in `cards/`, [`schema.md`](questions/schema.md) |
| [`scripts/`](scripts/) | `quiz.py` (Leitner boxes, weighted predicted score), `awesome_digest.py`, `smoke.py`, the book pipeline, `pr.sh` / `uprd.sh` |
| [`AWESOME-AGENTIC-ARCHITECT_202609.md`](AWESOME-AGENTIC-ARCHITECT_202609.md) | Curated, dated links; every entry fetched |
| [`EXAM-BRIEF.md`](EXAM-BRIEF.md) · [`STUDY-CALENDAR.md`](STUDY-CALENDAR.md) · [`STUDY-GUIDE.md`](STUDY-GUIDE.md) · [`STUDY-LOG.md`](STUDY-LOG.md) | The guide as a checklist + cost plan · 15 days to the MCQ · the per-lesson loop and which lessons need notes · one line per day |
| [`marola/`](marola/) | Draft MIP and exam-to-architecture mapping, upstreamed to marola by its own `mip` skills |
| [`publications/`](publications/) | The study book (pandoc defaults, template, Lua filter) and the post-exam template; PDFs land in `pdf/` on `main` |
| [`docs/PROMPT-SERIES_202609.md`](docs/PROMPT-SERIES_202609.md) | The seven-session prompt series that built this repo (plan of record) |
| [`.claude/`](.claude/) · [`.ai-jail`](.ai-jail) | Deny list + `guard-gcloud.sh` hook for coding agents; the sandbox policy |
| `flake.nix` · `justfile` | The toolchain and every task: `just` lists them |

## Quickstart

Needs [Nix](https://nixos.org) (flakes on). Everything else comes from the locked flake.

```bash
git clone git@github.com:h0ffmann/gcp-agentic-architect.git && cd gcp-agentic-architect
nix develop            # python, uv, gcloud, ollama, node, lint tools, ai-jail
just                   # list recipes
just smoke             # layout + question banks + self-tests + gcloud guard + all 12 cases (~2 s)
just case 04           # one lesson's case: RAG, top-k then rerank
just quiz --lesson 04  # 20 questions; also --section 3, --mock 1 --minutes 120, --weak, --stats
just quiz --stats      # accuracy per objective, weighted predicted score, weakest three
```

Then start at [`course/00-orientation.md`](course/00-orientation.md). No Google Cloud account is
needed for anything in `cases/`; Python 3.12+ alone runs them (`bash cases/04-rag-rerank/run.sh`).

## Toolchain (nix-config labs)

`flake.nix` follows marola's shape: the lab's own tools locally, the shared labs from
[nix-config](https://github.com/h0ffmann/nix-config) appended as flake inputs on one nixpkgs pin.

```bash
just dev               # == nix develop
just toolchain         # exact versions and the pinned nixpkgs rev
just lock              # bump every input (`just lock lint` for one)
just check             # nix flake check: shells evaluate, checks.smoke builds in the sandbox
```

<details>
<summary>Environment details</summary>

| Type | Program | From |
| :--- | :------ | :--- |
| Scripts & cases | python 3 (stdlib only), [uv](https://docs.astral.sh/uv/) for the optional `google-adk` venv | `flake.nix` |
| Google Cloud | [gcloud](https://cloud.google.com/sdk) — read-only recon; creates and deploys are gated | `flake.nix` |
| Open weights | [Ollama](https://ollama.com/) (`ollama serve` is the host's) | `flake.nix` |
| MCP servers | node | `flake.nix` |
| Lint | ruff, shellcheck, actionlint, hadolint, pyflakes, cloc, coverage, pdoc | [`labs/lint`](https://github.com/h0ffmann/nix-config/tree/main/labs/lint) |
| Nix hygiene | nixpkgs-fmt, statix, deadnix | `flake.nix` |
| Agent sandbox | [ai-jail](https://github.com/akitaonrails/ai-jail), `jail-run`, `gh-token`, gh, OpenCode | [`labs/agentic`](https://github.com/h0ffmann/nix-config/tree/main/labs/agentic) |
| Publishing | pandoc, TeX Live (xelatex), `mkPdf`, the composite Action | [`labs/publisher`](https://github.com/h0ffmann/nix-config/tree/main/labs/publisher) |

Shells: `default` (all of the above but TeX), `pubs` (publisher), `lint` (what CI enters, no
ai-jail build). Outputs: `packages.book`, `checks.smoke`, `formatter`.

What `nix develop --command just toolchain` prints today (`(v)`, lab machine, 2026-09-15; `jq`,
`pandoc` and `nix` lines trimmed):

```
nixpkgs    eaad089433ca2bb662274377d33df3d0e51ef28b
python3    Python 3.14.7
uv         uv 0.12.11 (x86_64-unknown-linux-gnu)
just       just 1.58.0
node       v24.20.0
gcloud     Google Cloud SDK 581.0.0
ollama     ollama version is 0.12.11
ruff       ruff 0.16.6
shellcheck version: 0.11.0
actionlint 1.7.12
gh         gh version 2.100.0 (nixpkgs)
ai-jail    ai-jail 1.21.0
```

</details>

## Coding agents, and the cloud bill

Claude Code (or OpenCode) runs inside ai-jail, from this directory, with the host's GitHub token
forwarded and `.env` masked:

```bash
just gh-auth           # which GitHub credential the jail will borrow
just jco               # Claude Code, opus (jcf fable, jcs sonnet); `just jail-dry-run ls` to audit
```

Paid resources are gated twice, on purpose differently (details in [`AGENTS.md`](AGENTS.md)):
`.claude/settings.json` denies the literal prefixes (`gcloud run deploy`, `gcloud … create`,
`terraform apply`, `adk deploy`, …) with no override, and `.claude/hooks/guard-gcloud.sh` catches
every other shape, overridable once with `GCP_ALLOW_DEPLOY=1` after a human go-ahead.
`just guard-test` proves both lists. Cost ceiling before Sept 30: **$25**.

## Publications (markdown → PDF)

The pipeline is ww3-gpu's, on nix-config's [`labs/publisher`](https://github.com/h0ffmann/nix-config/tree/main/labs/publisher):
`scripts/book_prep.py` turns lesson links into in-book links, pandoc + xelatex render
`course/*.md` with `publications/book/{defaults.yaml,template.tex,filters/symbols.lua}`.

```bash
just book              # build/agentic-architect-book.pdf, in the pubs shell
just book-nix          # the same in the Nix sandbox (what CI runs) -> result/
```

[`pubs.yml`](.github/workflows/pubs.yml) builds it on every PR that touches the course and
commits `pdf/agentic-architect-book.pdf` back to `main`. PT generation is not wired yet.

## Automations

| Where | What |
|---|---|
| [`ci.yml`](.github/workflows/ci.yml) | smoke (stdlib: layout, banks, self-tests, guard, cases) · quality (`nix flake check` + `just quality`) · markdown links (lychee, non-blocking) |
| [`pubs.yml`](.github/workflows/pubs.yml) | the study book via `h0ffmann/nix-config/labs/publisher@main`, PDF committed on `main` |
| [`pr-body.yml`](.github/workflows/pr-body.yml) | fills a PR's description and title from its commits (`Tested:` / `Cost:` trailers) |
| [`dependabot.yml`](.github/dependabot.yml) | GitHub Actions, monthly, one grouped PR |
| `just pr` / `just uprd` | push the branch and open or refresh its PR from the commits |

## Conventions

- `(v)` — verified against a source actually fetched while writing, with URL and date.
- `⚠` — not verified; check before trusting.
- Product names in this family change fast (Agent Engine → Agent Runtime, Vertex AI Search →
  Agent Search). Newer name wins; old names stay struck through with their date.
- No exam content, ever: questions are written from the public guide and fetched docs.
- Commits carry `Tested:` and `Cost:` trailers; `just smoke && just quality` green before a PR.

## Status (2026-09-15)

| Area | State |
|---|---|
| AWESOME list | done; Google Skills path activities need a login to enumerate |
| Course | 15 lessons, 12 cases, 13 flashcard decks (65 cards); lessons 13/14 are the mock procedure |
| Questions | bank at **316**, exam-level scenarios; both 60-question mocks built and disjoint. Options are shuffled per session and `--validate` lints stems, rationales, answer-letter balance and option-length tells |
| marola | MIP draft + mapping doc in `marola/`. marola merged its own MIP-0057 (GCP as opt-in cloud backend, [#385](https://github.com/h0ffmann/marola/pull/385)) on 2026-09-15, so this draft takes the next free number or folds into it when upstreamed |
| Toolchain | `flake.nix` on nix-config `labs/{lint,agentic,publisher}`, locked; `nix flake check`, `just quality` and `nix build .#book` run green locally |
| Publications | EN book builds (35 pages); PT generation open |
| CI | workflows lint clean; the last GitHub run was refused before start by an account billing hold, so no green run on GitHub yet |

## Licensing

MIT for everything in this repo — see [`LICENSE`](LICENSE). Linked docs, courses and tools
carry their own terms.

## Trademarks

Google Cloud, Gemini and the product names in the exam guide are trademarks of Google LLC, used
here only to refer to those products. This repository is an independent study project, not
affiliated with or endorsed by Google, and contains no exam question content.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). The most useful contribution is confirming or
correcting anything marked `⚠`.
