# 02 — An agent that helps fraud analysts, at a retail bank

Time box: 45 min. Deliverable: `interviews/answers/02-YYYYMMDD.md` with `## Part A`, `## Part B`,
`## Part C`. Review: `use the design-reviewer agent on <that file>`.

## Setting

A retail bank's fraud operations team has 40 analysts who each review ~150 flagged transactions a
day. A data-science team shipped an "analyst copilot" as a hackathon project: the analyst pastes
a case id, the copilot pulls the customer's KYC file, recent transactions and past cases,
summarises them, and recommends *approve / block / escalate*. Analysts like it. Compliance has
just learned it exists. The interviewer is the bank's head of platform engineering; they want to
know whether to kill it or productise it, and what productising means.

## The system as found

- A Streamlit app on one VM inside the bank's network. One service account with read access to
  the customer database, the transactions warehouse and the case-management system.
- A single prompt: the three data pulls are concatenated as JSON, followed by "Recommend
  approve, block or escalate and explain." The model is a hosted frontier model reached over the
  internet; the bank has a contract with the provider but no data-processing addendum for this
  use.
- The recommendation is shown as a green/red/amber badge. Analysts report that they now decide
  faster and that they "mostly agree with it". Nobody has measured either claim.
- Full card numbers (PAN) and national ids appear in the transaction rows and are sent verbatim.
- Logs are stdout on the VM. A case takes 4–12 s.

## Constraints

- PCI DSS: PAN must not leave the cardholder data environment unmasked. LGPD: customers may ask
  what automated processing was applied to them and on what basis.
- The bank's model-risk policy says any model that influences a customer-affecting decision needs
  a documented evaluation, a challenger, and an owner.
- Analysts must remain the decision-maker; the regulator has said so in writing.
- Fraud patterns drift weekly. Cases arrive in bursts (payday, Black Friday).
- The platform team runs Kubernetes on-prem and one public cloud; both are available to you.

## Part A — improve it without changing infrastructure

Same VM, same model provider, same three data sources. What do you change so that Compliance
signs off on a *pilot*? Order the changes. Say which are a day's work and which are a month's.

## Part B — you may change infrastructure

Design the production system. Show the boundary between what the model sees and what it must
not; show where the human sits; show how you would know the copilot is helping rather than
anchoring. Say what happens on a payday burst and what happens when the provider is down.

## Part C — FOSS stack vs Google Cloud Agent Runtime stack

| Concern | FOSS option | Google Cloud option | What tips it |
|---|---|---|---|
| Orchestration: gather → summarise → recommend → human | | | |
| PAN / national-id masking before any model call | | | |
| Agent credentials to the three data sources, least privilege | | | |
| Audit record per case: inputs, model, output, analyst decision | | | |
| Evaluation: agreement rate, anchoring, drift | | | |
| Prompt injection via transaction memo fields | | | |
| Serving during bursts; graceful degradation | | | |
| Model choice: hosted frontier vs self-hosted open weights, given PCI | | | |
| Cost per case at 6 000 cases/day | | | |

Products you may name on either side are listed with their sources in
[README — Sources](README.md#sources). Anything not on that list is `⚠` in your answer until you
fetch it.

## Related lessons

[06 Multi-agent, A2A, Runtime](../course/06-multi-agent-a2a-runtime.md) ·
[07 Evaluation](../course/07-evaluation.md) · [10 Security & governance](../course/10-security-governance.md).
Objectives 3.3 · 4.1 · 5.1 · 5.2.
