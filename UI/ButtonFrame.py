import tkinter as tk
import navigation as nav

LARGEFONT =("", 20)

class ButtonFrame(tk.Frame):
    def __init__(self, container, frame_status):
        super().__init__(container)

        if frame_status == "start":
            b1 = tk.Button(
                self,
                text="Room A",
                font=LARGEFONT,
                bg='black',
                fg='white',
                command=lambda : pressRoomA(container))
            b1.pack(expand=True, side='left', fill='both', padx=5, pady=5)

            b2 = tk.Button(
                self,
                text="Home",
                font=LARGEFONT,
                bg='black',
                fg='white')
            b2.pack(expand=True, side='right', fill='both', padx=5, pady=5)

        elif frame_status == "travel":
            b1 = tk.Button(
                self,
                text="Start",
                font=LARGEFONT,
                bg='black',
                fg='white',
                command=lambda : pressStart(container))
            b1.pack(expand=True, fill="both", side="left", padx=5, pady=5)
        elif frame_status == "end":
            b1 = tk.Button(
                self,
                text="Start a new journey",
                font=LARGEFONT,
                bg='red',
                fg='white',
                command=lambda : pressNewJourney(container))
            b1.pack(expand=True, fill="both", side="left", padx=20, pady=5)
        else:
            print("Invalid status.")

def pressRoomA(container):
    ROS()
    container.change_frame('travel')

def pressStart(container):
    ROS()
    container.change_frame('end')

def pressStart(container):
    ROS()
    container.change_frame('start')
