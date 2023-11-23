import sqlite3

conn = sqlite3.connect('books.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute('''
            INSERT INTO books (title, author, published_year)
            VALUES ('Harry Potter', 'J.K. Rowling', 2005);
            ''')

conn.commit()
conn.close()