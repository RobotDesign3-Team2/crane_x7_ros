#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import rosnode
import csv
from tf.transformations import quaternion_from_euler
import csv #csvファイルを開くと宣言

def main():
#読み込むcsvファイル＊＊＊＊csvファイルの中身を変えるだけで動きが変更出来る＊＊＊＊	
    fl = ["KO.csv","RO.csv","NA.csv"] #[コ、ロ、ナ]が入っている
    fl1 = ["ROs.csv","SUs.csv"]#[ロ、ス]が入っている
    fl2 = "NURA.csv"#ぬらすモーション

    rospy.init_node("pose_groupstate_example")
    robot = moveit_commander.RobotCommander()
    arm = moveit_commander.MoveGroupCommander("arm")
    arm.set_max_velocity_scaling_factor(0.1)
    gripper = moveit_commander.MoveGroupCommander("gripper")
    def move_max_velocity(value = 0.2):#速度調節関数
        arm.set_max_velocity_scaling_factor(value)#速度を調整する部分()の中に値を入れると変更出来る
    while len([s for s in rosnode.get_node_names() if 'rviz' in s]) == 0:
        rospy.sleep(1.0)
    rospy.sleep(1.0)

    def move_arm(pos_x, pos_y, pos_z, move):#アームの動き関数 move_arm(0.5, 0.5, 0.1 ,0.1)などのように使用
	    move_max_velocity(move)#速度調整関数
	    target_pose = geometry_msgs.msg.Pose()
	    target_pose.position.x = pos_x#x代入
	    target_pose.position.y = pos_y#y代入
	    target_pose.position.z = pos_z#z代入
	    q = quaternion_from_euler(3.14/2.0, 0.0, 3.14/2.0) 
	    target_pose.orientation.x = q[0]
	    target_pose.orientation.y = q[1]
	    target_pose.orientation.z = q[2]
	    target_pose.orientation.w = q[3]
	    arm.set_pose_target(target_pose)  # 目標ポーズ設定
	    arm.go()  # 実行
	    print("位置")
	    print(pos_x, pos_y, pos_z)
	    print("速度")
	    print(move)

    # アーム初期ポーズを表示
    arm_initial_pose = arm.get_current_pose().pose
    print("Arm initial pose:")
    print(arm_initial_pose)

    # 何かを掴んでいた時のためにハンドを開く
    gripper.set_joint_value_target([0.9, 0.9])#アームの開閉に使用値がでかいほど大きく開く*アームを開く
    gripper.go()

    # SRDFに定義されている"vertical"の姿勢にする
    print("vertical")
    move_max_velocity(0.2)
    arm.set_named_target("vertical")
    arm.go()
	
#筆をつかむ位置に移動
    move_arm(0.38*1.3-0.1, 0.024*1.3, 0.2, 0.2)#(x,y,z,速さ)
    print("筆を掴ませる待ち時間")
    rospy.sleep(5.0) #ここで筆を掴む
    
    gripper.set_joint_value_target([0.1, 0.1])#アームを閉じる
    gripper.go()
    move_arm(0.386*1.2-0.08,0.024*1.2,0.2, 0.1)#コを書く最初の位置に移動

     #筆に水をつける
#     import csv
#     with open(fl2) as f: # |
#         for row in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):#ファイル
#             rospy.sleep(1.0)
#             move_arm(row[0],row[1],row[2], 0.05) #move_arm(X,Y,Z, アームの>    スピード)
#     rospy.sleep(8.0)
#     move_arm(0.386,0.024,0.2, 0.05)


#文字を書く(コロナ)
    for FL in fl:#ファイルの数ループ
<<<<<<< HEAD
=======
	 #csvファイルを開くと宣言
>>>>>>> ecbac35f9b601d9b43d65fd0cdd10fc0574f2ecf
	with open(FL) as f: #ファイルを開く
	    for row in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):#ファイルを数値型に変更しrowに代入
		move_arm(row[0]*1.2-0.08,row[1]*1.2,row[2], 0.05) #move_arm(X,Y,Z, アームのスピード)
		rx = row[0]#最終座標のメモ
		ry = row[1]#  |
		rz = row[2]#  |
	rospy.sleep(1.0) #一秒待機

    move_arm(rx*1.2,ry*1.2,rz+0.05, 0.05)#垂直持ち上げ
    move_arm(rx*1.2,ry*1.2,rz+0.1, 0.1)#     |

#文字を書く(ロス)
#    for FL in fl1:#ファイルの数ループ
#	import csv#csvファイルを開くと宣言
#	with open(FL) as f:#ファイルを開く
#	    for row in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):#ファイルを数値型に変更しrowに代入
#		rospy.sleep(1.0)#一秒待機
#		move_arm(row[0]-0.05,row[1]+0.03,row[2], 0.02) #move_arm(X,Y,Z, アームのスピード)
#		rx = row[0] #最終座標のメモ
#		ry = row[1] #　｜
#		rz = row[2] #　｜
#
#    move_arm(rx,ry,rz+0.05, 0.05)#垂直持ち上げ
#    move_arm(rx,ry,rz+0.1, 0.1)#     |


    print("vertical")
    move_max_velocity(0.2)#アームを初期位置に戻す
    arm.set_named_target("vertical")
    arm.go()

if __name__ == '__main__':
    try:
        if not rospy.is_shutdown():
            main()
    except rospy.ROSInterruptException:
        pass
