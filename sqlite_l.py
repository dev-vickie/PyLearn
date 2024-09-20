import sqlite3

data = (
    ("Jean-Baptise Zorg","Human",122),
    ("Korben Dallas","Meat Popsicle",100),
    ("Ak'not","Mangalore",-5)
        )

with sqlite3.connect("another_test.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Roster(
        Name TEXT,
        Species TEXT,
        IQ INT
        );"""
            )

    cursor.executemany("INSERT INTO Roster VALUES(?,?,?)",data)

