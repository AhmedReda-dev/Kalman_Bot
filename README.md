# Kalman_Bot Setup Instructions

Follow these steps to start the Kalman_Bot setup:

1. **Start the ROS core:**
    ```bash
    roscore
    ```

2. **Launch the TurtleBot3 simulation world:**
    ```bash
    roslaunch turtlebot3_gazebo turtlebot3_world.launch
    ```

3. **Launch RViz for TurtleBot3:**
    ```bash
    roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
    ```

4. **Add the IMU topic from RViz:**
   - Open RViz and add the IMU topic to visualize sensor data.

5. **Start the TurtleBot3 teleoperation node:**
    ```bash
    roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
    ```

6. **Run the IMU to Degrees Node:**
    ```bash
    rosrun imu_to_degrees imu_listener_node.py
    ```

## Copy Commands

Click the button below to copy all the commands:

<button onclick="copyCommands()">Copy All Commands</button>

<script>
function copyCommands() {
    const commands = `
roscore
roslaunch turtlebot3_gazebo turtlebot3_world.launch
roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
rosrun imu_to_degrees imu_listener_node.py
    `;
    navigator.clipboard.writeText(commands).then(() => {
        alert('Commands copied to clipboard!');
    }, (err) => {
        console.error('Failed to copy commands: ', err);
    });
}
</script>
