#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription


# this is the function launch  system will look for


def generate_launch_description():

    entity_name = "box_bot"


    spawn_controller = Node(
        package="controller_manager",
        executable="spawner.py",
        namespace=entity_name,
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    spawn_controller_traj = Node(
        package="controller_manager",
        executable="spawner.py",
        namespace=entity_name,
        arguments=["joint_trajectory_controller"],
        output="screen",
    )

    spawn_controller_velocity = Node(
        package="controller_manager",
        executable="spawner.py",
        namespace=entity_name,
        arguments=["velocity_controller"],
        output="screen",
    )

    

    # create and return launch description object
    return LaunchDescription(
        [
            spawn_controller,
            spawn_controller_traj,
            spawn_controller_velocity
        ]
    )