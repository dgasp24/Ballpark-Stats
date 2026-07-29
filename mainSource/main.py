from plot import generateBarGraph, generateScatterPlot
from databases.database import get_cached_team_stats
from mainFunctions import grabbingStatsforBar, grabbingStatsforScatter, loadTeams
from apiLoader import allMLBPlayerData

allMLBPlayerData(2022)

playerStats = {}
global statChoice

teams = loadTeams()

while True:

    ##START OF PROGRAM
    userTeam = input("Enter team: ")
    try:
        year = int(input("Enter year: "))
        minimumPA = int(input("What would like the minimum plate appearances be? "))
        whichGraph = int(input("Which graph would you like?\n1. Bar Graph\n2. Scatter Plot "))

        ##LOADING TEAMS AND CACHED PLAYER STATS
        teamId = teams[userTeam.lower()]
        cached = get_cached_team_stats(teamId, year)

        match whichGraph:
            case 1:

                statChoice = int(input("What would you like to have the chart show?\n1. Batting Average\n2. OPS\n3. Homeruns\n4. SLG"))

                Stat, isInt, playerStats = grabbingStatsforBar(statChoice, teamId, year, minimumPA)

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

                compareStat1 = int(input("What would you like to compare? (X Axis)\n1. Batting Average\n2. OPS\n3. Homeruns\n4. SLG\n"))
                compareStat2 = int(input("and? (Y Axis)\n"))
                playerStats = grabbingStatsforScatter(teamId, year, minimumPA)
                userExit = input("Would you like to exit (y/n): ")
                graph = input("Would you want a chart? (y/n): ")
                if userExit == "y" and graph == "n":
                    break
                elif userExit == "y" and graph == "y":
                    generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1, userTeam.capitalize(), year, minimumPA)
                    break
                elif userExit == "n" and graph == "y":
                    generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1, userTeam.capitalize(), year, minimumPA)
                    playerStats.clear()
                    continue
                elif userExit == "n" and graph == "n":
                    playerStats.clear()
                    continue
            case _:
                print("Please enter a valid input")
    except:
        print("Error! Please try again")
        continue

    break