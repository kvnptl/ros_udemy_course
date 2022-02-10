#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def counter_callback(msg):
    rospy.loginfo("Message received: {}".format(msg.data))
    
    msg_num = Int64()
    msg_num.data = msg.data + 1
    pub.publish(msg_num)


if __name__ == "__main__":
    rospy.init_node("number_counter")

    pub = rospy.Publisher("/number_count", Int64, queue_size=10)
    sub = rospy.Subscriber("/number", Int64, counter_callback)

    rospy.spin()
    
    rospy.loginfo("Node exited")
