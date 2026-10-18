# AeroGuard — LiDAR-Based Obstacle Avoidance Drone

## Project Overview

AeroGuard is an autonomous drone research and development project
focused on detecting obstacles and improving flight safety using
LiDAR and other onboard sensors.

The project uses ROS 2 and Gazebo to develop and test a drone model
and its obstacle avoidance capabilities in simulation.

## Objectives

- Develop a quadcopter model for simulation.
- Integrate LiDAR-based obstacle detection.
- Explore obstacle avoidance algorithms using ROS 2.
- Simulate the drone and obstacles in Gazebo.
- Prepare the system for future hardware integration.

## Technologies Used

- Ubuntu 22.04 LTS
- ROS 2 Humble
- Gazebo
- URDF and Xacro
- Python and ROS 2 nodes
- LiDAR and distance sensors (planned integration)
- PX4 Autopilot (simulation integration in progress)

## Project Structure

```text
AeroGuard/
├── urdf/        # Drone robot description files
├── meshes/      # 3D models of drone components
├── launch/      # ROS 2 launch files
├── worlds/      # Gazebo simulation worlds
├── config/      # Configuration files
├── package.xml  # ROS 2 package dependencies
├── CMakeLists.txt
└── README.md
