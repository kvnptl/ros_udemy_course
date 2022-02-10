#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    #we can't have two nodes with same name
    # rospy.init_node("robot_news_radio_transmitter")
    #init node with anonymous = True, means it will end some random number at the end of 
    # the node name to make it unique
    rospy.init_node("robot_news_radio_transmitter", anonymous=True)

    pub = rospy.Publisher("/robot_news_radio", String, queue_size=10) #queue_size is buffer that stores 10 msgs

    rate = rospy.Rate(2)

    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hi, this is Kevin from the Robot news radio !"
        pub.publish(msg)
        rate.sleep()
    
    rospy.loginfo("Node has stopped")
