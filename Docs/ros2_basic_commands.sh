box_bot_gazebo

ros2 pkg create box_bot_gazebo --build-type ament_cmake --dependencies ament_cmake rclcpp rclpy


colcon build --symlink-install --packages-ignore dolly_ignition

 colcon build --symlink-install --packages-select box_bot_gazebo

source install/setup.bash

ros2 launch box_bot_gazebo start_world_launch.py

ros2 topic list

ros2 topic pub /box_bot/cmd_vel 
