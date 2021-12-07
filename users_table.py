import sqlite3
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3)

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Users
    (user_id INTEGER PRIMARY KEY AUTOINCREMENT , first_name TEXT, last_name TEXT, email TEXT UNIQUE)"""
)

# Insert 5 new entries
users = [
    ("Caricia", "Briones", "cari@changuis.com"),
    ("Franzche", "Briones", "punky@changuis.com"),
    ("Brigitte", "Briones", "gigitte@changuis.com"),
    ("Michele", "Briones", "chenis@changuis.com"),
    ("Jemima", "Briones", "jemi@changuis.com"),
]

# cursor.executemany("INSERT INTO Users(first_name, last_name, email) VALUES (?, ?, ?)", users)

cursor.execute("SELECT email FROM Users")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Users")
pp.pprint(cursor.fetchall())

connection.commit()
connection.close()
