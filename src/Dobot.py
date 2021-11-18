#!/usr/bin/env python3
import rospy
import DobotClient as dc


if __name__ == "__main__":
    resp = dc.set_ptp_cmd(1,200,0,0,0)
    resp = dc.set_ptp_cmd(1,250,0,0,0)
    resp = dc.set_home_cmd()
    resp = dc.get_pose()
    print(resp)
    resp = dc.set_wait_cmd(3)
    # resp = dc.set_end_effector_gripper(1,0,1)
    # resp = dc.set_end_effector_gripper(1,1,1)
    resp = dc.set_ptp_cmd(1,200,0,0,0)
    resp = dc.set_ptp_cmd(1,250,0,0,0)