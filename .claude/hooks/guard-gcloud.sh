#!/usr/bin/env bash
# PreToolUse hook on Bash: refuse commands that create or deploy billable Google Cloud resources
# unless GCP_ALLOW_DEPLOY=1 was set after a human go-ahead. Literal prefixes are also in
# .claude/settings.json permissions.deny, which fires before this hook and cannot be overridden.
set -euo pipefail

PATTERNS=(
  'gcloud[[:space:]].*[[:space:]](create|deploy|enable|apply)([[:space:]]|$)'
  'gcloud[[:space:]]+run[[:space:]]+(deploy|jobs[[:space:]]+create|services[[:space:]]+update)'
  'gcloud[[:space:]]+(container|compute|sql|redis|ai|alpha|beta)[[:space:]]'
  'terraform[[:space:]]+(apply|destroy)'
  'tofu[[:space:]]+(apply|destroy)'
  'adk[[:space:]]+deploy'
  'agents-cli[[:space:]]+deploy'
  'agents[[:space:]]+deploy'
  'gsutil[[:space:]]+mb'
  'bq[[:space:]]+mk'
)

denied() {
  local cmd="$1"
  for p in "${PATTERNS[@]}"; do
    if [[ "$cmd" =~ $p ]]; then return 0; fi
  done
  return 1
}

if [[ "${1:-}" == "--self-test" ]]; then
  fail=0
  for c in "gcloud run deploy svc --image x" "cd infra && terraform apply" "/usr/bin/gcloud compute instances create vm" \
           "adk deploy agent_engine" "bash -c 'gcloud services enable aiplatform.googleapis.com'" "bq mk ds"; do
    denied "$c" || { echo "should deny: $c"; fail=1; }
  done
  for c in "gcloud config list" "gcloud auth print-access-token" "adk web" "terraform plan" "git push" "python3 scripts/quiz.py --stats"; do
    denied "$c" && { echo "should allow: $c"; fail=1; }
  done
  [[ $fail -eq 0 ]] && echo "guard-gcloud self-test ok"
  exit $fail
fi

CMD=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null || true)

if denied "$CMD"; then
  if [[ "${GCP_ALLOW_DEPLOY:-0}" == "1" ]]; then
    echo "guard-gcloud: allowed once by GCP_ALLOW_DEPLOY=1" >&2
    exit 0
  fi
  cat >&2 <<EOF
guard-gcloud: blocked — this command may create or deploy a billable Google Cloud resource.
  $CMD
Propose it, state the expected cost, and wait for a human. After go-ahead: GCP_ALLOW_DEPLOY=1.
EOF
  exit 2
fi
exit 0
