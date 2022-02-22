import tkinter as tk

LARGEFONT =("", 20)

class TitleFrame(tk.Frame):
    def __init__(self, container, frame_status):
        super().__init__(container)

        l1 = tk.Label(self, font=("", 20))
        l1.pack()
        if frame_status == "start":
            l1.configure(text="Where do you want to go?")
        elif frame_status == "travel":
            l1.configure(text="Going to: Room A.")
        elif frame_status == "end":
            l1.configure(text="You have arrived at your destination.")
        else:
            print("Invalid status")
