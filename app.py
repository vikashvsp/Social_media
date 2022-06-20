from crypt import methods
import sqlite3
from flask import CORS
from flask import Flask,render_template,request

from models import get_posts 
connection = sqlite3.connect("database.db")
cur = connection.cursor()
with open('schema.sql') as fp:
    cur.executescript(fp.read())
connection.commit()

app=Flask(__name__)
CORS(app)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        pass
    if request.method=='POST':
        name=request.form.get('name')
        post=request.form.get('post')
        create_post(name,post)
    posts=get_posts()

    return render_template('index.html',posts=posts )