#!/usr/bin/env python3
"""
This file should run on the Pi
There are 3 key features that need to be implemented

1. UI
2. Voice recognition
3. Initialise a topic and transfer the recognised text to Laptop
"""

from UI import UI
import time


class RaspberryPi:

    def __init__(self):
        self.ui = UI()
        self.text = None

    def initialize_UI(self):
        self.ui.mainloop()

    # TODO Send recognised text to Relay
    def send_text(self):
        return

    # TODO send target if touch the buttom
    def SendTarget(self):
        return


if __name__ == "__main__":
    pi = RaspberryPi()
    pi.initialize_UI()
