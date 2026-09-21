import tkinter as tk
from tkinter import *
from tkinter import ttk, simpledialog, messagebox
import pymongo
from pymongo import MongoClient

BG_COLOR = "#0F172A"
FG_COLOR = "#F8FAFC"
SURFACE_COLOR = "#151F32"
ACCENT_COLOR = "#93C5FD"
Danger_COLOR = "#F74F4F"

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "NOTES_APP"
COLLECTION_NAME = "notes"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

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
                        bg=ACCENT_COLOR, fg=BG_COLOR,
                        command=lambda: [create_note(input_entry.get()), root.destroy()])
    ok_button.pack(side=LEFT, padx=20)
    cancel_button = Button(button_frame, text="Cancel", font=("Cambria", 16),
                            bg=ACCENT_COLOR, fg=BG_COLOR,command=lambda: root.destroy())
    cancel_button.pack(side=RIGHT, padx=20)
    root.resizable(False, False)
    pass

def create_note(Title):
    if Title=="":
        messagebox.showerror("Error", "Title cannot be empty.")
        return
    for widget in right_frame.winfo_children():
        widget.destroy()
    note_title=Label(right_frame, text=Title, font=("Cambria", 22), bg=BG_COLOR, fg=ACCENT_COLOR)
    note_title.pack(anchor="nw", padx=20, pady=(20,10))

    sav_del_frame = Frame(right_frame, bg=BG_COLOR)
    sav_del_frame.pack(padx=20, pady=(0,0))

    save_button = Button(sav_del_frame, text="Save", font=("Cambria", 16),
                          bg=ACCENT_COLOR, fg=BG_COLOR,
                          command=lambda: save_note(Title, text_area.get("1.0", END)))
    save_button.pack(side=LEFT, padx=20, pady=10)

    del_button = Button(sav_del_frame, text="Delete", font=("Cambria", 16),
                          bg=Danger_COLOR, fg=BG_COLOR,
                          command=lambda: delete_note(Title))
    del_button.pack(side=RIGHT, padx=20, pady=10)

    text_area = Text(right_frame, font=("Cambria", 14), bg=SURFACE_COLOR, fg=FG_COLOR,
                      insertbackground=FG_COLOR, wrap="word", bd=0, highlightthickness=0)
    text_area.pack(fill="both", expand=True, padx=20, pady=(20,40))
    notes_listbox.insert(END, Title)
    pass

def save_note(title, content):
    collection.update_one({"title": title}, {"$set": {"content": content}}, upsert=True)
    # print(f"Saving note: {title} with content: {content}")
    messagebox.showinfo("Saved", f"Note '{title}' has been saved.")

    pass

def delete_note(title):
    collection.delete_one({"title": title})
    # print(f"Deleting note: {title}")
    messagebox.showinfo("Deleted", f"Note '{title}' has been deleted.")

    for widget in right_frame.winfo_children():
        widget.destroy()
    initial_label.pack(anchor="center", expand=True)

    pass

def list_click(event,):
    selected_index = notes_listbox.curselection()
    if selected_index:
        selected_title = notes_listbox.get(selected_index)
        for widget in right_frame.winfo_children():
            widget.destroy()
        note_title=Label(right_frame, text=selected_title, font=("Cambria", 22), bg=BG_COLOR, fg=ACCENT_COLOR)
        note_title.pack(anchor="nw", padx=20, pady=(20,10))
        sav_del_frame = Frame(right_frame, bg=BG_COLOR)
        sav_del_frame.pack(padx=20, pady=(0,0))

        save_button = Button(sav_del_frame, text="Save", font=("Cambria", 16),
                          bg=ACCENT_COLOR, fg=BG_COLOR,
                          command=lambda: save_note(selected_title, text_area.get("1.0", END)))
        save_button.pack(side=LEFT, padx=20, pady=10)

        del_button = Button(sav_del_frame, text="Delete", font=("Cambria", 16),
                          bg=Danger_COLOR, fg=BG_COLOR,
                          command=lambda: delete_note(selected_title))
        del_button.pack(side=RIGHT, padx=20, pady=10)
        text_area = Text(right_frame, font=("Cambria", 14), bg=SURFACE_COLOR, fg=FG_COLOR,
                          insertbackground=FG_COLOR, wrap="word", bd=0, highlightthickness=0)
        text_area.pack(fill="both", expand=True, padx=20, pady=(20,40))

    pass

root = Tk()
root.title("Notes")
root.geometry("800x700")
root.resizable(False, False)
root.iconbitmap("notes.ico")
root.config(bg=BG_COLOR)

root.grid_columnconfigure(2, weight=1)
right_frame = Frame(root, bg=BG_COLOR)
right_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")

notes_listbox = Listbox(root, font=("Cambria", 14), bg=SURFACE_COLOR, fg=FG_COLOR,
                      selectbackground=ACCENT_COLOR, selectforeground=BG_COLOR)
notes_listbox.grid(row=2, column=0, rowspan=2, sticky="nsew", padx=20, pady=20)
notes_listbox.bind("<<ListboxSelect>>", list_click)

title_label = Label(root, text="Notes", font=("Cambria", 32), bg=BG_COLOR, fg=ACCENT_COLOR)
title_label.grid(row=0, column=0, padx=20, pady=20)

new_note_button = Button(root, text="New Note", font=("Cambria", 16), bg=ACCENT_COLOR,
                          fg=BG_COLOR,command=lambda: new_note())
new_note_button.grid(row=1, column=0, padx=20, pady=10)

root.grid_rowconfigure(3, weight=1)

partition = ttk.Separator(root, orient='vertical')
partition.grid(row=0, column=1,rowspan=4, sticky="ns", pady=10)

initial_label = Label(right_frame, text="Select a note or Start Fresh", font=("Cambria", 16), bg=BG_COLOR, fg=FG_COLOR)
initial_label.pack(anchor="center", expand=True)

root.mainloop()