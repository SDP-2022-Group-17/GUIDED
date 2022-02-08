import tkinter as tk
import navigation as nav


class Display(object):
    def __init__(self):

        # root window
        self.root = tk.Tk()
        self.root.title("Welcome to guidED")
        self.root .geometry("400x200")

        # Centralise widgets by giving empty columns a weight
        # so that they consume all extra space
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Title
        title = tk.Frame(self.root)
        title.grid(column=1, row=0, sticky="N")
        title.columnconfigure(0, weight=1)
        title.columnconfigure(2, weight=1)

        label = tk.Label(title, text="Welcome to guidED")
        label.grid(row=0, column=1)

        # Buttons
        buttons = tk.Frame(self.root)
        buttons.grid(column=1, row=1)
        buttons.columnconfigure(0, weight=1)
        buttons.columnconfigure(4, weight=1)

        b1 = tk.Button(buttons, text="Room A", command=nav.talker).grid(row=0, column=1)
        b2 = tk.Button(buttons, text="Home").grid(row=0, column=2)
        # b3 = tk.Button(buttons, text="Room ").grid(row=0, column=3)
        # img = tk.PhotoImage(file="images/logo.jpg")      
        # self.root.create_image(20,20, anchor=NW, image=img)
        self.root.mainloop()

Display()
