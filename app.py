import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv(


)
app = Flask(__name__)


@app.route("/main")
def main_func():
    return "This is a main package!"

@app.route("/")
def index_func():
    return render_template("base.html")

@app.route("/birth")
def bir_func():
    return "30/10/2009"

@app.route("/pib")
def pib_func():
    return "Maksim Belosokhov Alexyovich"

@app.route("/hobbi")
def hobbi_func():
    return "Computer programming, Baskteball, walk with friends"




if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))