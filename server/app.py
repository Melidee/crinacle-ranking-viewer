from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"<p>hello index</p>"

@app.route("/people/<name>")
def people_name(name):
    return f"<p>hello {name}</p>"