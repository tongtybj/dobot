#!/usr/bin/env python3
import rospy

from dobot.srv import *


def run(command, *args, **kwargs):
    rospy.wait_for_service(f'/DobotServer/{command.__name__}/')
    cmd = rospy.ServiceProxy(f'/DobotServer/{command.__name__}', command)
    response = cmd(*args, **kwargs)
    return response


def set_ptp_cmd(ptpMode, x, y, z, r):
    return run(SetPTPCmd, ptpMode, x, y, z, r)

def set_home_cmd():
    return run(SetHOMECmd)

def set_wait_cmd(timeout):
    return run(SetWAITCmd, timeout)

def set_end_effector_gripper(enableCtrl, grip, isQueued):
    return run(SetEndEffectorGripper, enableCtrl, grip, isQueued)

def get_pose():
    return run(GetPose)

