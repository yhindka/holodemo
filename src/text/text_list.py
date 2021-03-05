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

def getText(name):

    getBag = None
    try:
        getBag = rosbag.Bag(bag_path, 'r')
    except Exception as e1:
        print("Bag does not exist. Normal if this is your first text.")
        return

    for topic, msg, t in getBag.read_messages(topics=['/text_bag']):
        if msg.name == name:
            return msg
    getBag.close()

def transferToTemp():


    # transfer messages to temporary bag
    try:
        getBag = rosbag.Bag(bag_path, 'r')
        tempBag = rosbag.Bag(temp_path, 'w')
    except Exception as e:
        print("Bag does not exist or cannot be created")
        return

    for topic, msg, t in getBag.read_messages(topics=['/text_bag']):
        tempBag.write(topic, msg, t)
    tempBag.close()
    getBag.close()


def updateText(name, updatedMsg):

    transferToTemp()

    try:
        getBag = rosbag.Bag(bag_path, 'w')
        tempBag = rosbag.Bag(temp_path, 'r')
    except Exception as e1:
        print("Error with bags")

    for topic, msg, t in tempBag.read_messages(topics=['/text_bag']):
        # write updated message
        if msg.name == name:
            getBag.write(topic, updatedMsg, t)
        else:
            getBag.write(topic, msg, t)
    getBag.close()
    tempBag.close()

def deleteText(name):

    transferToTemp()

    try:
        getBag = rosbag.Bag(bag_path, 'w')
        tempBag = rosbag.Bag(temp_path, 'r')
    except Exception as e1:
        print("Error with bags")

    for topic, msg, t in tempBag.read_messages(topics=['/text_bag']):
        # skip message to delete
        if msg.name != name:
            getBag.write(topic, msg, t)
    getBag.close()
    tempBag.close()
    

if __name__ == "__main__":


    rospy.init_node('text_list')
    
    while not rospy.is_shutdown():
        continue
