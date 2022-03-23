import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

# this is the function launch  system will look for


def generate_launch_description():

    # Base Name or robot
    entity_name = "box_bot"
    robot_description_topic_name = "/" + entity_name + "_robot_description"
    robot_state_publisher_name= entity_name + "_robot_state_publisher"
    joint_state_topic_name= "/" + entity_name + "/joint_states"

    ####### DATA INPUT ##########
    urdf_file = 'box_bot.urdf'
    #xacro_file = "box_bot.xacro"
    package_description = "box_bot_description"    

    ####### DATA INPUT END ##########
    print("Fetching URDF ==>")
    robot_desc_path = os.path.join(get_package_share_directory(
        package_description), "urdf", urdf_file)

    robot_desc = xacro.process_file(robot_desc_path)
    xml = robot_desc.toxml()

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name=robot_state_publisher_name,
        emulate_tty=True,
        parameters=[{'use_sim_time': True, 'robot_description': xml}],
        remappings=[("/robot_description", robot_description_topic_name),
                    ("/joint_states", joint_state_topic_name)
                    ],
        output="screen"
    )

    # create and return launch description object
    return LaunchDescription(
        [
            robot_state_publisher_node
        ]
    )
