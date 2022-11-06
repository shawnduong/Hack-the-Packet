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

@app.route("/api/entry/create", methods=["POST"])
def create_entry():
	"""
	Some team has found a username:password.
	"""

	try:
		team = Team.query.filter_by(name=request.json["team"]).first()
		assert team is not None
		assert Entry.query.filter_by(
			team=team.id, username=request.json["username"],
			password=request.json["password"], website=request.json["website"]
		).first() is None
		entry = Entry(team.id, request.json["username"], request.json["password"], request.json["website"])
		db.session.add(entry)
		db.session.commit()
		return {"Status": "Successfully added entry."}, 200
	except Exception as e:
		print(e)
		return {"Status": "Failed."}, 500

