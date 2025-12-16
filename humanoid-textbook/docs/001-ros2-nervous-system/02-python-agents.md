---
sidebar_position: 2
---

# Chapter 2: Bridging Python AI Agents to Robot Control

In the previous chapter, we learned about the conceptual building blocks of ROS 2. Now, let's get practical. How do we actually create these nodes, publishers, and subscribers? For developers and researchers in the AI and robotics community, Python is the language of choice. ROS 2 fully supports Python through its client library, `rclpy`.

This chapter will guide you through writing your first ROS 2 nodes in Python to send and receive messages, forming the bridge between your AI logic and the robot's actions.

## Introducing `rclpy`: The Python Client Library

`rclpy` is the official library that allows you to interface with ROS 2 using Python. It provides the necessary classes and functions to create nodes, publishers, subscribers, services, and actions. To use it, you'll typically start by initializing the library and creating a node.

### Your First Python Node

Let's create the simplest possible ROS 2 node. This node will initialize itself, print a message, and then shut down.

```python
# first_node.py
import rclpy
from rclpy.node import Node

def main(args=None):
    # 1. Initialize the rclpy library
    rclpy.init(args=args)

    # 2. Create a class that inherits from the Node class
    class MyFirstNode(Node):
        def __init__(self):
            # Call the Node constructor and give it a name
            super().__init__('my_first_node')
            # Use the node's logger to print a message
            self.get_logger().info('Hello from my first ROS 2 node!')

    # 3. Create an instance of your node
    node = MyFirstNode()

    # 4. rclpy.spin() is not needed here as the node does its work in the constructor.
    #    We'll see spin() later with subscribers.

    # 5. Shutdown the rclpy library
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

While this node doesn't communicate with anything, it demonstrates the basic structure: initialize `rclpy`, create a node, do something, and then shut down.

## Creating a Publisher

A publisher node sends messages to a specific topic. Let's create a node that publishes a "Hello World" message to a topic named `/chatter` every second.

```python
# publisher_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String # Import the String message type

class ChatterPublisher(Node):
    def __init__(self):
        super().__init__('chatter_publisher')
        # Create a publisher on the '/chatter' topic with a String message type.
        # The '10' is the queue size - a quality of service (QoS) setting.
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        
        # Create a timer that calls the timer_callback function every 1 second.
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0
        self.get_logger().info('Publisher node started. Publishing to /chatter...')

    def timer_callback(self):
        # Create a String message
        msg = String()
        msg.data = f'Hello World: {self.i}'
        
        # Publish the message
        self.publisher_.publish(msg)
        
        # Log the published message
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    chatter_publisher = ChatterPublisher()
    
    # rclpy.spin() keeps the node alive so its callbacks can be called.
    rclpy.spin(chatter_publisher)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    chatter_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### Breaking Down the Publisher
1.  **`create_publisher(String, 'chatter', 10)`**: This method creates a publisher. It takes the message type (`String`), the topic name (`'chatter'`), and the queue size (a QoS setting that limits the amount of buffered messages).
2.  **`create_timer(1.0, self.timer_callback)`**: We use a timer to execute a function (`timer_callback`) at a regular interval (every 1.0 second). This is a common way to create a periodic publisher.
3.  **`self.publisher_.publish(msg)`**: Inside the callback, we create a `String` message, populate its `data` field, and use the `publish()` method to send it over the topic.
4.  **`rclpy.spin(node)`**: This is a crucial line. It enters a loop that keeps the node running, allowing its callbacks (like our `timer_callback`) to be processed. The program will stay in this loop until the node is shut down (e.g., by pressing `Ctrl+C` in the terminal).

## Creating a Subscriber

A subscriber node listens to a topic and processes the messages it receives. Let's create a node that subscribes to our `/chatter` topic.

```python
# subscriber_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChatterSubscriber(Node):
    def __init__(self):
        super().__init__('chatter_subscriber')
        # Create a subscription to the '/chatter' topic.
        # The callback function 'listener_callback' is called for each message.
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10) # QoS profile
        self.subscription  # prevent unused variable warning
        self.get_logger().info('Subscriber node started. Listening to /chatter...')

    def listener_callback(self, msg):
        # This function is called every time a message is received.
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    chatter_subscriber = ChatterSubscriber()
    
    # Spin the node to receive messages
    rclpy.spin(chatter_subscriber)
    
    chatter_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### Breaking Down the Subscriber
1.  **`create_subscription(String, 'chatter', self.listener_callback, 10)`**: This creates a subscriber. It takes the message type, topic name, the callback function to execute for each message, and the queue size.
2.  **`listener_callback(self, msg)`**: This function is the heart of the subscriber. `rclpy` automatically calls it whenever a new message arrives on the `/chatter` topic. The received message is passed as the `msg` argument.

## Running the Nodes
To see this in action, you would open two separate terminals. In the first, run the publisher:
```bash
python3 publisher_node.py
```
In the second, run the subscriber:
```bash
python3 subscriber_node.py
```
You will see the publisher printing what it's sending and the subscriber printing what it's hearing. You've just created your first distributed robotic application! This fundamental pattern is the basis for almost all communication in ROS 2.