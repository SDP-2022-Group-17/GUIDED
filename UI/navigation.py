#!/usr/bin/env python
import paramiko
from getpass import getpass

class Navigation():
    def __init__(self):
        self.password = getpass()
        self.sdp_robots = 'cassatt'
        self.username = 's1970051'
        self.hostname = 'cassatt.inf.ed.ac.uk'

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
            stdin, stdout, stderr = self.client.exec_command('hostname')
            print(stdout.read().decode())


        except:
            print("[!] Cannot connect to the SSH Server")
            exit()

    def entrance(self):
        stdin, stdout, stderr = self.client.exec_command('roslaunch simple_navigation_goals entrance.launch')

    def office(self):
        stdin, stdout, stderr = self.client.exec_command('roslaunch simple_navigation_goals office.launch')

    def restroom(self):
        stdin, stdout, stderr = self.client.exec_command('roslaunch simple_navigation_goals restroom.launch')

    def kitchen(self):
        stdin, stdout, stderr = self.client.exec_command('roslaunch simple_navigation_goals kitchen.launch')

    def stop(self):
        stdin, stdout, stderr = self.client.exec_command('rostopic pub /move_base/cancel actionlib_msgs/GoalID -- {}')

if __name__ == '__main__':
    pass
    # nav = Navigation()
    # nav.office()