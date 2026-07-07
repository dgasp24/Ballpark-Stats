from apiLoader import getPlayerID, getTeamID, getPlayerStats
from plot import generatePlot
season = "1990"

teams = {}
player = []
batting_avg = []

playerData = getPlayerID(season)
teamData = getTeamID()

for team in teamData['teams']:
    if team['sport']['name'] == "Major League Baseball":
        teams[team['teamName'].lower()] = team['id']
    else:
        continue

while True:
    userTeam = input("Enter team: ")
    try:
        for players in playerData['people']:
                if players['currentTeam']['id'] == teams[userTeam.lower()] and (players['primaryPosition']['type'] == "Outfielder" or players['primaryPosition']['type'] == "Infielder"  or players['primaryPosition']['type'] == "Hitter"):
                    playerStats = getPlayerStats(players['id'], season)['stats'][0]['splits'][0]['stat']
                    stats = { "avg": playerStats['avg'], 'hr': playerStats['homeRuns']
                    }
                    print(f"ID: {players['id']}, {players['firstName']} {players['lastName']}")
                    print(f"Batting Average: {stats['avg']}, Home Runs: {stats['hr']}")
                    player.append(f"{players['lastName']}")
                    batting_avg.append(stats['avg'])
                else:
                    continue
    except:
        print("Error, failed to grab player data")
        continue
    print(player)
    print(batting_avg)
    userExit = input("Would you like to exit (y/n): ")
    if userExit == "y":
        break
    else:
        player.clear()
        batting_avg.clear()
        continue

generatePlot(player, batting_avg)




