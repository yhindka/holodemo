#!/usr/bin/env python

import rospy
import tf
from geometry_msgs.msg import PoseStamped


robopos = [1.5, 0, -1]


def publishPose(tl):

    pandaRot = ()
    pandaTrans = ()
    try:
        (pandaTrans, pandaRot) = tl.lookupTransform("panda_link0", "sim_end_effector", rospy.Time(0))
        if pandaTrans != None and pandaRot != None:
            # publish PoseStamped of text 
            msg_pos = PoseStamped()
            msg_pos.pose.position.x = (pandaTrans[0] * -1) + (robopos[0] - 0.15) # 0.15 = 0.1 (cube size) + margin
            msg_pos.pose.position.y = (pandaTrans[1] * -1) + robopos[1]
            msg_pos.pose.position.z = pandaTrans[2] + robopos[2]
            pos_pub.publish(msg_pos)
    except Exception as e:
       pass 

def callback(msg):
    robopos[0] = msg.pose.position.x
    robopos[1] = msg.pose.position.y
    robopos[2] = msg.pose.position.z


if __name__ == "__main__":
    
    rospy.init_node('text_node')
    tl = tf.TransformListener()
    pos_pub = rospy.Publisher('/panda/text_pos', PoseStamped, queue_size=1)
    pos_sub = rospy.Subscriber('/panda_pose', PoseStamped, callback)
    while not rospy.is_shutdown():
        publishPose(tl)
