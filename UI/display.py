import os
import tkinter as tk
from tkinter import ttk

# from StopButton import StopButton

from format import *
import speech

class Display(tk.Tk):
    def __init__(self):
        super().__init__()
        Format(self)

        # Header with logo
        self.logo_frame = LogoFrame(self)
        self.logo_frame.grid(column=0, row=0, sticky='new', columnspan=3)

        # Room buttons
        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(column=1, row=2, sticky='nsew')

        # Stop button
        self.stop_photo =  tk.PhotoImage(file = "images/stopsign.png")
        stopButton = tk.Button(
                    self,
                    image = self.stop_photo,
                    background = Format.background,
                    bd = 0,
                    command = Functions.pressStop)
        stopButton.grid(row=3, column=1, sticky='nsew')

        # initializing title frames to an empty array
        self.title_frames = {}
        frame_statuses = ["start", "office", "restroom", "kitchen"]
        for frame_status in frame_statuses:
            title_frame = TitleFrame(self, frame_status)
            self.title_frames[frame_status] = title_frame
            title_frame.grid(column=1, row=1, sticky='nsew')

        self.change_frame('start')

        # self.text = None
        # self.speech_recognition = speech.Speech()
        # self.after(1000, self.listenAudioInput) ###

    def change_frame(self, frame_status):
        title_frame = self.title_frames[frame_status]
        title_frame.tkraise()

        path = os.path.join(os.getcwd(), 'sounds', "{}.mp3".format(frame_status))
        self.after(100, lambda : os.system("mpg123 -q " + u"{}".format(path)))

    def listenAudioInput(self):
        text = self.speech_recognition.listenMicrophone()
        self.after(1000, self.listenAudioInput)

        if text:
            if 'office' in text:
                #self.change_frame('office')
                self.button_frame.pressOffice(self)
                self.text = text
            elif 'bathroom' in text:
                #self.change_frame('bathroom')
                self.button_frame.pressBathroom(self)
                self.text = text

if __name__ == "__main__":
    display = Display()
    display.mainloop()
