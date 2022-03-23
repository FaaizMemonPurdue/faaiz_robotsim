#!/usr/bin/python3
# -*- coding: utf-8 -*-
from launch_ros.actions import Node
from launch import LaunchDescription

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction


def launch_setup(context, *args, **kwargs):

    box_bot_name = LaunchConfiguration('box_bot_name').perform(context)
    spawn_controller_1_name = box_bot_name + "spawn_controller_joint_state_broadcaster"
    spawn_controller_2_name = box_bot_name + "spawn_controller_joint_trajectory_controller"
    spawn_controller_3_name = box_bot_name + "spawn_controller_velocity_controller"
    controller_manager_name = "/"  + box_bot_name + "/controller_manager"

    #--controller-manager Name of the controller manager ROS node
    spawn_controller_1 = Node(
        package="controller_manager",
        executable="spawner",
        name=spawn_controller_1_name,
        namespace=box_bot_name,
        arguments=["joint_state_broadcaster", "--controller-manager", controller_manager_name],
        output="screen"
    )

    spawn_controller_2 = Node(
        package="controller_manager",
        executable="spawner",
        name=spawn_controller_2_name,
        namespace=box_bot_name,
        arguments=["joint_trajectory_controller", "--controller-manager", controller_manager_name],
        output="screen"
    )

    spawn_controller_3 = Node(
        package="controller_manager",
        executable="spawner",
        name=spawn_controller_3_name,
        namespace=box_bot_name,
        arguments=["velocity_controller", "--controller-manager", controller_manager_name],
        output="screen"
    )


    return [spawn_controller_1, spawn_controller_2, spawn_controller_3]


def generate_launch_description(): 

    box_bot_name_arg = DeclareLaunchArgument('box_bot_name', default_value='box_bot')

    return LaunchDescription([
        box_bot_name_arg,
        OpaqueFunction(function = launch_setup)
        ])