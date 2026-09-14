from flask import (
    Flask,
    redirect,
    render_template,
    request as req,
    session,
)
from werkzeug.security import check_password_hash, generate_password_hash

import config
import post
import user


app = Flask(__name__)
app.secret_key = config.secret


@app.route("/")
def index():
    if not session.get("username"):
        print("here")
        return redirect("/login")
    posts = post.get_n(4)
    return render_template("index.html", posts=posts)


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    username = req.form["username"]
    password1 = req.form["password1"]
    password2 = req.form["password2"]

    if password1 != password2:
        return "Passwords do not match."

    password_hash = generate_password_hash(password1)
    if user.add(username, password_hash):
        return "User created!"
    else:
        return "Username has been taken!"


@app.route("/login", methods=["GET", "POST"])
def login():
    if req.method == "GET":
        return render_template("login.html")
    username = req.form["username"]
    password = req.form["password"]

    password_hash = user.password_hash(username)
    if check_password_hash(password_hash, password):
        session["username"] = username
        return redirect("/")
    else:
        return "Incorrect username or password!"


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/posts/<int:post_id>")
def show_post(post_id: int):
    post_ = post.get_by_id(post_id)
    print(post_)
    return render_template("single_post.html", post=post_)


@app.route("/posts/create", methods=["GET", "POST"])
def create_post():
    if req.method == "GET":
        return render_template("new_challenge.html")
    poster_id = user.get_id(session["username"])
    title = req.form["title"]
    description = req.form["description"]
    post.add(poster_id, title, description)
    return redirect("/")


@app.route("/posts/delete/<int:post_id>")
def delete_post(post_id: int):
    post_ = post.get_by_id(post_id)
    if post_["username"] != session["username"]:
        return "Forbidden"
    post.delete(post_id)
    return redirect("/")


@app.route("/posts/modify/<int:post_id>")
def modify_post(post_id: int):
    post_ = post.get_by_id(post_id)
    if post_["username"] != session["username"]:
        return "Forbidden"
    return render_template("modify_post.html", post=post_)


@app.route("/posts/update/<int:post_id>", methods=["POST"])
def update_post(post_id: int):
    post_ = post.get_by_id(post_id)
    if post_["username"] != session["username"]:
        return "Forbidden"
    new_title = req.form["title"]
    new_description = req.form["description"]
    post.update(post_id, new_title, new_description)
    return redirect(f"/posts/{post_id}")


@app.route("/search")
def search_results():
    if not req.args:
        return render_template("search.html", posts=[])

    search_term = req.args["term"]
    results = post.search(search_term)
    return render_template("search.html", posts=results)

