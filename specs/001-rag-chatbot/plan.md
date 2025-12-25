# Implementation Plan: Physical AI & Humanoid Robotics — Unified Docusaurus UI with Embedded RAG Chatbot

**Branch**: `001-rag-chatbot` | **Date**: 2025-12-23 | **Spec**: [specs/001-rag-chatbot/spec.md](spec.md)
**Input**: Feature specification from `/specs/001-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a unified UI/UX for the Physical AI & Humanoid Robotics book where the homepage, book pages, and embedded RAG chatbot all feel like one consistent product. The solution includes a Docusaurus-based documentation site with Tailwind CSS, shadcn/ui components, and Framer Motion animations for a cohesive design language. The RAG chatbot will be seamlessly integrated with the book interface, providing students with a native study assistant experience. The architecture includes a Docusaurus-integrated UI, FastAPI backend with OpenAI Agent SDK orchestration, OpenRouter API for flexible LLM access, Qdrant Cloud for vector search, and Neon Postgres for citation metadata.

## Technical Context

**Language/Version**: Python 3.11, TypeScript/JavaScript for frontend
**Primary Dependencies**: Docusaurus, Tailwind CSS, shadcn/ui, Framer Motion, FastAPI, OpenAI Agent SDK, OpenRouter API, Qdrant client, Neon Postgres connector
**Storage**: Qdrant Cloud (vector storage), Neon Postgres (citations & metadata)
**Testing**: pytest for backend, Jest for frontend
**Target Platform**: Web application (browser-based, Docusaurus embedded)
**Project Type**: Web (frontend + backend)
**Performance Goals**: <5s response time for 95% of queries, handle 100 concurrent users, <500ms retrieval time, 60fps animations
**Constraints**: Zero hallucinations, model switching via env vars, no external internet content, ChatKit UI consistency, unified design language
**Scale/Scope**: 10k+ book content chunks, 1000+ students, 99% uptime during academic periods

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on project constitution and feature requirements, the system must:
- Ensure all responses are grounded in retrieved context only (zero hallucinations)
- Provide proper citations to book modules/chapters via Neon Postgres metadata
- Handle selected-text queries without global search contamination using OpenAI Agent SDK
- Maintain visual consistency across book + chatbot with unified design system
- Support model switching via OpenRouter API without touching agent logic
- Follow accessibility guidelines for educational content (WCAG 2.1 AA)
- Integrate seamlessly with Docusaurus documentation site
- Implement cohesive design language using specified color palette (#4f8cff primary, #0b0f1a background, etc.) and typography (Inter, JetBrains Mono)
- Ensure minimal cognitive load with clean, focused design
- Use subtle animations that enhance clarity, not distract (Framer Motion)
- Create floating chatbot widget that feels native, not embedded

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   ├── document_chunk.py      # Content chunk representations
│   │   ├── metadata.py           # Book metadata models
│   │   ├── query.py              # Query request/response models
│   │   └── agent.py              # OpenAI Agent SDK models
│   ├── services/
│   │   ├── retrieval_service.py  # RAG retrieval logic
│   │   ├── embedding_service.py  # Embedding generation
│   │   ├── citation_service.py   # Citation generation
│   │   ├── llm_service.py        # OpenRouter API interaction
│   │   ├── agent_service.py      # OpenAI Agent SDK orchestration
│   │   └── qdrant_service.py     # Qdrant Cloud integration
│   ├── tools/
│   │   ├── rag_tool.py           # Custom RAG tool for OpenAI Agent
│   │   └── citation_tool.py      # Citation generation tool
│   ├── api/
│   │   ├── v1/
│   │   │   ├── chat.py           # Chat endpoints with agent integration
│   │   │   ├── retrieval.py      # Retrieval endpoints
│   │   │   ├── health.py         # Health check endpoints
│   │   │   └── config.py         # Configuration endpoints
│   │   └── dependencies.py       # API dependencies
│   └── config/
│       ├── settings.py           # Configuration settings
│       ├── database.py           # Database connections
│       └── agent_config.py       # OpenAI Agent SDK configuration
└── tests/
    ├── unit/
    ├── integration/
    └── contract/

humanoid-textbook/
├── src/
│   ├── components/
│   │   ├── Chatbot/              # Embedded RAG chatbot components
│   │   │   ├── Chatbot.tsx       # Main chatbot widget
│   │   │   ├── ChatWindow.tsx    # Chat window interface
│   │   │   ├── MessageBubble.tsx # Message display components
│   │   │   └── CitationCard.tsx  # Citation rendering component
│   │   ├── Homepage/             # Homepage UI components
│   │   │   ├── HeroSection.tsx   # Hero section with title/subtitle
│   │   │   ├── ModuleCard.tsx    # Module card with hover animations
│   │   │   └── ModulesGrid.tsx   # Grid layout for module cards
│   │   └── LayoutWrapper/        # Docusaurus layout extensions
│   │       └── LayoutWrapper.tsx # Layout with embedded chatbot
│   ├── theme/                    # Docusaurus theme customization
│   │   └── *                     # Custom theme components
│   ├── css/
│   │   └── custom.css            # Tailwind and custom styles
│   └── static/
│       └── img/                  # Static assets
└── docusaurus.config.js          # Docusaurus configuration
```

