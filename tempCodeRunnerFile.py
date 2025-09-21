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