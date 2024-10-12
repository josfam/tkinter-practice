import tkinter as tk

def center_window(root: tk.Tk=None, window_width=800, window_height=800):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_center = int(screen_width / 2 - window_width / 2)
    y_center = int(screen_height / 2 - window_height / 2)

    # position the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{x_center}+{y_center}')
