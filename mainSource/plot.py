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

def generateScatterPlot(playerStats, stat1, stat2, team, year, pa):
    names = []
    stat_1 = []
    stat_2 = []
    x_label = ""
    y_label = ""

    for name, stat_list in playerStats.items():
        names.append(name)
        stat_1.append(float(stat_list[stat1]))
        stat_2.append(float(stat_list[stat2]))

    fig, ax = plt.subplots()

    ax.scatter(stat_1, stat_2, color='steelblue')


    print(stat1, stat2)
    if stat1 == 0 and stat2 == 1:
        ax.axvline(x=0.250, color='red', linestyle='--', linewidth=1.5, label='Batting League Average')
        x_label = "Batting Average"
        ax.axhline(y=0.750, color='blue', linestyle='--', linewidth=1.5, label=' OPS League Average')
        y_label = "OPS Average"
    elif stat1 == 0 and stat2 == 2:
        ax.axvline(x=.250, color='red', linestyle='--', linewidth=1.5, label='Batting League Average')
        x_label = "Batting Average"
        ax.axhline(y=20, color='blue', linestyle='--', linewidth=1.5, label='Homerun League Average')
        y_label = "Homeruns"
    elif stat1 == 1 and stat2 == 0:
        ax.axhline(y=0.250, color='red', linestyle='--', linewidth=1.5, label='Batting League Average')
        y_label = "Batting Average"
        ax.axvline(x=0.750, color='blue', linestyle='--', linewidth=1.5, label='OPS League Average')
        x_label = "OPS Average"
    elif stat1 == 1 and stat2 == 2:
        ax.axhline(y=20, color='red', linestyle='--', linewidth=1.5, label='Homeruns League Average')
        y_label = "Homeruns"
        ax.axvline(x=0.750, color='blue', linestyle='--', linewidth=1.5, label='OPS League Average')
        x_label = "OPS Average"
    elif stat1 == 2 and stat2 == 1:
        ax.axvline(x=20, color='red', linestyle='--', linewidth=1.5, label='Homeruns League Average')
        x_label = "Homeruns"
        ax.axhline(y=0.750, color='blue', linestyle='--', linewidth=1.5, label='OPS League Average')
        y_label = "OPS Average"
    elif stat1 == 2 and stat2 == 0:
        ax.axvline(x=20, color='red', linestyle='--', linewidth=1.5, label='Homeruns League Average')
        x_label = "Homeruns"
        ax.axhline(y=0.250, color='blue', linestyle='--', linewidth=1.5, label='Batting League Average')
        y_label = "Batting Average"
        ax.set_xlim(0, 70)
        ax.set_ylim(.150, .400)

    ax.legend()
    for i, name in enumerate(names):
        ax.annotate(name, (stat_1[i], stat_2[i]), textcoords="offset points", xytext=(5, 5))

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(f"{team} in {year} (Min. of {pa} PA)")

    plt.tight_layout()
    plt.show()