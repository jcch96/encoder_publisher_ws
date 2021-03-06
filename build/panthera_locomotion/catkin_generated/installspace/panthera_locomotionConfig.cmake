# generated from catkin/cmake/template/pkgConfig.cmake.in

# append elements to a list and remove existing duplicates from the list
# copied from catkin/cmake/list_append_deduplicate.cmake to keep pkgConfig
# self contained
macro(_list_append_deduplicate listname)
  if(NOT "${ARGN}" STREQUAL "")
    if(${listname})
      list(REMOVE_ITEM ${listname} ${ARGN})
    endif()
    list(APPEND ${listname} ${ARGN})
  endif()
endmacro()

# append elements to a list if they are not already in the list
# copied from catkin/cmake/list_append_unique.cmake to keep pkgConfig
# self contained
macro(_list_append_unique listname)
  foreach(_item ${ARGN})
    list(FIND ${listname} ${_item} _index)
    if(_index EQUAL -1)
      list(APPEND ${listname} ${_item})
    endif()
  endforeach()
endmacro()

# pack a list of libraries with optional build configuration keywords
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_pack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  set(_argn ${ARGN})
  list(LENGTH _argn _count)
  set(_index 0)
  while(${_index} LESS ${_count})
    list(GET _argn ${_index} lib)
    if("${lib}" MATCHES "^(debug|optimized|general)$")
      math(EXPR _index "${_index} + 1")
      if(${_index} EQUAL ${_count})
        message(FATAL_ERROR "_pack_libraries_with_build_configuration() the list of libraries '${ARGN}' ends with '${lib}' which is a build configuration keyword and must be followed by a library")
      endif()
      list(GET _argn ${_index} library)
      list(APPEND ${VAR} "${lib}${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}${library}")
    else()
      list(APPEND ${VAR} "${lib}")
    endif()
    math(EXPR _index "${_index} + 1")
  endwhile()
endmacro()

# unpack a list of libraries with optional build configuration keyword prefixes
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_unpack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  foreach(lib ${ARGN})
    string(REGEX REPLACE "^(debug|optimized|general)${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}(.+)$" "\\1;\\2" lib "${lib}")
    list(APPEND ${VAR} "${lib}")
  endforeach()
endmacro()


if(panthera_locomotion_CONFIG_INCLUDED)
  return()
endif()
set(panthera_locomotion_CONFIG_INCLUDED TRUE)

# set variables for source/devel/install prefixes
if("FALSE" STREQUAL "TRUE")
  set(panthera_locomotion_SOURCE_PREFIX /home/joel/encoder_publisher_ws/src/panthera_locomotion)
  set(panthera_locomotion_DEVEL_PREFIX /home/joel/encoder_publisher_ws/devel)
  set(panthera_locomotion_INSTALL_PREFIX "")
  set(panthera_locomotion_PREFIX ${panthera_locomotion_DEVEL_PREFIX})
else()
  set(panthera_locomotion_SOURCE_PREFIX "")
  set(panthera_locomotion_DEVEL_PREFIX "")
  set(panthera_locomotion_INSTALL_PREFIX /home/joel/encoder_publisher_ws/install)
  set(panthera_locomotion_PREFIX ${panthera_locomotion_INSTALL_PREFIX})
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "WARNING: package 'panthera_locomotion' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  message("${_msg}")
endif()

# flag project as catkin-based to distinguish if a find_package()-ed project is a catkin project
set(panthera_locomotion_FOUND_CATKIN_PROJECT TRUE)

if(NOT "include " STREQUAL " ")
  set(panthera_locomotion_INCLUDE_DIRS "")
  set(_include_dirs "include")
  if(NOT " " STREQUAL " ")
    set(_report "Check the issue tracker '' and consider creating a ticket if the problem has not been reported yet.")
  elseif(NOT " " STREQUAL " ")
    set(_report "Check the website '' for information and consider reporting the problem.")
  else()
    set(_report "Report the problem to the maintainer 'kai <kai@todo.todo>' and request to fix the problem.")
  endif()
  foreach(idir ${_include_dirs})
    if(IS_ABSOLUTE ${idir} AND IS_DIRECTORY ${idir})
      set(include ${idir})
    elseif("${idir} " STREQUAL "include ")
      get_filename_component(include "${panthera_locomotion_DIR}/../../../include" ABSOLUTE)
      if(NOT IS_DIRECTORY ${include})
        message(FATAL_ERROR "Project 'panthera_locomotion' specifies '${idir}' as an include dir, which is not found.  It does not exist in '${include}'.  ${_report}")
      endif()
    else()
      message(FATAL_ERROR "Project 'panthera_locomotion' specifies '${idir}' as an include dir, which is not found.  It does neither exist as an absolute directory nor in '\${prefix}/${idir}'.  ${_report}")
    endif()
    _list_append_unique(panthera_locomotion_INCLUDE_DIRS ${include})
  endforeach()
