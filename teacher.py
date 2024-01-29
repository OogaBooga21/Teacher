import tkinter as tk
from front import generate_layout,populate_section

root,frames = generate_layout("teacher")

noun_list = "sd das daa"

populate_section(frames["nouns"], noun_list)
populate_section(frames["verbs"], noun_list)
populate_section(frames["adjectives"], noun_list)
populate_section(frames["sentences"], noun_list)
populate_section(frames["to_translate"], noun_list)
populate_section(frames["translated"], noun_list)

# text = tk.Text(root, height=10, width=20)
# text.insert(tk.END, "hello \nhello \nhello")
# text.pack()

root.mainloop()