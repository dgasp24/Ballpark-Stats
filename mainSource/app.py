import time
import os
from flask import Flask, render_template, request, redirect, url_for
from mainFunctions import loadTeams, grabbingStatsforBar, grabbingStatsforScatter
from plot import generateBarGraph, generateScatterPlot

app = Flask(__name__)
team_lookup = loadTeams()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teams', methods = ['GET', 'POST'])
def teams():
    try:
        year = request.values.get('year')
        team = request.values.get('team')
        pa = request.values.get('PA')
        stat2 = request.values.get('statChoice2')
        stat = request.values.get('statChoice')

        if not team:
            return render_template('teams.html', teamId = None, playerStats = None, stat = None, stat2 = None)

        year = int(year)
        pa = int(pa) if pa else 0
        stat = int(stat) if stat else None
        teamId = team_lookup[team.lower()]

        if not stat2:
            Stat, isInt, playerStats = grabbingStatsforBar(stat, teamId, year, pa)
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
            return render_template('teams.html', playerStats=sortedStats, stat=stat, team=team.capitalize(), year=year,graph=graph)
        else:
            stat2 = int(stat2) if stat2 else None
            playerStats = grabbingStatsforScatter(teamId, year, pa)
            graph = generateScatterPlot(playerStats, stat - 1, stat2 - 1, team.capitalize(), year, pa, "")
            return render_template('teams.html', playerStats=playerStats, stat=stat, statChoice2 = stat2, team=team.capitalize(), year=year, graph=graph)
    except Exception as e:
        print(f"Error in /teams, {e}")
        return render_template('error.html')

@app.route('/mlb', methods = ['GET', 'POST'])
def mlb():
    try:
        year = request.values.get('year')
        pa = request.values.get('PA')
        stat = request.values.get('statChoice')
        stat2 = request.values.get('statChoice2')
        player = request.values.get('player')

        if not pa:
            return render_template('mlb.html', playerStats = None, stat = None, stat2 = None)

        year = int(year)
        pa = int(pa) if pa else 0
        stat = int(stat) if stat else None
        player = player.title()

        if not stat2:
            start = time.time()
            Stat, isInt, playerStats = grabbingStatsforBar(stat, "MLB", year, pa)
            print(f"API/fetch took {time.time() - start:.2f}s")

            if stat == 1:
                stat = "Batting Average"
            elif stat == 2:
                stat = "OPS"
            elif stat == 3:
                stat = "Homeruns"
            elif stat == 4:
                stat = "SLG"

            sortedStats = dict(sorted(playerStats.items(), key=lambda item: float(item[1]), reverse=True))
            start = time.time()
            graph = generateBarGraph(sortedStats, isInt, year, "MLB", stat, player, pa)
            print(f"Graph generation took {time.time() - start:.2f}s")
            return render_template('mlb.html', playerStats=sortedStats, stat=stat, team="MLB", year=year, graph=graph)
        else:
            stat2 = int(stat2) if stat2 else None
            playerStats = grabbingStatsforScatter("MLB", year, pa)

            graph = generateScatterPlot(playerStats, stat-1, stat2-1, "MLB", year, pa, player)

            return render_template('mlb.html', playerStats = playerStats, statChoice2 = stat2, stat = stat, team="MLB", year=year, graph=graph)
    except Exception as e:
        print(f"Error in /mlb, {e}")
        return render_template('error.html')

@app.route('/error')
def error():
    return render_template('styleError.css')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)