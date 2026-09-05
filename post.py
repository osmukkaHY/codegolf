import sqlite3

from db import db_access


@db_access
def add(conn: sqlite3.Connection,
        user_id: int,
        title: str,
        description: str) -> bool:
        try:
            conn.execute("""INSERT INTO Posts (poster_id, title, description)
                            VALUES (?, ?, ?)
                         """, (user_id, title, description))
        except sqlite3.IntegrityError:
            return False
        return True

