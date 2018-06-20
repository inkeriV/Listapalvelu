from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from application import app, db
from application.lists.models import Lists
from application.lists.forms import ListForm

from application.jobs.models import Jobs
from application.jobs.forms import JobForm


#listojen listaus
@app.route("/lists/", methods=["GET"])
@login_required
def lists_index():
	#näytä kaikki listat adminille
	if current_user.admin == 1:
		return render_template("lists/listaus.html", lists = Lists.query.all(), jobs = Jobs.query.all()) #kaikki työt
	#muuten vain käyttäjän omat listat
	return render_template("lists/listaus.html", lists = Lists.query.filter_by(account_id=current_user.id), jobs=Jobs.query.all())


@app.route("/lists/new/")
@login_required
def lists_form():
	return render_template("lists/new.html", form = ListForm())


#listan luonti
@app.route("/lists/", methods=["POST"])
@login_required
def lists_create():

	form = ListForm(request.form)

	if not form.validate():
		return render_template("lists/new.html", form = form)

	l = Lists(form.name.data, form.type.data)

	l.account_id = current_user.id
	#^ viitteen lisääminen. tässä oli db.account eikä l.account..tästä tuli virhe

	db.session().add(l)
	db.session().commit()

	return redirect(url_for("lists_index"))

#työn lisääminen
@app.route("/lists/job/<list_id>", methods=["POST"]) #tuli virhe list_id puuttuu: korjautu kun laitto urliin <list_id>
@login_required
def jobs_create(list_id):

	j = Jobs(name=request.form.get("name"), status="1")
	j.list_id=list_id

	db.session().add(j)
	db.session().commit()

	return redirect(url_for("lists_index"))

#työn lisääminen listan omalla sivulla
@app.route("/lists/<list_name>/<list_id>", methods=["POST"])
@login_required
def create_job(list_name, list_id):

	j = Jobs(name=request.form.get("name"), status="1")
	j.list_id=list_id

	db.session().add(j)
	db.session().commit()

	return redirect(url_for("show_list", list_id=list_id, list_name=list_name))


#listan poisto
@app.route("/lists/delete/<list_id>", methods=["GET","POST"])
@login_required
def lists_delete(list_id):
	#db.session.delete(Jobs.query.filter_by(list_id = list_id))
	#db.session().commit()
	db.session.delete(Lists.query.get(list_id))
	db.session().commit()
	return redirect(url_for("lists_index"))


#yhden listan sivut
@app.route("/lists/<list_name>/<list_id>", methods=["GET"])
@login_required
def show_list(list_id, list_name):
	#if list_id != Lists.query.get(list_id): #tänne myös jos lista on private + muut tyypit!
	#	flash("Listaa ei ole olemassa")
	#	return redirect(url_for("lists_index"))
	return render_template("lists/showlist.html", list=Lists.query.get(list_id), jobs=Jobs.query.filter_by(list_id=list_id))

#käyttöohjeiden tulostus
@app.route("/kayttoohje/", methods=["GET"])
def ohje():
	return render_template("/lists/kayttoohje.html")


#listan tyypin muuntaminen
@app.route("/lists/<list_name>/<list_id>/changetype", methods=["POST"])
@login_required
def type_change(list_name, list_id):
	#if request.method == 'POST':
		lista=Lists.sfsdfquery.get(list_id) #KORJAA VIRHE, testaan tuleeko metodi ikinä suoritukseen

		if lista.type == 1:
			lista.type = "2"
			db.session().commit()
			return redirect(url_for("show_list", list_id=list_id, list_name=list_name))

		if lista.type == 2:
			lista.type = "3"
			db.session().commit()
			return redirect(url_for("show_list", list_id=list_id, list_name=list_name))

		if lista.type == 3:
			lista.type = "1"
			db.session().commit()
			return redirect(url_for("show_list", list_id=list_id, list_name=list_name))

