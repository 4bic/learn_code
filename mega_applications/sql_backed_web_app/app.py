from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI']='postgresql://4bic:@localhost/heigh_collector'
db = SQLAlchemy(app)

class Data(object):
    """docstring for Data."""
    def __init__(self, arg):
        super(Data, self).__init__()
        self.arg = arg


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email=request.form["email_name"]
        height=request.form["height_name"]
    return render_template("success.html")

if __name__ == '__main__':
    app.debug = True
    app.run() #default or port=5001
