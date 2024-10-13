#!/usr/bin/env python3

"""Experiments with layout - pack, fill, UP, DOWN, LEFT, RIGHT"""

import tkinter as tk
from tkinter import ttk  # themed widgets
from utils.window_utils import setup_window
from utils.widget_utils import say_which_key, close_app, log_event

root = tk.Tk() # create app window
setup_window(root)

# stack from top to bottom with pack
label1 = ttk.Label(master=root, text='One', background='red', foreground='white')
label2 = ttk.Label(master=root, text='Two', background='green', foreground='white')
label3 = ttk.Label(master=root, text='Three', background='blue', foreground='white')
label4 = ttk.Label(master=root, text='Four', background='orange', foreground='black')
label5 = ttk.Label(master=root, text='Five', background='yellow', foreground='black')

label1.pack(side=tk.LEFT, fill='y')
label4.pack(side=tk.LEFT, fill='y') # expand in the y direction
label2.pack(side=tk.BOTTOM)
label3.pack(side=tk.BOTTOM, fill='x')
label5.pack(side=tk.TOP, fill='both') # expand in x and y direction

root.mainloop()
