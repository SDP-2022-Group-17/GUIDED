import tkinter as tk
from tkinter import ttk

LARGEFONT =("", 20)

class TitleFrame(ttk.Frame):
    def __init__(self, container, frame_status):
        super().__init__(container)

        l1 = ttk.Label(self)
        l1.pack()
        if frame_status == "start":
            l1.configure(text="Where do you want to go?")
        elif frame_status == "travel":
            l1.configure(text="Going to: Room A.")
        elif frame_status == "end":
            l1.configure(text="You have arrived at your destination.")
        else:
            print("Invalid status")
