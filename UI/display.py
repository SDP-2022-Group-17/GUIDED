import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from StopButton import StopButton
# import audio
import itertools

from ButtonFrame import ButtonFrame
from TitleFrame import TitleFrame
import speech
import concurrent.futures

class Display(ThemedTk):
    def __init__(self):
        super().__init__()
        self.set_theme('plastik')
        self.style = ttk.Style()
        self.style.configure('large_font.TButton', font=('Segoe UI', 20))
        self.style.configure('transparent.TButton', foreground='#efefef')

        width = 800
        height = 480
        self.title("Welcome to guidED")
        self.geometry(str(width)+"x"+str(height))
        self.configure(background='#efefef')
        # self.attributes("-fullscreen", True)


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
        logo = ttk.Frame(self)
        logo.grid(column=1, row = 0)
        canvas = tk.Canvas(logo, width=299, height=66)
        canvas.grid()
        self.logo_photo = tk.PhotoImage(file = "images/logo_small_transparent.png")
        canvas.create_image(0, 0, anchor="nw", image=self.logo_photo)

        # Stop button
        #phys_button = StopButton.getInstance()
        self.help_photo =  tk.PhotoImage(file = "images/stopsign.png")
        stopButton = tk.Button(
                    self,
                    image = self.help_photo,
                    bd = 0,
                    command = pressStop)
        stopButton.grid(row=2, column=0)

        # Call button
        #phys_button = StopButton.getInstance()
        self.photo =  tk.PhotoImage(file = "images/emergency call icon.png")
        stopButton = tk.Button(
                    self,
                    image = self.photo,
                    bd = 0,
                    command = pressCall)
        stopButton.grid(row=2, column=2)

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

        self.text = None
        self.after(500, self.listenAudioInput) ###

    def change_theme(self):
        self.style.theme_use(self.selected_theme.get())

    def change_frame(self, frame_status):
        title_frame = self.title_frames[frame_status]
        title_frame.tkraise()

        button_frame = self.button_frames[frame_status]
        button_frame.tkraise()

        path = os.path.join(os.getcwd(), 'sounds', "{}.mp3".format(frame_status))
        
        # self.after(100, lambda : os.system("mpg123 " + u"{}".format(path)))
        
    def listenAudioInput(self):
        speech_recognition = speech.Speech()
        text = speech_recognition.listenMicrophone()
        self.after(500, self.listenAudioInput)

        if 'office' in text:
            self.change_frame('travel')
            self.text = text
        elif 'bathroom' in text:
            self.change_frame('end')
            self.text = text

def pressStop():
    print("Stop button pressed.")
    
def pressCall():
    print("Call button pressed.")

if __name__ == "__main__":
    display = Display()
    display.mainloop()
