"""
Student Result Management (SQLite, CLI)
Run: python student_result_sqlite.py
"""
import sqlite3

DB = "results.db"

def init():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
        roll TEXT PRIMARY KEY,
        name TEXT NOT NULL
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS marks(
        roll TEXT,
        subject TEXT,
        score REAL,
        PRIMARY KEY (roll, subject),
        FOREIGN KEY (roll) REFERENCES students(roll)
    )""")
    con.commit(); con.close()

def add_student(roll, name):
    with sqlite3.connect(DB) as con:
        con.execute("INSERT OR REPLACE INTO students(roll,name) VALUES(?,?)", (roll,name))

def add_mark(roll, subject, score):
    with sqlite3.connect(DB) as con:
        con.execute("INSERT OR REPLACE INTO marks(roll,subject,score) VALUES(?,?,?)", (roll,subject,score))

def report_card(roll):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT name FROM students WHERE roll=?", (roll,))
        row = cur.fetchone()
        if not row:
            print("Student not found."); return
        name = row[0]
        cur.execute("SELECT subject, score FROM marks WHERE roll=?", (roll,))
        rows = cur.fetchall()
        if not rows:
            print("No marks entered."); return
        total = sum(s for _,s in rows)
        avg = total/len(rows)
        print(f"\nReport Card — {name} ({roll})")
        for sub, sc in rows:
            print(f"  {sub:15} {sc:5.1f}")
        print(f"Average: {avg:.2f}\n")

def menu():
    print("""
Result CLI
1. Add Student
2. Add/Update Mark
3. Report Card
0. Exit
""")

def main():
    init()
    while True:
        menu()
        ch = input("Choice: ").strip()
        if ch == "1":
            add_student(input("Roll: "), input("Name: "))
        elif ch == "2":
            add_mark(input("Roll: "), input("Subject: "), float(input("Score: ")))
        elif ch == "3":
            report_card(input("Roll: "))
        elif ch == "0":
            break
        else:
            print("Invalid.")
if __name__ == "__main__":
    main()
