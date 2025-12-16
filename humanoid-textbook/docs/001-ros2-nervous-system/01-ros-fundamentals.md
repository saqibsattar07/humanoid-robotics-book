---
sidebar_position: 1
---

# Chapter 1: ROS 2 Fundamentals

Welcome to the first step in understanding the mind and body of a modern humanoid robot. Before a robot can walk, talk, or think, its many components—motors, sensors, cameras, and processors—need a way to communicate. This is where the Robot Operating System (ROS) comes in.

Think of ROS 2 as the **central nervous system** of the robot. Just as your nervous system carries signals from your brain to your limbs and sensory information back to your brain, ROS 2 allows all the different software and hardware parts of a robot to exchange information seamlessly.

In this chapter, we'll explore the fundamental building blocks of ROS 2.

## What are Nodes?

In ROS 2, every independent process is called a **Node**. A node is the smallest unit of computation. You can think of each node as a specialist with a single job.

For example, a humanoid robot might have:
- A `camera_driver` node responsible for capturing images from a camera.
- A `motor_controller` node responsible for sending commands to the leg motors.
- A `path_planner` node responsible for calculating a route to a destination.

Each node is a separate program that can be started, stopped, and debugged independently. This modularity is a core strength of ROS 2, making complex systems easier to manage.

## How Do Nodes Communicate?

Nodes communicate with each other using a publish-subscribe messaging pattern. They do this over named channels called **Topics**.

- **Publishers**: A node can **publish** (send) messages to a topic. For example, the `camera_driver` node would publish images to a `/camera/image_raw` topic.
- **Subscribers**: A node can **subscribe** (listen) to a topic to receive messages. For example, a `person_detector` node could subscribe to the `/camera/image_raw` topic to get images to analyze.

![ROS 2 Pub/Sub Diagram](https://raw.githubusercontent.com/osrf/ros2_documentation/rolling/source/Tutorials/Beginner-CLI-Tools/Understanding-ROS2-Topics/images/topics.png)
*Image credit: ROS 2 Documentation*

This system decouples the nodes. The `camera_driver` doesn't need to know who is listening to its images; it just publishes them. Any number of other nodes can subscribe to that topic to use the data.

## What are Messages?

A **Message** is the data structure that is sent on a topic. ROS 2 has a rich set of standard message types for common robotics data, such as:
- `std_msgs/String`: A simple text string.
- `sensor_msgs/Image`: An image from a camera.
- `geometry_msgs/Twist`: A message for velocity commands (linear and angular speed).

You can also define your own custom message types to suit your robot's specific needs. For example, you could create a message to represent the state of a humanoid's hand, including the position of each finger.

## Request/Response: Services

While topics are great for continuous data streams, sometimes you need a direct request/response interaction. This is handled by **Services**.

A service has two parts:
- A **Server** node that provides a service (e.g., `calculate_inverse_kinematics`).
- A **Client** node that calls the service with a request and waits for a response.

For example, a `motion_planner` node could be a client that sends a request to a `kinematics_server` with a desired hand position. The server would perform the calculation and send back the required joint angles for the robot's arm as a response. This is a synchronous, one-to-one communication pattern.

## Long-Running Tasks: Actions

What if a task takes a long time to complete, like navigating to a specific room? For this, ROS 2 provides **Actions**.

Actions are similar to services but are designed for long-running, preemptible tasks. They provide feedback during execution.

An action has three parts:
- An **Action Server**: Manages the long-running task (e.g., `navigate_to_goal`).
- An **Action Client**: Sends a goal to the server.
- **Feedback**: The server can send periodic updates to the client (e.g., the robot's current distance from the goal).

This allows the client to monitor progress and even cancel the goal if needed, which is crucial for complex behaviors like navigation or manipulation.

## Summary

You've now learned about the core concepts that make up the "nervous system" of a ROS 2 robot:

- **Nodes**: The individual computational processes.
- **Topics**: The channels for continuous data streams (publish/subscribe).
- **Messages**: The data structures sent on topics.
- **Services**: The channels for request/response interactions.
- **Actions**: The channels for long-running, feedback-enabled tasks.

With these building blocks, we can construct sophisticated robot behaviors from simple, decoupled components. In the next chapter, we'll see how to create these components using the Python programming language.