endif()

set(libraries "")
foreach(library ${libraries})
  # keep build configuration keywords, target names and absolute libraries as-is
  if("${library}" MATCHES "^(debug|optimized|general)$")
    list(APPEND panthera_locomotion_LIBRARIES ${library})
  elseif(${library} MATCHES "^-l")
    list(APPEND panthera_locomotion_LIBRARIES ${library})
  elseif(${library} MATCHES "^-")
    # This is a linker flag/option (like -pthread)
    # There's no standard variable for these, so create an interface library to hold it
    if(NOT panthera_locomotion_NUM_DUMMY_TARGETS)
      set(panthera_locomotion_NUM_DUMMY_TARGETS 0)
    endif()
    # Make sure the target name is unique
    set(interface_target_name "catkin::panthera_locomotion::wrapped-linker-option${panthera_locomotion_NUM_DUMMY_TARGETS}")
    while(TARGET "${interface_target_name}")
      math(EXPR panthera_locomotion_NUM_DUMMY_TARGETS "${panthera_locomotion_NUM_DUMMY_TARGETS}+1")
      set(interface_target_name "catkin::panthera_locomotion::wrapped-linker-option${panthera_locomotion_NUM_DUMMY_TARGETS}")
    endwhile()
    add_library("${interface_target_name}" INTERFACE IMPORTED)
    if("${CMAKE_VERSION}" VERSION_LESS "3.13.0")
      set_property(
        TARGET
        "${interface_target_name}"
        APPEND PROPERTY
        INTERFACE_LINK_LIBRARIES "${library}")
    else()
      target_link_options("${interface_target_name}" INTERFACE "${library}")
    endif()
    list(APPEND panthera_locomotion_LIBRARIES "${interface_target_name}")
  elseif(TARGET ${library})
    list(APPEND panthera_locomotion_LIBRARIES ${library})
  elseif(IS_ABSOLUTE ${library})
    list(APPEND panthera_locomotion_LIBRARIES ${library})
  else()
    set(lib_path "")
    set(lib "${library}-NOTFOUND")
    # since the path where the library is found is returned we have to iterate over the paths manually
    foreach(path /home/joel/encoder_publisher_ws/install/lib;/home/joel/encoder_publisher_ws/devel/lib;/home/joel/catkin_ws/devel/lib;/home/joel/autoware.ai/install/ymc/lib;/home/joel/autoware.ai/install/xsens_driver/lib;/home/joel/autoware.ai/install/wf_simulator/lib;/home/joel/autoware.ai/install/lattice_planner/lib;/home/joel/autoware.ai/install/waypoint_planner/lib;/home/joel/autoware.ai/install/waypoint_maker/lib;/home/joel/autoware.ai/install/way_planner/lib;/home/joel/autoware.ai/install/vlg22c_cam/lib;/home/joel/autoware.ai/install/vision_ssd_detect/lib;/home/joel/autoware.ai/install/vision_segment_enet_detect/lib;/home/joel/autoware.ai/install/vision_lane_detect/lib;/home/joel/autoware.ai/install/vision_darknet_detect/lib;/home/joel/autoware.ai/install/vision_beyond_track/lib;/home/joel/autoware.ai/install/vel_pose_diff_checker/lib;/home/joel/autoware.ai/install/vehicle_socket/lib;/home/joel/autoware.ai/install/vehicle_model/lib;/home/joel/autoware.ai/install/vehicle_gazebo_simulation_launcher/lib;/home/joel/autoware.ai/install/vehicle_gazebo_simulation_interface/lib;/home/joel/autoware.ai/install/vehicle_engage_panel/lib;/home/joel/autoware.ai/install/vehicle_description/lib;/home/joel/autoware.ai/install/trafficlight_recognizer/lib;/home/joel/autoware.ai/install/op_utilities/lib;/home/joel/autoware.ai/install/op_simulation_package/lib;/home/joel/autoware.ai/install/op_local_planner/lib;/home/joel/autoware.ai/install/op_global_planner/lib;/home/joel/autoware.ai/install/lidar_kf_contour_track/lib;/home/joel/autoware.ai/install/op_ros_helpers/lib;/home/joel/autoware.ai/install/ff_waypoint_follower/lib;/home/joel/autoware.ai/install/dp_planner/lib;/home/joel/autoware.ai/install/op_simu/lib;/home/joel/autoware.ai/install/op_planner/lib;/home/joel/autoware.ai/install/op_utility/lib;/home/joel/autoware.ai/install/lidar_euclidean_cluster_detect/lib;/home/joel/autoware.ai/install/vector_map_server/lib;/home/joel/autoware.ai/install/road_occupancy_processor/lib;/home/joel/autoware.ai/install/costmap_generator/lib;/home/joel/autoware.ai/install/object_map/lib;/home/joel/autoware.ai/install/naive_motion_predict/lib;/home/joel/autoware.ai/install/lanelet_aisan_converter/lib;/home/joel/autoware.ai/install/map_file/lib;/home/joel/autoware.ai/install/libvectormap/lib;/home/joel/autoware.ai/install/lane_planner/lib;/home/joel/autoware.ai/install/imm_ukf_pda_track/lib;/home/joel/autoware.ai/install/decision_maker/lib;/home/joel/autoware.ai/install/vector_map/lib;/home/joel/autoware.ai/install/vector_map_msgs/lib;/home/joel/autoware.ai/install/vectacam/lib;/home/joel/autoware.ai/install/udon_socket/lib;/home/joel/autoware.ai/install/twist_generator/lib;/home/joel/autoware.ai/install/twist_gate/lib;/home/joel/autoware.ai/install/twist_filter/lib;/home/joel/autoware.ai/install/twist2odom/lib;/home/joel/autoware.ai/install/tablet_socket/lib;/home/joel/autoware.ai/install/runtime_manager/lib;/home/joel/autoware.ai/install/mqtt_socket/lib;/home/joel/autoware.ai/install/tablet_socket_msgs/lib;/home/joel/autoware.ai/install/state_machine_lib/lib;/home/joel/autoware.ai/install/sound_player/lib;/home/joel/autoware.ai/install/sick_lms5xx/lib;/home/joel/autoware.ai/install/sick_ldmrs_tools/lib;/home/joel/autoware.ai/install/sick_ldmrs_driver/lib;/home/joel/autoware.ai/install/sick_ldmrs_msgs/lib;/home/joel/autoware.ai/install/sick_ldmrs_description/lib;/home/joel/autoware.ai/install/points2image/lib;/home/joel/autoware.ai/install/rosinterface/lib;/home/joel/autoware.ai/install/rosbag_controller/lib;/home/joel/autoware.ai/install/pure_pursuit/lib;/home/joel/autoware.ai/install/points_preprocessor/lib;/home/joel/autoware.ai/install/mpc_follower/lib;/home/joel/autoware.ai/install/lidar_localizer/lib;/home/joel/autoware.ai/install/emergency_handler/lib;/home/joel/autoware.ai/install/autoware_health_checker/lib;/home/joel/autoware.ai/install/as/lib;/home/joel/autoware.ai/install/ros_observer/lib;/home/joel/autoware.ai/install/roi_object_filter/lib;/home/joel/autoware.ai/install/range_vision_fusion/lib;/home/joel/autoware.ai/install/pos_db/lib;/home/joel/autoware.ai/install/points_downsampler/lib;/home/joel/autoware.ai/install/pixel_cloud_fusion/lib;/home/joel/autoware.ai/install/pcl_omp_registration/lib;/home/joel/autoware.ai/install/pc2_downsampler/lib;/home/joel/autoware.ai/install/oculus_socket/lib;/home/joel/autoware.ai/install/obj_db/lib;/home/joel/autoware.ai/install/nmea_navsat/lib;/home/joel/autoware.ai/install/ndt_tku/lib;/home/joel/autoware.ai/install/ndt_cpu/lib;/home/joel/autoware.ai/install/multi_lidar_calibrator/lib;/home/joel/autoware.ai/install/mrt_cmake_modules/lib;/home/joel/autoware.ai/install/microstrain_driver/lib;/home/joel/autoware.ai/install/memsic_imu/lib;/home/joel/autoware.ai/install/marker_downsampler/lib;/home/joel/autoware.ai/install/map_tools/lib;/home/joel/autoware.ai/install/map_tf_generator/lib;/home/joel/autoware.ai/install/log_tools/lib;/home/joel/autoware.ai/install/lidar_shape_estimation/lib;/home/joel/autoware.ai/install/lidar_point_pillars/lib;/home/joel/autoware.ai/install/lidar_naive_l_shape_detect/lib;/home/joel/autoware.ai/install/lidar_fake_perception/lib;/home/joel/autoware.ai/install/lidar_apollo_cnn_seg_detect/lib;/home/joel/autoware.ai/install/libwaypoint_follower/lib;/home/joel/autoware.ai/install/lgsvl_simulator_bridge/lib;/home/joel/autoware.ai/install/lanelet2_extension/lib;/home/joel/autoware.ai/install/lanelet2_validation/lib;/home/joel/autoware.ai/install/lanelet2_examples/lib;/home/joel/autoware.ai/install/lanelet2_python/lib;/home/joel/autoware.ai/install/lanelet2_routing/lib;/home/joel/autoware.ai/install/lanelet2_traffic_rules/lib;/home/joel/autoware.ai/install/lanelet2_projection/lib;/home/joel/autoware.ai/install/lanelet2_maps/lib;/home/joel/autoware.ai/install/lanelet2_io/lib;/home/joel/autoware.ai/install/lanelet2_core/lib;/home/joel/autoware.ai/install/kvaser/lib;/home/joel/autoware.ai/install/kitti_launch/lib;/home/joel/autoware.ai/install/kitti_player/lib;/home/joel/autoware.ai/install/kitti_box_publisher/lib;/home/joel/autoware.ai/install/javad_navsat_driver/lib;/home/joel/autoware.ai/install/integrated_viewer/lib;/home/joel/autoware.ai/install/image_processor/lib;/home/joel/autoware.ai/install/hokuyo/lib;/home/joel/autoware.ai/install/graph_tools/lib;/home/joel/autoware.ai/install/gnss_localizer/lib;/home/joel/autoware.ai/install/gnss/lib;/home/joel/autoware.ai/install/glviewer/lib;/home/joel/autoware.ai/install/gazebo_world_description/lib;/home/joel/autoware.ai/install/gazebo_imu_description/lib;/home/joel/autoware.ai/install/gazebo_camera_description/lib;/home/joel/autoware.ai/install/garmin/lib;/home/joel/autoware.ai/install/freespace_planner/lib;/home/joel/autoware.ai/install/fastvirtualscan/lib;/home/joel/autoware.ai/install/ekf_localizer/lib;/home/joel/autoware.ai/install/ds4_msgs/lib;/home/joel/autoware.ai/install/ds4_driver/lib;/home/joel/autoware.ai/install/detected_objects_visualizer/lib;/home/joel/autoware.ai/install/decision_maker_panel/lib;/home/joel/autoware.ai/install/data_preprocessor/lib;/home/joel/autoware.ai/install/custom_msgs/lib;/home/joel/autoware.ai/install/calibration_publisher/lib;/home/joel/autoware.ai/install/autoware_system_msgs/lib;/home/joel/autoware.ai/install/autoware_rviz_plugins/lib;/home/joel/autoware.ai/install/autoware_quickstart_examples/lib;/home/joel/autoware.ai/install/autoware_pointgrey_drivers/lib;/home/joel/autoware.ai/install/autoware_driveworks_interface/lib;/home/joel/autoware.ai/install/autoware_connector/lib;/home/joel/autoware.ai/install/autoware_camera_lidar_calibrator/lib;/home/joel/autoware.ai/install/astar_search/lib;/home/joel/autoware.ai/install/amathutils_lib/lib;/home/joel/autoware.ai/install/autoware_msgs/lib;/home/joel/autoware.ai/install/autoware_map_msgs/lib;/home/joel/autoware.ai/install/autoware_launcher_rviz/lib;/home/joel/autoware.ai/install/autoware_launcher/lib;/home/joel/autoware.ai/install/autoware_lanelet2_msgs/lib;/home/joel/autoware.ai/install/autoware_external_msgs/lib;/home/joel/autoware.ai/install/autoware_driveworks_gmsl_interface/lib;/home/joel/autoware.ai/install/autoware_config_msgs/lib;/home/joel/autoware.ai/install/autoware_can_msgs/lib;/home/joel/autoware.ai/install/autoware_build_flags/lib;/home/joel/autoware.ai/install/autoware_bag_tools/lib;/home/joel/autoware.ai/install/adi_driver/lib;/opt/ros/melodic/lib)
      find_library(lib ${library}
        PATHS ${path}
        NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH)
      if(lib)
        set(lib_path ${path})
        break()
      endif()
    endforeach()
    if(lib)
      _list_append_unique(panthera_locomotion_LIBRARY_DIRS ${lib_path})
      list(APPEND panthera_locomotion_LIBRARIES ${lib})
    else()
      # as a fall back for non-catkin libraries try to search globally
      find_library(lib ${library})
      if(NOT lib)
        message(FATAL_ERROR "Project '${PROJECT_NAME}' tried to find library '${library}'.  The library is neither a target nor built/installed properly.  Did you compile project 'panthera_locomotion'?  Did you find_package() it before the subdirectory containing its code is included?")
      endif()
      list(APPEND panthera_locomotion_LIBRARIES ${lib})
    endif()
  endif()
