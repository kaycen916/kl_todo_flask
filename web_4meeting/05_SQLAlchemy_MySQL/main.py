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

#使用 MySQL 資料庫連線
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://user_name:password@IP:3306/db_name"

db.init_app(app)
 
@app.route('/')
def index():
 
    sql_cmd = """
        select *
        from product
        """
 
    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    return 'ok'
