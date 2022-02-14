#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool


class Number_Counter():
    def __init__(self) -> None:

        self.counter = 0

        self.pub = rospy.Publisher("/number_count", Int64, queue_size=10)
        self.sub = rospy.Subscriber("/number", Int64, self.counter_callback)

        self.service = rospy.Service("/reset_number_counter",
                                     SetBool, self.reset_counter_callback)

        rospy.loginfo("Number Counter server is ready...")

    def counter_callback(self, msg):

        rospy.loginfo("Message received: {}".format(msg.data))

        msg_num = Int64()
        self.counter += msg.data
        msg_num.data = self.counter
        self.pub.publish(msg_num)

    def reset_counter_callback(self, req):

        if req.data:
            self.counter = 0
            rospy.loginfo("Counter set to {}".format(self.counter))
            return True, "Counter has been reset to 0"
        else:
            return False, "Counter has not been reset"


if __name__ == "__main__":
    rospy.init_node("number_counter")
    Number_Counter()
    rospy.spin()
    rospy.loginfo("Server node exited")
