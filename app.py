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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.id}"





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

@app.route("/articles")
def articles():
    articles_list = Article.query.order_by(Article.date.desc()).all()
    return render_template("articles.html", articles=articles_list)

@app.route("/articles/<int:id>")
def article_detail(id):
    article = Article.query.get(id)
    return render_template("article_detail.html", article=article)

@app.route("/articles/<int:id>/del")
def article_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect("/articles")
    except Exception as exc:
        return f"При видаленні виникла помилка: {exc}"


@app.route("/articles/<int:id>/update", methods=["POST", "GET"])
def article_update(id):
    article = Article.query.get(id)

    if request.method == "POST":
        article.title = request.form["title"]
        article.intro = request.form["intro"]
        article.text= request.form["text"]
        try:
            db.session.commit()
            return redirect("/articles")
        except Exception as exc:
            return f"При оновленні запису виникла помилка: {exc}"
    else:
        return render_template("post_update.html", article=article)



@app.route("/users")
def users():
    users_list = User.query.order_by(User.date.desc()).all()
    return render_template("user.html", user=users_list)

@app.route("/users/<int:id>")
def user_detail(id):
    user = User.query.get(id)
    return render_template("user_detail.html", user=user)

@app.route("/users/<int:id>/del")
def user_delete(id):
    user = User.query.get_or_404(id)

    try:
        db.session.delete(user)
        db.session.commit()
        return redirect("/users")
    except Exception as exc:
        return f"При видаленні виникла помилка: {exc}"


@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    if request.method == "POST":
        # Отримання даних з форми
        title = request.form["title"]
        intro = request.form["intro"]
        text = request.form["text"]

        # Створення нового об'єкта користувача
        user = Article(
            title=title,
            intro=intro,
            text=text
        )

        try:
            # Збереження користувача в базу даних
            db.session.add(user)
            db.session.commit()
            return redirect("/users")
        except Exception as exc:
            return f"При збереженні користувача виникла помилка: {exc}"
    else:
        return render_template("create_user.html")


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))