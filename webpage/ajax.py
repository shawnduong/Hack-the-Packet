from app import *
from sqlalchemy import *

@app.route("/ajax/update", methods=["GET"])
def get_update():

	# Update all team points.
	for team in Team.query.all():
		team.update_points()

	teams = {t.name:t.points for t in Team.query.all()}
	leaderboard = [[k,v] for k,v in sorted(teams.items(), key=lambda i:i[1])[::-1]]

	return {
		"Leaderboard": leaderboard,
	}, 200

