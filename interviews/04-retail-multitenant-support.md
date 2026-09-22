# 04 — A support agent for a marketplace with 5 000 sellers

Time box: 45 min. Deliverable: `interviews/answers/04-YYYYMMDD.md` with `## Part A`, `## Part B`,
`## Part C`. Review: `use the design-reviewer agent on <that file>`.

## Setting

An online marketplace hosts 5 000 third-party sellers. Buyers contact "support" about orders;
the marketplace answers policy and payment questions itself and forwards product, shipping and
return questions to the seller. A product team launched a chat agent for the marketplace's own
half. It resolves 35 % of conversations without a human. The CEO now wants "the agent to answer
the seller half too", and three large sellers already run their own support bots and have asked
to plug them in. The interviewer is the marketplace's principal engineer for the support
platform.

## The system as found

- One agent, one system prompt, one tool set: `get_order`, `get_policy`, `refund` (capped at
  the order value), `handoff_to_human`. Tools call the marketplace's internal APIs with a service
  token.
- Retrieval over a single index of marketplace policy pages. Sellers' return policies are not
  indexed; the agent guesses or hands off.
- Conversation memory is the chat transcript passed back every turn. Long threads hit the context
  limit and the agent forgets the order id.
- One model, one region, one prompt version. A prompt change goes live for everyone at once.
- Cost is ~$0.09 per conversation; a human costs ~$2.40. Volume: 60 000 conversations/day.

## Constraints

- A seller must never see, or be able to make the agent reveal, another seller's orders, prices,
  or buyers. The marketplace has been fined for a data leak before.
- Sellers' own bots are black boxes on their own infrastructure; three vendors, three protocols.
- Refunds above the cap need a human; anything the agent says about a refund is legally binding.
- Peak is 6× baseline for two weeks a year. Latency budget: first token under 2 s.
- The platform team wants one place to see every conversation, every tool call, every handoff.

## Part A — improve it without changing infrastructure

Same agent, same tools, same index, same model. What do you change to safely index the sellers'
policies and stop the memory failures, before any seller bot is connected? Order the work; say
what you would ship per week for four weeks.

## Part B — you may change infrastructure

Design the multi-agent system that lets a seller's bot handle its half. Show the trust boundary
between the marketplace agent and a seller agent; show what a seller agent may ask for and what
it can never receive; show how a prompt rollout is staged. Say what "one place to see everything"
is and how a seller's bot appears in it.

## Part C — FOSS stack vs Google Cloud Agent Runtime stack

| Concern | FOSS option | Google Cloud option | What tips it |
|---|---|---|---|
| Orchestration and routing: marketplace agent ↔ seller agents | | | |
| Agent-to-agent protocol with three external vendors | | | |
| Tenant-scoped retrieval: policies per seller, no cross-talk | | | |
| Session state and long-term memory across turns and channels | | | |
| Identity of each seller agent; what tokens it holds | | | |
| Egress policy: what a seller agent may call, and what it may be told | | | |
| Registry of agents and tools; onboarding a fourth seller bot | | | |
| Observability across marketplace and seller agents | | | |
| Staged prompt/model rollout; canary and rollback | | | |
| Peak scaling and cost per conversation at 6× | | | |

Products you may name on either side are listed with their sources in
[README — Sources](README.md#sources). Anything not on that list is `⚠` in your answer until you
fetch it.

## Related lessons

[05 MCP, Registry, Identity](../course/05-mcp-registry-identity.md) ·
[06 Multi-agent, A2A, Runtime](../course/06-multi-agent-a2a-runtime.md) ·
[08 Deployment runtimes](../course/08-deployment-runtimes.md). Objectives 3.1 · 3.3 · 4.2 · 5.1.
