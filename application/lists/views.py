from flask import render_template, request, redirect, url_for

from application import app, db
from application.lists.models import Lists
from application.lists.forms import ListForm

@app.route("/lists", methods=["GET"])
def lists_index():
	return render_template("lists/listaus.html", lists =Lists.query.all())

@app.route("/lists/new/")
def lists_form():
	return render_template("lists/new.html", form = ListForm())

@app.route("/lists/", methods=["POST"])
def lists_create():

	form = ListForm(request.form)

	if not form.validate():
		return render_template("lists/new.html", form = form)

	l = Lists(form.name.data)

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("lists_index"))
