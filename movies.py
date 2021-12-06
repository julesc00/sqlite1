import sqlite3

connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Movies
    (Title TEXT, Director TEXT, Year INT )"""
)

# Insert one entry
# cursor.execute("INSERT INTO Movies VALUES ('Taxi Driver', 'Julito Chulito', 2006)")

famous_films = [
    ("Pulp Fiction", "Quentin Tarantino", 1994),
    ("Back to the Future", "Steven Spielberg", 1985),
    ("Moonrise Kingdom", "Wes Anderson", 2012)
]

# Insert several entries at once
# cursor.executemany("INSERT INTO Movies VALUES (?, ?, ?)", famous_films)

# records = cursor.execute("SELECT * FROM Movies")
#
# for record in records:
#     print(record)

# After printing once, it'll return an empty list.
# print(cursor.fetchall())

release_year = (1985,)

cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)
print(cursor.fetchall())

connection.commit()
connection.close()
