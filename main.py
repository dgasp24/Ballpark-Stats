from apiLoader import getTeamID, newMlbRosterData
from plot import generatePlot
from database import get_cached_team_stats, save_player_stat
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
    minimumPA = int(input("What would like the minimum plate appearances be? "))
    teamId = teams[userTeam.lower()]

    start = time.time()

    cached = get_cached_team_stats(teamId, year)

    if cached:
        print("Using cached data")
        for row in cached:
            last_name, full_name, avg, hr, gp, pa = row

            if pa < minimumPA:
                continue

            print(f"{full_name}\n"
                  f"Batting Average: {avg}, Home Runs: {hr}, "
                  f"Games Played: {gp}, PA: {pa}")

            if statChoice == 1:
                playerStats[last_name] = avg
                isInt = False
            elif statChoice == 2:
                playerStats[last_name] = hr
                isInt = True

    else:
        print("Fetching from API...")
        mlbData = newMlbRosterData(teamId, year)

        for players in mlbData['roster']:
            if players['person']['primaryPosition']['type'] in positions:

                if 'stats' not in players['person'] or not players['person']['stats']:
                    continue

                splits = players['person']['stats'][0]['splits']
                if not splits:
                    continue

                rawStat = splits[0]['stat']

                avg = rawStat['avg']
                hr = rawStat['homeRuns']
                gp = rawStat['gamesPlayed']
                pa = rawStat['plateAppearances']

                last_name = players['person']['lastName']
                full_name = players['person']['fullName']

                save_player_stat(teamId, year, last_name, full_name, avg, hr, gp, pa)

                if pa < minimumPA:
                    continue

                print(f"{full_name}\n"
                      f"Batting Average: {avg}, Home Runs: {hr}, "
                      f"Games Played: {gp}, PA: {pa}")

                if statChoice == 1:
                    playerStats[last_name] = avg
                    isInt = False
                elif statChoice == 2:
                    playerStats[last_name] = hr
                    isInt = True

    end = time.time()
    userExit = input("Would you like to exit (y/n): ")
    graph = input("Would you want a chart? (y/n): ")
    if userExit == "y" and graph == "n":
        break
    elif userExit == "y" and graph == "y":
        generatePlot(playerStats, isInt, year, userTeam.capitalize())
        break
    elif userExit == "n" and graph == "y":
        generatePlot(playerStats, isInt, year, userTeam.capitalize())
        playerStats.clear()
        continue
    elif userExit == "n" and graph == "n":
        playerStats.clear()
        continue

    break

print(f"Total time: {end - start:.9f} seconds")