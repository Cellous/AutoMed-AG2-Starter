
from typing import Optional

class MockMedicalDB:
    def lookup(self, symptoms: str, age: Optional[int]=None, sex: Optional[str]=None) -> str:
        s = (symptoms or "").lower()
        notes = []
        if "sore throat" in s:
            notes.append("Sore throat: salt‑water gargle, lozenges; consider strep/COVID testing per policy.")
        if "fever" in s:
            notes.append("Fever: track temp; red‑flag if >103°F or lasting >3 days.")
        if "cough" in s:
            notes.append("Cough: humidifier for dry cough; hydration; consider flu/COVID test as indicated.")
        if not notes:
            notes.append("No specific matches: provide general supportive‑care references.")
        redflags = "Data red‑flags: difficulty breathing, blue lips/face, chest pain, confusion, severe dehydration."
        return f"[DB] Age={age}, Sex={sex}\n" + "\n".join(notes) + "\n" + redflags
