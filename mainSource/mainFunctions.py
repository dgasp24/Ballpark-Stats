from apiLoader import getTeamID
from apiLoader import newMlbRosterData, allMLBPlayerData
from databases.database import save_player_stat, get_cached_team_stats

positions = {"Outfielder", "Infielder", "Hitter", "Catcher"}
playerStats = {}
teams = {}

def loadTeams():
    teamData = getTeamID()
    for team in teamData['teams']:
        if team['sport']['name'] == "Major League Baseball":
            teams[team['teamName'].lower()] = team['id']
        else:
            continue
    return teams

def whichStatBar(statChoice, last_name, avg, hr, ops, slg):
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
        case 4:
            playerStats[last_name] = slg
            return "SLG", False


def grabbingStatsforBar(statChoice, teamId, year, minimumPA):
    playerStats.clear()
    Stat = None
    isInt = None
    if teamId != "MLB":
        statsData = newMlbRosterData(teamId, year)
        splits = statsData['stats'][0]['splits']

        for split in splits:
            if split['stat']['plateAppearances'] < minimumPA:
                continue

            fullName = split['player']['fullName']
            avg = split['stat']['avg']
            homeRuns = split['stat']['homeRuns']
            ops = split['stat']['ops']
            slg = split['stat']['slg']
            gamesPlayed = split['stat']['gamesPlayed']
            pa = int(split['stat']['plateAppearances'])

            Stat, isInt = whichStatBar(
                statChoice,
                fullName,
                avg,
                homeRuns,
                ops,
                slg
            )
    else:
        statsData = allMLBPlayerData(year)
        splits = statsData['stats'][0]['splits']

        for split in splits:
            if split['stat']['plateAppearances'] < minimumPA:
                continue

            fullName = split['player']['fullName']
            avg = split['stat']['avg']
            homeRuns = split['stat']['homeRuns']
            ops = split['stat']['ops']
            slg = split['stat']['slg']
            gamesPlayed = split['stat']['gamesPlayed']
            pa = int(split['stat']['plateAppearances'])


            Stat, isInt = whichStatBar(
                statChoice,
                fullName,
                avg,
                homeRuns,
                ops,
                slg
            )


    return Stat, isInt, playerStats

def grabbingStatsforScatter(teamId, year, minimumPA):
    playerStats.clear()
    Stat = None
    isInt = None

    if teamId != "MLB":
        print("Fetching from API...")
        mlbData = newMlbRosterData(teamId, year)

        splits = mlbData['stats'][0]['splits']

        for split in splits:
            if split['stat']['plateAppearances'] < minimumPA:
                continue


            lastName = split['player']['lastName']
            fullName = split['player']['fullName']
            avg = split['stat']['avg']
            ops = split['stat']['ops']
            slg = split['stat']['slg']
            hr = split['stat']['homeRuns']
            gamesPlayed = split['stat']['gamesPlayed']
            plateAppearances = split['stat']['plateAppearances']


            playerStats[fullName] = avg, ops, hr, slg
    else:
        mlbData = allMLBPlayerData(year)

        splits = mlbData['stats'][0]['splits']

        for split in splits:
            if split['stat']['plateAppearances'] < minimumPA:
                continue


            lastName = split['player']['lastName']
            fullName = split['player']['fullName']
            avg = split['stat']['avg']
            ops = split['stat']['ops']
            slg = split['stat']['slg']
            hr = split['stat']['homeRuns']
            gamesPlayed = split['stat']['gamesPlayed']
            plateAppearances = split['stat']['plateAppearances']

            playerStats[fullName] = avg, ops, hr, slg

    return playerStats