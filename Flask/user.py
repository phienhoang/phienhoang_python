from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask.helpers import flash
from flask import Blueprint


user = Blueprint("user", __name__)

@user.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name:
            session["user"] = user_name
            found_user = User.query.filter_by(name = user_name).first()
            if found_user:
                session["email"] = found_user.email
            else:
                user = User(user_name, "temp@gmail.com")
                db.session.add(user)
                db.session.commit()
                flash("Created in DB!")
            flash ("You logged in successfully!","info")
            return redirect(url_for("user", user=user_name))
    if "user" in session:
        name = session["user"]
        flash("You have already logged in!", "info")
        return redirect(url_for("user", user=name))
    return render_template('login.html')

@user.route('/user', methods = ["POST","GET"])
def user():
    email = None
    if "user" in session:
        name = session["user"]
        if request.method == "POST":
            if not request.form["email"] and request.form["name"]:
                User.query.filter_by(name=name).delete()
                db.session.commit()
                flash("Deleted user!")
                return redirect(url_for("log_out"))
            else:
                email = request.form["email"]
                session["email"] = email
                found_user = User.query.filter_by(name = name).first()
                found_user.email = email
                db.session.commit()
                flash("Email updated!")
        elif "email" in session:
            email = session["email"]
        return render_template("information.html", user=name, email = email)
    else:
        flash("You haven't logged in!", "info")
        return redirect(url_for("login"))

@user.route("/logout")
def log_out():
    flash("You logged out!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))
