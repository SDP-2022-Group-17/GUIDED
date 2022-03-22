import tkinter as tk
from tkinter import ttk
from StopButton import StopButton
import navigation as nav

# import navigation as nav

class ButtonFrame(ttk.Frame):
    def __init__(self, container, frame_status):
        super().__init__(container)
        self.move_bot = nav.Navigation()

        #phys_button = StopButton.getInstance()

        stopButton = ttk.Button(
                self,
                text="STOP",
                style='large_font.TButton',
                command = self.pressStop)
        stopButton.pack(expand=True, side='left', fill='both', padx=5, pady=5)


        if frame_status == "start":
            b1 = ttk.Button(
                self,
                text="Room A",
                style='large_font.TButton',
                command=lambda : self.pressRoomA(container))
            b1.pack(expand=True, side='left', fill='both', padx=5, pady=5)

            b2 = ttk.Button(
                self,
                text="Home",
                style='large_font.TButton'
                )
            b2.pack(expand=True, side='right', fill='both', padx=5, pady=5)

        elif frame_status == "travel":
            b1 = ttk.Button(
                self,
                text="Start",
                style='large_font.TButton',
                command=lambda : self.pressStart(container))
            b1.pack(expand=True, fill="both", side="left", padx=5, pady=5)
        elif frame_status == "end":
            b1 = ttk.Button(
                self,
                text="Start a new journey",
                style='large_font.TButton',
                command=lambda : self.pressNewJourney(container))
            b1.pack(expand=True, fill="both", side="left", padx=20, pady=5)
        else:
            print("Invalid status.")


    def pressRoomA(self,container):
        self.move_bot.roomA()
        #container.change_frame(next(container.status_iterator))

    def pressStart(self,container):
        self.ROS()
        container.change_frame(next(container.status_iterator))

    def pressNewJourney(self,container):
        self.ROS()
        container.change_frame(next(container.status_iterator))

    def pressStop(self):
        self.move_bot.stop()
        print("Stop button pressed.")

    def ROS(self):
        pass
