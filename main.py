from apiLoader import getPlayerID, getTeamID, getPlayerStats
from plot import generatePlot

teams = {}
player = []
hitting_stat = []
isInt = True

while True:
    userTeam = input("Enter team: ")
    year = int(input("Enter year: "))
    statChoice = int(input("1. Batting Average\n2. Homeruns\n"))
    playerData = getPlayerID(year)
    teamData = getTeamID()

    for team in teamData['teams']:
        if team['sport']['name'] == "Major League Baseball":
            teams[team['teamName'].lower()] = team['id']
        else:
            continue
    try:
        for players in playerData['people']:
                if (players['currentTeam']['id'] == teams[userTeam.lower()] and
                        (players['primaryPosition']['type'] == "Outfielder" or
                         players['primaryPosition']['type'] == "Infielder"  or
                         players['primaryPosition']['type'] == "Hitter")):

                    playerStats = getPlayerStats(players['id'], year)['stats'][0]['splits'][0]['stat']
                    stats = { "avg": playerStats['avg'], 'hr': playerStats['homeRuns']}
                    print(f"{players['firstName']} {players['lastName']}")
                    print(f"Batting Average: {stats['avg']}, Home Runs: {stats['hr']}")
                    player.append(f"{players['lastName']}")
                    if statChoice == 1:
                        hitting_stat.append(f"{stats['avg']}")
                        isInt = False
                    elif statChoice == 2:
                        hitting_stat.append(f"{stats['hr']}")
                        isInt = True
                else:
                    continue
    except:
        print("Error, failed to grab player data")
        continue

    userExit = input("Would you like to exit (y/n): ")
    graph = input("Would you want a chart? (y/n): ")
    if userExit == "y" and graph == "n":
        break
    elif userExit == "y" and graph == "y":
        generatePlot(player, hitting_stat, isInt)
        break
    elif userExit == "n" and graph == "y":
        generatePlot(player, hitting_stat, isInt)
        player.clear()
        hitting_stat.clear()
        continue
    elif userExit == "n" and graph == "n":
        player.clear()
        hitting_stat.clear()
        continue




