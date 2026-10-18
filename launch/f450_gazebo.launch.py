import os
import xacro

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # F450 package
    pkg_path = get_package_share_directory('f450')

    # Drone Xacro file
    xacro_file = os.path.join(
        pkg_path,
        'urdf',
        'f450.xacro'
    )

    # Gazebo world
    world_file = os.path.join(
        pkg_path,
        'worlds',
        'f450_world.sdf'
    )

    # Convert Xacro to URDF
    robot_description = xacro.process_file(xacro_file).toxml()

    # Start Gazebo Sim
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('ros_gz_sim'),
                'launch',
                'gz_sim.launch.py'
            )
        ),
        launch_arguments={
            'gz_args': f'-r {world_file}'
        }.items()
    )

    # Publish robot description and TF
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': robot_description,
                'use_sim_time': True
            }
        ]
    )

    # Spawn the drone after Gazebo starts
    spawn_drone = TimerAction(
        period=4.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                name='spawn_f450',
                output='screen',
                arguments=[
                    '-topic', 'robot_description',
                    '-name', 'f450',
                    '-x', '0',
                    '-y', '0',
                    '-z', '0.5'
                ]
            )
        ]
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_drone
    ])

