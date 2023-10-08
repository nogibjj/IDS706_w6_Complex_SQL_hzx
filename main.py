"""
ETL-Query script
"""

from mylib.common import create_Table
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
from mylib.add import add
from mylib.update import update


# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

conn = create_Table()

# Query
print("Querying data...")
query(conn)

# Add
print("Adding data...")
add(conn)

# Update
print("Updating data...")
update(conn)

conn.close()
print("Done.")
