# Contributing

This is a personal study repo, public so others can use it. Corrections are very welcome,
especially these, in order of usefulness:

1. **Anything marked `⚠`.** A claim nobody fetched a source for. A link to the current doc and the
   date you checked is the highest-value fix here.
2. **Renames.** Products in this family change names fast (Agent Engine → Agent Runtime, Vertex AI
   Search → Agent Search). If a lesson uses an old name, say which doc shows the new one.
3. **Questions whose best answer is wrong or arguable.** Open an issue with the question `id`,
   the answer you think is right, and the doc that says so.
4. **Stale links** in `AWESOME-AGENTIC-ARCHITECT_202609.md`.

## Ground rules

- Keep the `(v)` / `⚠` convention. Marking uncertainty honestly is the point.
- **No exam content.** Nothing recalled from a sitting, nothing from dump sites or paid banks.
  Questions are written from the public guide and fetched docs.
- **No paid cloud resources in a case.** Cases run with no Google Cloud account; a `--gcp` path
  is documented and gated, never the default. See `AGENTS.md`.
- Scripts stay stdlib-only Python with a `--self-test`.
- `just smoke && just quality` green before a PR (inside `nix develop`).
- Prose: plain, direct, no filler.

## Opening a pull request

Write the commit message properly (subject, a body paragraph saying what and why, and
`Tested:` / `Cost:` trailers in the final block of the message), then `just pr`: it pushes the
branch and creates the PR with a description generated from the commits (`just uprd` regenerates
it later). A PR opened from the GitHub UI gets the same treatment from
`.github/workflows/pr-body.yml`. Delete the first `<!-- uprd -->` line of a description to
hand-edit it and keep it.
