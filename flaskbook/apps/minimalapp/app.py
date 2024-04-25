from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, flaskbook!!!"

# @app.route("/hello")
# def hello():
#     return "Hello, world!"

@app.route("/hello",                # Rule
    methods=["GET"],                # Methods
    endpoint="hello-endpoint")      # Endpoint
def hello():
    return "Hello, world!"

# @app.route("/hello",
#     methods=["GET", "POST"])
# def hello():
#     return "Hello, world!"

# @app.route("/hello/<huiii>",
#     methods=["GET", "POST"],
#     endpoint="hello-endpoint")
# def hello(huiii):
#     return f"Hello, {huiii}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/huiii?page=1
    print(url_for("show_name", name="huiii", page="1"))

@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method =="POST":
        # 傳送郵件

        # 重新導向 contact 端點
        return redirect(url_for("contact_complete"))
    
    return render_template("contact_complete.html")

if __name__ == "__main__":
    # from gevent import pywsgi
    # server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    # server.serve_forever()

    # from waitress import serve
    # serve(app, host="127.0.0.1", port=5000)
    app.run()