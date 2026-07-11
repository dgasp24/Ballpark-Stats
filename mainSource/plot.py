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

def generateScatterPlot(playerStats):
    names = []
    stat_1 = []
    stat_2 = []

    for name, stat_list in playerStats.items():
        names.append(name)
        stat_1.append(float(stat_list[0]))
        stat_2.append(float(stat_list[1]))

    fig, ax = plt.subplots()
    ax.scatter(stat_1, stat_2, color='steelblue')

    for i, name in enumerate(names):
        ax.annotate(name, (stat_1[i], stat_2[i]), textcoords="offset points", xytext=(5, 5))

    ax.set_xlabel("Average")
    ax.set_ylabel("OPS")
    ax.set_title(f"TEST")

    plt.tight_layout()
    plt.show()