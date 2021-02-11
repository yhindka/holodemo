#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import PoseStamped


def publishPose(tl):

    pandaRot = ()
    pandaTrans = ()
    try:
        (pandaTrans, pandaRot) = tl.lookupTransform("panda_link0", "sim_end_effector", rospy.Time(0))
        if pandaTrans != None and pandaRot != None:
            # publish PoseStamped of text 
            msg_pos = PoseStamped()
            msg_pos.pose.position.x = pandaTrans[0] + 0.5
            msg_pos.pose.position.y = pandaTrans[1] * -1
            msg_pos.pose.position.z = pandaTrans[2] - 1
            """msg_pos.pose.orientation.x = pandaRot[0]
            msg_pos.pose.orientation.y = pandaRot[1]
            msg_pos.pose.orientation.z = pandaRot[2]
            msg_pos.pose.orientation.w = pandaRot[3]"""
            pos_pub.publish(msg_pos)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    
    rospy.init_node('text_node')
    tl = tf.TransformListener()
    pos_pub = rospy.Publisher('/panda/text_pos', PoseStamped, queue_size=1)
    while not rospy.is_shutdown():
        publishPose(tl)
    #rospy.spin()
