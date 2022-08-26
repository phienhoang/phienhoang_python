from flask import Blueprint,render_template, request, flash, redirect, url_for, session
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from math import e
from re import template
from sqlalchemy.sql.expression import false
from . import views
from flask_change_password import ChangePassword, ChangePasswordForm, SetPasswordForm


user = Blueprint("user",__name__)

@user.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                session.permanent = True
                login_user(user, remember=True)
                flash("Logged in success!", category="success")
                return redirect(url_for("views.home"))
            else:
                flash("Wrong password, please check again!", category="error")
    return render_template("login.html", user=current_user)

@user.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method=="POST":
        email = request.form.get("email")
        user_name = request.form.get("user_name")
        password= request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        user = User.query.filter_by(email=email).first()
        # validate user
        if user:
            flash("User existed!", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(password) < 7:
            flash("Password must be greater than 7 characters.", category="error")
        elif password != confirm_password:
            flash("Password doesn not match!", category="error")
        else:
            password = generate_password_hash(password, method="sha256")
            new_user = User(email,password,user_name)
            try:
                db.session.add(new_user)
                db.session.commit()
                login_user(user,remember=True)
                flash("User created!", category="success")
                return redirect(url_for("views.home"))
            except:
                "Error when create user!"
    return render_template("signup.html", user=current_user)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.login"))

@user.route('/infor')
def infor():
    return render_template("information.html", user=current_user)

# def send_mail():
#     pass

# @user.route("/reset_password", methods=["GET", "POST"])
# def reset_request():
#     form = ResetRequestForm()
#     if form.validate_on_submit():
#         user=User.query.filter_by(email=form.email.data).first()
#         if user:
#             send_mail()
#             flash('Reset rquest sent. Check your mail.', category="success")
#             return redirect(url_for('login'))
#     return  render_template('reset_request.html', title="Reset Request", form=form, legend="Reset Password")


# @user.route('/changepassword', methods=["GET", "POST"])
# def change_password():
#     if request.method == "POST":
#         new_password = request.form.get("newpassword")
#         confirm_new_password = request.form.get("confirm_newpassword")
#         if new_password == User.password():
#             flash("The password is the same as the previous password", category="error")
#         elif new_password != confirm_new_password:
#             flash("Password doesn not match!", category="error")
#         elif len(new_password) < 7:
#             flash("Password must be greater than 7 characters.", category="error")
#         else:
#             password = generate_password_hash(new_password, method="sha256")
#             user = User.query.filter_by(email=User.email).first()
#             user.set_password(f"{password}")
#             db.session.commit()
#             flash("Change password successfully!", category="success")
#             return redirect(url_for("user.infor"))
#     return render_template("changepassword.html", user=current_user)


