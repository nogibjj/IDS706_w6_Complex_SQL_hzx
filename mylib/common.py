import sqlite3


def create_Table():
    conn = sqlite3.connect('Sp_elections.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Sp_elections (id INTEGER PRIMARY KEY AUTOINCREMENT, Date, State, Race, 'Median Household Income', '% Bachelor''s Degree or Higher', 'Clinton Margin Improvement Over Obama', '2017-2018 Dem Margin Improvement Over Partisan Lean')
        """
    )
    conn.commit()
    print("Database table created successfully")
    return conn