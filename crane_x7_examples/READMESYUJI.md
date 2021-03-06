
# crane_x7_syuji

私たちの課題、「crane_x7に文字を書かせる」に用いるコードをまとめたパッケージです。

## システムの起動方法

CRANE-X7の制御信号ケーブルを制御用パソコンへ接続します。
Terminalを開き、`crane_x7_bringup`の`demo.launch`を起動します。
このlaunchファイルには次のオプションが用意されています。

- fake_execution (default: true)

実機を使用する/使用しない

### シミュレータを使う場合 

実機無しで動作を確認する場合、
制御信号ケーブルを接続しない状態で次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=true
```

### 実機を使う場合

・実機起動

実機で動作を確認する場合、
制御信号ケーブルを接続した状態で次のコマンドを実行します。

```sh
roslaunch crane_x7_bringup demo.launch fake_execution:=false
```
・プログラム起動

まず次のディレクトリに移動します。

```sh
/catkin_ws/src/crane_x7_ros/crane_x7_syuji/scripts/MOJI/MOJIcsv
```

次のコマンドを実行します。
```sh
rosrun crane_x7_syuji Mcav4.py
```

### gazeboを使う場合

・gazebo起動

次のコマンドで起動します。実機との接続やcrane_x7_bringupの実行は必要ありません。

```sh
roslaunch crane_x7_gazebo crane_x7_with_table.launch
```

・プログラム起動

次のコマンドでプログラムのディレクトリに移動します。

```sh
/catkin_ws/src/crane_x7_ros/crane_x7_syuji/scripts/MOJI/MOJIcsv
```

次のコマンドでプログラムを実行します。

```sh
rosrun crane_x7_syuji Mcav4.py
```

コロナのみを書く場合は次のコマンドでプログラムを実行します。
```sh
rosrun crane_x7_syuji Mcav5.py
```


