from apiLoader import getTeamID
from plot import generateBarGraph, generateScatterPlot
from databases.database import get_cached_team_stats
from mainFunctions import grabbingStatsforBar, grabbingStatsforScatter

teams = {}
playerStats = {}
global statChoice

def loadTeams():
    teamData = getTeamID()
    for team in teamData['teams']:
        if team['sport']['name'] == "Major League Baseball":
            teams[team['teamName'].lower()] = team['id']
        else:
            continue

loadTeams()

while True:

    ##START OF PROGRAM
    userTeam = input("Enter team: ")
    year = int(input("Enter year: "))
    minimumPA = int(input("What would like the minimum plate appearances be? "))
    whichGraph = int(input("Which graph would you like?\n1. Bar Graph\n2. Scatter Plot "))

    ##LOADING TEAMS AND CACHED PLAYER STATS
    teamId = teams[userTeam.lower()]
    cached = get_cached_team_stats(teamId, year)

    match whichGraph:
        case 1:

            statChoice = int(input("What would you like to have the chart show?\n1. Batting Average\n2. OPS\n3. Homeruns\n"))

            Stat, isInt, playerStats = grabbingStatsforBar(statChoice, teamId, year, minimumPA)

            print(playerStats)
            print(Stat, isInt)

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
        case 2:

            compareStat1 = int(input("What would you like to compare?\n1. Batting Average\n2. OPS\n3. Homeruns\n"))
            compareStat2 = int(input("and?\n"))
            playerStats = grabbingStatsforScatter(teamId, year, minimumPA)
            userExit = input("Would you like to exit (y/n): ")
            graph = input("Would you want a chart? (y/n): ")
            print(playerStats)
            if userExit == "y" and graph == "n":
                break
            elif userExit == "y" and graph == "y":
                generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1)
                break
            elif userExit == "n" and graph == "y":
                generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1)
                playerStats.clear()
                continue
            elif userExit == "n" and graph == "n":
                playerStats.clear()
                continue
        case _:
            print("Please enter a valid input")


    break