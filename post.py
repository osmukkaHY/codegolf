import sqlite3

from db import db_access


@db_access
def add(conn: sqlite3.Connection,
        user_id: int,
        title: str,
        language_id: int,
        category_id: int,
        description: str) -> bool:
        try:
            conn.execute("""INSERT INTO Posts (poster_id, title, language_name, category_name, description)
                            VALUES (?, ?, ?, ?, ?)
                         """, (user_id, title, language_id, category_id, description))
        except sqlite3.IntegrityError as e:
            print(e)
            return False
        return True


@db_access
def get_by_id(conn: sqlite3.Connection, id: int) -> dict | None:
    row = conn.execute("""SELECT Posts.id, poster_id, title, description, username
                          FROM Posts JOIN Users ON Users.id = poster_id
                          WHERE Posts.id = ?
                       """, (id,)).fetchone()
    return row


@db_access
def get_n(conn: sqlite3.Connection, count: int) -> dict:
    rows = conn.execute("""SELECT Posts.id, poster_id, title, description, username
                              FROM Posts, Users
                              WHERE Posts.poster_id = Users.id
                              ORDER BY Posts.id DESC
                              LIMIT ?
                           """, (count,))
    return rows


@db_access
def delete(conn: sqlite3.Connection, post_id: int) -> None:
    conn.execute("""DELETE FROM Posts
                    WHERE id = ?
                 """, (post_id,))


@db_access
def update(conn: sqlite3.Connection, post_id: int, title: str, description: str) -> bool:
    conn.execute("""UPDATE Posts
                    SET title = ?, description = ?
                    WHERE id = ?
                 """, (title, description, post_id))


@db_access
def search(conn: sqlite3.Connection, search_term: str, language_filter: str, category_filter: str) -> list[sqlite3.Row]:
    language_filter = "%" if language_filter == "" else language_filter
    category_filter = "%" if category_filter == "" else category_filter
    rows = conn.execute("""SELECT Posts.id, poster_id, title, description, username
                           FROM Posts, Users
                           JOIN LanguageFilters ON Posts.language_name = LanguageFilters.id
                           JOIN CategoryFilters ON Posts.category_name = CategoryFilters.id
                           WHERE Posts.poster_id = Users.id
                             AND title LIKE ?
                             AND LanguageFilters.language_name LIKE ?
                             AND CategoryFilters.category_name LIKE ?
                        ORDER BY Posts.id DESC
                        """, (f"%{search_term}%", language_filter, category_filter)).fetchall()
    return rows

