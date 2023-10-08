import sqlite3

from mylib.common import create_Table

def update(conn):
    cursor = conn.cursor()
    data = ('$50,000', '3/13/19', 'Pennsylvania')
    cursor.execute("UPDATE Sp_elections SET 'Median Household Income' = ?  WHERE Date = ? AND State = ?", data)
    print("Update one item from Pennsylvania state into the table")
    conn.commit()
    return "Success"

if __name__ == "__main__":
    conn = create_Table()
    update(conn)