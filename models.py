from posixpath import dirname
import sqlite3 as sql
from os import path
ROOT=path.dirname(path.relpath((__file__)))
def create_post(id,name,content):
    con=sql.connect(path.join(ROOT,'database.db'))
    cur=con.cursor()
    cur.execute('insert into posts (id,names,content) values(?,?,?)',(id,name,content))
    con.commit()
    con.close()
def get_posts():
    con=sql.connect(path.join(ROOT,'database.db'))
    cur=con.cursor()
    cur.execute('select * from posts')
    posts=cur.fetchall()
    return posts