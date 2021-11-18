#!/usr/bin/env python3
import rospy

from dobot.srv import *


def set_ptp_cmd(ptpMode, x, y, z, r):
    rospy.wait_for_service('/DobotServer/SetPTPCmd')
    cmd = rospy.ServiceProxy('/DobotServer/SetPTPCmd', SetPTPCmd)
    response = cmd(ptpMode, x, y, z, r)
    return response

def set_home_cmd():
    rospy.wait_for_service('/DobotServer/SetHOMECmd')
    cmd = rospy.ServiceProxy('/DobotServer/SetHOMECmd', SetHOMECmd)
    response = cmd()
    return response

def set_wait_cmd(timeout):
    rospy.wait_for_service('/DobotServer/SetWAITCmd')
    cmd = rospy.ServiceProxy('/DobotServer/SetWAITCmd', SetWAITCmd)
    response = cmd(timeout)
    return response

def set_end_effector_gripper(enableCtrl, grip, isQueued):
    rospy.wait_for_service('/DobotServer/SetEndEffectorGripper')
    cmd = rospy.ServiceProxy('/DobotServer/SetEndEffectorGripper', SetEndEffectorGripper)
    response = cmd(enableCtrl, grip, isQueued)
    return response


def get_pose():
    rospy.wait_for_service('/DobotServer/GetPose')
    cmd = rospy.ServiceProxy('/DobotServer/GetPose', GetPose)
    response = cmd()
    return response

