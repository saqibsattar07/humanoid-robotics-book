---
sidebar_position: 3
---

# Chapter 3: Path Planning with Nav2 for Humanoid Movement

With a map of its environment and its own location from a SLAM system, a robot is ready for the final piece of the navigation puzzle: **Path Planning**. Given a destination, how does the robot decide what route to take to get there safely and efficiently?

In the ROS 2 ecosystem, the standard tool for this is **Nav2**, the second generation of the ROS Navigation Stack. Nav2 is a powerful, highly configurable system that provides all the necessary components for autonomous navigation.

## Core Principles of Nav2

Nav2 is not a single program, but a collection of nodes that work together. At its heart is a two-level planning approach:

1.  **The Global Planner**: This planner looks at the big picture. Given the full map of the environment and a goal location, it calculates an optimal, long-range path from the robot's current position to the goal. It's like using Google Maps to get directions before you start driving. It doesn't worry about small, immediate obstacles; it just finds the general route.

2.  **The Local Planner**: This planner's job is to follow the global plan while reacting to immediate surroundings. It uses data from short-range sensors like LiDAR or depth cameras to generate safe motor commands (`geometry_msgs/Twist`) that move the robot along the global path while avoiding any obstacles that might have appeared (like a person walking by). It's like your own driving, where you follow the main road but steer around potholes and other cars.

Both planners operate on a **Costmap**, which is a grid-based representation of the environment. Each cell in the grid has a value, or "cost," that represents how difficult or dangerous it is to travel through. Obstacles have an infinitely high cost, areas near obstacles have a high cost, and open space has a low cost. The planners then use algorithms (like A* or D*) to find the lowest-cost path through this grid.

## The Humanoid Navigation Challenge

Nav2 was originally designed with wheeled robots in mind—robots that are typically flat, have a consistent footprint, and can turn on a dime. Humanoid robots are a completely different beast, and applying Nav2 to them introduces unique challenges.

| Feature               | Wheeled Robot (e.g., TurtleBot)          | Humanoid Robot (e.g., Digit, Atlas)      |
| --------------------- | ---------------------------------------- | ---------------------------------------- |
| **Locomotion**        | Continuous (wheels rolling)            | Discrete (a sequence of steps)           |
| **Stability**         | Statically stable (low center of gravity) | Dynamically stable (like a walking person) |
| **Footprint**         | Constant and well-defined              | Constantly changing (one foot, two feet) |
| **Control Input**     | `Twist` (linear/angular velocity)        | `Twist` is not enough; needs foot placements |

You can't simply send a `Twist` command from Nav2's local planner to a humanoid's leg motors. Telling the robot "move forward at 0.5 m/s" doesn't explain *how* to move its legs to achieve that speed without falling over.

### Bridging the Gap: The Gait Controller

The solution is to add another layer of abstraction between Nav2 and the robot's hardware. The output of the local planner is treated as a high-level request, which is then fed into a specialized **gait controller** or **whole-body controller**.

```
+----------------+      +---------------------+      +---------------------+
|   Nav2 Local   |----->|   Gait / Whole-Body |----->|    Leg Motors &     |
|    Planner     |      |      Controller     |      |   Joint Controllers |
+----------------+      +---------------------+      +---------------------+
| Issues a target|      | Takes velocity cmd  |      | Executes the low-   |
| velocity cmd   |      | & calculates a      |      | level joint torque  |
| (/cmd_vel)     |      | stable sequence of  |      | commands for each   |
|                |      | foot placements.    |      | step.               |
+----------------+      +---------------------+      +---------------------+
```
*(Simplified diagram comparing a wheeled robot stack to a humanoid stack)*

This gait controller is a complex piece of software responsible for:
-   **Step Planning**: Deciding where to place the next footstep to achieve the desired velocity.
-   **Balance Control**: Continuously adjusting the robot's posture (its Center of Mass) to keep it from falling over.
-   **Whole-Body Inverse Kinematics**: Calculating all the joint angles for the legs, torso, and arms required to execute the step smoothly.

In this architecture, Nav2 still does what it does best: high-level path planning and obstacle avoidance. But the final, critical task of translating that plan into stable, bipedal locomotion is handled by the specialized gait controller. This modular approach allows us to combine the power of a general-purpose navigation system with the highly specific control required for a humanoid robot.