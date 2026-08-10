from flask import Flask, render_template, request, redirect, url_for
from mainFunctions import loadTeams, grabbingStatsforBar
app = Flask(__name__)
team_lookup = loadTeams()
@app.route('/')
def index():
    stat = request.args.get('stat')
    if stat == "team":
        return redirect(url_for('teams', **request.args))
    return render_template('index.html')

@app.route('/teams')
def teams():
    year = request.args.get('year')
    team = request.args.get('team')
    pa = request.args.get('PA')

    if not team:
        return render_template('teams.html', teamId = None, error = None)

    year = int(year)
    pa= int(pa)

    teamId = team_lookup[team.lower()]

    print(teamId)
    grabbingStatsforBar(2, teamId, year, pa)

    return render_template('teams.html')


app.run(host='0.0.0.0', port=5000, debug = True)