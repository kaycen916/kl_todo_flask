from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)

"""
1. 資料庫連線參數
"""
# MySQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db' 
# Postgres
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@server/db'
# SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////absolute/path/to/foo.db' #Windows

"""
2. 資料庫細節設定參數
"""
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_pre_ping": True,
    "pool_recycle": 300,
    'pool_timeout': 900,
    'pool_size': 10,
    'max_overflow': 5   #當 connection pool 連線都用光時，最多暫時額外再新增多少的連線數
}

"""
3. 用於 debug 的參數
"""
#app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True


 
db = SQLAlchemy(app)
 
@app.route('/')
def demo():
    return 'Hello Flask'