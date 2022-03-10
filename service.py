#!/usr/bin/env python

import rospy
import sys
from ur5_pruning_trails.srv import position
from std_srvs.srv import Empty, Trigger, SetBool
import serial
import time
arduino = serial.Serial(port='/dev/ttyACM1', baudrate=115200, timeout=.1)

class Service_linear_axis(object):
    def __init__(self):
        rospy.Service('Home_linear', Empty, self.callback_home)
        # rospy.Service('Move_linear',position, self.callback_move)
        # rospy.Service('Stop_linear', Empty, self.callback_stop)

    def callback_move(self, mess):
        tomove=str(mess)[10:]
        print(tomove)
        send_move=" ".join(("M", tomove))
        arduino.write(send_move.encode())
        print(send_move)
        print("Service to move")
        return []

    def callback_home(self, *_, **__):
        print("Service activated to home")
        arduino.write('H'.encode())
        return []

    def callback_stop(self, *_, **__):
        print("Service to stop")
        arduino.write('S'.encode())
        return []
if __name__ == '__main__':
    rospy.init_node('Service_linear_axis')
    service =Service_linear_axis()


    rospy.spin()
