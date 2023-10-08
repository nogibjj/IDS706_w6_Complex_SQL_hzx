import pytest
import sqlite3
from mylib.query import query
from mylib.add import add
from mylib.update import update


@pytest.fixture
def sqlite_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Sp_elections (id INTEGER PRIMARY KEY AUTOINCREMENT, Date, State, Race, 'Median Household Income', '% Bachelor''s Degree or Higher', 'Clinton Margin Improvement Over Obama', '2017-2018 Dem Margin Improvement Over Partisan Lean')"
    )
    yield conn
    cursor.execute("DROP TABLE Sp_elections")
    conn.close()


# def test_extract():
#     extract()
#     assert os.path.isfile("data/Sp_elections.csv") == True

# helper function
def insert_test(conn):
    cursor = conn.cursor()
    data_sample = [
        ("3/13/19", "Pennsylvania", "SD-14", "$49,252", "24.10%", "8%", "1%"),
        ("3/15/19", "Pennsylvania", "SD-15", "$59,252", "25.10%", "8%", "1%"),
        ("3/16/19", "Pennsylvania", "SD-16", "$69,252", "26.10%", "8%", "1%"),
    ]
    cursor.executemany(
        "INSERT INTO Sp_elections( Date, State, Race, 'Median Household Income', '% Bachelor''s Degree or Higher', 'Clinton Margin Improvement Over Obama', '2017-2018 Dem Margin Improvement Over Partisan Lean') VALUES (?, ?, ?, ?, ?, ?, ?)",
        data_sample,
    )
    print("Insert test items into the table")
    conn.commit()


def test_query(sqlite_connection):
    insert_test(sqlite_connection)
    res = query(sqlite_connection)
    assert res == "Success"


def test_add(sqlite_connection):
    insert_test(sqlite_connection)
    add(sqlite_connection)
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT * FROM Sp_elections WHERE Date = '3/17/19'")
    rows = cursor.fetchall()
    assert len(rows) == 1


def test_update(sqlite_connection):
    insert_test(sqlite_connection)
    update(sqlite_connection)
    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT * FROM Sp_elections WHERE Date = '3/13/19'")
    rows = cursor.fetchall()
    assert len(rows) == 1
