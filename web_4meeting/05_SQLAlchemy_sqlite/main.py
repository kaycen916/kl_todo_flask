from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
app.config['SQLALCHEMY_DATABASE_URI'] = 
        [DB_TYPE]+[DB_CONNECTOR]:
        //[USERNAME]:[PASSWORD]@[HOST]:
        [PORT]/[DB_NAME]
"""

db = SQLAlchemy()
app = Flask(__name__)

#使用 sqlite 資料庫連線
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
 
db.init_app(app)
 
@app.route('/create_db')
def index():
    db.create_all()
    return 'ok'
