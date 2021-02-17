cmake_minimum_required(VERSION 2.8.3)
project(holodemo)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS 
        roscpp 
        tf 
        cv_bridge 
        image_transport 
        visualization_msgs
        image_geometry 
        nodelet
	message_generation)

## System dependencies
find_package(OpenCV REQUIRED)

find_package(Eigen3 REQUIRED)

message(STATUS "OpenCV version: ${OpenCV_VERSION}")
if(2.9.0 VERSION_GREATER ${OpenCV_VERSION})
    message(FATAL "OpenCV3 required!")
endif()

add_message_files(
  FILES
  zone.msg
)

generate_messages(
  DEPENDENCIES 
)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES ros_markers
  CATKIN_DEPENDS 
    tf
    nodelet
    message_runtime
  DEPENDS OpenCV
  LIBRARIES 
)



###########
## Build ##
###########

include_directories(include ${catkin_INCLUDE_DIRS} ${EIGEN3_INCLUDE_DIR})


add_definitions(-std=c++11)

set(LIBS 
    ${catkin_LIBRARIES}
    ${OpenCV_LIBRARIES}
    )

add_executable(pandaJacob src/jacob.cpp)
target_include_directories(pandaJacob PUBLIC ${catkin_INCLUDE_DIRS} ${EIGEN3_INCLUDE_DIR} /home/senft/catkin_ws/devel/include )
target_link_libraries(pandaJacob
   ${catkin_LIBRARIES}
)

#############
## Install ##
#############

install(DIRECTORY
    launch/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
install(DIRECTORY
    rviz/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/rviz
)
install(DIRECTORY
    urdfs/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdfs
)
install(DIRECTORY
    meshes/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/meshes
)

catkin_install_python(PROGRAMS
    nodes/static_publisher
    nodes/viz_manager
    nodes/mover
    nodes/pose_broadcaster
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

install(TARGETS pandaJacob
  RUNTIME DESTINATION lib/holodemo
)
