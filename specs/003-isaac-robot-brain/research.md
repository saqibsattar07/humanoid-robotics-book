# Research & Decisions for Module 3

This document records the decisions made to resolve the "NEEDS CLARIFICATION" items in the implementation plan for Module 3.

## 1. Level of Detail for Isaac Sim Examples

- **Decision**: Examples for NVIDIA Isaac Sim will be presented as high-level workflow diagrams and conceptual Python snippets. The focus will be on the process and concepts of synthetic data generation.
- **Rationale**: This approach aligns with the module's goal of building conceptual understanding. Providing full, runnable projects would be overly complex and distract from the core learning objectives, which are centered on the "why" and "how" of simulation-driven training, not on mastering the Isaac Sim API.
- **Alternatives Considered**:
  - **Full, runnable projects**: Rejected as too complex for the scope, difficult to maintain, and not aligned with the conceptual focus.
  - **No code examples**: Rejected as too theoretical. Snippets are necessary to ground the concepts.

## 2. Depth of Coverage for VSLAM and Nav2

- **Decision**: The coverage of Isaac ROS for VSLAM and Nav2 will focus on the high-level principles, their roles within a robotics stack, and their conceptual APIs. The content will not delve into the complex mathematical algorithms that underpin these technologies.
- **Rationale**: The target audience needs to understand *what* these tools do and *why* they are important for robot autonomy. A deep dive into the algorithmic details is out of scope for a beginner-to-intermediate text and would detract from the primary goal of understanding the overall AI-robot brain architecture. This decision is consistent with the "Not Building" constraints in the feature specification, which exclude custom algorithm implementation.
- **Alternatives Considered**:
  - **Detailed algorithmic explanations**: Rejected as this would be too advanced for the target audience and would require a significant word count, violating the project constraints.
