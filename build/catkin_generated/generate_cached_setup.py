# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/joel/encoder_publisher_ws/devel;/home/joel/catkin_ws/devel;/home/joel/autoware.ai/install/ymc;/home/joel/autoware.ai/install/xsens_driver;/home/joel/autoware.ai/install/wf_simulator;/home/joel/autoware.ai/install/lattice_planner;/home/joel/autoware.ai/install/waypoint_planner;/home/joel/autoware.ai/install/waypoint_maker;/home/joel/autoware.ai/install/way_planner;/home/joel/autoware.ai/install/vlg22c_cam;/home/joel/autoware.ai/install/vision_ssd_detect;/home/joel/autoware.ai/install/vision_segment_enet_detect;/home/joel/autoware.ai/install/vision_lane_detect;/home/joel/autoware.ai/install/vision_darknet_detect;/home/joel/autoware.ai/install/vision_beyond_track;/home/joel/autoware.ai/install/vel_pose_diff_checker;/home/joel/autoware.ai/install/vehicle_socket;/home/joel/autoware.ai/install/vehicle_model;/home/joel/autoware.ai/install/vehicle_gazebo_simulation_launcher;/home/joel/autoware.ai/install/vehicle_gazebo_simulation_interface;/home/joel/autoware.ai/install/vehicle_engage_panel;/home/joel/autoware.ai/install/vehicle_description;/home/joel/autoware.ai/install/trafficlight_recognizer;/home/joel/autoware.ai/install/op_utilities;/home/joel/autoware.ai/install/op_simulation_package;/home/joel/autoware.ai/install/op_local_planner;/home/joel/autoware.ai/install/op_global_planner;/home/joel/autoware.ai/install/lidar_kf_contour_track;/home/joel/autoware.ai/install/op_ros_helpers;/home/joel/autoware.ai/install/ff_waypoint_follower;/home/joel/autoware.ai/install/dp_planner;/home/joel/autoware.ai/install/op_simu;/home/joel/autoware.ai/install/op_planner;/home/joel/autoware.ai/install/op_utility;/home/joel/autoware.ai/install/lidar_euclidean_cluster_detect;/home/joel/autoware.ai/install/vector_map_server;/home/joel/autoware.ai/install/road_occupancy_processor;/home/joel/autoware.ai/install/costmap_generator;/home/joel/autoware.ai/install/object_map;/home/joel/autoware.ai/install/naive_motion_predict;/home/joel/autoware.ai/install/lanelet_aisan_converter;/home/joel/autoware.ai/install/map_file;/home/joel/autoware.ai/install/libvectormap;/home/joel/autoware.ai/install/lane_planner;/home/joel/autoware.ai/install/imm_ukf_pda_track;/home/joel/autoware.ai/install/decision_maker;/home/joel/autoware.ai/install/vector_map;/home/joel/autoware.ai/install/vector_map_msgs;/home/joel/autoware.ai/install/vectacam;/home/joel/autoware.ai/install/udon_socket;/home/joel/autoware.ai/install/twist_generator;/home/joel/autoware.ai/install/twist_gate;/home/joel/autoware.ai/install/twist_filter;/home/joel/autoware.ai/install/twist2odom;/home/joel/autoware.ai/install/tablet_socket;/home/joel/autoware.ai/install/runtime_manager;/home/joel/autoware.ai/install/mqtt_socket;/home/joel/autoware.ai/install/tablet_socket_msgs;/home/joel/autoware.ai/install/state_machine_lib;/home/joel/autoware.ai/install/sound_player;/home/joel/autoware.ai/install/sick_lms5xx;/home/joel/autoware.ai/install/sick_ldmrs_tools;/home/joel/autoware.ai/install/sick_ldmrs_driver;/home/joel/autoware.ai/install/sick_ldmrs_msgs;/home/joel/autoware.ai/install/sick_ldmrs_description;/home/joel/autoware.ai/install/points2image;/home/joel/autoware.ai/install/rosinterface;/home/joel/autoware.ai/install/rosbag_controller;/home/joel/autoware.ai/install/pure_pursuit;/home/joel/autoware.ai/install/points_preprocessor;/home/joel/autoware.ai/install/mpc_follower;/home/joel/autoware.ai/install/lidar_localizer;/home/joel/autoware.ai/install/emergency_handler;/home/joel/autoware.ai/install/autoware_health_checker;/home/joel/autoware.ai/install/as;/home/joel/autoware.ai/install/ros_observer;/home/joel/autoware.ai/install/roi_object_filter;/home/joel/autoware.ai/install/range_vision_fusion;/home/joel/autoware.ai/install/pos_db;/home/joel/autoware.ai/install/points_downsampler;/home/joel/autoware.ai/install/pixel_cloud_fusion;/home/joel/autoware.ai/install/pcl_omp_registration;/home/joel/autoware.ai/install/pc2_downsampler;/home/joel/autoware.ai/install/oculus_socket;/home/joel/autoware.ai/install/obj_db;/home/joel/autoware.ai/install/nmea_navsat;/home/joel/autoware.ai/install/ndt_tku;/home/joel/autoware.ai/install/ndt_cpu;/home/joel/autoware.ai/install/multi_lidar_calibrator;/home/joel/autoware.ai/install/mrt_cmake_modules;/home/joel/autoware.ai/install/microstrain_driver;/home/joel/autoware.ai/install/memsic_imu;/home/joel/autoware.ai/install/marker_downsampler;/home/joel/autoware.ai/install/map_tools;/home/joel/autoware.ai/install/map_tf_generator;/home/joel/autoware.ai/install/log_tools;/home/joel/autoware.ai/install/lidar_shape_estimation;/home/joel/autoware.ai/install/lidar_point_pillars;/home/joel/autoware.ai/install/lidar_naive_l_shape_detect;/home/joel/autoware.ai/install/lidar_fake_perception;/home/joel/autoware.ai/install/lidar_apollo_cnn_seg_detect;/home/joel/autoware.ai/install/libwaypoint_follower;/home/joel/autoware.ai/install/lgsvl_simulator_bridge;/home/joel/autoware.ai/install/lanelet2_extension;/home/joel/autoware.ai/install/lanelet2_validation;/home/joel/autoware.ai/install/lanelet2_examples;/home/joel/autoware.ai/install/lanelet2_python;/home/joel/autoware.ai/install/lanelet2_routing;/home/joel/autoware.ai/install/lanelet2_traffic_rules;/home/joel/autoware.ai/install/lanelet2_projection;/home/joel/autoware.ai/install/lanelet2_maps;/home/joel/autoware.ai/install/lanelet2_io;/home/joel/autoware.ai/install/lanelet2_core;/home/joel/autoware.ai/install/kvaser;/home/joel/autoware.ai/install/kitti_launch;/home/joel/autoware.ai/install/kitti_player;/home/joel/autoware.ai/install/kitti_box_publisher;/home/joel/autoware.ai/install/javad_navsat_driver;/home/joel/autoware.ai/install/integrated_viewer;/home/joel/autoware.ai/install/image_processor;/home/joel/autoware.ai/install/hokuyo;/home/joel/autoware.ai/install/graph_tools;/home/joel/autoware.ai/install/gnss_localizer;/home/joel/autoware.ai/install/gnss;/home/joel/autoware.ai/install/glviewer;/home/joel/autoware.ai/install/gazebo_world_description;/home/joel/autoware.ai/install/gazebo_imu_description;/home/joel/autoware.ai/install/gazebo_camera_description;/home/joel/autoware.ai/install/garmin;/home/joel/autoware.ai/install/freespace_planner;/home/joel/autoware.ai/install/fastvirtualscan;/home/joel/autoware.ai/install/ekf_localizer;/home/joel/autoware.ai/install/ds4_msgs;/home/joel/autoware.ai/install/ds4_driver;/home/joel/autoware.ai/install/detected_objects_visualizer;/home/joel/autoware.ai/install/decision_maker_panel;/home/joel/autoware.ai/install/data_preprocessor;/home/joel/autoware.ai/install/custom_msgs;/home/joel/autoware.ai/install/calibration_publisher;/home/joel/autoware.ai/install/autoware_system_msgs;/home/joel/autoware.ai/install/autoware_rviz_plugins;/home/joel/autoware.ai/install/autoware_quickstart_examples;/home/joel/autoware.ai/install/autoware_pointgrey_drivers;/home/joel/autoware.ai/install/autoware_driveworks_interface;/home/joel/autoware.ai/install/autoware_connector;/home/joel/autoware.ai/install/autoware_camera_lidar_calibrator;/home/joel/autoware.ai/install/astar_search;/home/joel/autoware.ai/install/amathutils_lib;/home/joel/autoware.ai/install/autoware_msgs;/home/joel/autoware.ai/install/autoware_map_msgs;/home/joel/autoware.ai/install/autoware_launcher_rviz;/home/joel/autoware.ai/install/autoware_launcher;/home/joel/autoware.ai/install/autoware_lanelet2_msgs;/home/joel/autoware.ai/install/autoware_external_msgs;/home/joel/autoware.ai/install/autoware_driveworks_gmsl_interface;/home/joel/autoware.ai/install/autoware_config_msgs;/home/joel/autoware.ai/install/autoware_can_msgs;/home/joel/autoware.ai/install/autoware_build_flags;/home/joel/autoware.ai/install/autoware_bag_tools;/home/joel/autoware.ai/install/adi_driver;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/joel/Desktop/encoder_publisher_ws/devel/env.sh')

output_filename = '/home/joel/Desktop/encoder_publisher_ws/build/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
