import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)

load_dotenv()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.id}"






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


@app.route("/create-article", methods=["POST", "GET"])
def create_article():
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        text = request.form["text"]

        article = Article(
            title=title,
            intro=intro,
            text=text
        )

        try:
            db.session.add(article)
            db.session.commit()
            return redirect("/")
        except Exception as exc:
            return f"При збереженні виникла помилка: {exc}"
    else:
        return render_template("create_article.html")


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))