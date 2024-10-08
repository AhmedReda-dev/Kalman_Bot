# Kalman_Bot Setup Instructions

##final release is in branch "master"

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
    ** This runs the python script responsible for publishing the yaw
   ` imu/yaw` as publisher
   ` imu/data` as subscriber**

7. **Print the yaw:**
    ```bash
    rostopic echo /imu/yaw 
    ```
    *Warning*: `no messages received and simulated time is active.
Is /clock being published?`
