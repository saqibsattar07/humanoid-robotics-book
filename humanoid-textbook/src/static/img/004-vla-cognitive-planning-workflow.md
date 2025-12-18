```mermaid
graph TD
    A[High-Level Goal <br> (Natural Language)] --> B{LLM <br> (Cognitive Planner)}
    B --> C{Task Decomposition <br> & Action Sequencing}
    C --> D{Action Grounding <br> (ROS 2 Primitives)}
    D --> E[ROS 2 Executive <br> (Execution Monitoring)]
    E --> F[Robot Hardware <br> (Sensors & Actuators)]
    F --> G[Environment <br> (Perception Feedback)]
    G --> B

    subgraph Robot Brain
        B --- C --- D --- E
    end
```