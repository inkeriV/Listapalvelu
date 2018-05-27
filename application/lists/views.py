from application import app, db
from flask import redirect, render_template, request, url_for
from application.lists.models import Lists

@app.route("/lists", methods=["GET"])
def lists_index():
	return render_template("lists/listaus.html", lists =Lists.query.all())

@app.route("/lists/new/")
def lists_form():
	return render_template("lists/new.html")

@app.route("/lists/", methods=["POST"])
def lists_create():
	l = Lists(request.form.get("name"))

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("lists_index"))
