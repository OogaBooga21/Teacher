import tkinter as tk
from enum import Enum

def create_section(root, color, row, column, width, height, name,rowspan=1, columnspan=1):
    section = tk.Frame(root, bg=color, width=width, height=height, name=name)
    section.grid(row=row, column=column, padx=1, pady=1, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return section

def populate_section(frame, text):
    label = tk.Label(frame, text=text, background=frame['bg'], justify="left")
    label.pack()
    
def generate_layout(name):
    root = tk.Tk()
    root.title(name)
    
    sections = {
        'nouns': create_section(root, "white", 0, 0, 75, 75, "nouns"),
        'verbs': create_section(root, "white", 0, 1, 75, 75, "verbs"),
        'adjectives': create_section(root, "white", 1, 0, 75, 75, "adjectives"),
        'sentences': create_section(root, "white", 1, 1, 75, 75, "sentences"),
        'to_translate': create_section(root, "light gray", 2, 0, 150, 50, "to_translate", columnspan=2),
        'translated': create_section(root, "light gray", 3, 0, 150, 50, "translated", columnspan=2)
    }
    return root, sections

