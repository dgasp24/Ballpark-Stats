import requests
mlbAPI = "https://statsapi.mlb.com"

def newMlbRosterData(team, season):
    newMLBAPI = f"https://statsapi.mlb.com/api/v1/teams/{team}/roster"
    param = {
        "rosterType": "40Man",
        'hydrate': f"person(stats(group=hitting,type=season,season={season}))"
    }

    response = requests.get(newMLBAPI, params=param)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error, failed to get data")
        return None

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

def getTeamID():
    response = requests.get(f"{mlbAPI}/api/v1/teams/")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error, failed to get data")
        return None