import sqlite3

from db import db_access


@db_access
def languages(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute("SELECT language_name FROM LanguageFilters").fetchall()
    return [row["language_name"] for row in rows]


@db_access
def get_language_id(conn: sqlite3.Connection, language: str) -> int | None:
    row = conn.execute("SELECT id FROM LanguageFilters WHERE language_name = ?", (language,)).fetchone()
    if row is None:
        return None
    return row["id"]


@db_access
def categories(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute("SELECT category_name FROM CategoryFilters").fetchall()
    return [row["category_name"] for row in rows]

@db_access
def get_category_id(conn: sqlite3.Connection, category: str) -> int | None:
    row = conn.execute("SELECT id FROM CategoryFilters WHERE category_name = ?", (category,)).fetchone()
    if row is None:
        return None
    return row["id"]
