
import sqlite3
from pathlib import Path

from flask import current_app, g


def get_database_path():
    database_url = current_app.config["DATABASE_URL"]

    if database_url.startswith("sqlite:///"):
        database_path = database_url[len("sqlite:///"):]

        path = Path(database_path)

        if not path.is_absolute():
            path = Path(current_app.root_path).parent / path

        return path

    raise ValueError("Only SQLite databases are supported.")


def get_db():
    if "db" not in g:
        database_path = get_database_path()

        database_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        g.db = sqlite3.connect(database_path)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")

    return g.db


def close_db(error=None):
    database = g.pop("db", None)

    if database is not None:
        database.close()


def init_db():
    database = get_db()

    database.executescript("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT DEFAULT '',
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT DEFAULT '',
            status TEXT DEFAULT 'pending',
            project_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(project_id)
                REFERENCES projects(id)
                ON DELETE SET NULL
        );

        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            category TEXT DEFAULT 'general',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    database.commit()
