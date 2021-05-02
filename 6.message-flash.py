from flask import Flask, request, render_template, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__, template_folder="views")

# This is mandatory to work with strings, value can be anything

app.secret_key = "Hello"

# To save session for specific period
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        name = request.form["name"]
        session["name"] = name
        flash("You are logged in sucessfully !!")
        return redirect(url_for("user"))
    else:
        if "name" in session:
            flash("Already Loggedin !!!")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "name" in session:
        user = session['name']
        return render_template("user.html", user=user)
    else:
        flash("you are not logged in")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "name" in session:
        user = session['name']
        flash(f"you have been logged out {user}", "info")
    session.pop("name", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)