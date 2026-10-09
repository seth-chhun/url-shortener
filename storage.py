import sqlite3
from contextlib import closing

DB_FILE = "storage.db"

def init_db():
    # Create tables if they do not exist
    with closing(sqlite3.connect(DB_FILE)) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS urls (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code VARCHAR(10) NOT NULL UNIQUE,
                    url TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

def insert(code:str, url:str):
    with closing(sqlite3.connect(DB_FILE)) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO urls (code, url) VALUES (?, ?)", (code, url))

def find_code(url:str):
    with closing(sqlite3.connect(DB_FILE)) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT code FROM urls WHERE url = ?", (url,))
            return cursor.fetchone()

def find_url(code:str):
    with closing(sqlite3.connect(DB_FILE)) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT url FROM urls WHERE code = ?", (code,))
            return cursor.fetchone()

def fetch_all():
    with closing(sqlite3.connect(DB_FILE)) as conn:
            with conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM urls")
                return cursor.fetchall()

if __name__ == "__main__":
    init_db()


