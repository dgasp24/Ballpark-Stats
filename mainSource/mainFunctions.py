from fontTools.ttLib.tables import sbixGlyph

from apiLoader import getTeamID
from apiLoader import newMlbRosterData
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
    Stat = None
    isInt = None

    statsData = newMlbRosterData(teamId, year)
    splits = statsData['stats'][0]['splits']

    for split in splits:
        if split['stat']['plateAppearances'] < minimumPA:
            continue

        print(f"{split['player']['fullName']}\n"
              f"Batting Average: {split['stat']['avg']}, Home Runs: {split['stat']['homeRuns']}, "
              f"OPS: {split['stat']['ops']} SLG:{split['stat']['slg']} Games Played: {split['stat']['gamesPlayed']}, "
              f"PA: {split['stat']['plateAppearances']}")

        save_player_stat(
            teamId, year,
            split['player']['lastName'],
            split['player']['fullName'],
            split['stat']['avg'],
            split['stat']['homeRuns'],
            split['stat']['gamesPlayed'],
            split['stat']['ops'],
            split['stat']['slg'],
            split['stat']['plateAppearances']
        )

        Stat, isInt = whichStatBar(
            statChoice,
            split['player']['lastName'],
            split['stat']['avg'],
            split['stat']['homeRuns'],
            split['stat']['ops'],
            split['stat']['slg']
        )

    return Stat, isInt, playerStats

def grabbingStatsforScatter(teamId, year, minimumPA):
    Stat = None
    isInt = None

    cached = get_cached_team_stats(teamId, year)

    if cached:
        print("Using cached data")
        for row in cached:
            last_name, full_name, avg, hr, gp, ops, slg, pa = row

            if pa < minimumPA:
                continue

            print(f"{full_name}\n"
                  f"Batting Average: {avg}, Home Runs: {hr}, OPS: {ops} SLG: {slg}"
                  f"Games Played: {gp}, PA: {pa}")

            playerStats[last_name] = avg, ops, hr, slg

    else:
        print("Fetching from API...")
        mlbData = newMlbRosterData(teamId, year)

        splits = mlbData['stats'][0]['splits']

        for split in splits:
            if split['stat']['plateAppearances'] < minimumPA:
                continue

            print(f"{split['player']['fullName']}\n"
                  f"Batting Average: {split['stat']['avg']}, Home Runs: {split['stat']['homeRuns']}, "
                  f"OPS: {split['stat']['ops']} SLG:{split['stat']['slg']} Games Played: {split['stat']['gamesPlayed']}, "
                  f"PA: {split['stat']['plateAppearances']}")

            lastName = split['player']['lastName']
            fullName = split['player']['fullName']
            avg = split['stat']['avg']
            ops = split['stat']['ops']
            slg = split['stat']['slg']
            hr = split['stat']['homeRuns']
            gamesPlayed = split['stat']['gamesPlayed']
            plateAppearances = split['stat']['plateAppearances']

            save_player_stat(
                teamId, year,
                lastName,
                fullName,
                avg,
                hr,
                gamesPlayed,
                ops,
                slg,
                plateAppearances
            )

            playerStats[lastName] = avg, ops, hr, slg
    return playerStats