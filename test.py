import tkinter as tk

def create_section(root, color, row, column, width, height, rowspan=1, columnspan=1):
    section = tk.Frame(root, bg=color, width=width, height=height)
    section.grid(row=row, column=column, padx=1, pady=1, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return section

root = tk.Tk()
root.title("Three Sections Example")

section1 = create_section(root, "red", 0, 0, 75, 75)
section2 = create_section(root, "green", 0, 1, 75, 75)
sectiona = create_section(root, "red", 1, 0, 75, 75)
sectionb = create_section(root, "green", 1, 1, 75, 75)

section3 = create_section(root, "blue", 2, 0, 150, 50, columnspan=2)
section4 = create_section(root, "blue", 3, 0, 150, 50, columnspan=2)

root.mainloop()