import tkinter as tk
from tkinter import *
from tkinter import ttk

BG_COLOR = "#0F172A"
FG_COLOR = "#F8FAFC"
ACCENT_COLOR = "#93C5FD"

root = Tk()
root.title("Notes")
root.geometry("800x700")
root.iconbitmap("notes.ico")
root.config(bg=BG_COLOR)

title_label = Label(root, text="Notes", font=("Cambria", 32), bg=BG_COLOR, fg=ACCENT_COLOR)
title_label.grid(row=0, column=0, padx=20, pady=20)

new_note_button = Button(root, text="New Note", font=("Cambria", 16), bg=ACCENT_COLOR, fg=BG_COLOR)
new_note_button.grid(row=1, column=0, padx=20, pady=10)

partition_below_nnb = ttk.Separator(root, orient='horizontal')
partition_below_nnb.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

root.grid_rowconfigure(3, weight=1)

partition = ttk.Separator(root, orient='vertical')
partition.grid(row=0, column=1,rowspan=4, sticky="ns", padx=10, pady=10)

initial_label = Label(root, text="Select a note or Start Fresh", font=("Cambria", 16), bg=BG_COLOR, fg=FG_COLOR)
initial_label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()