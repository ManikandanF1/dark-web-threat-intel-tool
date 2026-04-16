import sqlite3
import os

# Force same DB path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "threats.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS threats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        value TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_data(data_type, value):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO threats (type, value) VALUES (?, ?)",
        (data_type, value)
    )

    conn.commit()
    conn.close()


def fetch_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT type, value FROM threats ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    data = []
    for r in rows:
        data.append({"type": r[0], "value": r[1]})

    return data