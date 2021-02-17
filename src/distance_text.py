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
            msg_pos.pose.position.x = (pandaTrans[0] * -1) + 1.35 # 1.35 = 1.5 - (0.1 (cube size) + margin)
            msg_pos.pose.position.y = pandaTrans[1] * -1
            msg_pos.pose.position.z = pandaTrans[2] - 1
            pos_pub.publish(msg_pos)
    except Exception as e:
       pass 


if __name__ == "__main__":
    
    rospy.init_node('text_node')
    tl = tf.TransformListener()
    pos_pub = rospy.Publisher('/panda/text_pos', PoseStamped, queue_size=1)
    while not rospy.is_shutdown():
        publishPose(tl)
