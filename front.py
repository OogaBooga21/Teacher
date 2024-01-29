import tkinter as tk
from enum import Enum

def close_window(root):
    root.destroy()

def create_section(root, color, row, column, width, height, rowspan=1, columnspan=1):
    section = tk.Frame(root, bg=color, width=width, height=height)
    section.grid(row=row, column=column, padx=1, pady=1, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return section

def populate_section(frame, text):
    label = tk.Label(frame, text=text, background=frame['bg'], justify="left")
    label.pack(side=tk.LEFT)
    
def generate_layout(name):
    root = tk.Tk()
    root.title(name)
    root.overrideredirect(True)
    
    close_section = create_section(root, "white", 0, 0, 1, 0, columnspan=2)
    close_button = tk.Button(close_section, text="x", command=lambda: close_window(root), height=1, width=2)
    close_button.pack(side=tk.RIGHT)

    
    sections = {
        'nouns': create_section(root, "white", 1, 0, 75, 75),
        'verbs': create_section(root, "white", 1, 1, 75, 75),
        'adjectives': create_section(root, "white", 2, 0, 75, 75),
        'sentences': create_section(root, "white", 2, 1, 75, 75),
        'to_translate': create_section(root, "light gray", 3, 0, 150, 50, columnspan=2),
        'translated': create_section(root, "light gray", 4, 0, 150, 50, columnspan=2)
    }
    return root, sections

