#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk  # themed widgets
from utils.window_utils import setup_window

root = tk.Tk() # create app window
setup_window(root)

# place a label on the root window and make it visible (pack)
message = ttk.Label(root, text='Hello, World!').pack()

root.mainloop() # keep the window visible on screen
