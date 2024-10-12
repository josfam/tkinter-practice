#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk  # themed widgets
from utils.window_utils import setup_window
from utils.widget_utils import say_which_key, close_app, log_event

root = tk.Tk() # create app window
setup_window(root)

# stack from top to bottom with pack
label1 = ttk.Label(master=root, text='Tkinter', background='red', foreground='white').pack()
label2 = ttk.Label(master=root, text='Pack Layout', background='green', foreground='white').pack()
label2 = ttk.Label(master=root, text='Demo', background='blue', foreground='white').pack()

root.mainloop()
