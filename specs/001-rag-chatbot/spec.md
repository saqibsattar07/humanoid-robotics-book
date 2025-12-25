# 001-rag-chatbot: Physical AI & Humanoid Robotics — Docusaurus Book with Embedded RAG Chatbot

## 1. Overview

### 1.1 Purpose
Create a premium, unified UI/UX for a Docusaurus-based robotics book where the homepage, book pages, and embedded RAG chatbot all feel like one consistent product. The solution will provide an integrated learning experience for students and researchers in physical AI and humanoid robotics.

### 1.2 Goal
Develop a cohesive Docusaurus-based book with an embedded RAG chatbot that serves as a native study assistant, providing contextual help and information retrieval for the robotics content.

### 1.3 Target Audience
- AI & Robotics students
- Technical readers (CS / AI background)
- Educators & researchers

### 1.4 User Experience Goals
- Academic tone with futuristic aesthetic
- Calm, focused learning environment
- High-signal, low-noise interface

## 2. Requirements

### 2.1 Functional Requirements

#### 2.1.1 Homepage UI
- **RAG-REQ-001**: Homepage must feature a hero section with title "Physical AI & Humanoid Robotics" and subtitle "From Digital Intelligence to Embodied Machines"
- **RAG-REQ-002**: Hero section must include a primary CTA button labeled "Start Learning" that scrolls to the Modules section
- **RAG-REQ-003**: Modules section must display a grid of exactly 4 module cards
- **RAG-REQ-004**: Each module card must show module number, title, and one-line description
- **RAG-REQ-005**: Each module card must be clickable and navigate to the corresponding module index page
- **RAG-REQ-006**: Module cards must use shadcn Card components with hover animations (soft glow + slight lift)

#### 2.1.2 RAG Chatbot UI
- **RAG-REQ-007**: Chatbot must appear as a floating widget in the bottom-right corner, visible on all pages
- **RAG-REQ-008**: Chatbot must be built with shadcn/ui components using the same Tailwind tokens as the book
- **RAG-REQ-009**: Chat window header must match Docusaurus navbar style
- **RAG-REQ-010**: Message bubbles must be styled with user messages in primary blue and bot messages in dark indigo
- **RAG-REQ-011**: Citations must be rendered as mini cards within the chat interface
- **RAG-REQ-012**: Selected-text queries must be clearly highlighted
- **RAG-REQ-013**: Chatbot must have smooth open/close animations and typing indicators

#### 2.1.3 Content Navigation
- **RAG-REQ-014**: All modules must be accessible through the homepage module grid
- **RAG-REQ-015**: Module index pages must provide clear navigation to specific topics within each module

#### 2.1.4 RAG Functionality
- **RAG-REQ-016**: System MUST answer student questions based only on retrieved context from the Physical AI & Humanoid Robotics book content with zero hallucinations
- **RAG-REQ-017**: System MUST distinguish between full-book queries and selected-text queries to prevent context mixing
- **RAG-REQ-018**: System MUST provide accurate citations showing the specific module/chapter where answer information originated
- **RAG-REQ-019**: System MUST process selected-text queries without using global book search functionality
- **RAG-REQ-020**: System MUST integrate with OpenRouter API as the LLM provider instead of hardcoding specific models
- **RAG-REQ-021**: System MUST allow model switching via environment configuration without modifying agent logic
- **RAG-REQ-022**: System MUST use OpenAI Agent SDK for tool orchestration, prompt enforcement, and RAG flow control
- **RAG-REQ-023**: System MUST store document embeddings in Qdrant Cloud for vector similarity search
- **RAG-REQ-024**: System MUST store citations and metadata in Neon Serverless Postgres database
- **RAG-REQ-025**: System MUST embed the chatbot interface globally in Docusaurus documentation site
- **RAG-REQ-026**: System MUST reject questions that cannot be answered from the book content with appropriate response instead of hallucinating
- **RAG-REQ-027**: System MUST provide clear indication when retrieved context is insufficient for answering
- **RAG-REQ-028**: System MUST ensure all responses contain citations to book content (no citation-free responses)
- **RAG-REQ-029**: System MUST handle failure scenarios gracefully when Qdrant Cloud or Neon Postgres are unavailable
- **RAG-REQ-030**: System MUST ensure no web search or external information is used in responses (book-only content)

### 2.2 Non-Functional Requirements

#### 2.2.1 Performance
- **RAG-NFR-001**: Page load time must be under 3 seconds on standard broadband
- **RAG-NFR-002**: Chatbot response time must be under 5 seconds for typical queries
- **RAG-NFR-003**: UI animations must maintain 60fps performance

#### 2.2.2 Usability
- **RAG-NFR-004**: Interface must follow accessibility standards (WCAG 2.1 AA)
- **RAG-NFR-005**: UI must maintain visual consistency across all pages
- **RAG-NFR-006**: Cognitive load must be minimized with clean, focused design

#### 2.2.3 Compatibility
- **RAG-NFR-007**: Must work on all modern browsers (Chrome, Firefox, Safari, Edge)
- **RAG-NFR-008**: Must be responsive across desktop, tablet, and mobile devices

## 3. Design System

### 3.1 Color Palette
- Primary: #4f8cff
- Background: #0b0f1a
- Card: #12172a
- Accent: #6ee7ff
- Text Primary: #e5e7eb
- Text Muted: #9ca3af

### 3.2 Typography
- Headings + Body: Inter font
- Code: JetBrains Mono font

### 3.3 Components
- shadcn/ui component library
- Framer Motion for animations
- Tailwind CSS for styling

## 4. Technical Architecture

### 4.1 Tech Stack
- Docusaurus (existing framework)
- Tailwind CSS
- shadcn/ui
- Framer Motion
- No separate frontend
- Chatbot UI embedded inside Docusaurus Layout

### 4.2 Implementation Constraints
- No separate chatbot frontend
- No inconsistent colors or fonts
- No marketing-style visuals
- No heavy animation libraries
- Everything must live inside Docusaurus

## 5. User Scenarios & Testing

### 5.1 User Story 1 - Full Book Question Answering (Priority: P1)

Student asks a question about the Physical AI & Humanoid Robotics book content and receives an accurate, grounded answer with proper citations to the relevant chapters/modules. The system retrieves relevant context from the entire book and generates responses based solely on that context with zero hallucinations.

**Why this priority**: This is the core functionality that enables students to interact with the entire book content through natural language queries, providing the primary value proposition of the RAG system with guaranteed grounding in the book content.

**Independent Test**: Can be fully tested by submitting various questions about different book topics and verifying that responses are accurate, relevant, properly cited to specific modules/chapters, and contain zero hallucinations.

**Acceptance Scenarios**:

1. **Given** student accesses the ChatKit-style RAG chatbot interface embedded in Docusaurus, **When** student submits a question about book content, **Then** system responds with an accurate answer citing specific chapters/modules from the book with no external information
2. **Given** student asks a complex question requiring information from multiple book sections, **When** system processes the query using OpenAI Agent SDK orchestration, **Then** response synthesizes information from relevant sections with proper citations and zero hallucinations

---

### 5.2 User Story 2 - Selected Text Question Answering (Priority: P2)

Student selects specific text from the book and asks a question about only that selected text. The system answers based solely on the selected text without retrieving from the broader book context, using the same ChatKit-style UI maintained from the existing design.

**Why this priority**: This provides focused assistance for specific passages students are studying, preventing confusion between selected text and broader book context during study sessions while maintaining UI consistency.

**Independent Test**: Can be tested by selecting text portions and asking targeted questions, verifying that responses only reference the selected text and not the broader book, with consistent ChatKit-style UI.

**Acceptance Scenarios**:

1. **Given** student highlights specific text in the Docusaurus textbook, **When** student asks a question about that text using the ChatKit-style interface, **Then** response is generated only from the selected text context without global search
2. **Given** student selects a paragraph about a specific concept in the Physical AI & Humanoid Robotics book, **When** student asks for clarification, **Then** system provides explanation based only on the selected text with proper citations

---

### 5.3 User Story 3 - Model Switching Capability (Priority: P1)

Developer or student can switch between different LLM models (Gemini, Claude, GPT, etc.) through environment configuration without modifying agent logic, maintaining the same grounded response quality and citation behavior.

**Why this priority**: This provides flexibility in LLM selection without requiring code changes, enabling optimal performance and cost management while maintaining consistent behavior across different models.

**Independent Test**: Can be tested by changing environment variables to switch models and verifying that the OpenAI Agent SDK orchestration continues to work with the same RAG flow, citations, and zero hallucination guarantees.

**Acceptance Scenarios**:

1. **Given** system configured with one LLM model via OpenRouter API, **When** environment variables change to select a different model, **Then** agent logic remains unchanged and system continues to provide grounded responses with citations
2. **Given** developer wants to switch from Claude to GPT model, **When** updating environment configuration, **Then** system uses new model without code changes while maintaining zero hallucinations and citation accuracy

---

### 5.4 User Story 4 - Citation and Metadata Management (Priority: P1)

Student receives answers with accurate citations that are properly sourced from Qdrant Cloud vector search and Neon Serverless Postgres metadata, ensuring academic integrity and traceability of information sources.

**Why this priority**: This ensures academic integrity and allows students to verify information by referring to original sources, while leveraging the specified technology stack for reliable metadata management.

**Independent Test**: Can be tested by verifying that every answer includes proper citations sourced from the specified Qdrant Cloud and Neon Postgres infrastructure, with links to correct book sections.

**Acceptance Scenarios**:

1. **Given** student receives an answer from the chatbot, **When** reviewing the response, **Then** answer includes accurate citations sourced from Qdrant Cloud vector search and Neon Postgres metadata
2. **Given** system retrieves information from book content, **When** generating response, **Then** all citations are properly linked to original book sections with metadata from Neon Postgres

---

### 5.5 User Story 5 - Homepage Navigation (Priority: P1)

Student accesses the homepage and can clearly see learning modules, click on them to navigate to specific content, and understand the learning path structure of the Physical AI & Humanoid Robotics book.

**Why this priority**: This provides the primary entry point and navigation structure for students to access different modules of the book content in a structured way.

**Independent Test**: Can be tested by verifying that the homepage displays 4 module cards correctly, each with proper information, and clicking each card navigates to the correct module index page.

**Acceptance Scenarios**:

1. **Given** student accesses the homepage, **When** viewing the modules section, **Then** 4 module cards are displayed with module number, title, and description
2. **Given** student clicks on a module card, **When** the click action occurs, **Then** the system navigates to the corresponding module index page
3. **Given** student hovers over module cards, **When** hover action occurs, **Then** smooth animations trigger (soft glow and slight lift)

---

### 5.6 User Story 6 - Integrated Chat Experience (Priority: P1)

Student interacts with the embedded chatbot that feels like a native part of the book experience rather than a separate component, with consistent styling and behavior across all pages.

**Why this priority**: This ensures the chatbot enhances the learning experience without disrupting the book's cohesive design and user flow.

**Independent Test**: Can be tested by verifying that the chatbot appears consistently on all pages, uses the same design tokens as the book, and provides smooth interactions.

**Acceptance Scenarios**:

1. **Given** student is on any page of the book, **When** viewing the page, **Then** the floating chatbot widget appears in the bottom-right corner
2. **Given** student opens the chat interface, **When** interacting with the chat, **Then** the UI uses consistent design tokens and styling as the rest of the book
3. **Given** student sees citations in chat responses, **When** viewing the citations, **Then** they appear as mini cards with proper styling

---

### 5.7 Edge Cases

- What happens when a student's question cannot be answered from the available book content? (System should respond with appropriate message, not hallucinate)
- How does the system handle ambiguous questions that could relate to multiple book sections?
- What occurs when selected text is too brief to provide sufficient context for answering?
- How does the system respond when asked about topics not covered in the Physical AI & Humanoid Robotics book? (Must not provide external information)
- What happens when the Qdrant Cloud vector search or Neon Postgres metadata retrieval fails?
- How does the system behave when OpenRouter API is unavailable?
- What occurs when the OpenAI Agent SDK orchestration fails during processing?
- How does the system handle large text selections that exceed context limits?
- What happens when multiple students use the chatbot simultaneously?

