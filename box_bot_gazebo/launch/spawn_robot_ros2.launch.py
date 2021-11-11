import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

from launch_ros.actions import Node
import xacro


# this is the function launch  system will look for
def generate_launch_description():

    urdf_file = 'box_bot_v2.urdf'
    xacro_file = "box_bot.xacro"

    package_description = "box_bot_description"

    urdf_path = os.path.join(get_package_share_directory(package_description), "robot", urdf_file)
    xacro_path = os.path.join(get_package_share_directory(package_description), "robot", xacro_file)

    robot_desc = xacro.process_file(xacro_path)
    xml = robot_desc.toxml()

    # Spawn ROBOT Set Gazebo
    spawn_robot = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_entity',
        output='screen',
        arguments=['-entity',
                   'box_bot',
                   '-x', '0.75', '-y', '0.5', '-z', '1.1',
                   '-topic', '/robot_description'
                   ]
    )
    
    # Publish Robot Desciption in String form in the topic /robot_description
    publish_robot_description = Node(
        package='box_bot_gazebo',
        executable='robot_description_publisher.py',
        name='robot_description_publisher',
        output='screen',
        arguments=['-xml_string', xml,
                   '-robot_description_topic', '/robot_description'
                   ]
    )

    # create and return launch description object
    return LaunchDescription(
        [            
            spawn_robot,
            publish_robot_description
        ]
    )
