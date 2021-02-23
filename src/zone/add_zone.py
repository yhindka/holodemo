#!/usr/bin/env python

import sys
import rospy
import time
import getopt
from holodemo.msg import zone
from std_msgs.msg import String
from Zone import Zone
from zone_list import addZone, getZone, updateZone, deleteZone


initialized = False


def init():
    
    print("initializing node")
    rospy.init_node('panda_zone')
    initialized = True


def zoneAdd():
   
    

    print("initializing topic")
    pub = rospy.Publisher('/gui/create_zone', zone, queue_size=1)
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
        print(zone.name + '\n' + 
                    'X: ' + str(zone.dimx) + '\n' +
                    'Z: ' + str(zone.dimz) + '\n' +
                    'Pos: (' + str(zone.posx) + ', ' + str(zone.posy) + ', ' + str(zone.posz) + ')\n' +
                    'Danger Zone: ' + str(bool(zone.danger)))



def zoneUpdate(name):

    # check if zone exists
    currZone = getZone(name)
    if currZone == None:
        print("No zone with name: " + name)
        return


    print("initializing topic")
    pub = rospy.Publisher('/gui/update_zone', zone, queue_size=1)
    namePub = rospy.Publisher('/prev_name', String, queue_size=1)

    msg = zone()

    
    msg.name = input('Update name to? (Currently: ' + currZone.name + '): ')
    msg.dimx = int(input('Update x dimension to? (Currently: ' + str(currZone.dimx) + '): '))
    msg.dimz = int(input('Update Z dimension to? (Currently: ' + str(currZone.dimz) + '): '))
    msg.posx = float(input('Update x position to? (Currently: ' + str(currZone.posx) + '): '))
    msg.posy = float(input('Update y position to? (Currently: ' + str(currZone.posy) + '): '))
    msg.posz = float(input('Update z position to? (Currently: ' + str(currZone.posz) + '): '))
    dang = input('Danger Zone? y/n (Currently: ' + str(bool(currZone.danger)) + '): ')

    if (dang == 'y'):
        msg.danger = 1
    elif (dang == 'n'):
        msg.danger = 0
    else:
        rospy.signal_shutdown("Incorrect input. Shutting down node.")
        sys.exit(1)


    updateZone(name, msg)
    prevName = String()
    prevName.data = name
    namePub.publish(prevName)
    time.sleep(1)
    pub.publish(msg)


def zoneDelete(name):
    
    # check if zone exists
    currZone = getZone(name)
    if currZone == None:
        print("No zone with name: " + name)
  
    print("initializing topic")
    pub = rospy.Publisher('/gui/delete_zone', String, queue_size=1)
    time.sleep(1)


    deleteZone(name)
    msg = String()
    msg.data = name
    pub.publish(msg)



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
            zoneAdd()
        elif opt == '-g':
            zoneDetails(arg)
        elif opt == '-u':
            if not initialized:
                init()
            zoneUpdate(arg)
        elif opt == '-d':
            if not initialized:
                init()
            zoneDelete(arg)

