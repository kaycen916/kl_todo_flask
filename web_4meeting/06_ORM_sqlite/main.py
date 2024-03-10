import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate
 
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
 
# datebase
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)

class Users():
    pass

class Users(db.Model):
    __tablename__ = 'users'
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.Text)
    age     = db.Column(db.Integer)
    mobile  = db.Column(db.Text)

    def __init__(self, name, age, mobile):
        self.name      = name
        self.age       = age
        self.mobile    = mobile
    def __repr__(self):
        return f'使用者名稱為 {self.name} ，年齡為 {self.age} 歲。'

db.drop_all()
db.create_all()

# 建立Python物件
kaycen = Users('Kaycen', 25, '88888888')
# 將物件加入session
db.session.add(kaycen)
# commit物件
db.session.commit()

Migrate(app, db)
