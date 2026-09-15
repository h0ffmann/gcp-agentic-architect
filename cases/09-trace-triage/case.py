"""Troubleshooting from spans: detect a reasoning loop and the latency bottleneck."""
from collections import Counter
SPANS = [("llm", 400), ("tool:get_order", 120), ("llm", 380), ("tool:get_order", 118), ("llm", 390), ("tool:get_order", 121),
         ("llm", 410), ("tool:search_kb", 6100), ("llm", 420)]
calls = Counter(n for n, _ in SPANS if n.startswith("tool:"))
loop = [n for n, k in calls.items() if k >= 3]; slow = max(SPANS, key=lambda s: s[1])
print("repeated tool calls (loop suspect):", loop); print("slowest span:", slow); print("total ms:", sum(d for _, d in SPANS))
assert loop == ["tool:get_order"] and slow[0] == "tool:search_kb"
print("ok: loops show as repeated identical calls; bottlenecks show as one fat span")
