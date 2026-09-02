from flask import (
    Flask,
    render_template,
    request as req,
    session,
)
from werkzeug.security import generate_password_hash

import config
import user


app = Flask(__name__)
app.secret_key = config.secret


@app.route("/")
def index():
    return "Hello World!"


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
