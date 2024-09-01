#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32
from tf.transformations import euler_from_quaternion
import math

def imu_callback(data):
    try:
        quaternion = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
        roll, pitch, yaw = euler_from_quaternion(quaternion)
        yaw_deg = yaw * 180.0 / math.pi
        
        # Publish yaw
        yaw_pub.publish(yaw_deg)
    except Exception as e:
        rospy.logerr("Error processing IMU data: %s", str(e))

def imu_listener():
    rospy.init_node('imu_listener_node', anonymous=True)
    global yaw_pub
    yaw_pub = rospy.Publisher('imu/yaw', Float32, queue_size=10)
    rospy.Subscriber('/imu/data', Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        imu_listener()
    except rospy.ROSInterruptException:
        pass

