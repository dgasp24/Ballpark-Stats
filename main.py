from apiLoader import getPlayerID, getTeamID, getPlayerStats
from plot import generatePlot
import time

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
        start = time.time()
        for players in playerData['people']:
                if (players['currentTeam']['id'] == teams[userTeam.lower()] and
                        (players['primaryPosition']['type'] == "Outfielder" or
                         players['primaryPosition']['type'] == "Infielder"  or
                         players['primaryPosition']['type'] == "Hitter" or
                         players['primaryPosition']['type'] == "Catcher")):

                    playerStats = getPlayerStats(players['id'], year)['stats'][0]['splits'][0]['stat']
                    stats = { "avg": playerStats['avg'], 'hr': playerStats['homeRuns'],
                              'gp': playerStats['gamesPlayed'], 'pa': playerStats['plateAppearances'] }
                    print(f"{players['firstName']} {players['lastName']}\n"
                          f"Batting Average: {stats['avg']}, Home Runs: {stats['hr']}, "
                          f"Games Played: {stats['gp']}, PA: {stats['pa']} ")
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
    end = time.time()
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

print(f"Took {end - start:.3f} seconds")


