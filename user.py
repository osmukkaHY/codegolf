import sqlite3

from db import db_access


@db_access
def add(conn: sqlite3.Connection, username: str, password_hash: str) -> bool:
    try:
        conn.execute("""INSERT INTO Users (username, password_hash)
                        VALUES (?, ?)
                     """, (username, password_hash))
    except sqlite3.IntegrityError:
        return False
    return True
