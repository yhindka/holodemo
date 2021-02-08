#!/usr/bin/env python

import rospy
import tf
from nav_msgs.msg import Path
from geometry_msgs.msg import Pose, PoseStamped, Twist


def getPath(msg, args):
    pandaTrans = ()
    pandaRot = ()
    try:
        (pandaTrans, pandaRot) = tl.lookupTransform("panda_link0", "sim_end_effector", rospy.Time(0))
        path = Path()
        pose1 = PoseStamped()
        pose2 = msg
        path.header.frame_id = "panda_link0"
        if pandaTrans != None:
            pose1.pose.position.x = pandaTrans[0]
            pose1.pose.position.y = pandaTrans[1]
            pose1.pose.position.z = pandaTrans[2]
            pose1.pose.orientation.x = pandaRot[0]
            pose1.pose.orientation.y = pandaRot[1]
            pose1.pose.orientation.z = pandaRot[2]
            path.poses.append(pose1)
            path.poses.append(pose2)
            pub.publish(path)


    except:
        #print("no transform")
        print()



if __name__ == "__main__":

    rospy.init_node('path_test')
    tl = tf.TransformListener()
    pub = rospy.Publisher('/panda/path', Path, queue_size=1)
    #sub = rospy.Subscriber('/panda_pose', PoseStamped, callback)
    #sub = rospy.Subscriber('/mover/cart_vel', PoseStamped, callback)
    sub = rospy.Subscriber('/panda/goal', PoseStamped, getPath, (tl))
    rospy.spin()
