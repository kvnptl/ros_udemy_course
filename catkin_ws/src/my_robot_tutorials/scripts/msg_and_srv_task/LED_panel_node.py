#!/usr/bin/env python3

import rospy
from my_robot_msgs.srv import SetLed


def handle_LED_state(req):
    if req.state == 1:
        rospy.loginfo("LED state : LED {} : ON".format(req.ledNumber))
        return True
    elif req.state == 0:
        rospy.loginfo("LED state : LED {} : OFF".format(req.ledNumber))
        return True
    else:
        rospy.loginfo("Given LED state is not valid")
        return False


if __name__ == "__main__":
    rospy.init_node("led_panel")
    rospy.loginfo("LED panel node created")

    service = rospy.Service("/set_LED", SetLed, handle_LED_state)
    rospy.loginfo("Service server has been started")

    rospy.spin()
