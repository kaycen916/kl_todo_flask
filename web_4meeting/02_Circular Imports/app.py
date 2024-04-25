from flask import Flask
import auth
 
app = Flask(__name__)
auth.init_app(app)
 
@app.route('/')
def index():
    return 'foo'


# 在development下，部署到server上通常是使用nginx + uwsgi方式，
# 而不再使用flask自帶的app.run啟動服務。如果沒有這個判斷，那麼在server上就會啟動兩個服務。