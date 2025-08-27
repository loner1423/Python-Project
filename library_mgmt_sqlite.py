"""
Library Management (SQLite, CLI)
Run: python library_mgmt_sqlite.py
"""
import sqlite3, os

DB = "library.db"

def init():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        available INTEGER DEFAULT 1
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS members(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS loans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        member_id INTEGER,
        returned INTEGER DEFAULT 0
    )""")
    con.commit(); con.close()

def add_book(title, author):
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO books(title,author) VALUES(?,?)", (title,author))

def list_books():
    with sqlite3.connect(DB) as con:
        for row in con.execute("SELECT id,title,author,available FROM books"):
            print(row)

def add_member(name):
    with sqlite3.connect(DB) as con:
        con.execute("INSERT INTO members(name) VALUES(?)", (name,))

def borrow(book_id, member_id):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT available FROM books WHERE id=?", (book_id,))
        row = cur.fetchone()
        if not row or row[0] == 0:
            print("Book not available."); return
        cur.execute("INSERT INTO loans(book_id, member_id) VALUES(?,?)", (book_id, member_id))
        cur.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
        con.commit(); print("Borrowed.")

def ret(book_id):
    with sqlite3.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE loans SET returned=1 WHERE book_id=? AND returned=0", (book_id,))
        cur.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
        con.commit(); print("Returned.")

def menu():
    print("""
Library CLI
1. Add Book
2. List Books
3. Add Member
4. Borrow Book
5. Return Book
0. Exit
""")

def main():
    init()
    while True:
        menu()
        ch = input("Choice: ").strip()
        if ch == "1":
            add_book(input("Title: "), input("Author: "))
        elif ch == "2":
            list_books()
        elif ch == "3":
            add_member(input("Member name: "))
        elif ch == "4":
            borrow(int(input("Book ID: ")), int(input("Member ID: ")))
        elif ch == "5":
            ret(int(input("Book ID: ")))
        elif ch == "0":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
