
import yaml

def load_config(path="agent_config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def generate(prompt: str, max_tokens: int = 300):
    """Provider‑agnostic call. Defaults to MOCK so the demo runs offline."""
    cfg = load_config()
    provider = (cfg.get("provider") or "mock").lower()
    if provider == "mock":
        # Deterministic summary for demo purposes.
        return (
            "Assessment: Likely minor viral illness based on reported symptoms.\n"
            "Red‑flags to watch: trouble breathing, chest pain, confusion, persistent high fever, severe dehydration.\n"
            "Next steps: hydrate, rest, consider OTC symptom relief, home isolation if contagious disease suspected; seek care if symptoms worsen or red‑flags present.\n"
            "Disclaimer: Educational demo only — not medical advice."
        )
    # Stubs for real providers (to be filled with classroom SDKs)
    return "[Provider stub] Configure your classroom provider in llm.generate()."
