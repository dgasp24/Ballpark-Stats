from apiLoader import getTeamID, newMlbRosterData
from plot import generateBarGraph
from databases.database import get_cached_team_stats, save_player_stat

teams = {}
playerStats = {}
positions = {"Outfielder", "Infielder", "Hitter", "Catcher"}
Stat = ""
isInt = True

def loadTeams():
    teamData = getTeamID()
    for team in teamData['teams']:
        if team['sport']['name'] == "Major League Baseball":
            teams[team['teamName'].lower()] = team['id']
        else:
            continue

def whichStat(statChoice, last_name, avg, ops, hr, gp, pa):
    match statChoice:
        case 1:
            playerStats[last_name] = avg
            return "Batting Average", False
        case 2:
            playerStats[last_name] = ops
            return "OPS", False
        case 3:
            playerStats[last_name] = hr
            return "Homeruns",  True

loadTeams()

while True:
    userTeam = input("Enter team: ")
    year = int(input("Enter year: "))
    minimumPA = int(input("What would like the minimum plate appearances be? "))
    statChoice = int(input("What would you like to have the chart show?\n1. Batting Average\n2. OPS\n3. Homeruns\n"))
    teamId = teams[userTeam.lower()]

    cached = get_cached_team_stats(teamId, year)

    if cached:
        print("Using cached data")
        for row in cached:
            last_name, full_name, avg, hr, gp, ops, pa = row

            if pa < minimumPA:
                continue

            print(f"{full_name}\n"
                  f"Batting Average: {avg}, Home Runs: {hr}, OPS: {ops} "
                  f"Games Played: {gp}, PA: {pa}")

            Stat, isInt = whichStat(statChoice, last_name, avg, ops, hr, gp, pa)

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
                ops = rawStat['ops']
                gp = rawStat['gamesPlayed']
                pa = rawStat['plateAppearances']

                last_name = players['person']['lastName']
                full_name = players['person']['fullName']

                save_player_stat(teamId, year, last_name, full_name, avg, hr, gp, ops, pa)

                if pa < minimumPA:
                    continue

                print(f"{full_name}\n"
                      f"Batting Average: {avg}, Home Runs: {hr}, OPS: {ops} "
                      f"Games Played: {gp}, PA: {pa}")

                Stat, isInt = whichStat(statChoice, last_name, avg, ops, hr, gp, pa)


    userExit = input("Would you like to exit (y/n): ")
    graph = input("Would you want a chart? (y/n): ")
    if userExit == "y" and graph == "n":
        break
    elif userExit == "y" and graph == "y":
        generateBarGraph(playerStats, isInt, year, userTeam.capitalize(), Stat)
        break
    elif userExit == "n" and graph == "y":
        generateBarGraph(playerStats, isInt, year, userTeam.capitalize(), Stat)
        playerStats.clear()
        continue
    elif userExit == "n" and graph == "n":
        playerStats.clear()
        continue

    break