#!/usr/bin/env python

import rospy
import tf2_ros
from geometry_msgs.msg import Pose, PoseStamped, TransformStamped

trans = ()
rot = ()

def getPose():
    
    try:
        trans = buf.lookup_transform("tag1", "panda_link0", rospy.Time(0))
        msg = Pose()
        msg.position.x = trans.transform.translation.x
        msg.position.y = trans.transform.translation.y
        msg.position.z = trans.transform.translation.z
        msg.orientation.x = trans.transform.rotation.x
        msg.orientation.y = trans.transform.rotation.y
        msg.orientation.z = trans.transform.rotation.z
        pub.publish(msg)

    except Exception as e:
        print(e)
        pass

def callback(msg):
    t = TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "panda_link0"
    t.child_frame_id = "Camera"
    t.transform.translation.x = msg.pose.position.x
    t.transform.translation.y = msg.pose.position.y
    t.transform.translation.z = msg.pose.position.z
    t.transform.rotation.x = msg.pose.orientation.x
    t.transform.rotation.y = msg.pose.orientation.y
    t.transform.rotation.z = msg.pose.orientation.z
    t.transform.rotation.w = msg.pose.orientation.w

    br.sendTransform(t)


if __name__ == "__main__":
    rospy.init_node('place_robot')
    buf = tf2_ros.Buffer()
    tl = tf2_ros.TransformListener(buf)
    br = tf2_ros.TransformBroadcaster()
    sub = rospy.Subscriber('/panda_pose', PoseStamped, callback)
    pub = rospy.Publisher('/robot_pos', Pose, queue_size=1)
    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        getPose()
        rate.sleep()
