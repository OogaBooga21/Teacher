import tkinter as tk
from enum import Enum
from ttkthemes import ThemedTk
import configparser
import os

opacity = 0.6
offsetx = 250
offsety = 350
font = 8

def read_config():
    global opacity, offsetx, offsety, font
    config = configparser.ConfigParser()
    # config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'))
    config.read('config.ini')
    opacity = float(config.get('settings', 'opacity'))
    offsetx = int(config.get('settings', 'offsetx'))
    offsety = int(config.get('settings', 'offsety'))
    font = int(config.get('settings', 'font'))
    return config

def create_section(root, color, row, column, width, height, rowspan=1, columnspan=1):
    section = tk.Frame(root, bg=color, width=width, height=height)
    section.grid(row=row, column=column, padx=1, pady=1, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return section

def populate_section(frame, text):
    label = tk.Label(frame, text=text,font=("Roboto", font,"bold"), fg="white", background=frame['bg'], justify="left",wraplength=120)
    label.pack(side=tk.LEFT)
    
def generate_layout(name):
    root = ThemedTk(theme="equilux")
    root.title(name)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"+{screen_width-offsetx}+{screen_height-offsety}")
    root.resizable(False, False)
    root.attributes('-top', 1)
    root.attributes('-alpha', opacity)
    
    sections = {
        'nouns': create_section(root, "black", 1, 0, 75, 75),
        'verbs': create_section(root, "black", 1, 1, 75, 75),
        'adjectives': create_section(root, "black", 2, 0, 75, 75),
        'sentences': create_section(root, "black", 2, 1, 75, 75),
    }

    return root, sections

