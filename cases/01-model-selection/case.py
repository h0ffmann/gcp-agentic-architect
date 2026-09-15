"""Model selection as a scored decision: constraints → LLM/SLM, hosted/SaaS, OSS/proprietary."""
import sys
OPTIONS = {
    "gemini-saas":        dict(residency=0, latency=2, breadth=3, ops=3, cost_small=2),
    "open-slm-self-host": dict(residency=3, latency=3, breadth=1, ops=1, cost_small=3),
    "open-llm-self-host": dict(residency=3, latency=1, breadth=2, ops=0, cost_small=1),
}
def choose(need):  # need: weights 0-3 per dimension
    return max(OPTIONS, key=lambda o: sum(need[k] * OPTIONS[o][k] for k in need))
SCENARIOS = {
    "bank-pii-narrow-fast":   (dict(residency=3, latency=3, breadth=0, ops=0, cost_small=1), "open-slm-self-host"),
    "startup-broad-no-ops":   (dict(residency=0, latency=1, breadth=3, ops=3, cost_small=1), "gemini-saas"),
    "onprem-general-assistant":(dict(residency=3, latency=1, breadth=3, ops=0, cost_small=0), "open-llm-self-host"),
}
for name, (need, want) in SCENARIOS.items():
    got = choose(need); print(f"{name:28s} -> {got}")
    assert got == want, (name, got, want)
print("ok: constraints, not model size, decide")
