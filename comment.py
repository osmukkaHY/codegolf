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

  
@db_access
def count_by_user(conn: sqlite3.Connection, user_id: int) -> int:
    row = conn.execute("SELECT COUNT(*) AS row_count FROM Comments WHERE commenter_id = ?", (user_id,)).fetchone()
    return row["row_count"]
