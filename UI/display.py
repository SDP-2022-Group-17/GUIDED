import tkinter as tk
from ButtonFrame import ButtonFrame
from TitleFrame import TitleFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        width = 800
        height = 480
        self.title("Welcome to guidED")
        self.geometry(str(width)+"x"+str(height))

        # Centralise widgets by giving empty columns a weight
        # so that they consume all extra space
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.columnconfigure(2, weight=1)

        # Logo
        logo = tk.Frame(self, background="black")
        logo.grid(column=1, row = 0)
        canvas = tk.Canvas(logo, width=300, height=162)
        canvas.grid()
        self.photo = tk.PhotoImage(file = "images/logo_small.png")
        canvas.create_image(0, 0, anchor="nw", image=self.photo)

        # initializing frames to an empty array
        self.title_frames = {}
        self.button_frames = {}

        for frame_status in ("start", "travel", "end"):
            title_frame = TitleFrame(self, frame_status)
            self.title_frames[frame_status] = title_frame
            title_frame.grid(column=1, row=1, sticky='nsew')

            button_frame = ButtonFrame(self, frame_status)
            self.button_frames[frame_status] = button_frame
            button_frame.grid(column=1, row=2, sticky='nsew')

        self.change_frame("start")

    def change_frame(self, frame_status):
        title_frame = self.title_frames[frame_status]
        title_frame.tkraise()

        button_frame = self.button_frames[frame_status]
        button_frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
