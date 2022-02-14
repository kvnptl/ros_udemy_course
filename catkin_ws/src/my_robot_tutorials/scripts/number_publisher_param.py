#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
import random

if __name__ == "__main__":
    rospy.init_node("number_publisher")

    pub = rospy.Publisher("/number", Int64, queue_size=10)

    # get param value
    publish_freq = rospy.get_param("/number_publish_freq")
    rate = rospy.Rate(publish_freq)

    # set param value
    rospy.set_param("/another_param", "hallo")

    while not rospy.is_shutdown():
        num = random.randrange(1, 30, 2)
        msg = Int64()
        msg.data = num

        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("Node exited")
