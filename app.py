#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk  # themed widgets
from utils.window_utils import center_window

root = tk.Tk() # create app window
root.title('Tk experiments')
icon = tk.PhotoImage(file='./assets/icons/conway-lovelace.png')
root.iconphoto(True, icon)
root.resizable(False, False)

# place a label on the root window and make it visible (pack)
message = ttk.Label(root, text='Hello, World!').pack()

center_window(root)

root.mainloop() # keep the window visible on screen
