import sqlite3
connection = sqlite3.connect("database.db")
cur = connection.cursor()
with open('schema.sql') as fp:
    cur.executescript(fp.read())
connection.commit()