#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription


# this is the function launch  system will look for


def generate_launch_description():

    entity_name = "box_bot"

    # More info on arguments:
    # https://github.com/ros-controls/ros2_control/blob/galactic/controller_manager/scripts/spawner.py

    spawn_controller_1 = Node(
        package="controller_manager",
        executable="spawner",
        name="bob1",
        namespace=entity_name,
        arguments=["joint_state_broadcaster", "--controller-manager", "/box_bot/controller_manager"],
        output="screen"
    )

    spawn_controller_2 = Node(
        package="controller_manager",
        executable="spawner",
        name="bob2",
        namespace=entity_name,
        arguments=["joint_trajectory_controller", "--controller-manager", "/box_bot/controller_manager"],
        output="screen"
    )

    spawn_controller_3 = Node(
        package="controller_manager",
        executable="spawner",
        name="bob3",
        namespace=entity_name,
        arguments=["velocity_controller", "--controller-manager", "/box_bot/controller_manager"],
        output="screen"
    )

    

    # create and return launch description object
    return LaunchDescription(
        [
            spawn_controller_1,
            spawn_controller_2,
            spawn_controller_3,
        ]
    )