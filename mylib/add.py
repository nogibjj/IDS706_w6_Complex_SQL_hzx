"""CRUD operations for the Sp_elections table"""

import sqlite3

from mylib.common import create_Table


def add(conn):
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM Sp_elections WHERE State = 'Pennsylvania'")
    # cursor add one item
    print("Insert one item from Pennsylvania state into the table")
    data2 = ('3/17/19', 'Pennsylvania', 'SD-14', '$49,252', '25.10%', '8%', '1%')
    cursor.execute("INSERT INTO Sp_elections( Date, State, Race, 'Median Household Income', '% Bachelor''s Degree or Higher', 'Clinton Margin Improvement Over Obama', '2017-2018 Dem Margin Improvement Over Partisan Lean') VALUES (?, ?, ?, ?, ?, ?, ?)", data2)
    conn.commit()
    return "Success"


if __name__ == "__main__":
    conn = create_Table()
    add(conn)


