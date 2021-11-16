#!/usr/bin/env python3

import rospy

from dynamic_reconfigure.server import Server
from dobot_ros.cfg import dobotConfig
from dobot_ros.msg import dobot
from rospy import client
import serial
import time
import pydobot

class dobot_ros():
    def __init__(self):
        #通信の接続
        port = "/dev/ttyUSB1"
        self.device = pydobot.Dobot(port=port, verbose=True)
        self.srv = Server(dobotConfig, self.callback)

    def callback(self, config, level):
        rospy.loginfo("""Reconfigure Request: {x}, {y}, {z}, {r}, {velocity}, {acceleration}, {grip}, {suck}""".format(**config))
        dobot.x = float("{x}".format(**config))
        dobot.y = float("{y}".format(**config))
        dobot.z = float("{z}".format(**config))
        dobot.r = float("{r}".format(**config))
        dobot.velocity = int("{velocity}".format(**config))
        dobot.acceleration = int("{acceleration}".format(**config))
        dobot.grip = "{grip}".format(**config)
        dobot.suck = "{suck}".format(**config)
        self.device.move_to(dobot.x, dobot.y, dobot.z, dobot.r, wait=False)
        # self.device.speed(dobot.velocity,dobot.acceleration)
        # self.device.suck(dobot.suck)
        # self.device.grip(dobot.grip)
        self.device.wait(1000)
        return config

if __name__ == "__main__":
    rospy.init_node("dobot_ros", anonymous = True)
    dobot_controller = dobot_ros()
    rospy.spin()