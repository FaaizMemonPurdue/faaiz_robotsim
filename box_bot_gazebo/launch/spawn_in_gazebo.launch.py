import os
from launch import LaunchDescription
from launch_ros.actions import Node

# this is the function launch  system will look for


def generate_launch_description():

    # Position and orientation
    # [X, Y, Z]
    position = [0.0, 0.0, 1.0]
    # [Roll, Pitch, Yaw]
    orientation = [0.0, 0.0, 0.0]
    # Base Name or robot
    entity_name = "box_bot_1"
    robot_description_topic_name = "/" + entity_name + "_robot_description"

    # Spawn ROBOT Set Gazebo
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='cam_bot_spawn_entity',
        output='screen',
        emulate_tty=True,
        arguments=['-entity',
                   entity_name,
                   '-x', str(position[0]), '-y', str(position[1]
                                                     ), '-z', str(position[2]),
                   '-R', str(orientation[0]), '-P', str(orientation[1]
                                                        ), '-Y', str(orientation[2]),
                   '-topic', robot_description_topic_name
                   ]
    )

    return LaunchDescription(
        [
            spawn_robot
        ]
    )
