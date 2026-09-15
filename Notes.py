from tkinter import *

BG_COLOR = "#0F172A"
FG_COLOR = "#F8FAFC"
ACCENT_COLOR = "#93C5FD"

root = Tk()
root.title("Notes")
root.geometry("800x700")
root.iconbitmap("notes.ico")
root.config(bg=BG_COLOR)

title_label = Label(root, text="Notes", font=("Cambria", 32), bg=BG_COLOR, fg=ACCENT_COLOR)
title_label.pack(pady=20)

root.mainloop()