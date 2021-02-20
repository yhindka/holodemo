#!/usr/bin/env python

import sys
import rospy
import getopt
from holodemo.msg import custom_text
from text_list import addText

initialized = False

def init():
    print("initializing node")
    rospy.init_node('custom_text')
    initialized = True

def textAdd():

    pub = rospy.Publisher('/gui/add_text', custom_text, queue_size=1)

    msg = custom_text()
    msg.text = input("Enter text: ")
    msg.posx = float(input("Enter x position: "))
    msg.posy = float(input("Enter y position: "))
    msg.posz = float(input("Enter z position: "))
    msg.name = input("Enter name for this text object: ")

    addText(msg)
    pub.publish(msg)
    

if __name__ == "__main__":

    try:
        (opts, args) = getopt.getopt(sys.argv[1:], "hcg:u:d:")
    except getopt.GetoptError as e1:
        print(e1)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print("Use -c to create text, -u <text_number> to update, or -d <text_number> to delete")
            sys.exit(0)
        elif opt == '-c':
            if not initialized:
                init()
            textAdd()

