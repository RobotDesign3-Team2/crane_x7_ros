#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler


def main():
    Pos = [[0.2,-0.2,0.3],[0.2, -0.2, 0.1],[0.2, -0.2, 0.3],[0.2, -0.2, 0.3],[0.2, 0.0, 0.3]] #マニュピレータの位置を決める2次元配列配列みたいなの[2次元のリスト型]
    Ang = [[-3.14, 0.0, -1.57],[-1.57, 0.0, -1.57]] #アームの角度の調整のリスト
    gri = [[0.7,0.7],[0.15, 0.15],[1,1],[1,1],[1,1]] #アームのパワーを決めるリスト[１，１]はif文で無視されるようになっている
    Num = [0, 0, 0, 1, 1] #for文でループさせるときに使っている＆アームの角度を調整する
    c = 0;
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

#    for Nums in Num:  #カウンタ変数で for文を回せないっぽいので配列Numを使っている　（Numのリストの数のぶんループさせる）カウンタ変数をつかえたら教えてほしい！
    for i in range(0,5):  #カウンタ変数で for文を回せないっぽいので配列Numを使っている　（Numのリストの数のぶんループさせる）カウンタ変数をつかえたら教えてほしい！
        target_pose = geometry_msgs.msg.Pose()
        target_pose.position.x = Pos[i][0]
        target_pose.position.y = Pos[i][1]
        target_pose.position.z = Pos[i][2]
        q = quaternion_from_euler(Ang[c][0], Ang[c][1], Ang[c][2])  # 上方から掴み>に行く場合    target_pose = geometry_msgs.msg.Pose()
        target_pose.orientation.x = q[0]
        target_pose.orientation.y = q[1]
        target_pose.orientation.z = q[2]
        target_pose.orientation.w = q[3]
        arm.set_pose_target(target_pose)  # 目標ポーズ設定
        arm.go()
        print("位置")
        print(Pos[i])
        print("角度")
        print(Ang[c])
        if gri[i][0] < 1:#毎回グリップの力を宣言しているのは動きのロスになるのでgirの配列の中が１の時の場合は宣言しないようにしている（良いやり方があったら教えてほしい）
            print("グリップ力")
            print(gri[i])
            gripper.set_joint_value_target([gri[i][0], gri[i][1]])
            gripper.go()
        if i > 2:
            c+=1

    gripper.set_joint_value_target([0.15, 0.15])
    gripper.go()


    print("end")

if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
