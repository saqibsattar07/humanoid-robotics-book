---
sidebar_position: 3
---

# Chapter 3: Modeling the Humanoid Body with URDF

So far, we've learned how different software components of a robot can communicate. But how does a ROS 2 system know what the robot actually *is*? How does it understand the robot's physical structure—its limbs, joints, and sensors?

This is where the **Unified Robot Description Format (URDF)** comes in. URDF is an XML-based file format used in ROS to describe all the physical elements of a robot. Creating a URDF model is like giving your robot a digital blueprint or a "body schema." This model is essential for a wide range of robotics tasks, including:
- **Simulation**: Simulators like Gazebo use URDF to create a virtual version of your robot.
- **Visualization**: Tools like RViz2 use URDF to display the robot's state.
- **Kinematics & Dynamics**: Libraries for motion planning use URDF to calculate how the robot's joints and limbs can move.

## Core Components of URDF

A URDF file is structured around two fundamental components: **links** and **joints**.

### `<link>`: The Physical Parts

A **link** represents a rigid part of the robot's body, like a torso, an upper arm, or a finger segment. Each link has several properties you can define:

- **`<visual>`**: This tag describes what the link looks like. You can define its shape (like a box, cylinder, or sphere) and its material (color and texture). This is what you see in a visualizer like RViz2.
- **`<collision>`**: This describes the collision geometry of the link. It's used by physics engines to calculate collisions with other objects. It's often a simpler version of the visual geometry to save computation.
- **`<inertial>`**: This defines the dynamic properties of the link, such as its mass and moment of inertia. These are crucial for realistic physics simulation.

```xml
<link name="upper_arm_link">
  <visual>
    <geometry>
      <cylinder length="0.5" radius="0.05" />
    </geometry>
    <origin xyz="0 0 0.25" rpy="0 0 0" />
    <material name="blue" />
  </visual>
  <collision>
    <geometry>
      <cylinder length="0.5" radius="0.05" />
    </geometry>
    <origin xyz="0 0 0.25" rpy="0 0 0" />
  </collision>
  <inertial>
    <mass value="1.5" />
    <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1" />
    <origin xyz="0 0 0.25" />
  </inertial>
</link>
```

### `<joint>`: Connecting the Links

A **joint** describes how two links are connected and how they can move relative to each other. Every joint connects a **parent** link to a **child** link.

Key properties of a joint include:

- **`name`**: A unique name for the joint (e.g., "shoulder_joint").
- **`type`**: The most important property, defining the joint's motion. Common types are:
  - `revolute`: A hinge joint that rotates around a single axis, like an elbow. It has defined upper and lower limits.
  - `continuous`: Similar to revolute, but without limits; it can spin freely.
  - `prismatic`: A sliding joint that moves along an axis, like a piston.
  - `fixed`: A rigid connection that allows no movement. This is used to connect parts that are bolted together.
- **`<parent link="..." />`**: The name of the parent link.
- **`<child link="..." />`**: The name of the child link.
- **`<origin xyz="..." rpy="..." />`**: Defines the pose (position and orientation) of the child link's origin relative to the parent link's origin. This transform is crucial for getting the robot's structure right.
- **`<axis xyz="..." />`**: For non-fixed joints, this defines the axis of motion (rotation for revolute, translation for prismatic).

```xml
<joint name="shoulder_joint" type="revolute">
  <parent link="torso_link"/>
  <child link="upper_arm_link"/>
  <origin xyz="0 0.2 0.5" rpy="0 0 0" />
  <axis xyz="0 1 0" />
  <limit lower="-1.57" upper="1.57" effort="10" velocity="1.0" />
</joint>
```

## Example: A Simple Two-Link Arm

Let's put it together. Here is a complete URDF for a very simple arm with two links connected by a revolute joint.

```xml
<?xml version="1.0"?>
<robot name="simple_arm">

  <!-- Base Link -->
  <link name="base_link">
    <visual>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
      <material name="gray">
        <color rgba="0.5 0.5 0.5 1"/>
      </material>
    </visual>
  </link>

  <!-- Arm Link -->
  <link name="arm_link">
    <visual>
      <geometry>
        <box size="0.5 0.1 0.1"/>
      </geometry>
       <origin xyz="0.25 0 0" rpy="0 0 0"/>
      <material name="blue">
        <color rgba="0.1 0.1 0.8 1"/>
      </material>
    </visual>
  </link>

  <!-- Joint connecting Base to Arm -->
  <joint name="base_to_arm_joint" type="revolute">
    <parent link="base_link"/>
    <child link="arm_link"/>
    <origin xyz="0 0 0.025" rpy="0 0 0"/>
    <axis xyz="0 0 1"/>
    <limit lower="-3.14" upper="3.14" effort="10" velocity="1.0"/>
  </joint>

</robot>
```

This simple file defines two links (`base_link` and `arm_link`) and one joint (`base_to_arm_joint`) that allows the arm to rotate around a vertical axis relative to the base. A full humanoid robot URDF is much larger, containing hundreds of links and joints, but it is built from these exact same fundamental principles.

With this digital blueprint, ROS 2 tools can now understand your robot's body, visualize it, and begin to plan its movements in a simulated world.