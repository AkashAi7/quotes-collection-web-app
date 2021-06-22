from flask import Flask , render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy
import os
import re


app=Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:qwerty9090@localhost/quotes'     #ye local db hai
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://yqlgavfmcfvqlg:442d12a3fae1a4b192766fd866ae8891eea4715d035e9aea7891f9471c09b0ac@ec2-54-158-232-223.compute-1.amazonaws.com:5432/d6hec5qfjr71nr'
# uri = os.getenv("SQLALCHEMY_DATABASE_URI")  # or other relevant config var
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
# this is like a event notification system toh isko off kar diya hai 
db = SQLAlchemy(app)


class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))



@app.route("/")
def index():
    result=Favquotes.query.all()
    return render_template('index.html',result=result)


@app.route("/quotes")
def quotes():
    return render_template('quotes.html')


@app.route("/process",methods=['POST'])   #here the default method is get but since we are using form then we can use POST
def process():
    author=request.form['author']
    quote =request.form['quote']  #ye dono na form se value access karenge 
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()


    return redirect(url_for('index'))