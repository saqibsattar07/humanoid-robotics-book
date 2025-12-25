---
description: "Task list for Physical AI & Humanoid Robotics — Unified Docusaurus UI with Embedded RAG Chatbot implementation"
---

# Tasks: Physical AI & Humanoid Robotics — Unified Docusaurus UI with Embedded RAG Chatbot

**Input**: Design documents from `/specs/001-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Tests**: The feature specification does not explicitly request test tasks, so they are not included in this implementation.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `humanoid-textbook/src/`
- Paths based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in backend/ and humanoid-textbook/
- [ ] T002 Set up Git repository with proper .gitignore for Python, Node.js, and IDE files
- [ ] T003 Configure development environment with Python 3.11 and Node.js
- [ ] T004 Install and configure Docusaurus in humanoid-textbook directory
- [ ] T005 [P] Set up backend project structure with FastAPI
- [ ] T006 [P] Initialize package.json with required dependencies for frontend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

### Design System Setup
- [ ] T007 Configure Tailwind CSS in Docusaurus per plan requirements
- [ ] T008 Define global design tokens with specified color palette (Primary: #4f8cff, Background: #0b0f1a, etc.)
- [ ] T009 Set up typography with Inter font for headings/body and JetBrains Mono for code
- [ ] T010 Install and configure shadcn/ui components in Docusaurus project
- [ ] T011 Set up Framer Motion for animations in Docusaurus components
- [ ] T012 Create custom CSS file with Tailwind and custom styles in humanoid-textbook/src/css/custom.css
- [ ] T013 Validate styling decisions with design system requirements

### Backend Foundation
- [ ] T014 Set up FastAPI application structure in backend/src
- [ ] T015 Create configuration management for OpenRouter API models
- [ ] T016 Implement basic API endpoints structure
- [ ] T017 Set up database connections for Qdrant and Neon Postgres
- [ ] T018 Create basic models for document chunks and metadata
- [ ] T019 Setup Qdrant Cloud collection for document chunks
- [ ] T020 Setup Neon Postgres database schema for citations and metadata

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Full Book Question Answering (Priority: P1) 🎯 MVP

**Goal**: Student asks a question about the Physical AI & Humanoid Robotics book content and receives an accurate, grounded answer with proper citations to the relevant chapters/modules.

**Independent Test**: Can be fully tested by submitting various questions about different book topics and verifying that responses are accurate, relevant, properly cited to specific modules/chapters, and contain zero hallucinations.

### Implementation for User Story 1

- [ ] T021 [P] [US1] Create DocumentChunk model in backend/src/models/document_chunk.py
- [ ] T022 [P] [US1] Create Query model in backend/src/models/query.py
- [ ] T023 [P] [US1] Create QueryResponse model in backend/src/models/query_response.py
- [ ] T024 [P] [US1] Create Citation model in backend/src/models/citation.py
- [ ] T025 [P] [US1] Create Agent model in backend/src/models/agent.py
- [ ] T026 [US1] Implement embedding service in backend/src/services/embedding_service.py
- [ ] T027 [US1] Implement Qdrant service in backend/src/services/qdrant_service.py
- [ ] T028 [US1] Implement retrieval service in backend/src/services/retrieval_service.py
- [ ] T029 [US1] Implement citation service in backend/src/services/citation_service.py
- [ ] T030 [US1] Implement basic LLM service with OpenRouter integration in backend/src/services/llm_service.py
- [ ] T031 [US1] Create RAG tool for OpenAI Agent in backend/src/tools/rag_tool.py
- [ ] T032 [US1] Create citation tool for OpenAI Agent in backend/src/tools/citation_tool.py
- [ ] T033 [US1] Implement agent service with OpenAI Agent SDK in backend/src/services/agent_service.py
- [ ] T034 [US1] Implement chat endpoint for full-book queries in backend/src/api/v1/chat.py
- [ ] T035 [US1] Implement grounding validation to prevent hallucinations in backend/src/services/validation_service.py
- [ ] T036 [P] [US1] Create Chatbot component in humanoid-textbook/src/components/Chatbot/Chatbot.tsx
- [ ] T037 [P] [US1] Create ChatWindow component in humanoid-textbook/src/components/Chatbot/ChatWindow.tsx
- [ ] T038 [P] [US1] Create MessageBubble component with specified styling in humanoid-textbook/src/components/Chatbot/MessageBubble.tsx
- [ ] T039 [P] [US1] Create CitationCard component for mini cards in humanoid-textbook/src/components/Chatbot/CitationCard.tsx
- [ ] T040 [P] [US1] Create API client for chat functionality in humanoid-textbook/src/services/apiClient.ts
- [ ] T041 [US1] Connect frontend to backend API endpoints
- [ ] T042 [US1] Add typing indicators with Framer Motion animations
- [ ] T043 [US1] Test full book question answering with proper citations

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Selected Text Question Answering (Priority: P2)

**Goal**: Student selects specific text from the book and asks a question about only that selected text. The system answers based solely on the selected text without retrieving from the broader book context, using the same ChatKit-style UI maintained from the existing design.

**Independent Test**: Can be tested by selecting text portions and asking targeted questions, verifying that responses only reference the selected text and not the broader book, with consistent ChatKit-style UI.

### Implementation for User Story 2

- [ ] T044 [P] [US2] Update Query model to support selected-text context in backend/src/models/query.py
- [ ] T045 [US2] Enhance retrieval service to handle selected-text queries in backend/src/services/retrieval_service.py
- [ ] T046 [US2] Implement selected-text query routing logic in backend/src/services/agent_service.py
- [ ] T047 [US2] Add context isolation for selected-text queries in backend/src/services/retrieval_service.py
- [ ] T048 [US2] Update chat endpoint to handle selected-text queries in backend/src/api/v1/chat.py
- [ ] T049 [P] [US2] Create TextSelector component for selected text processing in humanoid-textbook/src/components/Chatbot/TextSelector.tsx
- [ ] T050 [P] [US2] Update Chatbot component to support selected-text queries in humanoid-textbook/src/components/Chatbot/Chatbot.tsx
- [ ] T051 [US2] Update API client to handle selected-text requests in humanoid-textbook/src/services/apiClient.ts
- [ ] T052 [US2] Implement selected text query interface in humanoid-textbook/src/components/Chatbot/TextSelector.tsx
- [ ] T053 [US2] Add visual feedback for selected-text mode in humanoid-textbook components
- [ ] T054 [US2] Test selected text answering with proper isolation from global search

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Model Switching Capability (Priority: P1)

**Goal**: Developer or student can switch between different LLM models (Gemini, Claude, GPT, etc.) through environment configuration without modifying agent logic, maintaining the same grounded response quality and citation behavior.

**Independent Test**: Can be tested by changing environment variables to switch models and verifying that the OpenAI Agent SDK orchestration continues to work with the same RAG flow, citations, and zero hallucination guarantees.

### Implementation for User Story 3

- [ ] T055 [P] [US3] Update LLM service to support multiple OpenRouter models in backend/src/services/llm_service.py
- [ ] T056 [US3] Implement model configuration management in backend/src/config/settings.py
- [ ] T057 [US3] Update agent service to work with different models without logic changes in backend/src/services/agent_service.py
- [ ] T058 [US3] Implement model switching validation in backend/src/services/validation_service.py
- [ ] T059 [US3] Update chat endpoint to use configurable models in backend/src/api/v1/chat.py
- [ ] T060 [P] [US3] Create model switching interface for developers in humanoid-textbook/src/components/ConfigPanel.tsx
- [ ] T061 [US3] Update API client to support model configuration in humanoid-textbook/src/services/apiClient.ts
- [ ] T062 [US3] Test model switching without touching agent logic
- [ ] T063 [US3] Validate consistent behavior across different models (Claude, GPT, etc.)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Citation and Metadata Management (Priority: P1)

**Goal**: Student receives answers with accurate citations that are properly sourced from Qdrant Cloud vector search and Neon Serverless Postgres metadata, ensuring academic integrity and traceability of information sources.

**Independent Test**: Can be tested by verifying that every answer includes proper citations sourced from the specified Qdrant Cloud and Neon Postgres infrastructure, with links to correct book sections.

### Implementation for User Story 4

- [ ] T064 [P] [US4] Enhance Citation model with full metadata support in backend/src/models/citation.py
- [ ] T065 [US4] Update citation service to retrieve from Neon Postgres in backend/src/services/citation_service.py
- [ ] T066 [US4] Implement metadata mapping between Qdrant and Neon in backend/src/services/retrieval_service.py
- [ ] T067 [US4] Enhance citation generation with proper linking in backend/src/tools/citation_tool.py
- [ ] T068 [US4] Update chat endpoint to include detailed citations in backend/src/api/v1/chat.py
- [ ] T069 [P] [US4] Enhance CitationCard component with navigation links in humanoid-textbook/src/components/Chatbot/CitationCard.tsx
- [ ] T070 [P] [US4] Create citation formatting utilities in humanoid-textbook/src/utils/citationFormatter.ts
- [ ] T071 [P] [US4] Update API client to handle detailed citation data in humanoid-textbook/src/services/apiClient.ts
- [ ] T072 [US4] Implement citation navigation functionality in humanoid-textbook components
- [ ] T073 [US4] Test citation accuracy and linking to original sources

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: User Story 5 - Homepage Navigation (Priority: P1)

**Goal**: Student accesses the homepage and can clearly see learning modules, click on them to navigate to specific content, and understand the learning path structure of the Physical AI & Humanoid Robotics book.

**Independent Test**: Can be tested by verifying that the homepage displays 4 module cards correctly, each with proper information, and clicking each card navigates to the correct module index page.

### Implementation for User Story 5

- [ ] T074 [P] [US5] Create hero section component with title/subtitle in humanoid-textbook/src/components/Homepage/HeroSection.tsx
- [ ] T075 [P] [US5] Implement "Start Learning" CTA button with shadcn Button and Framer Motion animation in humanoid-textbook/src/components/Homepage/HeroSection.tsx
- [ ] T076 [US5] Create scroll-to-modules functionality in humanoid-textbook/src/components/Homepage/HeroSection.tsx
- [ ] T077 [P] [US5] Implement 4-module card grid in humanoid-textbook/src/components/Homepage/ModulesGrid.tsx
- [ ] T078 [P] [US5] Create reusable ModuleCard component with hover animations in humanoid-textbook/src/components/Homepage/ModuleCard.tsx
- [ ] T079 [US5] Implement clickable navigation to module index pages in humanoid-textbook/src/components/Homepage/ModuleCard.tsx
- [ ] T080 [US5] Add Framer Motion hover animations (soft glow + slight lift) to module cards in humanoid-textbook/src/components/Homepage/ModuleCard.tsx
- [ ] T081 [US5] Ensure responsive layout across devices in humanoid-textbook/src/components/Homepage/
- [ ] T082 [US5] Validate accessibility compliance for homepage components
- [ ] T083 [US5] Test homepage navigation with 4 module cards

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: User Story 6 - Integrated Chat Experience (Priority: P1)

**Goal**: Student interacts with the embedded chatbot that feels like a native part of the book experience rather than a separate component, with consistent styling and behavior across all pages.

**Independent Test**: Can be tested by verifying that the chatbot appears consistently on all pages, uses the same design tokens as the book, and provides smooth interactions.

### Implementation for User Story 6

- [ ] T084 [P] [US6] Implement floating chat widget in bottom-right corner in humanoid-textbook/src/components/Chatbot/Chatbot.tsx
- [ ] T085 [P] [US6] Ensure consistent styling with book UI design tokens in humanoid-textbook/src/components/Chatbot/
- [ ] T086 [US6] Add smooth open/close animations with Framer Motion in humanoid-textbook/src/components/Chatbot/Chatbot.tsx
- [ ] T087 [US6] Implement global chatbot integration in Docusaurus layout in humanoid-textbook/src/components/LayoutWrapper/LayoutWrapper.tsx
- [ ] T088 [P] [US6] Create LayoutWrapper component with embedded chatbot in humanoid-textbook/src/components/LayoutWrapper/LayoutWrapper.tsx
- [ ] T089 [US6] Test chatbot visibility and functionality on all pages
- [ ] T090 [US6] Validate consistent design across all book pages
- [ ] T091 [US6] Test that chatbot feels native rather than embedded
- [ ] T092 [US6] Implement citation rendering as mini cards in chat interface
- [ ] T093 [US6] Test selected-text query highlighting functionality

**Checkpoint**: All user stories should now be independently functional

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T094 [P] Documentation updates in docs/
- [ ] T095 [P] Configuration endpoints for health and model info in backend/src/api/v1/config.py
- [ ] T096 [P] Health check endpoints in backend/src/api/v1/health.py
- [ ] T097 Error handling for Qdrant/Neon/OpenRouter failures in backend/src/services/
- [ ] T098 [P] Update quickstart guide with implementation details
- [ ] T099 [P] Frontend animation utilities in humanoid-textbook/src/utils/animation.ts
- [ ] T100 [P] Text processing utilities in humanoid-textbook/src/utils/textProcessor.ts
- [ ] T101 [P] Citation formatting utilities in humanoid-textbook/src/utils/citationFormatter.ts
- [ ] T102 Optimize UI animations to maintain 60fps performance
- [ ] T103 Optimize page load times to be under 3 seconds
- [ ] T104 Optimize chatbot response times to be under 5 seconds for 95% of queries
- [ ] T105 Validate accessibility compliance (WCAG 2.1 AA) for all components
- [ ] T106 Test responsive layout across desktop, tablet, and mobile devices
- [ ] T107 Test cross-browser compatibility (Chrome, Firefox, Safari, Edge)
- [ ] T108 Implement keyboard navigation for all interactive elements
- [ ] T109 Conduct visual consistency check across all components
- [ ] T110 Review animation subtlety to ensure they enhance clarity
- [ ] T111 Perform cross-page UI consistency validation
- [ ] T112 Execute production readiness assessment
- [ ] T113 Run comprehensive tests for zero hallucinations requirement
- [ ] T114 Test model swap functionality to verify agent logic independence
- [ ] T115 Validate all acceptance criteria from spec are met

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May build on US1 models/services but should be independently testable
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - May build on US1 services but should be independently testable
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - Independent of backend functionality
- **User Story 6 (P1)**: Can start after Foundational (Phase 2) - Depends on US1, US2, US4 for complete chat functionality

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all models for User Story 1 together:
Task: "Create DocumentChunk model in backend/src/models/document_chunk.py"
Task: "Create Query model in backend/src/models/query.py"
Task: "Create QueryResponse model in backend/src/models/query_response.py"
Task: "Create Citation model in backend/src/models/citation.py"
Task: "Create Agent model in backend/src/models/agent.py"

# Launch all frontend components for User Story 1 together:
Task: "Create Chatbot component in humanoid-textbook/src/components/Chatbot/Chatbot.tsx"
Task: "Create ChatWindow component in humanoid-textbook/src/components/Chatbot/ChatWindow.tsx"
Task: "Create MessageBubble component with specified styling in humanoid-textbook/src/components/Chatbot/MessageBubble.tsx"
Task: "Create CitationCard component for mini cards in humanoid-textbook/src/components/Chatbot/CitationCard.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Add User Story 6 → Test independently → Deploy/Demo
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
   - Developer F: User Story 6
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence