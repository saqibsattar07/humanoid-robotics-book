# Tasks: Module 4: Vision-Language-Action (VLA)

**Input**: Design documents from `/specs/004-vla-capstone/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: No automated tests are required for this content-focused feature. Validation will be done manually.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for the Docusaurus book module.

- [ ] T001 Create the directory structure for the module at `src/docs/004-vla-capstone/`.
- [ ] T002 Create placeholder files: `01-voice-to-action.md`, `02-cognitive-planning.md`, and `03-capstone-overview.md` in `src/docs/004-vla-capstone/`.
- [ ] T003 Create the module category file `_category_.json` in `src/docs/004-vla-capstone/` to configure the module's appearance in the sidebar.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: For this content-creation feature, there are no foundational code tasks that block user stories. This phase is not applicable.

---

## Phase 3: User Story 1 - Voice-to-Action (Priority: P1) 🎯 MVP

**Goal**: Create the content for the first chapter, explaining how to convert voice commands into robot actions.

**Independent Test**: A reviewer can read `01-voice-to-action.md` and understand the conceptual flow from spoken language to a structured robot command.

### Implementation for User Story 1

- [ ] T004 [US1] Write the full content for the "Voice-to-Action with Speech and Language Models" chapter in `src/docs/004-vla-capstone/01-voice-to-action.md`.
- [ ] T005 [P] [US1] Create high-level block diagrams for the voice-to-action workflow (Audio -> Speech-to-Text -> LLM -> ROS 2 Actions) and save them to `src/static/img/`.
- [ ] T006 [US1] Embed the workflow diagrams into `src/docs/004-vla-capstone/01-voice-to-action.md`.

**Checkpoint**: The first chapter of Module 4 is complete and readable within the Docusaurus site.

---

## Phase 4: User Story 2 - Cognitive Planning with LLMs (Priority: P2)

**Goal**: Create the content for the second chapter, explaining how to use LLMs for cognitive planning.

**Independent Test**: A reviewer can read `02-cognitive-planning.md` and understand how to prompt an LLM to generate a sequence of tasks for a robot.

### Implementation for User Story 2

- [ ] T007 [US2] Write the full content for the "Cognitive Planning with LLMs and ROS 2" chapter in `src/docs/004-vla-capstone/02-cognitive-planning.md`.
- [ ] T008 [P] [US2] Create diagrams and conceptual pseudo-code examples of LLM prompts for task decomposition and save any generated images to `src/static/img/`.
- [ ] T009 [US2] Embed the diagrams and prompt examples into `src/docs/004-vla-capstone/02-cognitive-planning.md`.

**Checkpoint**: The second chapter is complete, providing a clear explanation of LLM-based planning.

---

## Phase 5: User Story 3 - End-to-End System (Priority: P3)

**Goal**: Create the content for the third chapter, providing a capstone overview of the entire VLA system.

**Independent Test**: A reviewer can read `03-capstone-overview.md` and understand how the components from all four modules connect into a single system.

### Implementation for User Story 3

- [ ] T010 [US3] Write the full content for the "Capstone: The Autonomous Humanoid" overview chapter in `src/docs/004-vla-capstone/03-capstone-overview.md`.
- [ ] T011 [P] [US3] Create a comprehensive, end-to-end system diagram of the VLA pipeline, showing perception, planning, and action stacks, and save it to `src/static/img/`.
- [ ] T012 [US3] Embed the system diagram into `src/docs/004-vla-capstone/03-capstone-overview.md`.

**Checkpoint**: All three chapters of Module 4 are now complete.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final review and validation for the entire module.

- [ ] T013 Review all content in `src/docs/004-vla-capstone/` for technical accuracy, clarity, grammar, and style.
- [ ] T014 [P] Add citations in APA format to all three chapter files where external sources were used.
- [ ] T015 Validate that the writing level for all chapters is within the Flesch-Kincaid Grade 9–11 range.
- [ ] T016 Run a plagiarism check on the final content.
- [ ] T017 Run `npm start` (or `yarn start`) and perform a final check of the built Docusaurus site for Module 4.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must be completed first.
- **User Stories (Phases 3, 4, 5)** can be worked on in parallel after setup is complete.
- **Polish (Phase 6)** depends on the completion of all user story phases.

## Implementation Strategy

The recommended approach is to implement the user stories sequentially (P1 -> P2 -> P3) to ensure a coherent flow of content. However, if multiple authors are available, they can work on the user story phases in parallel. The Polish phase should be performed last.
