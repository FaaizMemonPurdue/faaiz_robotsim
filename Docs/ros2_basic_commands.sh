box_bot_gazebo

ros2 pkg create box_bot_gazebo --build-type ament_cmake --dependencies ament_cmake rclcpp rclpy

ros2 pkg create box_bot_description --build-type ament_cmake --dependencies ament_cmake urdf


colcon build --symlink-install --packages-ignore dolly_ignition

 colcon build --symlink-install --packages-select box_bot_gazebo

source install/setup.bash

# Launch single liner
ros2 launch box_bot_gazebo box_bot_launch.py
# If you want separted
ros2 launch box_bot_gazebo start_world_launch.py
ros2 launch box_bot_description start_world_launch.py

ros2 topic list

ros2 topic pub /box_bot/cmd_vel 


ros2 run teleop_twist_keyboard teleop_twist_keyboard cmd_vel:=/box_bot/cmd_vel
