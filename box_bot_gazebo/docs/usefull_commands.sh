commands:

ros2 daemon stop;ros2 daemon start;rm -rf build/ install/ log/;colcon build --symlink-install;source install/setup.bash ;ros2 launch box_bot_gazebo start_world.launch.py 

ros2 daemon stop;ros2 daemon start;rm -rf build/ install/ log/;colcon build --symlink-install;source install/setup.bash ;ros2 launch box_bot_gazebo main.launch.xml 



source install/setup.bash;reset;ros2 launch box_bot_gazebo main_box_bot_1.launch.xml
source install/setup.bash;reset;ros2 launch box_bot_gazebo main_box_bot_2.launch.xml

rviz2

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/box_bot_1/cmd_vel
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/box_bot_2/cmd_vel


ros2 topic pub /box_bot_2/velocity_controller/commands std_msgs/msg/Float64MultiArray "layout:
  dim: []
  data_offset: 0
data: [-20.0]
"

ros2 topic pub /box_bot_1/velocity_controller/commands std_msgs/msg/Float64MultiArray "layout:
  dim: []
  data_offset: 0
data: [-20.0]
"


ros2 run box_bot_gazebo move_laser.py -0.0 box_bot_1
ros2 run box_bot_gazebo move_laser.py -0.05 box_bot_1

