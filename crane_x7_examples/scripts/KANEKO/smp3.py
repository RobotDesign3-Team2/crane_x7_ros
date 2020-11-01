#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
from tf.transformations import quaternion_from_euler


def main():
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
    gripper.go() #gripper.go()＜－このコードでなんか動かす

    
    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.2 #xの位置決める　奥行
    target_pose.position.y = -0.2 #yの位置決める　左右の移動
    target_pose.position.z = 0.3 #zの位置決める　高さ
    q = quaternion_from_euler(-3.14, 0.0, -3.14/2.0)  # 上方から掴み　原理はオイラー角を調べればわかりそう（わかっていない）
    target_pose.orientation.x = q[0]　#おまじない的な
    target_pose.orientation.y = q[1]  #｜
    target_pose.orientation.z = q[2]  #｜　
    target_pose.orientation.w = q[3]  #｜
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()
    
    gripper.set_joint_value_target([0.7, 0.7]) #アームの開閉
    gripper.go() 


    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.2
    target_pose.position.y = -0.2
    target_pose.position.z = 0.1
    q = quaternion_from_euler(-3.14, 0.0, -3.14/2.0)  # 上方から掴み
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()  # 実行

    gripper.set_joint_value_target([0.15, 0.15])
    gripper.go()

    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.2
    target_pose.position.y = -0.2
    target_pose.position.z = 0.3
    q = quaternion_from_euler(-3.14, 0.0, -3.14/2.0)  # 上方から掴み
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()

    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.2
    target_pose.position.y = -0.2
    target_pose.position.z = 0.3
    q = quaternion_from_euler(-3.14/2, 0.0, -3.14/2.0)  # 横から掴み
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()



    target_pose = geometry_msgs.msg.Pose()
    target_pose.position.x = 0.2
    target_pose.position.y = 0.0
    target_pose.position.z = 0.3 
    q = quaternion_from_euler(-3.14/2, 0.0, -3.14/2.0)  # 横から掴み
    target_pose.orientation.x = q[0]
    target_pose.orientation.y = q[1]
    target_pose.orientation.z = q[2]
    target_pose.orientation.w = q[3]
    arm.set_pose_target(target_pose)  # 目標ポーズ設定
    arm.go()


    print("あああああああああああ")

    
    # 移動後の手先ポーズを表


if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass