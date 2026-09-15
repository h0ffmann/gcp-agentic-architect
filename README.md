# gcp-agentic-architect

A public exam lab for **PR000340 — Google Cloud Certified · Professional Agentic Architect
(beta)**: a self-paced course, runnable local cases, a scenario-style question bank with
spaced repetition, a verified awesome-list, and the design docs for porting what the exam teaches
into [marola](https://github.com/h0ffmann/marola) without breaking its no-cloud default.

Shape borrowed from [ww3-gpu](https://github.com/h0ffmann/ww3-gpu): lessons + cases + AWESOME
list + Nix-pinned toolchain + markdown→PDF publications, every product claim marked `(v)` or
`⚠`. Nix tooling lives in [nix-config](https://github.com/h0ffmann/nix-config)
(`labs/agentic-architect`); this repo's `flake.nix` only consumes it.

## The exam in one screen (verified 2026-09-15 — see `EXAM-BRIEF.md`)

| | |
|---|---|
| Sections · weights | 1 low-code 13% · 2 coding agents 17% · 3 custom agents 33% · 4 eval & deploy 22% · 5 security & governance 15% |
| Part 1 | Proctored multiple-choice, 3 h, Pearson, window **Sept 8–30, 2026**, $120 beta |
| Part 2 | Hands-on labs in Google Skills (< 5 h), **only after passing Part 1**, delivered late Oct–Dec |
| Results | Part 1 late October; both parts required; credential valid 1 year |
| Guide | <https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf> |

Everything before Sept 30 is Part 1. Lab prep is a separate block after results.

## Run

```bash
nix develop            # toolchain from nix-config (python, uv, ADK, ollama, just, pandoc, gcloud, node)
just                   # list recipes
just smoke             # what CI runs: layout + scripts self-tests + bank parse (+ flake, PDF when available)
just case NN           # run lesson NN's local case
just quiz --lesson NN  # 20 questions; also --section 3, --mock 1 --minutes 120, --weak, --stats
just pdf               # build publications/ into pdf/
just cases             # run all 12 local cases
```

No Google Cloud account is needed for anything in `cases/` by default. Paid resources are gated
twice (`.claude/settings.json` deny list + `.claude/hooks/guard-gcloud.sh`); see `AGENTS.md`.

## Layout

```
gt.md                    the seven-session prompt series that builds this repo (plan of record)
AGENTS.md                rules for any AI agent (and human) working here
EXAM-BRIEF.md            exam guide as a checklist, in-scope tools verified, beta facts, cost plan
STUDY-CALENDAR.md        15 days to the MCQ, weighted 13/17/33/22/15
STUDY-LOG.md             one line per day: hours, quiz score, predicted score
AWESOME-AGENTIC-ARCHITECT_202609.md   curated, dated, every link fetched (Prompt 1)
course/NN-*.md           15 lessons (Prompt 2)          cases/NN-*/   runnable local cases
questions/               bank.jsonl, mock-N.jsonl, cards/, schema.md (Prompt 3)
scripts/                 stdlib Python, --self-test, --json
marola/                  MIP-0057 + AGENTIC-ARCHITECT-MAPPING.md drafts, upstreamed as stacked PRs (Prompt 4)
publications/            course book + post-exam writeup; EN source, PT generated (Prompt 6)
flake.nix · justfile · .github/workflows/ci.yml · .claude/
```

## Status (2026-09-15)

| Prompt | State |
|---|---|
| 0 skeleton | done |
| 1 AWESOME list | done; Google Skills path activities need a login to enumerate (D1) |
| 2 course | 15 lessons + 12 runnable cases + 13 flashcard decks written; lessons 13/14 are the mock procedure |
| 3 questions | runner done; bank at 124 (needs ~300 for two disjoint 60-question mocks — add 20 per lesson while studying) |
| 4 marola | MIP-0057 + mapping doc drafted in `marola/`; upstream via marola's `mip`/`mip-tasks` skills on D13 |
| 5 nix | `contrib/nix-config/labs/agentic-architect/` ready to drop into nix-config; lab flake consumes it as a `?dir=` subflake with a fallback shell |
| 6 publications | `publications/build.sh` builds the EN book (HTML always, PDF when an engine exists); PT generation is a follow-up reusing ww3-gpu's step |

Not run in the authoring sandbox (no network / no nix): `nix develop`, `nix flake check`, `just` itself. Everything Python was run.

## License

MIT — see `LICENSE`.
