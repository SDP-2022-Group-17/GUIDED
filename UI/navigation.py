#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import roslaunch
import actionlib

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

class Navigation():
    def __init__(self):
        print("Initialising Nav")
        self.action_timeout = 10
        rospy.init_node('talker', anonymous=True)
        self.path = "/home/group17/catkin_ws/src/simple_navigation_goals/launch/"
        self.move_base = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.move_base.wait_for_server(rospy.Duration(self.action_timeout))

    def launch_file(self, file_name):
        pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(10) # 10hz
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)
        launch = roslaunch.parent.ROSLaunchParent(uuid, [self.path+file_name])
        launch.start()
        rospy.loginfo("started")


    def roomA(self):
        self.launch_file('movebase_seq.launch')

    def home(self):
        self.launch_file('movebase_seq_home.launch')

    def stop(self):
        self.move_base.cancel_all_goals()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
