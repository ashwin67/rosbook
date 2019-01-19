#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from basics.msg import Complex

def subs_callback(msg):
    print str(msg.real) + " + " + str(msg.imaginary) + "i"

rospy.init_node ('topic_subscriber')

sub = rospy.Subscriber('complex', Complex, subs_callback)

rospy.spin()
