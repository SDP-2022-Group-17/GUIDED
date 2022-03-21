import tkinter as tk
from tkinter import ttk
import navigation as nav

class ButtonFrame(ttk.Frame):
    def __init__(self, container, frame_status):
        container.style.configure('redbg.TFrame', background = 'red')

        super().__init__(container, style = 'red.TFrame')

        if frame_status == "start":
            b1 = ttk.Button(
                self,
                text="Room A",
                style='large_font.TButton',
                command=lambda : pressRoomA(container))
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
                command=lambda : pressStart(container))
            b1.pack(expand=True, fill="both", side="left", padx=5, pady=5)
        elif frame_status == "end":
            b1 = ttk.Button(
                self,
                text="Start a new journey",
                style='large_font.TButton',
                command=lambda : pressNewJourney(container))
            b1.pack(expand=True, fill="both", side="left", padx=20, pady=5)
        else:
            print("Invalid status.")


def pressRoomA(container):
    ROS()
    container.change_frame(next(container.status_iterator))

def pressStart(container):
    ROS()
    container.change_frame(next(container.status_iterator))

def pressNewJourney(container):
    ROS()
    container.change_frame(next(container.status_iterator))

def ROS():
    pass
