# README.md

Hi! This file is the instruction for using ROS when running this project.

# ROS on DICE

## Accessing ROS
ROS is already installed on DiCE but the ROS tools need to be made available to your DiCE user   account so you can run them from the terminal. 

Several Steps need to be done before running ROS

Open a terminal, then type
```gedit ~/.bashrc```
Add the line to the file
`source /opt/ros/noetic/setup.bash`
Remember to save  ~/.bashrc. Then at the terminal, run:
`source ~/.bashrc`
To check you now have access to ROS, try running:
`roscore`
This can take a moment to start, the final line should read:
`started core service [/rosout]`
If  roscore  starts successfully, you can move on.

# Remember to `source ~/.bashrc` everytime you open a new terminal !!!

## Creating workspace
Before you start, you need to set up your workspace in terminal.
Open a terminal:
`mkdir -p ~/catkin_ws/src`  \
`cd ~/catkin_ws` \
`catkin_make`

Again, open  ~/.bashrc  and at the end of the file, add
`source ~/catkin_ws/devel/setup.bash`

# Turtlebot Interaction

## Setup - Software  Dependencies
The turtlebot ROS libraries need to be installed from source, to do this, use:
`cd ~/catkin_ws/src` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git` \
`git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git`

We also need to install SLAM(Simultaneous Localization and Mapping) packages
`git clone https://github.com/ros-perception/openslam_gmapping.git` \
`git clone https://github.com/ros-perception/slam_gmapping.git` \
`git clone https://github.com/ros/geometry2.git` \
`git clone https://github.com/ros-planning/navigation.git` \

After that:
`cd ~/catkin_ws` \
`catkin_make`

## Setup - Communicating With a Turtlebot
To set this  up you need to add some environment variables to your .bashrc file on DiCE.  
`gedit ~/.bashrc`   
and jump to the end of the file, then add:
`export TURTLEBOT3_MODEL=waffle_pi` \
`export ROS_MASTER_URI=http://XATU:11311` \
`export ROS_HOSTNAME=$HOSTNAME`

## Connect To a Turtlebot
Start up the turtlebot, wait for a minute or so, then SSH in:
`ssh pi@<turtlebot_name>` In here, our robot name is XATU. 
The password is `turtlebot`

## Time Calibration For the Turtlebot
The built in time in the turtlebot is incorrect and will bring many
troubles
Open: time.is
After SSH to the turtlebot, write:
`sudo timedetectl set-ntp 0` \
`timedetectl set-time 'yyyy-mm-dd hh-mm-ss'` \
Then press 1 and enter `turtlebot`
Now the turtlebot has synchronised the time

# SLAM
The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space.

A detailed instructions could be seen from this website: https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-node

### Run SLAM node
1. Run roscore from Remote PC.
`roscore`

2. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup. **Skip this step if you have launched bringup previously**.

-   Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Turtlebot. The default password is **turtlebot**.
`ssh pi@<turtlebot_name>` In here, the name is XATU
On the turtlebot, run: \
`roscore &`
Wait for  roscore  to start, then run: \
`roslaunch turtlebot3_bringup turtlebot3_robot.launch`

3. Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and launch the SLAM node. The Gmapping is used as a default SLAM method. \
`roslaunch turtlebot3_slam turtlebot3_slam.launch`

4. Run Teleoperation Node
- Once SLAM node is successfully up and running, TurtleBot3 will be exploring unknown area of the map using teleoperation. It is important to avoid vigorous movements such as changing the linear and angular speed too quickly. When building a map using the TurtleBot3, it is a good practice to scan every corner of the map.
- Open a new terminal and run the teleoperation node from the Remote PC. \
`roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`
- Now you could start to navigate the robot using keyboard.
5. There are several parameters for tuning the function. Check them out in the website.

6. Save the map
- Launch the **map_saver** node in the map_server package to create map files.  
The map file is saved in the directory where the map_saver node is launched at.  
Unless a specific file name is provided, `map` will be used as a default file name and create `map.pgm` and `map.yaml`.
- Run \
```rosrun map_server map_saver -f ~/map```
- The `-f` option specifies a folder location and a file name where files to be saved.  
With the above command, `map.pgm` and `map.yaml` will be saved in the home folder `~/`(/home/${username}).

# Navigation
**[Navigation](http://wiki.ros.org/navigation)** is to move the robot from one location to the specified destination in a given environment. For this purpose, a map that contains geometry information of furniture, objects, and walls of the given environment is required. As described in the previous [SLAM](https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/) section, the map was created with the distance information obtained by the sensor and the pose information of the robot itself.

## Run Navigation Node
1. If `roscore` is not running on the Remote PC, run roscore. **Skip this step if roscore is already running**. \
```roscore```
2. If the `Bringup` is not running on the TurtleBot3, launch the Bringup. **Skip this step if you have launched bringup previously**. (BEFORE running the bring up, remember to calibrate the time first) \
```roslaunch turtlebot3_bringup turtlebot3_robot.launch```
3. Launch the Navigation. \
```roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml``` (You could change the path of the map file)

## Estimate Initial Pose
**Initial Pose Estimation** must be performed before running the Navigation as this process initializes the AMCL parameters that are critical in Navigation. TurtleBot3 has to be correctly located on the map with the LDS sensor data that neatly overlaps the displayed map.

1. Click the `2D Pose Estimate` button in the RViz menu.  
    ![](https://emanual.robotis.com/assets/images/platform/turtlebot3/navigation/2d_pose_button.png)
2. Click on the map where the actual robot is located and drag the large green arrow toward the direction where the robot is facing.
3. Repeat step 1 and 2 until the LDS sensor data is overlayed on the saved map.
4. Launch keyboard teleoperation node to precisely locate the robot on the map. \
```roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch```
5. Move the robot back and forth a bit to collect the surrounding environment information and narrow down the estimated location of the TurtleBot3 on the map which is displayed with tiny green arrows.  
    ![](https://emanual.robotis.com/assets/images/platform/turtlebot3/navigation/tb3_amcl_particle_01.png) ![](https://emanual.robotis.com/assets/images/platform/turtlebot3/navigation/tb3_amcl_particle_02.png)
6. Terminate the keyboard teleoperation node by entering `Ctrl` + `C` to the teleop node terminal in order to prevent different **cmd_vel** values are published from multiple nodes during Navigation.
## Set Navigation Goal

1.  Click the `2D Nav Goal` button in the RViz menu.  
    ![](https://emanual.robotis.com/assets/images/platform/turtlebot3/navigation/2d_nav_goal_button.png)
2.  Click on the map to set the destination of the robot and drag the purple arrow toward the direction where the robot will be facing.
    -   This purple arrow is a marker that can specify the destination of the robot.
    -   The root of the arrow is `x`, `y` coordinate of the destination, and the angle `θ` is determined by the orientation of the arrow.
    -   As soon as x, y, θ are set, TurtleBot3 will start moving to the destination immediately. 
    - ![](https://emanual.robotis.com/assets/images/platform/turtlebot3/navigation/2d_nav_goal.png)
## Turning Guide
Navigation stack has many parameters to change performances for different robots.

You can get more information about Navigation tuning from [Basic Navigation Tuning Guide](http://wiki.ros.org/navigation/Tutorials/Navigation%20Tuning%20Guide), [ROS Navigation Tuning Guide by Kaiyu Zheng](http://kaiyuzheng.me/documents/navguide.pdf), and the chapter 11 of [ROS Robot Programming](https://community.robotsource.org/t/download-the-ros-robot-programming-book-for-free/51) book.
