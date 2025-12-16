# Research & Decisions for Module 4

This document records the decisions made to resolve the "NEEDS CLARIFICATION" items in the implementation plan for Module 4.

## 1. Level of Detail for Voice-to-Action Workflow Diagrams

- **Decision**: The workflow will be illustrated using high-level block diagrams. The diagram will clearly show the major stages of the pipeline: `Audio Input -> Speech-to-Text (e.g., Whisper) -> Text Output -> LLM Planner -> ROS 2 Actions`. Each block in the diagram will be accompanied by a brief description of its function.
- **Rationale**: This approach effectively communicates the end-to-end architecture at a conceptual level, which is the primary goal of the capstone module. It avoids implementation-specific details that are not relevant to the learning objectives and could become quickly outdated.
- **Alternatives Considered**:
  - **Detailed sequence diagrams**: Rejected as this would introduce unnecessary complexity, delving into API calls and data formats that are beyond the scope of a conceptual overview.

## 2. Specificity of LLM Prompts for Cognitive Planning Examples

- **Decision**: The examples of prompts for the LLM planner will be presented in a conceptual, pseudo-code format. They will illustrate the essential components of a good prompt for robotic planning:
  1.  A **system message** that defines the robot's role, its available tools (as ROS 2 actions), and its constraints.
  2.  A **user message** containing the high-level goal.
- **Rationale**: This strategy focuses on teaching the *principle* of how to structure a prompt to elicit a plan from an LLM. It is model-agnostic and more durable than providing a specific prompt syntax for a particular model (e.g., OpenAI's API), which is subject to change. The goal is to teach the thinking process, not a transient API format.
- **Alternatives Considered**:
  - **Real, tested prompts for a specific model**: Rejected because this would be too brittle. LLM APIs and models evolve rapidly, and a concrete prompt could become suboptimal or even non-functional in a short time. This would also require readers to have access to a specific paid API, which is a barrier to entry.
