import numpy as np
import matplotlib.pyplot as plt


def generateBarGraph(playerStats, isINT, season, team, whichStat):
    player = list(playerStats.keys())
    stats = list(playerStats.values())

    try:
        if isINT:
            fig, ax = plt.subplots()
            hitting_stats = [int(x) for x in stats]
            ax.bar(player, hitting_stats, color="steelblue")

            ax.set_ylabel(f'{whichStat}')
            ax.set_title(f'{whichStat} by {team} Player ({season})')
            ax.set_ylim(0, max(hitting_stats)+10)
            ax.set_yticks(np.arange(0, max(hitting_stats)+10, 5))# batting avg realistically caps under .400

            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
        elif not isINT:
            fig, ax = plt.subplots()
            hitting_stats = [float(x) for x in stats]
            ax.bar(player, hitting_stats, color="steelblue")

            ax.set_ylabel(f'{whichStat}')
            ax.set_title(f'{whichStat} by {team} Player ({season})')
            ax.set_ylim(0.05, 0.400)
            ax.set_yticks(np.arange(.05, max(hitting_stats)+.100, 0.050))  # batting avg realistically caps under .400

            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
    except:
        print("Error, failed to generate chart")

def generateScatterPlot(playerStats, isINT, season, team, whichStat):
    player = list(playerStats.keys())
    stats = list(playerStats.values())

    names = ['Altuve', 'Alvarez', 'Bregman', 'Tucker']

    fig, ax = plt.subplots()
    ax.scatter(avg, home_runs)

    ax.set_xlabel('Batting Average')
    ax.set_ylabel('Home Runs')
    ax.set_title('Batting Average vs Home Runs')

    plt.tight_layout()
    plt.show()