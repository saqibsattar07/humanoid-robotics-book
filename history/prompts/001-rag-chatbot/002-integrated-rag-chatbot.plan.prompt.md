---
id: 002
title: Integrated RAG Chatbot Plan
stage: plan
date: 2025-12-21
surface: agent
model: claude-sonnet-4-5-20250929
feature: rag-chatbot
branch: 001-rag-chatbot
user: saqib
command: sp.plan
labels: ["rag", "chatbot", "docusaurus", "ai", "textbook", "architecture"]
links:
  spec: specs/001-rag-chatbot/spec.md
  plan: specs/001-rag-chatbot/plan.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-rag-chatbot/plan.md
 - specs/001-rag-chatbot/checklists/plan-requirements.md
tests:
 - plan alignment with feature spec verified
 - architecture phases match user requirements
 - quality checklist confirms plan standards
---

## Prompt

Architecture:
- Frontend: Docusaurus + ChatKit-style UI
- Backend: FastAPI + OpenAI Agent SDK
- LLM access: OpenRouter API
- Retrieval: Qdrant + Neon

Phases:
1. Foundation
   - Environment setup
   - MCP servers connected
   - UI preserved

2. Retrieval
   - Chunking
   - Embeddings
   - Citation mapping

3. Agent Layer
   - OpenAI Agent SDK
   - Custom LLM tool using OpenRouter
   - Strict grounding prompt

4. API Layer
   - /chat endpoint
   - Selected-text routing
   - Citation generation

5. Frontend
   - Same ChatKit UI
   - Animated responses
   - Citation chips

Key decisions:
- OpenRouter used to avoid vendor lock-in
- Agent SDK controls logic, not the model
- MCP servers used for correctness & repo safety

Testing:
- Selected-text-only queries
- Out-of-scope queries
- Model swap tests (Gemini ↔ Claude)

## Response snapshot

Created comprehensive implementation plan for the Integrated RAG Chatbot for Docusaurus AI Textbook. The plan includes:

- Architecture alignment with all specified technologies (Docusaurus + ChatKit UI, FastAPI + OpenAI Agent SDK, OpenRouter API, Qdrant + Neon)
- 5-phase implementation approach matching user requirements (Foundation, Retrieval, Agent Layer, API Layer, Frontend)
- Detailed project structure with backend and frontend components
- Technical context specifying Python 3.11, TypeScript/JavaScript, and all required dependencies
- Architecture decisions for OpenRouter integration, OpenAI Agent SDK orchestration, and MCP server usage
- Validation strategy for zero hallucinations, model switching, and selected-text queries
- Quality checklist confirming all validation items completed

The plan addresses all requirements from the user's architecture specification and aligns with the feature specification.

## Outcome

- ✅ Impact: Complete implementation plan created that captures all architecture requirements from the user command
- 🧪 Tests: Plan validated against feature requirements with all items confirmed
- 📁 Files: plan.md and plan-requirements checklist created/updated in feature directory
- 🔁 Next prompts: Ready to proceed with /sp.tasks for task breakdown
- 🧠 Reflection: Plan successfully captures complex architecture including OpenAI Agent SDK orchestration and OpenRouter flexibility

## Evaluation notes (flywheel)

- Failure modes observed: None - all requirements successfully incorporated
- Graders run and results (PASS/FAIL): PASS - all quality criteria met
- Prompt variant (if applicable): Standard plan creation prompt
- Next experiment (smallest change to try): Proceed with task generation