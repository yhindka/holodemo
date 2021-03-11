#!/usr/bin/env python

import rospy
from sensor_msgs.msg import CompressedImage, CameraInfo
from holodemo.msg import MyCameraInfo

def callback(msg):
    print("photo received")

def callback2(msg):
    camMsg = CameraInfo()
    camMsg.header.frame_id = msg.frameID
    camMsg.distortion_model = msg.distortion_model
    camMsg.height = msg.height
    camMsg.width = msg.width
    camMsg.D = [0.6679244637489319, -2.6938982009887695, 0.0009035157854668796, 
                -0.0001931091828737408, 1.4591891765594482, 0.5460429191589355, 
                -2.528550148010254, 1.3961073160171509]
    camMsg.K = [980.1734619140625, 0.0, 1024.3494873046875, 0.0, 979.7545166015625, 
                782.9638671875, 0.0, 0.0, 1.0]
    camMsg.R = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
    camMsg.P = [980.1734619140625, 0.0, 1024.3494873046875, 0.0, 0.0, 979.7545166015625, 
                782.9638671875, 0.0, 0.0, 0.0, 1.0, 0.0]
    camMsg.binning_x = msg.binning_x
    camMsg.binning_y = msg.binning_y
    caminfo_pub.publish(camMsg)
    print("camera info published")
    

if __name__ == "__main__":
    rospy.init_node('photo_sub')
    compressed_sub = rospy.Subscriber('/compressed_photo/compressed', CompressedImage, callback)
    cam_sub = rospy.Subscriber('/my_camera_info', MyCameraInfo, callback2)
    caminfo_pub = rospy.Publisher('/camera_info', CameraInfo, queue_size=1)
    while not rospy.is_shutdown():
        continue
