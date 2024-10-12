"""Utility functions concerning widget events"""

import tkinter as tk

def close_app(root: tk.Tk):
    """closes the application"""
    root.destroy()

def say_which_key(event):
    """Prints out what key was pressed"""
    print(f'{event.keysym} key pressed')
