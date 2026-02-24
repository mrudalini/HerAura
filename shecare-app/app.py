from flask import Flask, render_template, request, redirect, session, url_for
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.secret_key = "heraura_secret"

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form["name"]
        session["age"] = request.form["age"]
        session["last_period"] = request.form["last_period"]
        session["experience"] = request.form["experience"]
        return redirect("/calendar")
    return render_template("login.html")


@app.route("/calendar")
def calendar():
    last = datetime.strptime(session["last_period"], "%Y-%m-%d")
    next_period = last + timedelta(days=28)
    return render_template("calendar.html", next_date=next_period.strftime("%d %B %Y"))


@app.route("/routine")
def routine():
    return render_template("routine.html")


@app.route("/care")
def care():
    return render_template("care.html")


@app.route("/reflect", methods=["GET", "POST"])
def reflect():
    diary = session.get("diary", [])
    if request.method == "POST":
        diary.append(request.form["entry"])
        session["diary"] = diary
    return render_template("reflect.html", entries=diary)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        file = request.files["photo"]
        if file.filename:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)
            session["photo"] = path
    return render_template("profile.html", user=session)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
