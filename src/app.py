# !/bin/python3

from flask import Flask, render_template
from views.upload import upload

app = Flask(__name__)

app.register_blueprint(upload, url_prefix='/upload')


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
