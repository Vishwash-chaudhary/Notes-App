import tkinter as tk
from tkinter import *
from tkinter import ttk

BG_COLOR = "#0F172A"
FG_COLOR = "#F8FAFC"
SURFACE_COLOR = "#151F32"
ACCENT_COLOR = "#93C5FD"

def new_note():
    root = Tk()
    root.title("New Note")
    root.iconbitmap("notes.ico")
    root.geometry("300x200")
    root.config(bg=BG_COLOR)
    title_label = Label(root, text="Enter title of new note:", font=("Cambria", 20), bg=BG_COLOR, fg=ACCENT_COLOR)
    title_label.pack(pady=25)
    input_entry = Entry(root, font=("Cambria", 16), bg=SURFACE_COLOR, fg=FG_COLOR, insertbackground=FG_COLOR)
    input_entry.pack()
    button_frame = Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=18)
    ok_button = Button(button_frame, text="OK", font=("Cambria", 16),
                        bg=ACCENT_COLOR, fg=BG_COLOR,)
    ok_button.pack(side=LEFT, padx=20)
    cancel_button = Button(button_frame, text="Cancel", font=("Cambria", 16),
                            bg=ACCENT_COLOR, fg=BG_COLOR,)
    cancel_button.pack(side=RIGHT, padx=20)
    root.resizable(False, False)
    pass


root = Tk()
root.title("Notes")
root.geometry("800x700")
root.resizable(False, False)
root.iconbitmap("notes.ico")
root.config(bg=BG_COLOR)

title_label = Label(root, text="Notes", font=("Cambria", 32), bg=BG_COLOR, fg=ACCENT_COLOR)
title_label.grid(row=0, column=0, padx=20, pady=20)

new_note_button = Button(root, text="New Note", font=("Cambria", 16), bg=ACCENT_COLOR, fg=BG_COLOR,command=lambda: new_note())
new_note_button.grid(row=1, column=0, padx=20, pady=10)

partition_below_nnb = ttk.Separator(root, orient='horizontal')
partition_below_nnb.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

root.grid_rowconfigure(3, weight=1)

partition = ttk.Separator(root, orient='vertical')
partition.grid(row=0, column=1,rowspan=4, sticky="ns", padx=10, pady=10)

initial_label = Label(root, text="Select a note or Start Fresh", font=("Cambria", 16), bg=BG_COLOR, fg=FG_COLOR)
initial_label.place(relx=0.68, rely=0.5, anchor="center")

root.mainloop()