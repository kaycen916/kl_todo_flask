from flask import Flask, render_template

app = Flask(__name__)

@app.route('/calculator')
def calculator():
    return render_template('cal.html')