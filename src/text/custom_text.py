#!/usr/bin/env python

import sys
import rospy
import getopt
import time
from holodemo.msg import custom_text
from std_msgs.msg import String
from text_list import addText, getText, updateText, deleteText

initialized = False

def init():
    print("initializing node")
    rospy.init_node('custom_text')
    initialized = True

def textAdd():

    print("initializing topic")
    pub = rospy.Publisher('/gui/add_text', custom_text, queue_size=1)

    msg = custom_text()
    msg.text = input("Enter text: ")
    msg.posx = float(input("Enter x position: "))
    msg.posy = float(input("Enter y position: "))
    msg.posz = float(input("Enter z position: "))
    msg.name = input("Enter name for this text object: ")

    addText(msg)
    pub.publish(msg)

def textDetails(name):
    text = getText(name)
    if text == None:
        print("No text with name: " + name)
    else:
        print(text.name + '\n' +
                'Text: ' + text.text + '\n' +
                'Pos: (' + str(text.posx) + ', ' + str(text.posy) + ', ' + str(text.posz) + ')')

def textUpdate(name):

    currText = getText(name)
    if currText == None:
        print("No text with name: " + name)
        return
    
    print("initializing topic")
    pub = rospy.Publisher('/gui/update_text', custom_text, queue_size=1)
    namePub = rospy.Publisher('/prev_name', String, queue_size=1)

    msg = custom_text()
    msg.name = input("Update name to? (Currently: " + currText.name + "): ")
    msg.text = input("Update text to? (Currently: " + currText.text + "): ")
    msg.posx = float(input("Update x position to? (Currently: " + str(currText.posx) + "): "))
    msg.posy = float(input("Update y position to? (Currently: " + str(currText.posy) + "): "))
    msg.posz = float(input("Update z position to? (Currently: " + str(currText.posz) + "): "))

    updateText(name, msg)

    prevName = String()
    prevName.data = name
    namePub.publish(prevName)
    time.sleep(1)
    pub.publish(msg)

def textDelete(name):
    # check if zone exists
    text = getText(name)
    if text == None:
        print("No text with name: " + name)
        return

    print("initializing topic")
    pub = rospy.Publisher('/gui/delete_text', String, queue_size=1)
    time.sleep(1)

    deleteText(name)
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
            print("Use -c to create text, -g <text_name> to get text details, -u <text_name> to update, or -d <text_name> to delete")
            sys.exit(0)
        elif opt == '-c':
            if not initialized:
                init()
            textAdd()
        elif opt == '-g':
            textDetails(arg)
        elif opt == '-u':
            if not initialized:
                init()
            textUpdate(arg)
        elif opt == '-d':
            if not initialized:
                init()
            textDelete(arg)

