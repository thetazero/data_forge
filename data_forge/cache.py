import sqlite3
import hashlib


class Cache:
    def __init__(self):
        self.conn: sqlite3.Connection = sqlite3.connect('cache.db')
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS cache ( 
time TEXT, caller TEXT, hash TEXT, value TEXT
)
                            """)

    def _hash(self, key: str) -> str:
        return hashlib.sha256(key.encode()).hexdigest()

    def get(self, caller: str, key: str) -> str | None:
        self.cursor.execute(
            "SELECT value FROM cache WHERE caller = ? AND hash = ?", (caller, self._hash(key)))
        try:
            return self.cursor.fetchone()[0]
        except:
            return None

    def set(self, caller: str, key: str, value: str):
        self.cursor.execute(
            "INSERT INTO cache (time, caller, hash, value) VALUES (datetime('now'), ?, ?, ?)", (caller, self._hash(key), value))
        self.conn.commit()


cache = Cache()
