#!/usr/bin/env python3

from tokenize import Number
import rospy
from std_msgs.msg import Int64
import random
from std_srvs.srv import SetBool


class Number_Publisher():

    def __init__(self) -> None:
        self.pub = rospy.Publisher("/number", Int64, queue_size=10)
        self.rate = rospy.Rate(1)

        while not rospy.is_shutdown():
            num = random.randrange(1, 30, 2)
            msg = Int64()
            msg.data = num
            self.pub.publish(msg)
            rospy.loginfo("Number sent: {}".format(msg.data))
            self.rate.sleep()


if __name__ == "__main__":
    rospy.init_node("number_publisher")
    Number_Publisher()
    rospy.spin()
    rospy.loginfo("Client node exited")