## 6. Key Entities

- **Book Content Chunks**: Segments of the Physical AI & Humanoid Robotics book content, with associated metadata stored in Neon Postgres
- **Embedding Vectors**: Numerical representations of content chunks stored in Qdrant Cloud for similarity search
- **Metadata Records**: Structured information about content chunks (module, chapter, page numbers) stored in Neon Serverless Postgres
- **Student Queries**: Natural language questions submitted by students with context indicators (full-book vs selected-text)
- **Generated Responses**: AI-generated answers with proper citations to source material, using models from OpenRouter API
- **Citation Links**: References connecting response content to specific book modules/chapters in the Physical AI & Humanoid Robotics book
- **LLM Configuration**: Environment-based settings that determine which model (Gemini, Claude, GPT, etc.) is used via OpenRouter API
- **OpenAI Agent Tools**: Custom tools orchestrated by OpenAI Agent SDK for RAG functionality, retrieval, and citation management
- **Module Cards**: UI components displaying learning modules with hover animations and navigation capability
- **Chat Interface**: Embedded widget providing conversational access to book content with consistent styling

## 7. Success Criteria

### 7.1 Homepage Experience
- Homepage must clearly guide learning path
- Modules must open in one click
- UI must look professional and production-ready

### 7.2 Chatbot Experience
- Chatbot must feel native, not embedded
- Design choices must be traceable to Context7 MCP references
- Chatbot must provide contextual help effectively

### 7.3 Measurable Outcomes

- **SC-001**: Zero hallucinations - 100% of responses contain information sourced only from the Physical AI & Humanoid Robotics book content
- **SC-002**: Selected-text questions receive responses based exclusively on selected context without global search (100% accuracy)
- **SC-003**: Citations always returned - 100% of responses include correct citations linking to appropriate book modules/chapters
- **SC-004**: UI remains consistent with design system - all pages and components use the same color palette and typography
- **SC-005**: Model switching capability - LLM can be changed via environment configuration without touching agent logic (100% of model changes work without code modifications)
- **SC-006**: System responds to queries within 5 seconds for 95% of requests
- **SC-007**: Students report 80% improvement in ability to find relevant book content through natural language queries
- **SC-008**: No web search functionality is available or used - system only accesses book content for answers (0% of responses contain external information)
- **SC-009**: Homepage module cards display correctly and navigate to appropriate pages (100% success rate)
- **SC-010**: Chatbot widget appears consistently on all pages (100% availability)

## 8. Acceptance Criteria

### 8.1 Homepage Implementation
- [ ] Hero section displays correct title and subtitle
- [ ] "Start Learning" button scrolls to modules section
- [ ] 4 module cards display with correct information
- [ ] Module cards are clickable and navigate to correct pages
- [ ] Hover animations work on module cards
- [ ] Homepage uses consistent design tokens

### 8.2 Chatbot Implementation
- [ ] Floating widget appears in bottom-right corner
- [ ] Chat interface uses consistent design tokens
- [ ] Message bubbles display with correct styling
- [ ] Citations render as mini cards
- [ ] Smooth animations for open/close states
- [ ] Selected-text queries are clearly highlighted
- [ ] Typing indicators function properly

### 8.3 RAG Functionality Implementation
- [ ] System answers questions with zero hallucinations
- [ ] Full-book and selected-text queries are properly distinguished
- [ ] Citations are provided with all responses
- [ ] Model switching works via environment variables
- [ ] OpenAI Agent SDK orchestrates tools correctly
- [ ] Qdrant Cloud integration works for vector search
- [ ] Neon Postgres integration works for metadata

### 8.4 Overall Experience
- [ ] Visual consistency maintained across all pages
- [ ] Performance requirements met
- [ ] Responsive design works across devices
- [ ] Accessibility standards met
- [ ] All constraints are satisfied
