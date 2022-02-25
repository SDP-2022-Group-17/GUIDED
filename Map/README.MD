# SLAM
The **SLAM (Simultaneous Localization and Mapping)** is a technique to draw a map by estimating current location in an arbitrary space.

A detailed instructions could be seen from this website: https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-node

### Run SLAM node
1. Run roscore from Remote PC. \
`roscore`

2. If the `Bringup` is not running on the TurtleBot3 SBC, launch the Bringup. **Skip this step if you have launched bringup previously**.

-   Open a new terminal from Remote PC with `Ctrl` + `Alt` + `T` and connect to Turtlebot. The default password is **turtlebot**. \
`ssh pi@<turtlebot_name>` In here, the name is XATU \
On the turtlebot, run: \
`roscore &` \
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