endforeach()

set(panthera_locomotion_EXPORTED_TARGETS "panthera_locomotion_generate_messages_cpp;panthera_locomotion_generate_messages_eus;panthera_locomotion_generate_messages_lisp;panthera_locomotion_generate_messages_nodejs;panthera_locomotion_generate_messages_py")
# create dummy targets for exported code generation targets to make life of users easier
foreach(t ${panthera_locomotion_EXPORTED_TARGETS})
  if(NOT TARGET ${t})
    add_custom_target(${t})
  endif()
endforeach()

set(depends "geometry_msgs;roscpp;rospy;std_msgs;message_runtime;nav_msgs;tf;tf_conversions;tf2_ros")
foreach(depend ${depends})
  string(REPLACE " " ";" depend_list ${depend})
  # the package name of the dependency must be kept in a unique variable so that it is not overwritten in recursive calls
  list(GET depend_list 0 panthera_locomotion_dep)
  list(LENGTH depend_list count)
  if(${count} EQUAL 1)
    # simple dependencies must only be find_package()-ed once
    if(NOT ${panthera_locomotion_dep}_FOUND)
      find_package(${panthera_locomotion_dep} REQUIRED NO_MODULE)
    endif()
  else()
    # dependencies with components must be find_package()-ed again
    list(REMOVE_AT depend_list 0)
    find_package(${panthera_locomotion_dep} REQUIRED NO_MODULE ${depend_list})
  endif()
  _list_append_unique(panthera_locomotion_INCLUDE_DIRS ${${panthera_locomotion_dep}_INCLUDE_DIRS})

  # merge build configuration keywords with library names to correctly deduplicate
  _pack_libraries_with_build_configuration(panthera_locomotion_LIBRARIES ${panthera_locomotion_LIBRARIES})
  _pack_libraries_with_build_configuration(_libraries ${${panthera_locomotion_dep}_LIBRARIES})
  _list_append_deduplicate(panthera_locomotion_LIBRARIES ${_libraries})
  # undo build configuration keyword merging after deduplication
  _unpack_libraries_with_build_configuration(panthera_locomotion_LIBRARIES ${panthera_locomotion_LIBRARIES})

  _list_append_unique(panthera_locomotion_LIBRARY_DIRS ${${panthera_locomotion_dep}_LIBRARY_DIRS})
  list(APPEND panthera_locomotion_EXPORTED_TARGETS ${${panthera_locomotion_dep}_EXPORTED_TARGETS})
endforeach()

set(pkg_cfg_extras "panthera_locomotion-msg-extras.cmake")
foreach(extra ${pkg_cfg_extras})
  if(NOT IS_ABSOLUTE ${extra})
    set(extra ${panthera_locomotion_DIR}/${extra})
  endif()
  include(${extra})
endforeach()
