import tkinter as tk
from enum import Enum
from ttkthemes import ThemedTk

# focused=True

# def on_click(root):
#     global focused
#     focused = True
#     check_focus(root)

# def check_focus(root):
#     global focused
#     if root.focus_get() == root:
#         focused = True
#         root.after(1000, check_focus, root)
#     else:
#         focused = False

# def update_overrideredirect(root):
#     global focused
#     root.overrideredirect(focused)

def create_section(root, color, row, column, width, height, rowspan=1, columnspan=1):
    section = tk.Frame(root, bg=color, width=width, height=height)
    section.grid(row=row, column=column, padx=1, pady=1, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return section

def populate_section(frame, text):
    label = tk.Label(frame, text=text,font=("Roboto", 8,"bold"), fg="white", background=frame['bg'], justify="left",wraplength=120)
    label.pack(side=tk.LEFT)
    
def generate_layout(name):
    root = ThemedTk(theme="equilux")
    root.title(name)
    # update_overrideredirect(root)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    

# Set the initial position of the window to the lower left corner
    root.geometry(f"+{screen_width-250}+{screen_height-300}")
    root.resizable(False, False)
    # root.attributes("-topmost", True)
    root.attributes('-top', 1)  # Give it a lower "top" value
    root.attributes('-alpha', 0.6)
    # root.bind("<Button-1>",lambda event: on_click(root))
    sections = {
        'nouns': create_section(root, "black", 1, 0, 75, 75),
        'verbs': create_section(root, "black", 1, 1, 75, 75),
        'adjectives': create_section(root, "black", 2, 0, 75, 75),
        'sentences': create_section(root, "black", 2, 1, 75, 75),
    }

    return root, sections

