from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:891624@localhost:3306/db"

db = SQLAlchemy(app)
Migrate(app, db)

class Product(db.Model):
    __tablename__ = 'product'
    pid         = db.Column(db.Integer, 
                            primary_key=True)
    name        = db.Column(db.String(30), 
                            unique=True, 
                            nullable=False)
    price       = db.Column(db.Integer, 
                            nullable=False)
    img         = db.Column(db.String(100), 
                            unique=True, 
                            nullable=False)
    description = db.Column(db.String(255), 
                            nullable=False)
    state       = db.Column(db.String(10), 
                            nullable=False)
    insert_time = db.Column(db.DateTime, 
                            default=datetime.now)
    update_time = db.Column(db.DateTime, 
                            onupdate=datetime.now, 
                            default=datetime.now)

    # 一對多, 設定 db.relationship, 讓 SQLAlchemy 知道 Product 和 AddToCar 有關聯
    # backref, 爾後在讀取 AddToCar 表格時，後面只需像這樣加上 AddToCar.product
    db_product_addtocar = db.relationship("AddToCar", backref="product")

    def __init__(self, name, price, img, description, state):
        self.name        = name
        self.price       = price
        self.img         = img
        self.description = description
        self.state       = state

class User(db.Model):
    __tablename__ = 'user'
    uid           = db.Column(db.Integer, 
                              primary_key=True)
    name          = db.Column(db.String(30), 
                              unique=True, 
                              nullable=False)
    password      = db.Column(db.String(255), 
                              nullable=False)
    role          = db.Column(db.String(10), 
                              nullable=False)
    insert_time   = db.Column(db.DateTime, 
                              default=datetime.now, 
                              nullable=False)
    update_time   = db.Column(db.DateTime, 
                              onupdate=datetime.now, 
                              default=datetime.now, 
                              nullable=False)

    # 一對多, 設定 db.relationship, 讓 SQLAlchemy 知道 User 和 AddToCar 有關聯
    # backref, 爾後在讀取 AddToCar 表格時，後面只需像這樣加上 AddToCar.user
    db_user_atc = db.relationship("AddToCar", backref="user")
 
    def __init__(self, name, password, role):
        self.name = name
        self.password = password
        self.role = role

class AddToCar(db.Model):
    __tablename__ = 'addtocar'
    id            = db.Column(db.Integer, 
                              primary_key=True)
    quantity      = db.Column(db.Integer, 
                              nullable=False)
    state         = db.Column(db.String(5),
                              nullable=False)
    insert_time   = db.Column(db.DateTime, 
                              default=datetime.now, 
                              nullable=False)
    update_time   = db.Column(db.DateTime, 
                              onupdate=datetime.now, 
                              default=datetime.now, 
                              nullable=False)

    # "多"需要設定db.ForeignKey() 告訴 SQLAlchemy 當兩張表格連結時要以什麼為外接的 key
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey('product.pid'), nullable=False)
 
    def __init__(self, uid, pid, quantity, state):
        self.uid = uid
        self.pid = pid
        self.quantity = quantity
        self.state = state

def create_data():
    
    # 新增單筆資料
    # product_max = Product('Max', 8888,'https://picsum.photos/id/1047/1200/600', '', '')
    # db.session.add(product_max)
    # db.session.commit()

    # 新增多筆資料
    p1 = Product('Isacc', 8888, 'https://picsum.photos/id/1047/1200/600', '', 'Y')
    p2 = Product('Dennis', 9999,'https://picsum.photos/id/1049/1200/600', '', 'Y')
    p3 = Product('Joey', 7777, 'https://picsum.photos/id/1033/1200/600', '', 'Y')
    p4 = Product('Fergus', 6666,'https://picsum.photos/id/1041/1200/600', '', '')
    p5 = Product('Max', 5555, 'https://picsum.photos/id/1070/1200/600', '', '')
    p6 = Product('Jerry', 4444, 'https://picsum.photos/id/1044/1200/600', '', '')
    p = [p1, p2, p3, p4, p5, p6]

    db.session.add_all(p)

    # 新增使用者
    u1 = User('Max', '123456', 'Admin')
    db.session.add(u1)

    # 新增購物車
    atc1 = AddToCar(1, 1, 5, 'Y')
    
    db.session.add_all([atc1])


    db.session.commit()

# def data_op():
    # query = Product.query.filter_by(name='Isacc').first()
    # print(f"Product: {query.name:<10} Number: {query.number}\n")
    # """
    # 用動態參數傳入
    # filters = {'name': 'Max', 'price': 5555}
    # query = Product.query.filter_by(**filters).first()
    # """

    # 以價格降冪排序後印出
    # orders = Product.query.order_by(Product.number.desc()).all()
    # for product in orders:
    #     print(f"Product: {product.name:<10} Number: {product.number}")

    # print("*"*32)

    # 刪除排序後的最後一筆
    # if orders:
    #     last_product = orders.pop()
    #     db.session.delete(last_product)
    #     db.session.commit()

    # for Product in orders:
    #     print(f"USERS: {product.name:<10} Number: {product.number}")

@app.route('/')
def index():
    # Create database and table
    db.create_all()
    create_data()

    return 'ok'