#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
import random
from std_srvs.srv import SetBool

if __name__ == "__main__":
    rospy.init_node("number_publisher")

    pub = rospy.Publisher("/number", Int64, queue_size=10)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        num = random.randrange(1, 30, 2)
        msg = Int64()
        msg.data = num
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node exited")
