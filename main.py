# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signinpage")
def signinpage():
    return render_template('signinpage.html')

if __name__ == '__main__':
    app.run(debug=True)
