#!/usr/bin/env python

import rospy
import rosbag
import subprocess
from holodemo.msg import zone
from Zone import Zone




def addZone(zone):

    addBag = None    
    try: 
        addBag = rosbag.Bag('zone.bag', 'a')
    except Exception as e:
        addBag = rosbag.Bag('zone.bag', 'w')
        #currBag = rosbag.Bag('zone.bag')
        #for topic, msg, t in currBag.read_messages(topics=['/zone_bag']):
        #    addBag.write('/zone_bag', msg)
        #currBag.close()

    addBag.write('/zone_bag', zone)
    addBag.close()

def getZone(name):
    
    #global zonesObj
    #getBag = rosbag.Bag('zone.bag')
    try:
        getBag = rosbag.Bag('zone.bag', 'r')
    except Exception as e:
        print("Bag does not exist")
        return
    
    for topic, msg, t in getBag.read_messages(topics=['/zone_bag']):
        if msg.name == name:
            getBag.close()
            return msg

    getBag.close()
        

if __name__ == "__main__":


    
    rospy.init_node('zone_list')
    # remove bag
    subprocess.call('~/catkin_ws/src/holodemo/src/setup.sh', shell=True)

    
    while not rospy.is_shutdown():
        continue
    
