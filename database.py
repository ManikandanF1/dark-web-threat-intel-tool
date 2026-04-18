import sqlite3

DB_NAME = "threats.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
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


def insert_data(type, value):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO threats (type, value) VALUES (?, ?)", (type, value))

    conn.commit()
    conn.close()


def fetch_data():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT type, value FROM threats ORDER BY id DESC")
    rows = cursor.fetchall()   # IMPORTANT: returns list of tuples

    conn.close()
    return rows