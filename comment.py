import sqlite3

from db import db_access


@db_access
def add(conn: sqlite3.Connection, post_id: int, commenter_id: int, content: str) -> None:
    conn.execute("""INSERT INTO Comments (commenter_id, post_id, content)
                    VALUES (?, ?, ?)
                 """, (commenter_id, post_id, content))


@db_access
def get_by_post(conn: sqlite3.Connection, post_id: int) -> list[dict]:
    rows = conn.execute("""SELECT Comments.id, Users.username AS commenter, post_id, content
                           FROM Comments
                           JOIN Users ON commenter_id = Users.id
                           WHERE post_id = ?
                        """, (post_id,)).fetchall()
    return rows

  
