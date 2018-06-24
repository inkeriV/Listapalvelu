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

	lists = db.relationship("Lists", backref='account', lazy=True)
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

	#yhteenvetokysely
	@staticmethod
	def users_with_no_started_jobs():
		stmt = 	text(	"SELECT DISTINCT Account.id FROM Account, Lists, Jobs" 
		              	" WHERE Account.id = Lists.account_id AND Lists.id = Jobs.list_id"
		                " AND Jobs.id NOT IN(SELECT Jobs.id FROM Jobs WHERE"
		                " Jobs.status=2 OR Jobs.status=3)")
		tulos=db.engine.execute(stmt)

		lista=[]
		for row in tulos:
			lista.append({"id":row[0]})
		return lista
