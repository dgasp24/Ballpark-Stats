import requests

mlbAPI = "https://statsapi.mlb.com"
season = "2026"

teams = {
    
}

def getPlayerID(season):
    response = requests.get(f"{mlbAPI}/api/v1/sports/1/players?season={season}")

    if response.status_code == 200:
        return response.json()
    else:
        print("Error, failed to get data")
        return None

def getPlayerStats(id, season):
    response = requests.get(f"{mlbAPI}/api/v1/people/{id}/stats?stats=season&season={season}")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error, failed to get data")
        return None

playerData = getPlayerID(season)

for players in playerData['people']:
    try:
        if players['currentTeam']['id'] == 117 and (players['primaryPosition']['type'] == "Outfielder" or players['primaryPosition']['type'] == "Infielder"  or players['primaryPosition']['type'] == "Hitter"):
            playerStats = getPlayerStats(players['id'], season)['stats'][0]['splits'][0]['stat']
            stats = { "avg": playerStats['avg']
            }
            print(f"ID: {players['id']}, {players['firstName']} {players['lastName']}")
            print(f"Batting Average: {stats['avg']}")
        else:
            continue
    except:
        print("Error, failed to grab player data")


