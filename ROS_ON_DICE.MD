# ROS on DICE

## Accessing ROS
ROS is already installed on DiCE but the ROS tools need to be made available to your DiCE user   account so you can run them from the terminal. 

Several Steps need to be done before running ROS

Open a terminal, then type \
```gedit ~/.bashrc``` \
Add the line to the file \
`source /opt/ros/noetic/setup.bash` \
Remember to save  ~/.bashrc. Then at the terminal, run: \
`source ~/.bashrc` \
To check you now have access to ROS, try running: \
`roscore` \
This can take a moment to start, the final line should read: \
`started core service [/rosout]` \
If  roscore  starts successfully, you can move on.

# Remember to `source ~/.bashrc` everytime you open a new terminal !!!

## Creating workspace
Before you start, you need to set up your workspace in terminal.
Open a terminal: \
`mkdir -p ~/catkin_ws/src`  \
`cd ~/catkin_ws` \
`catkin_make`

Again, open  ~/.bashrc  and at the end of the file, add \
`source ~/catkin_ws/devel/setup.bash`
