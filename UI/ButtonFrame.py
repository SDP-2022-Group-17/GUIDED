import tkinter as tk
from tkinter import ttk
#import navigation as nav
from StopButton import StopButton
import audio

class ButtonFrame(ttk.Frame):
    def __init__(self, container, frame_status):
        container.style.configure('redbg.TFrame', background = 'red')

        super().__init__(container, style = 'red.TFrame')

        phys_button = StopButton.getInstance()
        #self.move_bot = nav.Navigation()

        b1 = ttk.Button(
            self,
            text="Office",
            style='large_font.TButton',
            command=lambda : self.pressRoomA(container))
        b1.pack(expand=True, side='left', fill='both', padx=5, pady=5)

        b2 = ttk.Button(
            self,
            text="Bathroom",
            style='large_font.TButton',
            command=lambda : self.pressHome(container)
            )
        b2.pack(expand=True, side='right', fill='both', padx=5, pady=5)

    def pressRoomA(self,container):
        pass
        #self.move_bot.roomA()
        container.change_frame(next(container.status_iterator))
    def pressHome(self,container):
        pass
        #self.move_bot.home()
        #container.change_frame(next(container.status_iterator))


    def pressStart(self,container):
        self.ROS()


    def pressNewJourney(self,container):
        self.ROS()


    def pressStop(self):
        #self.move_bot.stop()
        print("Stop button pressed.")

    def ROS(self):
        pass
