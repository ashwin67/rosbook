#!/usr/bin/env python

import rospy
from basics.srv import WordCount
import sys

rospy.init_node ('service_client')
rospy.wait_for_service('wordCount')
word_counter = rospy.ServiceProxy('wordCount', WordCount)
words = ' '.join(sys.argv[1:])

word_count = word_counter(words)

print words, '->', word_count.count
