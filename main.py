from apiLoader import getPlayerID, getTeamID, getPlayerStats
season = "2026"

teams = {
}

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
                    stats = { "avg": playerStats['avg']
                    }
                    print(f"ID: {players['id']}, {players['firstName']} {players['lastName']}")
                    print(f"Batting Average: {stats['avg']}")
                else:
                    continue
    except:
        print("Error, failed to grab player data")
        continue
    break


