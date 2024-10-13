#!/usr/bin/env python3

"""Experiments with layout - pack, fill, UP, DOWN, LEFT, RIGHT"""

import tkinter as tk
from tkinter import ttk  # themed widgets
from utils.window_utils import setup_window
from utils.widget_utils import say_which_key, close_app, log_event

root = tk.Tk() # create app window
setup_window(root)

label1 = ttk.Button(master=root, text='One', padding=(10, 60))
label1.bind('<Enter>', log_event) # on hover
label1.bind('<Enter>', say_which_key, add=True) # on hover, additional event bind
label1.pack(expand=True)

root.mainloop()
