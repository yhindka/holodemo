#!/usr/bin/env python

import rospy
import rosbag
from holodemo.msg import custom_text

bag_path = '/home/user/catkin_ws/src/holodemo/src/bags/text.bag'
temp_path = '/home/user/catkin_ws/src/holodemo/src/bags/temp.bag'

def addText(msg):

    addBag = None
    try:
        addBag = rosbag.Bag(bag_path, 'a')
    except Exception as e1:
        addBag = rosbag.Bag(bag_path, 'w')

    addBag.write('/text_bag', msg)
    addBag.close()
    

if __name__ == "__main__":




    rospy.init_node('text_list')
    
    while not rospy.is_shutdown():
        continue
