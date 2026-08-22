import requests
session = requests.Session()
mlbAPI = "https://statsapi.mlb.com"

def newMlbRosterData(team, season):
    newMLBAPI = f"{mlbAPI}/api/v1/stats"
    param = {
        "stats": "season",
        "group": "hitting",
        "season": season,
        "sportId": 1,
        "teamId": team,
        "limit": 100,
        "playerPool": "ALL"
    }

    response = session.get(newMLBAPI, params=param)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error, failed to get data")
        return None

def allMLBPlayerData(season):
    allMLBAPI = f"{mlbAPI}/api/v1/stats"
    param = {
        "stats": "season",
        "group": "hitting",
        "season": season,
        "sportId": 1,
        "limit": 1000,
        "playerPool": "ALL"
    }
    response = session.get(allMLBAPI, params=param)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error, failed to get data")
        return None


def getTeamID():
    response = session.get(f"{mlbAPI}/api/v1/teams/")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error, failed to get data")
        return None