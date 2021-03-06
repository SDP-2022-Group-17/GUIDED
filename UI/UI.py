import tkinter as tk
from tkinter import ttk
from style import *

import os
import speech

class UI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = Style(self)

        # Header with logo
        self.logo_frame = LogoFrame(self)
        self.logo_frame.grid(column=0, row=0, sticky='new', columnspan=3)

        # Stop page
        self.stop_frame = StopFrame(self)
        self.stop_frame.grid(column=1, row=1, rowspan=3, sticky='nsew')

        # Stop button at bottom of page
        self.stop_button_frame = StopButtonFrame(self)
        self.stop_button_frame.grid(row=3, column=1, sticky='nsew')

        # Help page
        self.help_frame = HelpFrame(self)
        self.help_frame.grid(column=1, row=1, rowspan=2, sticky='nsew')

        # Room buttons
        self.button_frame = ButtonFrame(self)
        self.button_frame.grid(column=1, row=2, sticky='nsew')

        # initializing title frames to an empty array
        self.title_frames = {}
        self.frame_statuses = ["start", "office", "bathroom", "kitchen", 'invalid']
        for frame_status in self.frame_statuses:
            title_frame = TitleFrame(self, frame_status)
            self.title_frames[frame_status] = title_frame
            title_frame.grid(column=1, row=1, sticky='nsew')

        self.change_frame('start')

        self.speech_recognition = speech.Speech()
        self.after(1000, self.listenAudioInput)


    def change_stop_frame(self, stop=True):
        if stop:
            self.stop_frame.tkraise()
            path = os.path.join(os.getcwd(), 'sounds', "stop.mp3")
            # self.after(100, lambda: os.system("mpg123 -q " + u"{}".format(path)))
            self.after(100, lambda: os.system("start " + u"{}".format(path)))

            self.after(5000, lambda : self.change_stop_frame(stop=False))

        else:
            self.change_frame('start')

    def change_help_frame(self, help=True):
        if help:
            self.help_frame.tkraise()
            self.stop_button_frame.tkraise()
            path = os.path.join(os.getcwd(), 'sounds', "info.mp3")
            # self.after(100, lambda: os.system("mpg123 -q " + u"{}".format(path)))
            self.after(100, lambda: os.system("start " + u"{}".format(path)))

        else:
            self.change_frame('start')

    def change_frame(self, frame_status):
        self.button_frame.tkraise()
        self.stop_button_frame.tkraise()

        if frame_status in self.frame_statuses:
            title_frame = self.title_frames[frame_status]
            title_frame.tkraise()

            path = os.path.join(os.getcwd(), 'sounds', "{}.mp3".format(frame_status))
            # self.after(100, lambda: os.system("mpg123 -q " + u"{}".format(path)))
            self.after(100, lambda: os.system("start" + u"{}".format(path)))


    def listenAudioInput(self):
        text = self.speech_recognition.listenMicrophone()
        text

        help_words = ['help', 'information', 'info']
        stop_words = ['stop', 'danger', 'halt']
        office_words = ['office', 'workspace', 'workplace', 'desk']
        toilet_words = ['toilet', 'washroom', 'bathroom', 'lavatory', 'wc']
        kitchen_words = ['kitchen']

        if text:
            if any(word in text for word in stop_words):
                Functions.pressStop(self)
                print("stop")
            elif any(word in text for word in help_words):
                self.change_help_frame(help=True)
            elif any(word in text for word in office_words):
                self.change_frame('office')
                Functions.pressOffice(self)
                print("push office")
            elif any(word in text for word in toilet_words):
                self.change_frame('bathroom')
                Functions.pressBathroom(self)
                print("push bathroom")
            elif any(word in text for word in kitchen_words):
                self.change_frame('kitchen')
                Functions.pressKitchen(self)
                print("push kitchen")
            else:
                self.change_frame('invalid')

        self.after(2000, self.listenAudioInput)

if __name__ == "__main__":
    ui = UI()
    ui.mainloop()
