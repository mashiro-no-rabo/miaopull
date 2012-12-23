# coding=utf8

from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route("/welcome")
def hello():
    return u"｢喵噗兒｣"

if __name__ == "__main__":
    app.run(host="0.0.0.0")