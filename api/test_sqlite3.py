import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "fantasy_data.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT league_name FROM league LIMIT 1;")
print(c.fetchone())
conn.close()