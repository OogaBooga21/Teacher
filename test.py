import tkinter as tk

def create_section(root, color, row, column, width, height, rowspan=1, columnspan=1):
    section = tk.Frame(root, bg=color, width=width, height=height)
    section.grid(row=row, column=column, padx=1, pady=1, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    return section

def populate_section(section, text):
    label = tk.Label(section, text=text, background=section['bg'], justify="left")
    label.pack()

root = tk.Tk()
root.title("Three Sections Example")

noun_section = create_section(root, "white", 0, 0, 75, 75)
verb_section = create_section(root, "white", 0, 1, 75, 75)
adjective_section = create_section(root, "white", 1, 0, 75, 75)
sentence_section = create_section(root, "white", 1, 1, 75, 75)

to_translate_section = create_section(root, "light gray", 2, 0, 150, 50, columnspan=2)
translated_section = create_section(root, "light gray", 3, 0, 150, 50, columnspan=2)

noun_list = "sd das daa"

populate_section(noun_section, noun_list)
populate_section(verb_section, noun_list)
populate_section(adjective_section, noun_list)
populate_section(sentence_section, noun_list)
populate_section(to_translate_section, noun_list)
populate_section(translated_section, noun_list)

root.mainloop()