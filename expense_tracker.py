"""
Expense Tracker (SQLite + Tkinter)
Run: python expense_tracker.py
"""
import tkinter as tk, sqlite3, datetime

DB="expenses.db"

def init():
    con=sqlite3.connect(DB); cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expenses(id INTEGER PRIMARY KEY, item TEXT, amount REAL, date TEXT)")
    con.commit(); con.close()

def add_item():
    item, amt=entry_item.get(), float(entry_amt.get())
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO expenses(item,amount,date) VALUES(?,?,?)",
                    (item,amt,datetime.date.today().isoformat()))
    entry_item.delete(0,"end"); entry_amt.delete(0,"end")
    refresh()

def refresh():
    listbox.delete(0,"end"); total=0
    with sqlite3.connect(DB) as con:
        for id,item,amt,date in con.execute("SELECT * FROM expenses ORDER BY id DESC"):
            listbox.insert("end",f"{date}: {item} - {amt}")
            total+=amt
    lbl_total.config(text=f"Total Spent: {total}")

init()
root=tk.Tk(); root.title("Expense Tracker")
tk.Label(root,text="Item").grid(row=0,column=0); entry_item=tk.Entry(root); entry_item.grid(row=0,column=1)
tk.Label(root,text="Amount").grid(row=1,column=0); entry_amt=tk.Entry(root); entry_amt.grid(row=1,column=1)
tk.Button(root,text="Add",command=add_item).grid(row=2,column=0,columnspan=2)
listbox=tk.Listbox(root,width=40); listbox.grid(row=3,column=0,columnspan=2)
lbl_total=tk.Label(root,text="Total Spent: 0"); lbl_total.grid(row=4,column=0,columnspan=2)
refresh(); root.mainloop()
