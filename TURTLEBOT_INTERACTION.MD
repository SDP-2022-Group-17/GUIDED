# Turtlebot Interaction

## Setup - Software  Dependencies
The turtlebot ROS libraries need to be installed from source, to do this, use: \
`cd ~/catkin_ws/src` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git`

We also need to install SLAM(Simultaneous Localization and Mapping) packages \
`git clone https://github.com/ros-perception/openslam_gmapping.git` \
`git clone https://github.com/ros-perception/slam_gmapping.git` \
`git clone https://github.com/ros/geometry2.git` \
`git clone https://github.com/ros-planning/navigation.git` 

After that: \
`cd ~/catkin_ws` \
`catkin_make`

## Setup - Communicating With a Turtlebot
To set this  up you need to add some environment variables to your .bashrc file on DiCE. \
`gedit ~/.bashrc`   \
and jump to the end of the file, then add: \
`export TURTLEBOT3_MODEL=waffle_pi` \
`export ROS_MASTER_URI=http://XATU:11311` \
`export ROS_HOSTNAME=$HOSTNAME`

## Connect To a Turtlebot
Start up the turtlebot, wait for a minute or so, then SSH in: \
`ssh pi@<turtlebot_name>` In here, our robot name is XATU.  \
The password is `turtlebot`

## Time Calibration For the Turtlebot
The built in time in the turtlebot is incorrect and will bring many
troubles.
- Open: time.is
- After SSH to the turtlebot, write: \
`sudo ntpdate extntp0.inf.ed.ac.uk` \
Then press 1 and enter `turtlebot` \
Now the turtlebot has synchronised the time.
