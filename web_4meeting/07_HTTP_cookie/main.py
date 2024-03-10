from flask import Flask, make_response, request, Response
import time

app = Flask(__name__)

# 1. 設定cookie
@app.route("/set")
def setcookie():
    resp = make_response('Setting cookie!')   # make_response創建後可修改
    # key       : cookie的名稱
    # value     : cookie的值
    # expires   : cookie的有效日期，預設為退出瀏覽器時
    resp.set_cookie(key     ='framework', 
                    value   ='flask', 
                    expires =time.time()+6*60)
    return resp

# 2. 取得cookie
@app.route("/get")
def getcookie():
    framework = request.cookies.get('framework')
    # <span class="pl-k">return</span><span class="pl-s"><span class="pl-pds">'</span>The framework is <span class="pl-pds">'</span></span> <span class="pl-k">+</span> framework
    if framework is not None:
        return 'The framework is ' + framework
    else:
        return 'The framework cookie is not set.'

# 3. 刪除cookie
@app.route('/del')
def del_cookie():
    resp = Response('delete cookies')
    resp.set_cookie(key       ='framework',
                    value     ='',
                    expires   =0)
    return resp
