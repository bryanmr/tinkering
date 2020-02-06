#!/usr/bin/python3
from tkinter import *
from tkinter import ttk

def convert(*args):
    try:
        num = float(entered.get())
        meters.set(num / 3.2808)
        feet.set(num * 3.2808)
        print("Meters to Feet:", meters.get(), "--- Feet to Meters:", feet.get())
    except ValueError:
        print("Did you enter a number? Value entered:", entered.get())
        pass
    finally:
        entry.focus()

# Create window and inner ttk frame
window = Tk()
window.title("Feet to meters, and meters to feet...")
mainframe = ttk.Frame(window, padding="10 10 24 24")
mainframe.grid(column=0, row=0)

# Variables
entered = StringVar()
feet = StringVar()
meters = StringVar()

# Entry
entry = ttk.Entry(mainframe, width=10, textvariable=entered)
entry.grid(column=2, row=1)
ttk.Button(mainframe, text="Convert", command=convert).grid(column=3, row=1)
ttk.Label(mainframe, text="Value:").grid(column=1, row=1)

# Separator
ttk.Separator(mainframe).grid(row=2, sticky="ew", columnspan=4, pady=10)

#Display
ttk.Label(mainframe, text="Meters to Feet: ").grid(column=1, row=3)
ttk.Label(mainframe, textvariable=feet).grid(column=2, row=3)
ttk.Label(mainframe, text="Feet to Meters: ").grid(column=1, row=4)
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=4)

# Focus input and accept return, then make the GUI
entry.focus()
window.bind('<Return>', convert)
window.mainloop()
