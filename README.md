# ROS_Learning
Me learning ROS

Launch Files Explained:
common.launch - This will launch the Lidar, driver node and joystick nodes required to move the robot with a controller. This is included in all other launch files.
hector.launch - Launches Hector_Mapping so that you can manually create a map of an area with the robot.
nav.launch - Using a precreated loaded in map, the robot tries to fill in any gaps in the map using Explore_Lite for navigation, and AMCL for localisation
hector_nav.launch - Uses Hector_Mapping to localise instead of AMCL, and a static transform between odom and base_link. Will try create an entire map from scratch.
amcl_hector_nav.launch - Uses Hector_Mapping to generate odometry, and AMCL for localisation. Will try create an entire map from scratch, when explore_lite is uncommented.

Useful Commands:
roscd Bringup/Launch = Brings you to the location with all the launch files
roslaunch Bringup <launch file> = Launches your chosen launch file
rqt_logger_level = Displays all current RosLogs and lets you control what levels will be printed
rqt_graph = Displays a graph showing relations between nodes