**Structure Decision**: Selected integrated approach with embedded frontend components in Docusaurus to ensure unified UI/UX across homepage, book pages, and chatbot. Backend handles OpenAI Agent SDK orchestration, RAG logic, and LLM integration via OpenRouter API, while Docusaurus frontend with Tailwind CSS, shadcn/ui, and Framer Motion provides consistent UI for student interactions.

## Architecture Implementation Phases

### Phase 1: Context7 Design Research
- Query Context7 MCP server for modern documentation UI layouts
- Research Tailwind + shadcn/ui patterns for docs
- Investigate Framer Motion usage in technical products
- Study dark-mode accessibility standards
- Document all design decisions and tradeoffs

### Phase 2: Design System Setup
- Configure Tailwind CSS in Docusaurus
- Define global design tokens:
  - Colors (Primary: #4f8cff, Background: #0b0f1a, Card: #12172a, etc.)
  - Typography (Inter for headings/body, JetBrains Mono for code)
  - Spacing and sizing
- Install and configure shadcn/ui components
- Set up Framer Motion for animations
- Validate styling decisions with Context7 references

### Phase 3: Homepage Implementation
- Implement Hero section with title "Physical AI & Humanoid Robotics" and subtitle "From Digital Intelligence to Embodied Machines"
- Implement "Start Learning" CTA button with shadcn Button and Framer Motion hover + tap animation
- Implement scroll-to-modules functionality
- Implement 4-module card grid
- Create reusable ModuleCard component with:
  - Module number, title, and one-line description
  - Clickable navigation to module index pages
  - Framer Motion hover animations (soft glow + slight lift)
- Ensure responsive layout across devices
- Validate accessibility compliance

### Phase 4: RAG Chatbot UI Integration
- Implement floating chat widget in bottom-right corner
- Create chat interface using shadcn/ui components
- Apply same Tailwind tokens as book (consistent color palette)
- Implement message bubbles with:
  - User messages in primary blue
  - Bot messages in dark indigo
- Create citation rendering as mini cards
- Add Framer Motion animations for:
  - Smooth open/close transitions
  - Typing indicators
  - Subtle response animations
- Connect UI to existing FastAPI backend
- Implement selected-text query highlighting

### Phase 5: Polish & Validation
- Visual consistency check across all components
- Animation subtlety review to ensure they enhance clarity
- Performance validation (60fps animations, load times <3s)
- Accessibility review (WCAG 2.1 AA compliance)
- Cross-page UI consistency validation
- Production readiness assessment

## Architectural Decisions to Document

### Design System Integration
- Decision: Implement unified design system with Tailwind CSS, shadcn/ui, and Framer Motion for consistent UI/UX
- Rationale: Ensures visual consistency across homepage, book pages, and chatbot as required by specifications
- Trade-offs: Initial setup complexity but provides maintainable and consistent user experience

### Docusaurus-Embedded Architecture
- Decision: Embed chatbot UI directly in Docusaurus layout instead of separate frontend
- Rationale: Creates seamless integration where chatbot feels native rather than embedded
- Trade-offs: Requires Docusaurus customization but achieves unified product experience

### OpenRouter API Integration
- Decision: Use OpenRouter API as LLM provider instead of hardcoded models
- Rationale: Enables model switching without touching agent logic, avoids vendor lock-in
- Trade-offs: Requires API key management but provides flexibility for cost/performance optimization

### Framer Motion Animation Strategy
- Decision: Use Framer Motion for subtle animations that enhance clarity rather than distract
- Rationale: Aligns with academic tone and minimal cognitive load requirements
- Trade-offs: Additional bundle size but provides smooth, professional interactions

### Context7 MCP Server Usage
- Decision: Integrate Context7 MCP server for documentation UI patterns and component design
- Rationale: Ensures modern, proven UI/UX patterns based on documentation-grade standards
- Trade-offs: Additional dependency but provides validated design decisions

## Validation Strategy

### Functional Validation
- Implement strict content filtering to reject answers not grounded in retrieved context
- Create "not found" response handling for empty context scenarios
- Add comprehensive error handling for Qdrant/Neon/OpenRouter failures
- Implement model swap tests to verify agent logic independence
- Set up automated testing for all critical paths including selected-text queries
- Test zero hallucinations requirement with out-of-scope queries

### UI/UX Validation
- Verify visual consistency across all pages using design tokens
- Test responsive layout across desktop, tablet, and mobile devices
- Validate accessibility compliance (WCAG 2.1 AA) for all components
- Confirm 60fps animation performance for Framer Motion components
- Test cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- Validate floating chatbot widget visibility and functionality on all pages
- Verify module card click functionality and navigation
- Test scroll-to-modules functionality from CTA button
- Confirm citation rendering as mini cards in chat interface
- Validate selected-text query highlighting functionality

### Performance Validation
- Measure page load times (must be under 3 seconds)
- Test chatbot response times (must be under 5 seconds for 95% of queries)
- Verify animation performance maintains 60fps
- Test concurrent user handling (up to 100 concurrent users)
- Validate retrieval performance (under 500ms)

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific need] | [why direct DB access insufficient] |