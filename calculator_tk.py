"""
Calculator GUI (Tkinter)
Run: python calculator_tk.py
"""
import tkinter as tk

root = tk.Tk()
root.title("Calculator")

expr = tk.StringVar()

def press(ch):
    expr.set(expr.get() + ch)

def clear():
    expr.set("")

def equals():
    try:
        result = eval(expr.get(), {"__builtins__": {}}, {})
        expr.set(str(result))
    except Exception:
        expr.set("Error")

entry = tk.Entry(root, textvariable=expr, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="nsew")

btns = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
]
for i, b in enumerate(btns):
    def cmd(x=b):
        if x == "=": equals()
        else: press(x)
    tk.Button(root, text=b, command=cmd, font=("Arial", 16), width=5, height=2).grid(row=1+i//4, column=i%4, padx=3, pady=3, sticky="nsew")

tk.Button(root, text="C", command=clear, font=("Arial", 16)).grid(row=5, column=0, columnspan=4, sticky="nsew", padx=3, pady=3)

for r in range(6):
    root.grid_rowconfigure(r, weight=1)
for c in range(4):
    root.grid_columnconfigure(c, weight=1)

root.mainloop()
