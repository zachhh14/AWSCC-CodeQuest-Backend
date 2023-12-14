import sqlite3

conn = sqlite3.connect('accounts.db')

with open("schema.sql") as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute('''
            INSERT INTO accounts (website, email, password) 
            VALUES ('youtube', 'zachary', 'tecson');
            ''')

conn.commit()
conn.close()