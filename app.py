from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
app.secret_key = "sovneotyhcdobneiwtfhrsdf"

client = MongoClient("mongodb://localhost:27017/")
db = client["NMIMS_GDG"]
users = db["users"]
notes = db["notes"]

@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("base.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users.find_one({"username": username}):
            return "❌ Username already exists."

        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        users.insert_one({"username": username, "password": hashed})
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = users.find_one({"username": username})
        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            session["user_id"] = str(user["_id"])
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))
        return "❌ Invalid credentials."

    return render_template("login.html")  

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
