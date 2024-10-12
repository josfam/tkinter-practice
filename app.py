#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk  # themed widgets
from utils.window_utils import setup_window
from utils.widget_utils import say_which_key, close_app

root = tk.Tk() # create app window
setup_window(root)

# place a label on the root window and make it visible (pack)
message = ttk.Label(root, text='Hello, World!').pack()

# binding a function
close_btn = ttk.Button(root, text='Close', command=lambda: close_app(root)).pack()

# binding an event
save_btn = ttk.Button(root, text='Which key?')
save_btn.bind('<Any-KeyPress>', say_which_key)
save_btn.focus() # focus the button when the app starts
save_btn.pack()

root.mainloop() # keep the window visible on screen
