
# AutoMed (AG2) — Talking Points

- **Goal**: Demonstrate a small multi‑agent system for healthcare triage using AG2/AutoGen concepts.
- **Agents**:
  - *UserAgent*: captures user input once.
  - *ClinicianAgent*: uses LLM reasoning to draft assessment, red‑flags, and next steps.
  - *DataAgent*: tool‑using agent that queries a mock medical database.
- **Coordinator**: round‑robin turn‑taking to simulate agent‑to‑agent communication.
- **LLM Integration**: abstracted in `llm.py`; default provider is **MOCK** so demo runs without keys; can be swapped to class provider.
- **Safety**: every run prints a clear **disclaimer**; mock DB includes red‑flag advice.
- **Mapping to Objectives**:
  1) Discuss multi‑agent systems → separation of roles & coordinator.  
  2) Explore LLM integration → replaceable `generate()` implementation.  
  3) Implement agent‑to‑agent communication → message history passed across agents.  
  4) Develop multiple agents → distinct classes with healthcare‑specific tasks.
- **Limitations**: mock data only; not HIPAA‑ready; not for clinical use.
