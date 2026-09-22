import sqlite3
from datetime import datetime, timezone

from config import DATABASE_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dedup_hash TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    url TEXT,
    source TEXT NOT NULL,
    created_at TEXT NOT NULL
    -- TODO: add more columns here once you know your actual data shape
    -- e.g. major, org_name, deadline, description, location, tags, etc.
);
"""


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = get_connection()
    try:
        conn.execute(SCHEMA)
        conn.commit()
    finally:
        conn.close()


def upsert_item(dedup_hash: str, title: str, url: str, source: str) -> bool:
    """
    Get-or-create an item by dedup_hash.

    Returns True if a new row was inserted, False if it already existed.
    """
    conn = get_connection()
    try:
        existing = conn.execute(
            "SELECT id FROM items WHERE dedup_hash = ?", (dedup_hash,)
        ).fetchone()
        if existing is not None:
            return False

        conn.execute(
            """
            INSERT INTO items (dedup_hash, title, url, source, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (dedup_hash, title, url, source, datetime.now(timezone.utc).isoformat()),
        )
        conn.commit()
        return True
    finally:
        conn.close()
