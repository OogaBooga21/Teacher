import tkinter as tk

root = tk.Tk()
root.title("Teacher")
root.geometry("200x100")

label = tk.Label(text="Teacher")
label.pack()

# text = tk.Text(root, height=10, width=20)
# text.insert(tk.END, "hello \nhello \nhello")
# text.pack()

root.mainloop()