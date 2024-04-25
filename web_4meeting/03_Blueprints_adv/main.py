from flask import Flask, Blueprint
from view.api import app2
 
app = Flask(__name__)
 
@app.route('/')
def index():
        return "Hello index"

app.register_blueprint(app2, url_prefix='/pages')    # 註冊新app, http://127.0.0.1:5000/pages/app2

# 指定新註冊的 app2 使用的 static 位置
app2 = Blueprint('app2', __name__, static_folder='static')
# 指定新註冊的 app2 使用的 template 位置
app2 = Blueprint('app2', __name__, template_folder='templates')