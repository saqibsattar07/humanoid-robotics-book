---
id: 001
title: Create Initial Project Constitution
stage: constitution
date: 2025-12-17
surface: agent
model: Gemini
feature: none
branch: 004-vla-capstone
user: user
command: /sp.constitution
labels: ["constitution", "initialization"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - "No tests run"
---

## Prompt

/sp.constitution

Project: Integrated RAG Chatbot for a Docusaurus-Based AI Book

Core Principles:
- Zero hallucination (answers must be grounded in book content)
- Transparency through citations
- Reproducibility and traceability
- Clear student-facing explanations

Standards:
- All answers must reference retrieved book sections
- Selected-text Q&A must restrict context strictly
- No external knowledge allowed during generation
- Chunk metadata must include source location

Constraints:
- Stack: OpenAI Agents/ChatKit, FastAPI, Qdrant, Neon Postgres
- UI embedded inside Docusaurus
- Hallucination tolerance: 0%

Success Criteria:
- Accurate answers grounded in book text
- Selected-text Q&A works reliably
- Citations always present

## Response snapshot

I have successfully updated the project constitution.

- **New Version**: 1.0.0
- **Rationale**: Initial creation of the project constitution.
- **Files updated**:
    - `.specify/memory/constitution.md`
- **Follow-up**:
    - Please set the `RATIFICATION_DATE` in `.specify/memory/constitution.md`.

## Outcome

- ✅ Impact: Created the initial project constitution, establishing foundational principles for the project.
- 🧪 Tests: No tests were run for this operation.
- 📁 Files: Created and wrote to `.specify/memory/constitution.md`.
- 🔁 Next prompts: The user may want to proceed with other setup tasks or begin development.
- 🧠 Reflection: The process of creating a constitution from user input is a good way to establish clear guidelines from the start.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): N/A
