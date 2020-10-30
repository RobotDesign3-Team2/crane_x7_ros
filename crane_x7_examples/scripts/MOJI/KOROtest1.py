#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler

def main():

    Pos = [[0.39, 0.025,0.15],[0.39,0.025,0.14],[0.39,0.025,0.13],[0.39,0.025,0.12],[0.39,0.025,0.12],[0.39,0.025,0.11],[0.39,0.025,0.1],[0.39,0.015,0.1],[0.39,0.005,0.1],[0.39,-0.005,0.1],[0.39,-0.015,0.1],[0.39, -0.025, 0.1],[0.38, -0.025, 0.1],[0.37, -0.025, 0.1],[0.36, -0.025, 0.1],[0.35, -0.025, 0.1],[0.34, -0.025, 0.1],[0.34, -0.025, 0.11],[0.34, -0.025, 0.12],[0.34, -0.025, 0.13],[0.34, -0.025, 0.14],[0.34, -0.025, 0.15],[0.34, -0.015, 0.15],[0.34, -0.005, 0.15],[0.34, 0.005, 0.15],[0.34, 0.015, 0.15],[0.34, 0.015, 0.14],[0.34, 0.015, 0.13],[0.34, 0.015, 0.12],[0.34, 0.015, 0.11],[0.34, 0.025, 0.1],[0.34, 0.015, 0.1],[0.34, 0.005, 0.1],[0.34, -0.005, 0.1],[0.34, -0.015, 0.1],[0.34, -0.025, 0.1]] #コを書くための座標
    Ang = [[-3.14, 0.0, -1.57],[-1.57, 0.0, -1.57]]#いらない
    gri = [[0.1,0.1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1],[1,1]]#要らない
    Num = [1, 1, 1, 1, 1, 1, 1, 1]#コを書くための数
    i = 0;
    j = 0;
    PosR = [[0.32,0.025,0.15],[0.32,0.025,0.1],[0.27,0.025,0.1],[0.27,0.025,0.15],[0.32,0.025,0.15],[0.32,0.025,0.1],[0.32,-0.025,0.1],[0.27,-0.025,0.1],[0.27,-0.025,0.15],[0.27,0.025,0.15],[0.27,0.025,0.1],[0.27,-0.025,0.1]]
    NumR = [1,1,1,1,1,1,1,1,1,1,1,1]
    rospy.init_node("pose_groupstate_example")
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(0.1)
    gripper = moveit_commander.MoveGroupCommander("gripper")

    while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
        rospy.sleep(1.0)
    rospy.sleep(1.0)

    print("Group names:")
    print(robot.get_group_names())

    print("Current state:")
    print(robot.get_current_state())

    # アーム初期ポーズを表示
    arm_initial_pose = arm.get_current_pose().pose
    print("Arm initial pose:")
    print(arm_initial_pose)

    # 何かを掴んでいた時のためにハンドを開く
    gripper.set_joint_value_target([0.9, 0.9])
    gripper.go()

    # SRDFに定義されている"home"の姿勢にする
    print("home")
    arm.set_named_target("home")
    arm.go()

    # SRDFに定義されている"vertical"の姿勢にする
    print("vertical")
    arm.set_named_target("vertical")
    arm.go()

    # ハンドを少し閉じる
    gripper.set_joint_value_target([0.7, 0.7])
    gripper.go()

    
    # 手動で姿勢を指定するには以下のように指定

    gripper.set_joint_value_target([0.9, 0.9])
    gripper.go()
    
    print("コを書く")

    for Nums in Num:
        rospy.sleep(1.0)
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = Pos[i][0]#前のカッコのiで何番目の()か、後ろのカッコの0～2で何番目かを設定している
        target_pose.position.y = Pos[i][1]
        target_pose.position.z = Pos[i][2]
        q = quaternion_from_euler(Ang[Nums][0], Ang[Nums][1], Ang[Nums][2])  # 上方から掴み>に行く場合    
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)  # 目標ポーズ設定
        arm.go()

        print("位置")
        print(Pos[i])
        print("角度")
        print(Ang[Nums])
        if gri[i][0] < 1:
            print("グリップ力")
            print(gri[i])
            gripper.set_joint_value_target([gri[i][0], gri[i][1]])
            gripper.go()

        i = i + 1    


    print("コを書いた")
    print("ロを書く")
    i = 0

    for Nums in NumR:
        rospy.sleep(1.0)
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = PosR[i][0]
        target_pose.position.y = PosR[i][1]
        target_pose.position.z = PosR[i][2]
        q = quaternion_from_euler(Ang[1][0], Ang[1][1], Ang[1][2])  # 上方から掴み>に行く場
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)  # 目標ポーズ設定
        arm.go()
        print("位置")
        print(PosR[i])
        print("角度")
        print(Ang[1])
        i = i + 1


    print("ロを書いた")
    print("コロ完成！")

    
    # 移動後の手先ポーズを表
#座標は+-で決定する、0.2～0.5が安定

if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
