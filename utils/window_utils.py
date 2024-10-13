"""Utility functions concerning the application window"""

import tkinter as tk
from pathlib import Path

def center_window(root: tk.Tk, window_width, window_height):
    """Centers this tk window on the screen"""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_center = int(screen_width / 2 - window_width / 2)
    y_center = int(screen_height / 2 - window_height / 2)

    # position the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{x_center}+{y_center}')

def setup_window(root: tk.Tk=None, width=800, height=800):
    """Sets up the window at the start of the application"""
    root.title('Tk experiments')
    icon_path = Path('./assets/icons/conway-lovelace.png')
    icon = tk.PhotoImage(file=str(icon_path))
    root.iconphoto(True, icon)
    root.resizable(False, False)
    center_window(root, width, height)
