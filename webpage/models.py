from app import db

class Team(db.Model):

	__tablename__ = "team"

	id = db.Column(db.Integer, primary_key=True)
	name   = db.Column(db.String(256), unique=True , nullable=False)
	points = db.Column(db.Integer    , unique=False, nullable=False)

	def __init__(self, name=None, points=None):

		self.name = name
		self.points = 0

	def update_points(self):

		self.points = 0

		for entry in Entry.query.filter_by(team=self.id):
			self.points += 25  # Points value per entry is 25.

class Entry(db.Model):

	__tablename__ = "entry"

	id = db.Column(db.Integer, primary_key=True)
	team     = db.Column(db.Integer, db.ForeignKey(Team.id), unique=False, nullable=False)
	username = db.Column(db.String(256), unique=False, nullable=False)
	password = db.Column(db.String(256), unique=False, nullable=False)
	website  = db.Column(db.String(256), unique=False, nullable=False)

	def __init__(self, team=None, username=None, password=None, website=None):

		self.team     = team
		self.username = username
		self.password = password
		self.website  = website

