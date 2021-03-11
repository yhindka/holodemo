#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import Pose

def getPose(tl):
    
    trans = ()
    rot = ()
    try:
        (trans, rot) = tl.lookupTransform("tag1", "Camera", rospy.Time(0))
        msg = PoseStamped()
        msg.position.x = trans[0]
        msg.position.y = trans[1]
        msg.position.z = trans[2]
        msg.orientation.x = rot[0]
        msg.orientation.y = rot[1]
        msg.orientation.z = rot[2]
        pub.publish(msg)
        print("robot position published")
    except Exception as e:
        pass


if __name__ == "__main__":
    rospy.init_node('place_robot')
    tl = tf.TransformListener()
    pub = rospy.Publisher('/robot_pos', Pose, queue_size=1)
    while not rospy.is_shutdown():
        getPose(tl)
