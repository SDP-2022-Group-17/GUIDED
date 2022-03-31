import tkinter as tk
from tkinter import ttk
#import navigation as nav
#from StopButton import StopButton

class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        container.style.configure('redbg.TFrame', background = 'red')

        super().__init__(container)

        #phys_button = StopButton.getInstance()
        #self.move_bot = nav.Navigation()


        # Stop button
        #phys_button = StopButton.getInstance()
        self.help_photo =  tk.PhotoImage(file = "images/stopsign.png")
        stopButton = tk.Button(
                    self,
                    image = self.help_photo,
                    bd = 0,
                    command = self.pressStop)
        stopButton.pack(side='left', fill='both', padx=5, pady=5)
        
        b1 = ttk.Button(
            self,
            text="Office",
            style='large_font.TButton',
            command=lambda : self.pressOffice(container))
        b1.pack(expand=True, side='left', fill='both', padx=5, pady=5)

        b2 = ttk.Button(
            self,
            text="Bathroom",
            style='large_font.TButton',
            command=lambda : self.pressBathroom(container)
            )
        b2.pack(expand=True, side='left', fill='both', padx=5, pady=5)

        # Call button
        #phys_button = StopButton.getInstance()
        self.photo =  tk.PhotoImage(file = "images/emergency call icon.png")
        stopButton = tk.Button(
                    self,
                    image = self.photo,
                    bd = 0,
                    command = self.pressCall)
        stopButton.pack(side='right', fill='both', padx=5, pady=5)


    def pressOffice(self, container):
        container.change_frame('office')
        #self.move_bot.roomA()
        
    def pressBathroom(self,container):
        container.change_frame('bathroom')
        #self.move_bot.home()

    def pressStop(self):
        print("Stop button pressed.")

    def pressCall(self):
        print("Call button pressed.")
