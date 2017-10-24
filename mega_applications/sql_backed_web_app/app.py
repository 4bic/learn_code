from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

POSTGRES = {
    'user': '4bic',
    'pw': 'password',
    'db': 'height_collector',
    'host': 'localhost',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///height_collector'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://USER:PWD@HOST/DB_NAME'

db = SQLAlchemy(app)
class Data(db.Model):
    """docstring for Data."""
    __tablename__='height_data'
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        email=request.form["email_name"]
        height=request.form["height_name"]
        data = Data(email, height)
        # db.init_app(app)
        db.session.add(data)
        db.session.commit()
    return render_template("success.html")

if __name__ == '__main__':
    app.debug = True
    app.run() #default or set port no with port=5001
