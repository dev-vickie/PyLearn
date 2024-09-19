import sqlite3

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(
        """
        CREATE TABLE People(
            FirstName TEXT,
            LastName TEXT,
            Age INT
        );
        INSERT INTO People VALUES(
        'Vic',
        'Max',
        23
        );
        """
    )

# No connection.commit() or connection.close()
# All changes are automatically commited when the 'with' block is done executing


    