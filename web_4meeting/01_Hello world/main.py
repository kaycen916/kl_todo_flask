from flask import Flask

# __name__ 定位目前載入資料夾的位置(template_folder / static_folder)
app = Flask(__name__)

# @app.route('/'), decorator, 讓 Flask 監聽此 URL, 並 return 結果
@app.route('/')
def hello_world():
    return 'Hello, world!'
