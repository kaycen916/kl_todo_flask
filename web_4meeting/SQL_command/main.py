from flask_sqlalchemy import SQLAlchemy
from flask import Flask
 
db = SQLAlchemy()
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://account:password@IP:3306/db"
 
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

@app.cli.command("init_db")
def init_db_command():
    sql = """
        CREATE TABLE collection (
        id INT NOT NULL AUTO_INCREMENT,
        website CHAR(100) NOT NULL,
        title CHAR(100),
        description CHAR(100),
        artical_time CHAR(100),
        insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        PRIMARY KEY (ID)
        )
    """
    db.engine.execute(sql)
    print("Database initialized.")
