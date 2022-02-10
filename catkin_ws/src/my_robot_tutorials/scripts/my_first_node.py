#i/usr/bin/env python3
#The first line is called shebang, or hash-bang line.
# What is the shebang? 
# The shebang is a special character sequence in a script file that specifies 
# which program should be called to run the script.
# source: https://www.a2hosting.com/kb/developer-corner/linux/using-the-shebang

import rospy

if __name__ == '__main__':
    rospy.init_node("my_first_python_node")
    rospy.loginfo("This node has been started")

    #set 10Hz frequency
    rate = rospy.Rate(10)

    #wait untill node killed by the user
    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        
        #wait for 0.1 sec, that means send run this loop 10 times a second
        #This way it is 10 Hz (10 msgs under 1 sec)
        rate.sleep()
