# publications

- `book/` — the course as one book: `defaults.yaml` (pandoc), `template.tex` and
  `filters/symbols.lua` (from ww3-gpu), `front-matter.md`. `scripts/build_pdf.sh` renders it with
  nix-config's `labs/publisher` toolchain: `just book` locally, `nix build .#book` in the sandbox,
  and `.github/workflows/pubs.yml` commits `pdf/agentic-architect-book.pdf` on `main`. EN only;
  PT generation is open.
- `post-exam.md` — template filled after 2026-09-30, within the NDA (no question content).
