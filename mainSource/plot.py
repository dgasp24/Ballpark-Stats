from logging import exception

import numpy as np
import matplotlib.pyplot as plt
import mpld3


def generateBarGraph(playerStats, isINT, season, team, whichStat, playerName, pa):
    player = list(playerStats.keys())
    stats = list(playerStats.values())
    name = None

    if team == "MLB":
        colors = ['red' if p == playerName else 'steelblue' for p in player]
        name = playerName in player
    else:
        colors = "steelblue"


    try:
        fig, ax = plt.subplots()

        if isINT:
            hitting_stats = [int(x) for x in stats]
            ax.bar(player, hitting_stats, color=colors)

            ax.set_ylabel(f'{whichStat}')
            ax.set_title(f'{whichStat} by {team} Player ({season}) (Min. of {pa} PA)')
            ax.set_ylim(0, max(hitting_stats) + 10)
            ax.set_yticks(np.arange(0, max(hitting_stats) + 10, 5))



        elif not isINT:
            hitting_stats = [float(x) for x in stats]
            ax.bar(player, hitting_stats, color=colors)

            ax.set_ylabel(f'{whichStat}')
            ax.set_title(f'{whichStat} by {team} Player ({season}) (Min. of {pa} PA)')
            ax.set_ylim(0.05, 0.400)
            ax.set_yticks(np.arange(.05, max(hitting_stats) + .100, 0.050))

        if team != "MLB":
            ax.set_xticks(range(len(player)))
            ax.set_xticklabels(player, fontsize=8)
        else:
            ax.set_xticks(player)
            ax.set_xticklabels(player, fontsize=8)


        plt.tight_layout()
        graph = mpld3.fig_to_html(fig)
        plt.close()
        return graph

    except Exception as e:
        print("Error, failed to generate chart", e)

def generateScatterPlot(playerStats, stat1, stat2, team, year, pa, playerName):
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

    colors = ['red' if p == playerName else 'steelblue' for p in names]

    ax.scatter(stat_1, stat_2, color=colors)

    STAT_INFO = {
        0: {"label": "Batting", "avg": 0.250},
        1: {"label": "OPS", "avg": 0.750},
        2: {"label": "Homeruns", "avg": 20},
        3: {"label": "SLG", "avg": 0.400}
    }

    x_info = STAT_INFO[stat1]
    y_info = STAT_INFO[stat2]

    ax.axvline(x=x_info["avg"], color='red', linestyle='--', linewidth=1.5,
               label=f'{x_info["label"]} League Average')
    ax.axhline(y=y_info["avg"], color='blue', linestyle='--', linewidth=1.5,
               label=f'{y_info["label"]} League Average')

    x_label = x_info["label"]
    y_label = y_info["label"]

    for i, name in enumerate(names):
        if team == "MLB":
            if name == playerName:
                ax.annotate(name, (stat_1[i], stat_2[i]), textcoords="offset points", xytext=(5, 5))
        else:
            ax.annotate(name, (stat_1[i], stat_2[i]), textcoords="offset points", xytext=(5, 5))

    ax.legend()

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(f"{team} in {year} (Min. of {pa} PA)")

    plt.tight_layout()
    plt.show()