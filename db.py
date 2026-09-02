import sqlite3
from typing import Callable


def db_access(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        with sqlite3.connect("database.db") as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            conn.row_factory = sqlite3.Row
            return func(conn, *args, **kwargs)
    return wrapper

