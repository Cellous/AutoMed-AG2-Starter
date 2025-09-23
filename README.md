# AutoMed-AG2-Starter

> Educational demo project based on **AG2 (AutoGen)** concepts.  
> Built for DeVry University / IBM Skills Network guided project.  
> ⚠️ Disclaimer: This is not medical advice — for educational use only.

## Features
- Multi-agent architecture with:
  - **UserAgent** (inputs symptoms)
  - **DataAgent** (queries mock medical DB + red-flags)
  - **ClinicianAgent** (LLM reasoning for assessments/recommendations)
- Coordinator enabling **agent-to-agent communication**
- Pluggable LLM integration (default = MOCK, swap with OpenAI/AutoGen in `llm.py`)
- Clear **safety disclaimer** in all outputs

## Demo
```bash
python main.py --symptoms "sore throat, mild fever, cough" --age 35 --sex M
