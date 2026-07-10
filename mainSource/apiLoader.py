import requests
mlbAPI = "https://statsapi.mlb.com"

def newMlbRosterData(team, season):
    newMLBAPI = f"{mlbAPI}/api/v1/teams/{team}/roster"
    param = {
        "rosterType": "40Man",
        "date": f"{season}-10-01",
        'hydrate': f"person(stats(group=hitting,type=season,season={season}))",
         "playerPool": "ALL"
    }

    response = requests.get(newMLBAPI, params=param)

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