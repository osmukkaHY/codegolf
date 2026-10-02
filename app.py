from flask import (
    abort,
    Flask,
    redirect,
    render_template,
    request as req,
    session,
)
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash

import config
import post
import user
import filter
import utils


app = Flask(__name__)
app.secret_key = config.secret


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("username"):
            abort(403)
        return f(*args, **kwargs)
    return wrapper


@app.get("/")
def index():
    if not session.get("username"):
        return redirect("/login")
    posts = post.get_n(4)
    return render_template("index.html", posts=posts)


@app.get("/signup")
def signup():
    if session.get("username"):
        abort(403)
    return render_template("signup.html")


@app.post("/create_user")
def create_user():
    username = req.form["username"]
    if (error := utils.validate_username(username)):
        return render_template("signup.html", alert=error)
    elif user.exists(username):
        return render_template("signup.html", alert="Username has been taken.")

    password1 = req.form["password1"]
    password2 = req.form["password2"]
    if (error := utils.validate_passwords(password1, password2)):
        return render_template("signup.html", alert=error)

    password_hash = generate_password_hash(password1)
    user.add(username, password_hash)
    return render_template("login.html", alert="User created!")


@app.get("/login")
def login_get():
    if session.get("username"):
        abort(403)
    return render_template("login.html")



@app.post("/login")
def login_post():
    username = req.form["username"]
    password = req.form["password"]

    password_hash = user.password_hash(username)
    if password_hash is None or not check_password_hash(password_hash, password):
        return render_template("login.html", alert="Incorrect Credidentials!")
    else:
        session["username"] = username
        return redirect("/")


@app.get("/logout")
def logout():
    if session.get("username"):
        del session["username"]
    return redirect("/")


@app.get("/posts/<int:post_id>")
@login_required
def show_post(post_id: int):
    post_ = post.get_by_id(post_id)
    print(post_)
    return render_template("single_post.html", post=post_)


@app.get("/posts/create")
@login_required
def posts_create():
    return render_template("new_challenge.html", languages=filter.languages(), categories=filter.categories())


@app.post("/posts/create")
@login_required
def create_post():
    poster_id = user.get_id(session["username"])
    title = req.form["title"]
    language_id = filter.get_language_id(req.form.get("language"))
    category_id = filter.get_category_id(req.form.get("category"))
    description = req.form["description"]
    post.add(poster_id, title, language_id, category_id, description)
    return redirect("/")


@app.get("/posts/delete/<int:post_id>")
@login_required
def delete_post(post_id: int):
    post_ = post.get_by_id(post_id)
    if post_["username"] != session["username"]:
        abort(403)
    post.delete(post_id)
    return redirect("/")


@app.get("/posts/modify/<int:post_id>")
@login_required
def modify_post(post_id: int):
    post_ = post.get_by_id(post_id)
    if post_["username"] != session["username"]:
        abort(403)
    return render_template("modify_post.html", post=post_)


@app.post("/posts/update/<int:post_id>")
@login_required
def update_post(post_id: int):
    post_ = post.get_by_id(post_id)
    if post_["username"] != session["username"]:
        abort(403)
    new_title = req.form["title"]
    new_description = req.form["description"]
    post.update(post_id, new_title, new_description)
    return redirect(f"/posts/{post_id}")


@app.get("/search")
@login_required
def search_results():
    results = []
    if req.args:
        search_term = req.args["term"]
        language_filter = req.args.get("language")
        category_filter = req.args.get("category")
        results = post.search(search_term, language_filter, category_filter)

    return render_template("search.html", languages=filter.languages(), categories=filter.categories(), posts=results)

