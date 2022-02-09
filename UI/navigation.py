#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import roslaunch

def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    # while not rospy.is_shutdown():
    #    roslaunch simple_navigation_goals movebase_seq.launch
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)
    path = "/afs/inf.ed.ac.uk/user/s19/s1970051/catkin_ws/src/simple_navigation_goals/launch/movebase_seq.launch"
    launch = roslaunch.parent.ROSLaunchParent(uuid, [path])
    launch.start()
    rospy.loginfo("started")


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass