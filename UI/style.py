from tkinter import ttk
import tkinter as tk
# import navigation as nav
# from StopButton import StopButton

class Style:
    background = '#efefef'
    yellow ='#F4F009'
    font=('Montserrat', 20, 'bold')
    header = '#181d21'
    def __init__(self, container):
        width = 800
        height = 480
        container.geometry(str(width)+"x"+str(height))
        container.title("Welcome to guidED")
        container.configure(background=self.background)

        # container.attributes("-fullscreen", True)

        # Centralise widgets by giving empty columns a weight
        # so that they consume all extra space
        container.rowconfigure(0, weight=1)
        container.rowconfigure(1, weight=1)
        container.rowconfigure(2, weight=1)
        container.rowconfigure(3, weight=1)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=2)
        container.columnconfigure(2, weight=1)

        self.style = ttk.Style(container)
        self.style.configure('transparent.TFrame', background=self.background)
        self.style.configure('transparent.TButton', background=self.background)

        # Logo frame styles
        self.style.configure('logo.TFrame', background=self.header)
        self.style.configure('logo.TLabel', background=self.header)
        self.style.configure('logo.TButton', background=self.header)

class TitleFrame(ttk.Frame):
    def __init__(self, container, frame_status):
        super().__init__(container, style='transparent.TFrame')

        l1 = tk.Label(self, font=('Montserrat', 30),
                      foreground=Style.header, background=Style.background)
        l1.pack()
        if frame_status == "start":
            l1.configure(text="Where do you want to go?")
        elif frame_status == "office":
            l1.configure(text="Going to: Office")
        elif frame_status == "restroom":
            l1.configure(text="Going to: Toilet")
        elif frame_status == "kitchen":
            l1.configure(text="Going to: Kitchen")
        elif frame_status == "invalid":
            l1.configure(text="Sorry, I didn't understand that.")
        else:
            print("Invalid status")

class LogoFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, height = 65, style='logo.TFrame')

        # Logo
        self.logo_photo = tk.PhotoImage(file = "images/logo.png")
        logo = ttk.Label(self, image=self.logo_photo, style='logo.TLabel')
        logo.place(relx = 0.5, rely=0, anchor='n')

        # Help button
        # phys_button = StopButton.getInstance()
        self.photo =  tk.PhotoImage(file = "images/small_help-modified.png")
        stopButton = tk.Button(
                    self,
                    image = self.photo,
                    background = '#181d21',
                    bd = 0,
                    command = lambda : Functions.pressCall(container))
        stopButton.pack(side='right', anchor='ne', pady=5)

class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, style='transparent.TFrame')
        self.photo = tk.PhotoImage(file = "images/office_hover.png")

        kitchen_button = tk.Button(
            self,
            foreground = '#fff',
            text = 'KITCHEN',
            font = ('Montserrat', 20, 'bold'),
            image = self.photo,
            compound='center',
            bd = 0,
            activeforeground = '#697B8B',
            command=lambda : Functions.pressKitchen(container))
        kitchen_button.pack(expand=True, side='left', fill='x', ipady=30, padx=5, pady=5)

        office_button = tk.Button(
            self,
            foreground = '#fff',
            text = 'OFFICE',
            font = ('Montserrat', 20, 'bold'),
            image = self.photo,
            compound='center',
            bd = 0,
            activeforeground = '#697B8B',
            command=lambda : Functions.pressOffice(container))
        office_button.pack(expand=True, side='left', fill='x', ipady=30, padx=5, pady=5)

        restroom_button = tk.Button(
            self,
            foreground = '#fff',
            text = 'TOILET',
            font = ('Montserrat', 20, 'bold'),
            image = self.photo,
            compound='center',
            bd = 0,
            activeforeground = '#697B8B',
            command=lambda : Functions.pressRestroom(container))
        restroom_button.pack(expand=True, side='left', fill='x', ipady=30, padx=5, pady=5)

class HelpFrame (ttk.Frame):
    def __init__(self, container):
        super().__init__(container, style='transparent.TFrame')

        l1 = tk.Label(self, font=('Montserrat', 18),
                      foreground=Style.header, background=Style.background)
        l1.pack(expand=1, fill='y')
        l1.configure(text="This robot can bring you to the Office, Kitchen or Toilet.")

        self.photo = tk.PhotoImage(file = "images/back.png")
        back_button = tk.Button(
            self,
            foreground = '#fff',
            text = 'BACK',
            font = ('Montserrat', 16, 'bold'),
            image = self.photo,
            compound='center',
            bd = 0,
            activeforeground = '#697B8B',
            command=lambda : container.change_help_frame(help=False))
        back_button.pack()

class Functions:
    global move_bot
    # move_bot = nav.Navigation()

    @staticmethod
    def pressCall(container):
         container.change_help_frame(help=True)

    def pressKitchen(container):
        container.change_frame('kitchen')
        move_bot.kitchen()

    @staticmethod
    def pressOffice(container):
        container.change_frame('office')
        move_bot.office()

    @staticmethod
    def pressRestroom(container):
        container.change_frame('restroom')
        move_bot.restroom()

    @staticmethod
    def pressStop():
        move_bot.stop()
        print("Stop button pressed.")