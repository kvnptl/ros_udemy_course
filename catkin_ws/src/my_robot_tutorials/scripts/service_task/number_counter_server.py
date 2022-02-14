#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

counter = 0
pub = None


def counter_callback(msg):
    global counter
    rospy.loginfo("Message received: {}".format(msg.data))

    msg_num = Int64()
    counter += msg.data
    msg_num.data = counter
    pub.publish(msg_num)


def reset_counter_callback(req):
    global counter
    if req.data:
        counter = 0
        rospy.loginfo("Counter set to {}".format(counter))
        return True, "Counter has been reset to 0"
    else:
        return False, "Counter has not been reset"


if __name__ == "__main__":
    rospy.init_node("number_counter")

    pub = rospy.Publisher("/number_count", Int64, queue_size=10)
    sub = rospy.Subscriber("/number", Int64, counter_callback)

    service = rospy.Service("/reset_number_counter",
                            SetBool, reset_counter_callback)

    rospy.loginfo("Number Counter server is ready...")

    rospy.spin()

    rospy.loginfo("Server node exited")
