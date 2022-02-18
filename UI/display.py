import tkinter as tk
from PIL import Image
import navigation as nav

class Display(object):
    def __init__(self):
        width  = 1600
        height = 1200

        # root window
        self.root = tk.Tk()
        self.root.title("Welcome to guidED")
        self.root.geometry(str(width)+"x"+str(height))

        # Centralise widgets by giving empty columns a weight
        # so that they consume all extra space
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(2, weight=1)

        # Logo
        logo = tk.Frame(self.root, background="black")
        logo.grid(column=1, row = 0)
        canvas = tk.Canvas(logo, width=636, height=344)
        canvas.grid()
        photo = tk.PhotoImage(file = "images/logo_small.png")
        canvas.create_image(0, 0, anchor="nw", image=photo)

        # Title
        title = tk.Frame(self.root)
        title.grid(column=1, row=1, sticky='NEWS')
        title.columnconfigure(0, weight=1)
        title.columnconfigure(2, weight=1)
        title.rowconfigure(0, weight=1)
        title.rowconfigure(3, weight=1)

        # l1 = tk.Label(title, text="Welcome to guidED", font=("", 24))
        # l1.grid(row=1, column=1, sticky="S")
        l2 = tk.Label(title, text="Where do you want to go?", font=("", 20))
        l2.pack(side="top")

        # Buttons
        buttons = tk.Frame(self.root)
        buttons.grid(column=1, row=2, sticky='NEWS')
        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(4, weight=1)

        b1 = tk.Button(buttons, text="Room A", font=("", 20), bg='black', fg='white', command=nav.talker)
        b1.pack(expand=True, fill="both", side="left", padx=20, pady=5)
        b2 = tk.Button(buttons, text="Home", font=("", 20), bg='black', fg='white',)
        b2.pack(expand=True, fill="both", side="right", padx=20, pady=5)
        b3 = tk.Button(buttons, text="Stop", font=("", 20), bg='red', fg='white',)
        b3.pack(expand=True, fill="both", side="right", padx=20, pady=5)
        
        self.root.mainloop()

Display()

