import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from model import Article

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)





@app.route("/main")
def main_func():
    return "This is a main package!"

@app.route("/")
def index_func():
    return render_template("base.html", title="Title test")


@app.route("/birth")
def bir_func():
    return "30/10/2009"


@app.route("/pib")
def pib_func():
    return "Maksim Belosokhov Alexyovich"


@app.route("/hobbi")
def hobbi_func():
    return "Computer programming, Basketball, walk with friends"





if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))