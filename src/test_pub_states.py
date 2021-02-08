#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Twist

#def callback(msg):
#        print(msg)

rospy.init_node('panda_read')
#sub = rospy.Subscriber('/pub_states', JointState, callback)
pub = rospy.Publisher('/mover/cart_vel', Twist, queue_size=1)

msg = Twist()
msg.linear.x = 0
msg.linear.y = -0.5
msg.linear.z = 1

rate = rospy.Rate(200)

while not rospy.is_shutdown():
        #pub.publish(msg)
        rate.sleep()
