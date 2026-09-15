"""ADK shape without ADK: agent = instruction + tools; runner yields events; a fake model routes."""
import json
def get_weather(city: str) -> str: return json.dumps({"city": city, "temp_c": 21})
def get_time(city: str) -> str: return json.dumps({"city": city, "time": "10:00"})
class FakeModel:
    def decide(self, text, tools):
        for t in tools:
            if t.__name__.split("_")[1] in text.lower(): return t, {"city": text.split()[-1].strip("?")}
        return None, None
class Agent:
    def __init__(self, name, instruction, tools): self.name, self.instruction, self.tools = name, instruction, tools
class Runner:
    def __init__(self, agent, model): self.agent, self.model = agent, model
    def run(self, text):
        yield {"author": "user", "text": text}
        tool, args = self.model.decide(text, self.agent.tools)
        if tool:
            yield {"author": self.agent.name, "function_call": {"name": tool.__name__, "args": args}}
            yield {"author": self.agent.name, "function_response": tool(**args)}
        yield {"author": self.agent.name, "text": "done"}
events = list(Runner(Agent("helper", "answer with tools", [get_weather, get_time]), FakeModel()).run("weather in Lisbon"))
for e in events: print(e)
assert events[1]["function_call"]["name"] == "get_weather" and json.loads(events[2]["function_response"])["city"] == "Lisbon"
print("ok: instruction + tools + runner + event stream")
