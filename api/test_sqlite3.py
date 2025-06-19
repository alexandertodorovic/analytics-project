import sqlite3
conn = sqlite3.connect("fantasy_data.db")
c = conn.cursor()
c.execute("SELECT league_name FROM league LIMIT 1;")
print(c.fetchone())
conn.close()