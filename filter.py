import sqlite3

from db import db_access


@db_access
def languages(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute("SELECT language_name FROM Filters").fetchall()
    return [row["language_name"] for row in rows]

