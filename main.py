
import argparse
from agents import UserAgent, ClinicianAgent, DataAgent, Coordinator
from llm import generate
from medical_db import MockMedicalDB

DISCLAIMER = "This demo is for educational use only and is not medical advice. Always consult a licensed clinician."

def build_app(symptoms: str, age: int, sex: str):
    user = UserAgent(prompt=f"My symptoms: {symptoms}")
    clinician = ClinicianAgent(llm_generate=generate)
    data = DataAgent(db=MockMedicalDB())
    return Coordinator(agents={"user": user, "clinician": clinician, "data": data})

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--symptoms", required=True, help="Comma‑separated symptom text")
    p.add_argument("--age", type=int, default=30)
    p.add_argument("--sex", type=str, default="U")
    p.add_argument("--turns", type=int, default=6)
    args = p.parse_args()

    app = build_app(args.symptoms, args.age, args.sex)
    history = app.run(max_turns=args.turns, context={"age": args.age, "sex": args.sex})

    print("\n" + "="*60)
    print("AutoMed Demo Conversation Complete")
    print(DISCLAIMER)

if __name__ == "__main__":
    main()
