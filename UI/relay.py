"""
This file should run on DICE or other laptop.
It acts as a relay between Raspberry Pi and the turtlebot.

It has some key features

1. Subscribe messages sent from the Pi
2. Process the texts and decide the target location
3. publish the target location to the turtlebot
"""
class Relay():

    # TODO receive messages from the topic
    def getMessages(self):
        return

    # TODO process the messages
    def decideTarget(self):
        return

    # TODO publish the target location to turtlebot
    def publishTarget(self):
        return