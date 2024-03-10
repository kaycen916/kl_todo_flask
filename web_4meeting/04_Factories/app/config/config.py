# 建立物件可能會導致大量的重複代碼，可能會需要複合物件存取不到的資訊，也可能提供不了足夠級別的抽象，還可能並不是複合物件概念的一部分。
# 工廠方法模式: 定義一個單獨的建立物件的方法，當傳入不同參數時，會取得不同的實例。

import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir)

class BaseConfig:
    SECRET_KEY = 'THIS IS MAX'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)

class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 與資料庫連線的參數設定 -> 使用 MySQL 當連線的資料庫
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@ip:3306/tablename'

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}