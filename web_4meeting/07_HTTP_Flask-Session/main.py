from flask import Flask, session
# from flask.ext.session import Session

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
app.config['SESSION_TYPE'] = 'redis'

# session(app) 新版本Flask會自動建立

# 在每個request前先執行
# @app.before_request
# def setup_session():
#     session.modified = True

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')