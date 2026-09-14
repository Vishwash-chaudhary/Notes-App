from tkinter import *

BG_COLOR = "#0F172A"
FG_COLOR = "#F8FAFC"

root = Tk()
root.title("Notes")
root.geometry("550x700")
root.iconbitmap("notes.ico")
root.config(bg=BG_COLOR)

text_label = Label(root, text="Notes", font=("Cambria", 32), bg=BG_COLOR, fg=FG_COLOR)
text_label.pack(pady=20)

root.mainloop()