import sqlite3
import os

DB_PATH = os.getenv("DATABASE_URL", "sqlite:///habits.db").replace("sqlite:///", "")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY,
            habit_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY(habit_id) REFERENCES habits(id)
        )
    """)
    conn.commit()
    conn.close()

def add_habit(user_id: int, name: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO habits (user_id, name) VALUES (?, ?)", (user_id, name))
    conn.commit()
    conn.close()

def get_habits(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM habits WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_record(habit_id: int, date: str, done: bool):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO records (habit_id, date, done) VALUES (?, ?, ?)",
        (habit_id, date, int(done))
    )
    conn.commit()
    conn.close()

def get_stats(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT h.name, COUNT(r.id) FILTER(WHERE r.done=1), COUNT(r.id)
        FROM habits h
        LEFT JOIN records r ON r.habit_id = h.id
        WHERE h.user_id = ?
        GROUP BY h.id
    """, (user_id,))
    stats = cursor.fetchall()
    conn.close()
    return stats
