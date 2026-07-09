from apiLoader import getPlayerID, getTeamID, getPlayerStats, newMlbRosterData
from plot import generatePlot
import time

teams = {}
playerStats = {}
positions = {"Outfielder", "Infielder", "Hitter", "Catcher"}
isInt = True

def loadTeams():
    teamData = getTeamID()
    for team in teamData['teams']:
        if team['sport']['name'] == "Major League Baseball":
            teams[team['teamName'].lower()] = team['id']
        else:
            continue

loadTeams()
while True:
    userTeam = input("Enter team: ")
    year = int(input("Enter year: "))
    statChoice = int(input("What would you like to have the chart show?\n1. Batting Average\n2. Homeruns\n"))
    teamData = getTeamID()

    mlbData = newMlbRosterData(teams[userTeam.lower()], year)
    start = time.time()
    for players in mlbData['roster']:
        if players['person']['primaryPosition']['type'] in positions:

            if 'stats' not in players['person'] or not players['person']['stats']:
                continue

            splits = players['person']['stats'][0]['splits']
            if not splits:
                continue

            rawStat = players['person']['stats'][0]['splits'][0]['stat']

            stats = {"avg": rawStat['avg'], 'hr': rawStat['homeRuns'],
                     'gp': rawStat['gamesPlayed'], 'pa': rawStat['plateAppearances']}

            print(f"{players['person']['fullName']}\n"
                  f"Batting Average: {stats['avg']}, Home Runs: {stats['hr']}, "
                  f"Games Played: {stats['gp']}, PA: {stats['pa']}")

            name = players['person']['lastName']

            if statChoice == 1:
                playerStats[name] = stats['avg']
                isInt = False
            elif statChoice == 2:
                playerStats[name] = stats['hr']
                isInt = True
        else:
            continue
    end = time.time()
    userExit = input("Would you like to exit (y/n): ")
    graph = input("Would you want a chart? (y/n): ")
    if userExit == "y" and graph == "n":
        break
    elif userExit == "y" and graph == "y":
        generatePlot(playerStats, isInt)
        break
    elif userExit == "n" and graph == "y":
        generatePlot(playerStats, isInt)
        playerStats.clear()
        continue
    elif userExit == "n" and graph == "n":
        playerStats.clear()
        continue

    break

print(f"Total time: {end - start:.9f} seconds")
    # try:
    #     for players in playerData['people']:
    #             if (players['currentTeam']['id'] == teams[userTeam.lower()] and
    #                     (players['primaryPosition']['type'] == "Outfielder" or
    #                      players['primaryPosition']['type'] == "Infielder"  or
    #                      players['primaryPosition']['type'] == "Hitter" or
    #                      players['primaryPosition']['type'] == "Catcher")):
    #
    #                 playerStats = getPlayerStats(players['id'], year)['stats'][0]['splits'][0]['stat']
    #                 stats = { "avg": playerStats['avg'], 'hr': playerStats['homeRuns'],
    #                           'gp': playerStats['gamesPlayed'], 'pa': playerStats['plateAppearances'] }
    #                 print(f"{players['firstName']} {players['lastName']}\n"
    #                       f"Batting Average: {stats['avg']}, Home Runs: {stats['hr']}, "
    #                       f"Games Played: {stats['gp']}, PA: {stats['pa']} ")
    #                 player.append(f"{players['lastName']}")
    #                 if statChoice == 1:
    #                     hitting_stat.append(f"{stats['avg']}")
    #                     isInt = False
    #                 elif statChoice == 2:
    #                     hitting_stat.append(f"{stats['hr']}")
    #                     isInt = True
    #             else:
    #                 continue
    # except:
    #     print("Error, failed to grab player data")
    #     continue




