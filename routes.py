from .models.database import session
from flask import render_template, request, redirect
from .models.article import Article
from .models.user import User
from . import app




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
            session.add(article)
            session.commit()
            return redirect("/articles")
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
        session.delete(article)
        session.commit()
        return redirect("/articles")
    except Exception as exc:
        return f"При видаленні виникла помилка: {exc}"

@app.route("/articles/<int:id>/update", methods=["POST", "GET"])
def article_update(id):
    article = Article.query.get(id)

    if request.method == "POST":
        article.title = request.form["title"]
        article.intro = request.form["intro"]
        article.text = request.form["text"]
        try:
            session.commit()
            return redirect("/articles")
        except Exception as exc:
            return f"При оновленні запису виникла помилка: {exc}"
    else:
        return render_template("post_update.html", article=article)

@app.route("/users")
def users():
    users_list = User.query.order_by(User.date.desc()).all()
    return render_template("user.html", users=users_list)

@app.route("/users/<int:id>")
def user_detail(id):
    user = User.query.get(id)
    return render_template("user_detail.html", user=user)

@app.route("/users/<int:id>/del")
def user_delete(id):
    user = User.query.get_or_404(id)

    try:
        session.delete(user)
        session.commit()
        return redirect("/users")
    except Exception as exc:
        return f"При видаленні виникла помилка: {exc}"

@app.route("/create-user", methods=["POST", "GET"])
def create_user():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        first_name = request.form["first_name"]

        user = User(
            username=username,
            password=password,
            first_name=first_name
        )

        try:
            session.add(user)
            session.commit()
            return redirect("/users")
        except Exception as exc:
            return f"При збереженні користувача виникла помилка: {exc}"
    else:
        return render_template("create_user.html")