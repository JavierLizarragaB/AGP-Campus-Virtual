from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required

from app import app, Messages
from app.forms import LoginForm
from app.models import User


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", user=current_user)


# TODO: Add user registration.
# TODO: Add user sessions.
@app.route("/login",methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # NOTE: Remember to unpack form fields with form.field.data.
        user = User.objects(email=form.email.data).first()

        if user is None:
            print("[DEBUG]: User not found: {}".format(form.email.data))
            return redirect(url_for("login"))
        
        if not user.check_password(form.password.data):
            print("[DEBUG]: Invalid user credentials: {} {}".format(form.email.data, form.password.data))
            return redirect(url_for("login"))

        if login_user(user, remember=form.remember_me.data):
            print("[DEBUG]: Login from user: {} {}".format(user.email, user.first_name))
        return redirect("/index")
    
    return render_template("login.html", title="Iniciar sesión", form=form)

@login_required
@app.route("/logout")
def logout():
    logout_user()
    flash(Messages.FLASH_LOGOUT_USER)
    return redirect("/index")