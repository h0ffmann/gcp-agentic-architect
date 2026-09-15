"""CX Agent Studio shape: pages, transition routes on intent/condition, event handlers for no-match."""
FLOW = {
  "start":   {"routes": {"intent:refund": "collect_order"}, "on_no_match": "start"},
  "collect_order": {"routes": {"param:order_id": "collect_reason"}, "on_no_match": "collect_order"},
  "collect_reason": {"routes": {"param:reason": "confirm"}, "on_no_match": "collect_reason"},
  "confirm": {"routes": {"intent:yes": "end", "intent:no": "start"}, "on_no_match": "confirm"}}
def step(page, signal): return FLOW[page]["routes"].get(signal, FLOW[page]["on_no_match"])
path, page = ["start"], "start"
for sig in ["intent:refund", "garbage", "param:order_id", "param:reason", "intent:yes"]:
    page = step(page, sig); path.append(page)
print(" -> ".join(path)); assert path == ["start", "collect_order", "collect_order", "collect_reason", "confirm", "end"]
print("ok: deterministic pages/routes; no-match handled by an event handler, not by the LLM")
