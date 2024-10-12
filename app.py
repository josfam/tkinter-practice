#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk() # create app window

# place a label on the root window
message = tk.Label(root, text='Hello, World!')
# make widget visible
message.pack()

root.mainloop() # keep the window visible on screen
