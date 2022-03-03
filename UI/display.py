import tkinter as tk
import itertools

from ButtonFrame import ButtonFrame
from TitleFrame import TitleFrame
import speech
# import concurrent.futures

class Display(tk.Tk):
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

        frame_statuses = ["start", "travel", "end"]
        for frame_status in frame_statuses:
            title_frame = TitleFrame(self, frame_status)
            self.title_frames[frame_status] = title_frame
            title_frame.grid(column=1, row=1, sticky='nsew')

            button_frame = ButtonFrame(self, frame_status)
            self.button_frames[frame_status] = button_frame
            button_frame.grid(column=1, row=2, sticky='nsew')

        self.status_iterator = itertools.cycle(frame_statuses)
        self.change_frame(next(self.status_iterator))

        # speech_recognition = speech.Speech()
        # with concurrent.futures.ThreadPoolExecutor() as executor:
        #     future = executor.submit(speech_recognition.listenMicrophone)
            # return_value = future.result()
            # print(f'HERE {return_value}')
            # if return_value == "room":
            #     self.change_frame(next(self.status_iterator))

        self.text = None
        # self.after(500, self.listenAudioInput)

    def change_frame(self, frame_status):
        title_frame = self.title_frames[frame_status]
        title_frame.tkraise()

        button_frame = self.button_frames[frame_status]
        button_frame.tkraise()

    def listenAudioInput(self):
        speech_recognition = speech.Speech()
        text = speech_recognition.listenMicrophone()
        self.after(500, display.listenAudioInput)

        if text:
            self.change_frame(next(self.status_iterator))
            self.text = text

if __name__ == "__main__":
    display = Display()
    display.mainloop()
