# Google Cloud in this repo

- Default is no account, no project, no billing. Cases run with ADK local + Ollama.
- `--gcp` paths are written-not-run unless a lesson states a run date.
- Creating or deploying anything billable: propose, state cost, wait. Two gates:
  `.claude/settings.json` deny prefixes (not overridable) and `guard-gcloud.sh`
  (overridable once with `GCP_ALLOW_DEPLOY=1` after a human go-ahead).
- Cost ceiling before Sept 30: $25. See EXAM-BRIEF.md.
- Never write a project id, key, or token into a tracked file. `.env` is gitignored.
- Product names: assume renames (Agent Engine → Agent Runtime, Vertex AI Search → Agent
  Search). Fetch the doc, mark (v) with date, or write ⚠.
