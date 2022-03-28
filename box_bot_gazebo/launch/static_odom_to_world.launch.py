#! /usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.actions import OpaqueFunction

def launch_setup(context, *args, **kwargs):

    entity_name = LaunchConfiguration('box_bot_name').perform(context)
    odom_frame_name = entity_name + "_odom"
    name_node = odom_frame_name + "_static_transform_publisher"

    # Spawn ROBOT Set Gazebo
    st_pub = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name=name_node,
        output='screen',
        emulate_tty=True,
        arguments=['0', '0', '0', '0', '0', '0', 'world', odom_frame_name]
    )


    return [st_pub]


def generate_launch_description(): 

    box_bot_name_arg = DeclareLaunchArgument('box_bot_name', default_value='box_bot')

    return LaunchDescription([
        box_bot_name_arg,
        OpaqueFunction(function = launch_setup)
        ])