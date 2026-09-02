import sqlite3

with open ("sql/schema.sql") as file:
    schema = file.read()
with sqlite3.connect("database.db") as conn:
    conn.executescript(schema)

