#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2021, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    hw_ns = LaunchConfiguration('hw_ns', default='xarm')
    log_level = LaunchConfiguration('log_level', default='info')

    # robot moveit fake launch
    # xarm_moveit_config/launch/_robot_moveit_fake.launch.py
    robot_moveit_fake_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([FindPackageShare('xarm_moveit_config'), 'launch', '_robot_moveit_fake.launch.py'])),
        launch_arguments={
            'dof': '6',
            'robot_type': 'xarm',
            'hw_ns': hw_ns,
            'no_gui_ctrl': 'false',
            'add_vacuum_gripper':'true',
        }.items(),
    )
    
    return LaunchDescription([
        DeclareLaunchArgument('log_level', default_value='info', description='Logging level'), 
        robot_moveit_fake_launch
    ])
