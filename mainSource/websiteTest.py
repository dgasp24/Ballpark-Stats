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
    stat = request.args.get('statChoice')

    if not team:
        return render_template('teams.html', teamId = None, playerStats = None, stat = None)

    year = int(year)
    pa = int(pa) if pa else 0
    stat = int(stat) if stat else None
    teamId = team_lookup[team.lower()]

    print(teamId)
    Stat, isInt, playerStats = grabbingStatsforBar(stat, teamId, year, pa)
    print(playerStats)

    if stat == 1:
        stat = "Batting Average"
    elif stat == 2:
        stat = "OPS"
    elif stat == 3:
        stat = "Homeruns"
    elif stat == 4:
        stat = "SLG"

    return render_template('teams.html', playerStats = playerStats, stat = stat, team=team.capitalize(), year=year)

@app.route('/mlb')
def mlb():
    year = request.args.get('year')
    pa = request.args.get('PA')
    stat = request.args.get('statChoice')

    if not pa:
        return render_template('mlb.html', playerStats = None, stat = None)

    year = int(year)
    pa = int(pa) if pa else 0
    stat = int(stat) if stat else None

    Stat, isInt, playerStats = grabbingStatsforBar(stat, "MLB", year, pa)


    if stat == 1:
        stat = "Batting Average"
    elif stat == 2:
        stat = "OPS"
    elif stat == 3:
        stat = "Homeruns"
    elif stat == 4:
        stat = "SLG"

    return render_template('mlb.html', playerStats = playerStats, stat = stat, team="MLB", year=year)


app.run(host='0.0.0.0', port=5000, debug = True)