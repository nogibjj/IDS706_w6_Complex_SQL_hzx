"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv
import os




#load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/IDS706_w5_SQL_hzx/data/Sp_elections.csv"):
    """"Transforms and Loads data into the local SQLite3 database"""

    #prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('Sp_elections.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Sp_elections")
    # The reason why some of the column names are enclosed in single quotes in the CREATE TABLE statement is because they contain spaces or special characters that are not allowed in unquoted column names.
    c.execute("CREATE TABLE Sp_elections (id INTEGER PRIMARY KEY AUTOINCREMENT, Date, State, Race, 'Median Household Income', '% Bachelor''s Degree or Higher', 'Clinton Margin Improvement Over Obama', '2017-2018 Dem Margin Improvement Over Partisan Lean')")    #insert
    # ID auto-increases
    c.executemany("INSERT INTO Sp_elections (Date, State, Race, 'Median Household Income', '% Bachelor''s Degree or Higher', 'Clinton Margin Improvement Over Obama', '2017-2018 Dem Margin Improvement Over Partisan Lean') VALUES (?, ?, ?, ?, ?, ?, ?)", payload)    
    conn.commit()
    conn.close()
    return "Sp_elections.db"

if __name__ == "__main__":
    load()

