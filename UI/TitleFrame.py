import tkinter as tk
from tkinter import ttk

LARGEFONT =("Segoe UI", 20)

class TitleFrame(ttk.Frame):
    def __init__(self, container, frame_status):
        # container.style.configure('redbg.TFrame', background = 'red')

        super().__init__(container)#, style = 'redbg.TFrame')

        l1 = ttk.Label(self, font=LARGEFONT)
        l1.pack()
        if frame_status == "start":
            l1.configure(text="Welcome to Guided")
        elif frame_status == "travel":
            l1.configure(text="Going to: Office")
        elif frame_status == "end":
            l1.configure(text="Going to: Bathroom")
        else:
            print("Invalid status")
