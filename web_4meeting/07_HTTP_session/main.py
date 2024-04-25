from flask import Flask, session
from datetime import timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) # return一個24bit的string, 用於加密
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

@app.route('/')
def index():
    # 設置session
    session['username'] = 'name'
    session.permanent = True # 過期時間為31天
    # 讀取session
    session.get('username')
    # 刪除session
    session['username'] = False