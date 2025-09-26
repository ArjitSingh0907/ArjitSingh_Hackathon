import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Connect to database
db = SQL("sqlite:///a.db")

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return "Error: must provide username", 403
        elif not request.form.get("password"):
            return "Error: must provide password", 403

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return "Error: invalid username or password", 403

        session["user_id"] = rows[0]["id"]
        return redirect("/homepage")

    return render_template("login.html")

@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("logout.html")

@app.route("/homepage", methods=["GET", "POST"])
def homepage():
    return render_template("homepage.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return "Error: set your username", 400
        elif not request.form.get("password"):
            return "Error: set your password", 400
        elif not request.form.get("confirmation"):
            return "Error: confirm your password", 400
        elif request.form.get("password") != request.form.get("confirmation"):
            return "Error: passwords are not the same", 400

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 0:
            return "Error: username already exists", 400

        db.execute(
            "INSERT INTO users (username, mobile, email, hash) VALUES (?, ?, ?, ?)",
            request.form.get("username"),
            request.form.get("mobile"),
            request.form.get("email"),
            generate_password_hash(request.form.get("password"))
        )

        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        return redirect("/homepage")

    return render_template("register.html")

@app.route("/movies")
def movies():
    return render_template("movies.html")


@app.route("/songs")
def songs():
    return render_template("songs.html")


@app.route("/adventure")
def adventure():
    return render_template("adventure.html")


@app.route("/wildlife")
def wildlife():
    return render_template("wildlife.html")


@app.route("/books")
def books():
    return render_template("books.html")


@app.route("/sci", methods=["GET", "POST"])
def sci():
    return render_template("sci.html")


@app.route("/comedy", methods=["GET", "POST"])
def comedy():
    return render_template("comedy.html")


@app.route("/horror", methods=["GET", "POST"])
def horror():
    return render_template("horror.html")


@app.route("/superhero", methods=["GET", "POST"])
def superhero():
    return render_template("superhero.html")


@app.route("/discovery", methods=["GET", "POST"])
def discovery():
    return render_template("discovery.html")


@app.route("/hbo", methods=["GET", "POST"])
def hbo():
    return render_template("hbo.html")


@app.route("/sportplaces", methods=["GET", "POST"])
def sportplaces():
    return render_template("sportplaces.html")


@app.route("/sportact", methods=["GET", "POST"])
def sportact():
    return render_template("sportact.html")


@app.route("/pacemaker", methods=["GET", "POST"])
def pacemaker():
    return render_template("pacemaker.html")


@app.route("/bedtime", methods=["GET", "POST"])
def bedtime():
    return render_template("bedtime.html")


@app.route("/supernatural", methods=["GET", "POST"])
def supernatural():
    return render_template("supernatural.html")


@app.route("/trip", methods=["GET", "POST"])
def trip():
    return render_template("trip.html")


@app.route("/love", methods=["GET", "POST"])
def love():
    return render_template("love.html")


@app.route("/party", methods=["GET", "POST"])
def party():
    return render_template("party.html")


@app.route("/english", methods=["GET", "POST"])
def english():
    return render_template("english.html")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        issue = request.form.get("issue")
        solution = request.form.get("solution")

        # Optional: Save to database or log it
        # db.execute("INSERT INTO feedback (...) VALUES (?, ?, ?, ?)", ...)

        return redirect("/feed_confirm")
    return render_template("feedback.html")

@app.route("/feed_confirm", methods=["GET", "POST"])
def feed_confirm():
    return render_template("feed_confirm.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template("profile.html")

@app.route("/home2", methods=["GET", "POST"])
def home2():
    return render_template("home2.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    return render_template("test.html")

@app.route("/language", methods=["GET", "POST"])
def language():
    return render_template("language.html")

@app.route("/easy", methods=["GET", "POST"])
def easy():
    return render_template("easy.html")

@app.route("/medium", methods=["GET", "POST"])
def medium():
    return render_template("medium.html")

@app.route("/hard", methods=["GET", "POST"])
def hard():
    return render_template("hard.html")

@app.route("/jobs", methods=["GET", "POST"])
def jobs():
    return render_template("jobs.html")

@app.route("/codelingo", methods=["GET", "POST"])
def codelingo():
    return render_template("codelingo.html")

@app.route("/interview", methods=["GET", "POST"])
def interview():
    return render_template("interview.html")

@app.route("/certificate", methods=["GET", "POST"])
def certificate():
    return render_template("certificate.html")
