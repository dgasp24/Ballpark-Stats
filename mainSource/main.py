from plot import generateBarGraph, generateScatterPlot
from databases.database import get_cached_team_stats
from mainFunctions import grabbingStatsforBar, grabbingStatsforScatter, loadTeams

playerStats = {}
global statChoice
name = None

teams = loadTeams()

while True:

    try:
        dataPick = int(input("Welcome! Please choose one...\n1. Team Data\n2. MLB Data\n"))
        if dataPick == 1:
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
                    statChoice = int(input("What would you like to have the chart show?\n1. Batting Average\n2. OPS\n3. Homeruns\n4. SLG"))

                    Stat, isInt, playerStats = grabbingStatsforBar(statChoice, teamId, year, minimumPA)

                    userExit = input("Would you like to exit (y/n): ")
                    graph = input("Would you want a chart? (y/n): ")
                    if userExit == "y" and graph == "n":
                        break
                    elif userExit == "y" and graph == "y":
                        generateBarGraph(playerStats, isInt, year, userTeam.capitalize(), Stat, name)
                        break
                    elif userExit == "n" and graph == "y":
                        generateBarGraph(playerStats, isInt, year, userTeam.capitalize(), Stat, name)
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
                        generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1, userTeam.capitalize(), year, minimumPA, name)
                        break
                    elif userExit == "n" and graph == "y":
                        generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1, userTeam.capitalize(), year, minimumPA, name)
                        playerStats.clear()
                        continue
                    elif userExit == "n" and graph == "n":
                        playerStats.clear()
                        continue
                case _:
                    print("Please enter a valid input")
        ##IF CHOOSING ALL MLB PLAYERS
        elif dataPick == 2:
            year = int(input("Enter year: "))
            minimumPA = int(input("What would like the minimum plate appearances be? "))
            whichGraph = int(input("Which graph would you like?\n1. Bar Graph\n2. Scatter Plot "))
            name = input("Please choose a name to highlight on the graph")

            match whichGraph:
                case 1:

                    statChoice = int(input(
                        "What would you like to have the chart show?\n1. Batting Average\n2. OPS\n3. Homeruns\n4. SLG"))

                    Stat, isInt, playerStats = grabbingStatsforBar(statChoice,"MLB", year, minimumPA)

                    userExit = input("Would you like to exit (y/n): ")
                    graph = input("Would you want a chart? (y/n): ")
                    if userExit == "y" and graph == "n":
                        break
                    elif userExit == "y" and graph == "y":
                        generateBarGraph(playerStats, isInt, year, "MLB", Stat, name)
                        break
                    elif userExit == "n" and graph == "y":
                        generateBarGraph(playerStats, isInt, year, "MLB", Stat, name)
                        playerStats.clear()
                        continue
                    elif userExit == "n" and graph == "n":
                        playerStats.clear()
                        continue
                case 2:

                    compareStat1 = int(input(
                        "What would you like to compare? (X Axis)\n1. Batting Average\n2. OPS\n3. Homeruns\n4. SLG\n"))
                    compareStat2 = int(input("and? (Y Axis)\n"))
                    playerStats = grabbingStatsforScatter("MLB", year, minimumPA)
                    userExit = input("Would you like to exit (y/n): ")
                    graph = input("Would you want a chart? (y/n): ")
                    if userExit == "y" and graph == "n":
                        break
                    elif userExit == "y" and graph == "y":
                        generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1, "MLB",
                                            year, minimumPA, name)
                        break
                    elif userExit == "n" and graph == "y":
                        generateScatterPlot(playerStats, compareStat1 - 1, compareStat2 - 1, "MLB",
                                            year, minimumPA, name)
                        playerStats.clear()
                        continue
                    elif userExit == "n" and graph == "n":
                        playerStats.clear()
                        continue
                case _:
                    print("Please enter a valid input")
                    continue

    except:
        print("Error! Please try again")
        continue
    break