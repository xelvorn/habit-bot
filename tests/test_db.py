import os
import sqlite3
import pytest
import db

TEST_DB = "test.db"

@pytest.fixture(autouse=True)
def setup_db(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{TEST_DB}")
    db.init_db()
    yield
    os.remove(TEST_DB)

def test_add_and_get_habit():
    db.add_habit(1, "тест")
    habits = db.get_habits(1)
    assert habits[0][1] == "тест"

def test_stats_empty():
    stats = db.get_stats(2)
    assert stats == []
