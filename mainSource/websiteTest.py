from flask import Flask, render_template, request, redirect, url_for
from mainFunctions import loadTeams, grabbingStatsforBar
from plot import generateBarGraph

app = Flask(__name__)
team_lookup = loadTeams()
@app.route('/')
def index():
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

    sortedStats = dict(sorted(playerStats.items(), key=lambda item: float(item[1]), reverse=True))
    graph = generateBarGraph(sortedStats, isInt, year, team.capitalize(), stat, "", pa)

    return render_template('teams.html', playerStats = sortedStats, stat = stat, team=team.capitalize(), year=year, graph=graph)

@app.route('/mlb')
def mlb():
    year = request.args.get('year')
    pa = request.args.get('PA')
    stat = request.args.get('statChoice')
    player = request.args.get('player')

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

    sortedStats = dict(sorted(playerStats.items(), key=lambda item: float(item[1]), reverse=True))
    graph = generateBarGraph(sortedStats, isInt, year, "MLB", stat, player, pa)


    return render_template('mlb.html', playerStats = sortedStats, stat = stat, team="MLB", year=year, graph=graph)


app.run(host='0.0.0.0', port=5000, debug = True)