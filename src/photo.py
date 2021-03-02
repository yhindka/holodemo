#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CompressedImage

def callback(msg):
    print("photo received")

if __name__ == "__main__":
    rospy.init_node('photo_sub')
    sub = rospy.Subscriber('/photo/compressed', CompressedImage, callback)
    while not rospy.is_shutdown():
        continue
