```mermaid
graph TD
    A[Audio Input] --> B(Speech-to-Text)
    B --> C{Natural Language Understanding <br> (LLM)}
    C --> D[Action Generation <br> (ROS 2 Commands)]
    D --> E[Robot Action Execution]

    subgraph Human-Robot Interaction
        A
        E
    end
```