#!/usr/bin/env python3

import rospy
from my_robot_msgs.srv import SetLed

if __name__ == "__main__":
    rospy.init_node("battery_node")

    rospy.wait_for_service("/set_LED")

    while not rospy.is_shutdown():
        try:
            set_led = rospy.ServiceProxy("/set_LED", SetLed)
            rospy.sleep(7)
            response = set_led(3, 1)
            rospy.loginfo("Status: {}".format(response.success))
            rospy.sleep(3)
            response = set_led(3, 0)
            rospy.loginfo("Status: {}".format(response.success))
        except rospy.ServiceException as e:
            rospy.logwarn("Service failed: " + str(e))
