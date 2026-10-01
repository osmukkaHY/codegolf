import sqlite3

from db import db_access


@db_access
def languages(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute("SELECT language_name FROM LanguageFilters").fetchall()
    return [row["language_name"] for row in rows]

@db_access
def categories(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute("SELECT category_name FROM CategoryFilters").fetchall()
    return [row["category_name"] for row in rows]
