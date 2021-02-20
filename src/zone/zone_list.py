#!/usr/bin/env python

import rospy
import rosbag
import subprocess
from holodemo.msg import zone
from Zone import Zone


bag_path = '/home/user/catkin_ws/src/holodemo/src/bags/zone.bag'
temp_path = '/home/user/catkin_ws/src/holodemo/src/bags/temp.bag'


def addZone(zone):

    addBag = None    
    try: 
        addBag = rosbag.Bag(bag_path, 'a')
    except Exception as e:
        addBag = rosbag.Bag(bag_path, 'w')

    addBag.write('/zone_bag', zone)
    addBag.close()

def getZone(name):
    
    try:
        getBag = rosbag.Bag(bag_path, 'r')
    except Exception as e:
        print("Bag does not exist")
        return
    
    for topic, msg, t in getBag.read_messages(topics=['/zone_bag']):
        if msg.name == name:
            getBag.close()
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

    for topic, msg, t in getBag.read_messages(topics=['/zone_bag']):
        tempBag.write(topic, msg, t)
    tempBag.close()
    getBag.close()


def updateZone(name, updatedMsg):

    transferToTemp()

    # transfer messages back to actual bag
    try:
        getBag = rosbag.Bag(bag_path, 'w')
        tempBag = rosbag.Bag(temp_path, 'r')
    except Exception as e:
        print("Error with bags")
        return

    for topic, msg, t in tempBag.read_messages(topics=['/zone_bag']):
        # write updated message
        if msg.name == name:
            getBag.write(topic, updatedMsg, t)
        else:
            getBag.write(topic, msg, t)
    getBag.close()
    tempBag.close()

def deleteZone(name):

    transferToTemp()

    # transfer messages back to actual bag
    try:
        getBag = rosbag.Bag(bag_path, 'w')
        tempBag = rosbag.Bag(temp_path, 'r')
    except Exception as e:
        print("Error with bags")
        return

    for topic, msg, t in tempBag.read_messages(topics=['/zone_bag']):
        # write all messages except one to be deleted
        if msg.name != name:
            getBag.write(topic, msg, t)
    getBag.close()
    tempBag.close()

        

if __name__ == "__main__":


    rospy.init_node('zone_list')

    # remove bag
    subprocess.call('~/catkin_ws/src/holodemo/src/setup.sh', shell=True)

    while not rospy.is_shutdown():
        continue
    
