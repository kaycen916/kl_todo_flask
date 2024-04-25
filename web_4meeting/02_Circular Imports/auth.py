from flask import Flask

# 當 app = Flask(__name__) 被準備好的時候，
# 把 app 透過 auth.init_app(app) 的方式啟動 auth.py 裡面的路徑
def init_app(app):
    @app.route('/auth')
    def auths():
        return 'auth'
