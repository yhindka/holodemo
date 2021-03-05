#!/usr/bin/env python

import sys
import rospy
import time
import getopt
from holodemo.msg import mesh
from std_msgs.msg import String
from mesh_list import addMesh, getMesh, updateMesh, deleteMesh



initialized = False


def init():
    
    print("initializing node")
    rospy.init_node('panda_mesh')
    initialized = True


def meshAdd(): 

    print("initializing topic")
    pub = rospy.Publisher('/gui/add_mesh', mesh, queue_size=1)
    time.sleep(3)

    msg = mesh()

    msg.name = input("Enter name of mesh: ")
    if (getMesh(msg.name) != None):
        print("Mesh name already exists.")
        return

    msg.posx = float(input("Enter x position of mesh: "))
    msg.posy = float(input("Enter y position of mesh: "))
    msg.posz = float(input("Enter z position of mesh: "))
    msg.rotx = float(input("Enter x rotation of mesh: "))
    msg.roty = float(input("Enter y rotation of mesh: "))
    msg.rotz = float(input("Enter z rotation of mesh: "))



    addMesh(msg)
    pub.publish(msg)

def meshDetails(name):
    mesh = getMesh(name)
    if mesh == None:
        print("No mesh with name: " + name)
    else:
        print(mesh.name + '\n' +
                    'Pos: (' + str(mesh.posx) + ', ' + str(mesh.posy) + ', ' + str(mesh.posz) + ')\n' +
                    'Rot: (' + str(mesh.rotx) + ', ' + str(mesh.roty) + ', ' + str(mesh.rotz) + ')')



def meshUpdate(name):

    # check if mesh exists
    currMesh = getMesh(name)
    if currMesh == None:
        print("No mesh with name: " + name)
        return


    print("initializing topic")
    pub = rospy.Publisher('/gui/update_mesh', mesh, queue_size=1)
    namePub = rospy.Publisher('/prev_name', String, queue_size=1)

    msg = mesh()

    
    msg.name = input('Update name to? (Currently: ' + currMesh.name + '): ')
    msg.posx = float(input('Update x position to? (Currently: ' + str(currMesh.posx) + '): '))
    msg.posy = float(input('Update y position to? (Currently: ' + str(currMesh.posy) + '): '))
    msg.posz = float(input('Update z position to? (Currently: ' + str(currMesh.posz) + '): '))
    msg.rotx = float(input('Update x rotation to? (Currently: ' + str(currMesh.rotx) + '): '))
    msg.roty = float(input('Update y rotation to? (Currently: ' + str(currMesh.roty) + '): '))
    msg.rotz = float(input('Update z rotation to? (Currently: ' + str(currMesh.rotz) + '): '))


    updateMesh(name, msg)
    prevName = String()
    prevName.data = name
    namePub.publish(prevName)
    time.sleep(1)
    pub.publish(msg)


def meshDelete(name):
    
    # check if mesh exists
    currMesh = getMesh(name)
    if currMesh == None:
        print("No mesh with name: " + name)
  
    print("initializing topic")
    pub = rospy.Publisher('/gui/delete_mesh', String, queue_size=1)
    time.sleep(1)


    deleteMesh(name)
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
            print("Use -c to create mesh, -g <mesh_name> to get mesh details, -u <mesh_name> to update, or -d <mesh_name> to delete")
            sys.exit(0)
        elif opt == '-c':
            if not initialized:
                init()
            meshAdd()
        elif opt == '-g':
            meshDetails(arg)
        elif opt == '-u':
            if not initialized:
                init()
            meshUpdate(arg)
        elif opt == '-d':
            if not initialized:
                init()
            meshDelete(arg)
