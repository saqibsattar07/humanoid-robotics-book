# ADR-001: Tech Stack and Architecture Decision for Docusaurus Book with RAG Chatbot

## Status
Accepted

## Date
2025-12-23

## Context
The Physical AI & Humanoid Robotics book requires a cohesive learning platform that integrates a Docusaurus-based textbook with an embedded RAG chatbot. Students need to access book content through natural language queries while maintaining academic integrity with proper citations. The system must provide a unified UI/UX experience where the homepage, book pages, and chatbot feel like one consistent product.

## Decision
We will implement a technology stack consisting of:

- **Frontend**: Docusaurus (existing framework) with Tailwind CSS, shadcn/ui components, and Framer Motion for animations
- **Backend**: FastAPI with OpenAI Agent SDK for orchestration, OpenRouter API for flexible LLM access
- **Storage**: Qdrant Cloud for vector search, Neon Serverless Postgres for citations and metadata
- **UI Components**: shadcn/ui for consistent design, Framer Motion for subtle animations
- **Deployment**: Embedded within Docusaurus layout (no separate frontend)

This integrated approach ensures visual consistency across all components while providing robust RAG functionality with zero hallucinations.

## Consequences
### Positive
- Unified design language across all components using consistent color palette (#4f8cff primary, #0b0f1a background, etc.) and typography (Inter, JetBrains Mono)
- Seamless user experience with floating chatbot widget that feels native to the book interface
- Model switching capability via environment variables without touching agent logic
- Proper academic citations with metadata stored in Neon Postgres
- Scalable architecture with Qdrant Cloud handling vector search for 10k+ content chunks
- Accessibility compliance for educational content

### Negative
- Complex architecture requiring coordination between multiple services (Qdrant, Neon, OpenRouter, OpenAI Agent SDK)
- Increased deployment complexity compared to simpler solutions
- Dependency on multiple external services (Qdrant Cloud, Neon Postgres, OpenRouter API)
- Steeper learning curve for developers unfamiliar with OpenAI Agent SDK

## Alternatives
### Alternative 1: Separate Frontend Application
- Approach: Create a separate React/Vue frontend for the chatbot with independent deployment
- Trade-offs: Would allow independent scaling and development but would break the unified UI/UX requirement and increase complexity of maintaining consistent design

### Alternative 2: Direct LLM Integration
- Approach: Use direct LLM API calls instead of OpenAI Agent SDK orchestration
- Trade-offs: Simpler implementation but less control over grounding and potential for hallucinations without proper tool orchestration

### Alternative 3: Self-hosted Vector Database
- Approach: Host vector database locally instead of using Qdrant Cloud
- Trade-offs: More control over data but increased operational overhead and scaling challenges

### Alternative 4: Traditional Search Instead of RAG
- Approach: Use traditional keyword search instead of vector search
- Trade-offs: Simpler but would not provide the semantic understanding needed for natural language queries

## References
- specs/001-rag-chatbot/spec.md
- specs/001-rag-chatbot/plan.md
- CLAUDE.md project instructions