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
