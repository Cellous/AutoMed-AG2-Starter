
from dataclasses import dataclass
from typing import Dict, Any, List, Optional
from rich.console import Console

console = Console()

@dataclass
class Message:
    role: str
    content: str

class BaseAgent:
    name: str = "agent"
    def step(self, history: List[Message], context: Dict[str, Any]) -> Optional[Message]:
        raise NotImplementedError

class Coordinator:
    """Very small round‑robin coordinator controlling turn order and max turns."""
    def __init__(self, agents: Dict[str, 'BaseAgent']):
        self.agents = agents

    def run(self, max_turns: int = 6, context: Dict[str, Any] = None) -> List[Message]:
        history: List[Message] = []
        order = ["user", "clinician", "data", "clinician"]  # simple loop
        i = 0
        while i < max_turns:
            name = order[i % len(order)]
            agent = self.agents.get(name)
            if not agent:
                break
            msg = agent.step(history, context or {})
            if msg:
                history.append(msg)
                console.print(f"[bold]{msg.role}[/]: {msg.content}")
            i += 1
        return history

class UserAgent(BaseAgent):
    name = "user"
    def __init__(self, prompt: str):
        self.prompt = prompt
    def step(self, history, context):
        # Only speak once
        if any(m.role == "user" for m in history):
            return None
        return Message(role="user", content=self.prompt)

class ClinicianAgent(BaseAgent):
    name = "clinician"
    def __init__(self, llm_generate):
        self.generate = llm_generate
    def step(self, history, context):
        # Summarize history and return next‑step plan
        transcript = "\n".join([f"{m.role}: {m.content}" for m in history])
        sys = (
            "You are a careful clinician assistant. Provide triage guidance, red‑flag checks, "
            "and next‑step recommendations. Consider age/sex context. Always add a disclaimer: "
            "not medical advice. Be concise and structured."
        )
        prompt = f"""
System: {sys}
History:
{transcript}

Task: Draft the next steps as bullet points with sections: Assessment, Red‑flags to watch, Next steps, Disclaimer.
        """
        out = self.generate(prompt, max_tokens=220)
        return Message(role="clinician", content=out)

class DataAgent(BaseAgent):
    name = "data"
    def __init__(self, db):
        self.db = db
    def step(self, history, context):
        # Extract the first user message
        try:
            user_msg = next(m for m in history if m.role == "user")
        except StopIteration:
            return None
        symptoms = user_msg.content
        data = self.db.lookup(symptoms, age=context.get("age"), sex=context.get("sex"))
        return Message(role="data", content=data)
