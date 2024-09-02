#!/usr/bin/env python3

#KG = EstError/(EstError+measurementError)
#Est2 = Est1 + KG(mea - Est1)
#EstError2 = (1-KG)EE
import rospy
from std_msgs.msg import Float32

Est = 0 #initial estimate
ME = 1 #measurment error
EE = 1 #estimate error
filter_pub = rospy.Publisher('imu/filtered', Float32, queue_size=10)
def kalman(data):
    global EE
    global Est
    global ME
    global filter_pub
    NM = data.data #new measurment
    KG = EE / (EE + ME)
    Est = Est + KG * (NM - Est)
    EE = (1 - KG) * EE
    filter_pub.publish(Est)

def receiver():
    rospy.init_node('filter')
    filter_pub = rospy.Publisher('imu/filtered', Float32, queue_size=10)
    rospy.Subscriber('/imu/yaw', Float32, kalman)
    rospy.spin()

if __name__ == '__main__':
    try:
        receiver()
    except rospy.ROSInterruptException:
        pass
