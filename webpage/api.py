from app import *

@app.route("/api/team/create", methods=["POST"])
def create_team():
	"""
	Make a team.
	"""

	try:
		team = Team(request.json["name"], 0)
		db.session.add(team)
		db.session.commit()
		return {"Status": "Successfully created team."}, 200
	except Exception as e:
		print(e)
		return {"Status": "Failed."}, 500

@app.route("/api/update", methods=["POST"])
def update():
	"""
	Some team has found a username:password.
	"""

	pass

