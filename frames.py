#!/usr/bin/env python3

"""Experiments with frames, via a login form"""

import tkinter as tk
from tkinter import ttk  # themed widgets
from tkinter.messagebox import showinfo
from utils.window_utils import setup_window
from utils.widget_utils import say_which_key, close_app, log_event

root = tk.Tk() # create app window
setup_window(root)


# s = ttk.Style()
# s.configure('TFrame', background='green') # default for all TFrames

# store email and password
email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    """Call back when the login is clicked"""
    msg = f'Your email: {email.get()}\nYour password: {password.get()}'
    showinfo(
        title='Login information',
        message=msg
    )

# sign in frame
signin = ttk.Frame(root)
signin.pack(fill='x', expand=True, padx=100, pady=100)

# email label
email_label = ttk.Label(signin, text='Email Address')
email_label.pack(expand=True, fill='x')
# email textbox
email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(expand=True, fill='x')
email_entry.focus()

# password label
password_label = ttk.Label(signin, text='Password')
password_label.pack(expand=True, fill='x')
# password textbox
password_entry = ttk.Entry(signin, textvariable=password)
password_entry.pack(expand=True, fill='x')

# login button
login_btn = ttk.Button(signin, text='Login', command=login_clicked)
login_btn.pack(fill='x', expand=True, pady=20)

root.mainloop()


"""
Styles and default names:
https://www.pythontutorial.net/tkinter/ttk-style/
"""