set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

# what CI runs: layout, scripts self-tests, question bank parse; flake + pdf when tools exist
smoke:
    python3 scripts/smoke.py
    for d in cases/*/; do bash "$d/run.sh" >/dev/null; done && echo "cases: ok"
    @if command -v nix >/dev/null; then nix flake check --no-build; else echo "nix: skipped (not installed)"; fi

# run lesson NN's local case (cases/NN-*/run.sh)
case NN:
    @dir=$(ls -d cases/{{NN}}-*/ 2>/dev/null | head -1); \
    [ -n "$dir" ] || { echo "no case for lesson {{NN}}"; exit 1; }; \
    bash "$dir/run.sh"

# quiz runner; see scripts/quiz.py --help (Prompt 3)
quiz *ARGS:
    python3 scripts/quiz.py {{ARGS}}

# build publications/ into pdf/ (EN source, PT generated); pipeline from ww3-gpu (Prompt 6)
pdf:
    @command -v pandoc >/dev/null || { echo "pandoc missing: nix develop"; exit 1; }
    bash publications/build.sh

# lint everything that has a linter here
quality:
    @if command -v shellcheck >/dev/null; then shellcheck .claude/hooks/*.sh cases/*/run.sh 2>/dev/null || true; else echo "shellcheck: skipped"; fi
    @if command -v ruff >/dev/null; then ruff check scripts; else python3 -m py_compile scripts/*.py && echo "ruff: skipped, py_compile ok"; fi
    @if command -v nixpkgs-fmt >/dev/null; then nixpkgs-fmt --check flake.nix; else echo "nixpkgs-fmt: skipped"; fi
    for s in scripts/*.py; do python3 "$s" --self-test; done

# exact tool versions, for the book's methods section
toolchain:
    @for t in python3 uv adk ollama just pandoc gcloud node shellcheck jq nix; do \
      if command -v "$t" >/dev/null; then printf '%-10s %s\n' "$t" "$($t --version 2>&1 | head -1)"; else printf '%-10s (absent)\n' "$t"; fi; done

# Claude Code inside ai-jail (recipes from nix-config); token from host gh
jail-claude:
    @command -v jcf >/dev/null || { echo "ai-jail recipes not on PATH: nix develop"; exit 1; }
    jcf

# guard self-test: every line must be denied, then allowed under GCP_ALLOW_DEPLOY=1
guard-test:
    bash .claude/hooks/guard-gcloud.sh --self-test

# git-clean zip of the repo (tracked files only: no .tmp, no pdf)
zip:
    @test -z "$(git status --porcelain)" || { echo "tree not clean"; exit 1; }
    git archive --format=zip -o "gcp-agentic-architect-$(date +%F).zip" HEAD
    @ls -la gcp-agentic-architect-*.zip

# run every case
cases:
    for d in cases/*/; do echo "== $d"; bash "$d/run.sh" | tail -1; done

# awesome-list candidates from GitHub (cached in .tmp; proposes, never edits)
digest:
    python3 scripts/awesome_digest.py
