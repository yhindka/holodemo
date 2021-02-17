#!/usr/bin/env python

import sys
import rospy
import time
import getopt
from holodemo.msg import zone
from Zone import Zone
from zone_list import addZone, getZone


initialized = False


def init():
    
    print("initializing node")
    rospy.init_node('panda_zone')
    initialized = True


def createZone():
   
    

    print("initializing topic")
    pub = rospy.Publisher('/panda/zone', zone, queue_size=1)
    time.sleep(3)

    msg = zone()

    msg.dimx = int(input("Enter x dimension of zone: "))
    msg.dimz = int(input("Enter z dimension of zone: "))
    msg.posx = float(input("Enter x position of zone: "))
    msg.posy = float(input("Enter y position of zone: "))
    msg.posz = float(input("Enter z position of zone: "))

    dang = input("Is this a danger zone? y/n ")
    if (dang == 'y'):
        msg.danger = 1
    elif (dang == 'n'):
        msg.danger = 0
    else:
        rospy.signal_shutdown("Incorrect input. Shutting down node.")
        sys.exit(1)

    msg.name = input("Enter name of zone: ")

    
    #toAdd = Zone(msg.dimx, msg.dimz, msg.posx, msg.posy, msg.posz, msg.danger)
    addZone(msg)
    pub.publish(msg)

def zoneDetails(name):
    zone = getZone(name)
    if zone == None:
        print("No zone with name: " + name)
    else:
        print(zone.name)




if __name__ == "__main__":

    try:
        (opts, args) = getopt.getopt(sys.argv[1:], "hcg:u:d:")
    except getopt.GetoptError as e1:
        print(e1)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print("Use -c to create zone, -u <zone_number> to update, or -d <zone_number> to delete")
            sys.exit(0)
        elif opt == '-c':
            if not initialized:
                init()
            createZone()
        elif opt == '-g':
            zoneDetails(arg)

