from flask import render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
	if request.method == "GET":
		return render_template("auth/loginform.html", form = LoginForm())

	form = LoginForm(request.form)

	user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
	if not user:
		return render_template("auth/loginform.html", form = form, error = "Käyttäjänimi tai salasana väärin.")

	login_user(user)
	return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
	logout_user()
	flash("Olet kirjautunut ulos.")
	return redirect(url_for("index"))


#rekisteröityminen
@app.route("/register", methods = ["GET", "POST"])
def register():
	form = RegisterForm(request.form)

	if not form.validate(): #class Meta formiin, jotta toimii
		return render_template("auth/registerform.html", form=form)

	if request.method == "POST":

		user = User(name=form.name.data, username=form.username.data, password=form.password.data, admin=0)
		db.session().add(user)
		db.session().commit()

		flash("Rekisteröityminen onnistui. Voit nyt kirjautua sisään.")

		return redirect(url_for("index"))

