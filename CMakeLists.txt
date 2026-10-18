cmake_minimum_required(VERSION 3.8)
project(f450)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY
    urdf
    meshes
    launch
    worlds
    config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
