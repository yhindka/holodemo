#!/usr/bin/env python

import rospy
import tf
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseStamped
from math import sqrt, pow

distanceToCube = 0.0

# create msg
msg = Marker()
msg.header.frame_id = "panda_link0"
msg.type = 9
msg.pose.position.x = 0
msg.pose.position.y = 0
msg.pose.position.z = 0
msg.pose.orientation.x = 0
msg.pose.orientation.y = 0
msg.pose.orientation.z = 0
msg.scale.z = 0.1
msg.color.a = 1



def calcDistance(pose_msg, args):

    global distanceToCube
    cubePose = pose_msg
    cubePosition = cubePose.pose.position
    pandaRot = ()
    pandaTrans = ()
    try:
        (pandaTrans, pandaRot) = tl.lookupTransform("panda_link0", "sim_end_effector", rospy.Time(0))
        if pandaTrans != None:
            distanceToCube = sqrt(pow(cubePosition.x - pandaTrans[0], 2) + 
                                  pow(cubePosition.y - pandaTrans[1], 2) +
                                  pow(cubePosition.z - pandaTrans[2], 2))
            msg.text = "Distance to cube: " + str(round(distanceToCube, 2))
            msg.pose.position.x = pandaTrans[0]
            msg.pose.position.y = pandaTrans[1]
            msg.pose.position.z = pandaTrans[2]
            pub.publish(msg)
    except:
        print()


if __name__ == "__main__":
    rospy.init_node('text_node')
    tl = tf.TransformListener()
    pub = rospy.Publisher('/panda/text', Marker, queue_size=1)
    cube_sub = rospy.Subscriber('/panda/goal', PoseStamped, calcDistance, (tl))
    rospy.spin()
