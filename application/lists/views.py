from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.lists.models import Lists
from application.lists.forms import ListForm

@app.route("/lists", methods=["GET"])
#ennen ei login_required, mutta nyt uloskirjautumisen jälkeen sovellus kaatuu kaikkien listojen näyttöön 
#@login_required
def lists_index():
	return render_template("lists/listaus.html", lists =Lists.query.all())

@app.route("/lists/new/")
@login_required
def lists_form():
	return render_template("lists/new.html", form = ListForm())



@app.route("/lists", methods=["POST"]) #ennen /lists/
@login_required
def lists_create():

	form = ListForm(request.form)

	if not form.validate():
		return render_template("lists/new.html", form = form)

	l = Lists(form.name.data)
	#viitteen lisääminen. tässä oli db.account eikä l.account..tästä tuli virhe
	l.account_id=current_user.id

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("lists_index"))
