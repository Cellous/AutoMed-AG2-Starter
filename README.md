# AutoMed-AG2-Starter

> AutoMed-AG2 is a multi-agent clinical triage prototype that demonstrates coordinated agent-to-agent reasoning using a modular > orchestration architecture. The system models how healthcare decision pipelines can be structured using specialized agents
> communicating through a central coordinator. 
> ⚠️ Disclaimer: This is not medical advice — for educational use only.

## Problem Statement

Healthcare triage workflows require structured intake, evidence retrieval, reasoning, and safety validation. Traditional chatbots lack modular reasoning separation. This project explores how multi-agent coordination can simulate structured clinical reasoning workflows.

User Input
   ↓
UserAgent (symptom intake)
   ↓
DataAgent (retrieves medical knowledge / red flags)
   ↓
ClinicianAgent (LLM reasoning & assessment)
   ↓
Coordinator (orchestrates flow & safety checks)
   ↓
Structured Output + Safety Disclaimer

---

## Technical Design

- Agents implemented in Python
- YAML-based agent configuration
- Mock LLM provider (pluggable for OpenAI/AutoGen)
- Structured output formatting
- Command-line interface for reproducible runs

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
