#!/usr/bin/python3
from tkinter import *
from tkinter import ttk

class converter():
    def convert_yards(self, event):
        try:
            num = float(event.widget.get())
            self.yards = round(num, 2)
            self.meters = round(num * .9144, 2)
            self.centimeters = round(num * 91.44, 2)
            self.inches = round(num * 36, 2)
        except ValueError:
            pass

    def convert_meters(self, event):
        try:
            num = float(event.widget.get())
            self.yards = round(num / 0.9144, 2)
            self.meters = round(num, 2)
            self.centimeters = round(num * 100, 2)
            self.inches = round(num / 0.0254, 2)
        except ValueError:
            pass

    def convert_centimeters(self, event):
        try:
            num = float(event.widget.get())
            self.yards = round(num / 91.44, 2)
            self.meters = round(num / 100, 2)
            self.centimeters = round(num, 2)
            self.inches = round(num / 2.54, 2)
        except ValueError:
            pass

    def convert_inches(self, event):
        try:
            num = float(event.widget.get())
            self.yards = round(num / 36, 2)
            self.meters = round(num * .0254, 2)
            self.centimeters = round(num * 2.54, 2)
            self.inches = round(num, 2)
        except ValueError:
            pass

    def revert(self):
        print("Resetting")
        self.inches_val.set(0.0)
        self.centimeters_val.set(0.0)
        self.yards_val.set(0.0)
        self.meters_val.set(0.0)
        self.inches = 0.0
        self.centimeters = 0.0
        self.yards = 0.0
        self.meters = 0.0

    def display(self, *event):
        try:
            float(self.yards_val.get())
            float(self.meters_val.get())
            float(self.inches_val.get())
            float(self.centimeters_val.get())
            self.yards_val.set(self.yards)
            self.meters_val.set(self.meters)
            self.inches_val.set(self.inches)
            self.centimeters_val.set(self.centimeters)
            print("Yards:", self.yards, "-- Meters:", self.meters, "-- Inches:", self.inches, "-- Centimeters:", self.centimeters)
        except ValueError:
            print("All fields must contain a number to calculate")

    def exit_now(self):
        quit()

    def __init__(self, master):
        self.meters = 0.0
        self.centimeters = 0.0
        self.yards = 0.0
        self.inches = 0.0
        self.master = master

        master.title("Conversion Calculator")

        # Create ttk (better looking) frame
        mainframe = ttk.Frame(master, padding="10 10 24 24")
        mainframe.grid(column=0, row=0, sticky="ewns")

        # Make ttk frame resize with window
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        # Centimeters
        self.centimeters_val = StringVar()
        self.centimeters_val.set(self.centimeters)
        centimeters_input = ttk.Entry(mainframe, width=10, textvariable=self.centimeters_val)
        centimeters_input.grid(column=1, row=1)
        centimeters_input.bind('<KeyRelease>', self.convert_centimeters)
        ttk.Label(mainframe, text="Centimeters").grid(column=2, row=1)

        # Inches
        self.inches_val = StringVar()
        self.inches_val.set(self.inches)
        inches_input = ttk.Entry(mainframe, width=10, textvariable=self.inches_val)
        inches_input.grid(column=3, row=1)
        inches_input.bind('<KeyRelease>', self.convert_inches)
        ttk.Label(mainframe, text="Inches").grid(column=4, row=1)

        # Meters
        self.meters_val = StringVar()
        self.meters_val.set(self.meters)
        meters_input = ttk.Entry(mainframe, width=10, textvariable=self.meters_val)
        meters_input.grid(column=1, row=3)
        meters_input.bind('<KeyRelease>', self.convert_meters)
        ttk.Label(mainframe, text="Meters").grid(column=2, row=3)

        # Yards
        self.yards_val = StringVar()
        self.yards_val.set(self.yards)
        yards_input = ttk.Entry(mainframe, width=10, textvariable=self.yards_val)
        yards_input.grid(column=3, row=3)
        yards_input.bind('<KeyRelease>', self.convert_yards)
        ttk.Label(mainframe, text="Yards").grid(column=4, row=3)

        # Buttons
        ttk.Button(mainframe, text="Clear", command=self.revert).grid(column=5, row=1)
        ttk.Button(mainframe, text="Calculate", command=self.display).grid(column=5, row=2)
        ttk.Button(mainframe, text="Exit", command=self.exit_now).grid(column=5, row=3)

# Starting the GUI
window = Tk()
gui = converter(window)
window.bind('<Return>', gui.display)
window.mainloop()
