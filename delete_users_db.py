import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Users")

connection.commit()
connection.close()
