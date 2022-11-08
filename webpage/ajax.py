from app import *
from sqlalchemy import *

@app.route("/ajax/update", methods=["GET"])
def get_update():
	"""
	Return the leaderboard and table. The table is such that the latest entry
	is first.
	"""

	# Update all team points.
	for team in Team.query.all():
		team.update_points()

	teams = {t.name:t.points for t in Team.query.all()}
	leaderboard = [[k,v] for k,v in sorted(teams.items(), key=lambda i:i[1])[::-1]]
	pwns = []

	for e in Entry.query.all():
		team = Team.query.get(e.team).name
		username = e.username.split("@")[0][:3] + "*"*8 + "@"+e.username.split("@")[1]
		password = e.password[:3]+"*"*8
		website = e.website
		pwns.append([team, username, password, website])

	return {
		"Leaderboard": leaderboard,
		"pwns": pwns[::-1]
	}, 200

