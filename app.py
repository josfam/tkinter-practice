#!/usr/bin/env python3

import tkinter as tk
from utils.window_utils import center_window

root = tk.Tk() # create app window
root.title('Tk experiments')

# place a label on the root window
message = tk.Label(root, text='Hello, World!')
# make widget visible
message.pack()

center_window(root)

root.mainloop() # keep the window visible on screen
