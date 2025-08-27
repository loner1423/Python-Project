"""
To-Do List (Tkinter)
Run: python todo_tk.py
"""
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import json, os

DATA_FILE = "todos.json"

def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            return json.load(f)
    return []

def save(items):
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(items, f, indent=2)

def add_item():
    text = simpledialog.askstring("New Task","Task:")
    if text:
        items.append({"text": text, "done": False})
        refresh(); save(items)

def delete_item():
    sel = listbox.curselection()
    if not sel: return
    del items[sel[0]]
    refresh(); save(items)

def toggle_done(event=None):
    sel = listbox.curselection()
    if not sel: return
    i = sel[0]
    items[i]["done"] = not items[i]["done"]
    refresh(); save(items)

def refresh():
    listbox.delete(0, tk.END)
    for it in items:
        mark = "✔" if it["done"] else "✗"
        listbox.insert(tk.END, f"[{mark}] {it['text']}")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root, padx=10, pady=10); frame.pack(fill="both", expand=True)
listbox = tk.Listbox(frame, font=("Consolas", 14))
listbox.pack(fill="both", expand=True)
listbox.bind("<Double-Button-1>", toggle_done)

btns = tk.Frame(root); btns.pack(pady=6)
tk.Button(btns, text="Add", width=10, command=add_item).pack(side="left", padx=5)
tk.Button(btns, text="Delete", width=10, command=delete_item).pack(side="left", padx=5)

items = load()
refresh()

root.mainloop()
