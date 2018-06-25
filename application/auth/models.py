from application import db

from sqlalchemy.sql import text

class User(db.Model):
	__tablename__="account"

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

	name = db.Column(db.String(144), nullable=False)
	username = db.Column(db.String(144), nullable=False)
	password = db.Column(db.String(144), nullable=False)

	lists = db.relationship("Lists",cascade='all, delete-orphan', backref='account', lazy=True)
	admin = db.Column(db.Boolean, nullable=False)



	def __init__(self, name, username, password, admin):
		self.name=name
		self.username=username
		self.password=password
		self.admin=admin


	def get_id(self):
	        return self.id

	def is_active(self):
	        return True

	def is_anonymous(self):
	       	return False

	def is_authenticated(self):
	        return True

	def get_admin(self):
		return self.admin

	#yhteenvetokyselyt
	@staticmethod
	def users_with_waiting_jobs():
		stmt = 	text(	"SELECT DISTINCT Account.id, Account.name FROM Account, Lists, Jobs"
		              	" WHERE Account.id = Lists.account_id AND Lists.id = Jobs.list_id"
		                " AND Jobs.id NOT IN(SELECT Jobs.id FROM Jobs WHERE"
		                " Jobs.status=2 OR Jobs.status=3)")
		tulos=db.engine.execute(stmt)

		lista=[]
		for row in tulos:
			lista.append({"id":row[0], "nimi":row[1]})
		return lista


	@staticmethod
	def users_and_lists_count():
		stms = text (	"SELECT Account.id, Account.name, COUNT(*) FROM Account"
				" INNER JOIN Lists ON Account.id=Lists.account_id"
				"  GROUP BY Account.id ORDER BY COUNT(Lists.id) DESC" )

		tulos=db.engine.execute(stms)

		lista=[]
		for row in tulos:
			lista.append({"id":row[0], "nimi":row[1], "lists":row[2]})
		return lista


	@staticmethod
	def users_with_no_lists():
		smtu = text(	"SELECT DISTINCT Account.id, Account.name FROM Account WHERE NOT EXISTS("
				"SELECT DISTINCT Lists.account_id FROM Lists WHERE"
				" Account.id=Lists.account_id)" )
		tulos=db.engine.execute(smtu)

		lista=[]
		for row in tulos:
			lista.append({"id":row[0], "nimi":row[1]})
		return lista
