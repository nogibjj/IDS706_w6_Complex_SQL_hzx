"""Query the database"""

import sqlite3

from mylib.common import create_Table

def query(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sp_elections WHERE State = 'Pennsylvania'")
    print("The elections' situation in Pennsylvania are:")
    rows = cursor.fetchall()
    # Print the column names
    column_names = [description[0] for description in cursor.description]
    print(column_names)

    # Print the rows beautifully
    for row in rows:
        print(row)
    return "Success"

if __name__ == "__main__":
    conn = create_Table()
    query(conn)
