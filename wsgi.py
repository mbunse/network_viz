from flask import Flask, render_template, Blueprint
from flask_restplus import Resource, Api, Namespace

from apis import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
