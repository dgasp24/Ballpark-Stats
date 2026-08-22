from logging import exception

import numpy as np
import matplotlib.pyplot as plt
import mpld3


PANEL = "#13291f"
ACCENT = "#f2b134"
ACCENT_HOT = "#e2574c"
TEXT = "#f5efe1"
GRIDLINE = "#f2b134"

def generateBarGraph(playerStats, isINT, season, team, whichStat, playerName, pa):
    player = list(playerStats.keys())
    stats = list(playerStats.values())
    name = None

    if team == "MLB":
        colors = [ACCENT_HOT if p == playerName else ACCENT for p in player]
        name = playerName in player
    else:
        colors = ACCENT


    try:
        fig, ax = plt.subplots()
        fig.patch.set_facecolor(PANEL)
        ax.set_facecolor(PANEL)

        if isINT:
            hitting_stats = [int(x) for x in stats]
            ax.bar(player, hitting_stats, color=colors)

            ax.set_ylabel(f'{whichStat}', color=TEXT)
            ax.set_title(f'{whichStat} by {team} Player ({season}) (Min. of {pa} PA)', color=TEXT)
            ax.set_ylim(0, max(hitting_stats) + 10)
            ax.set_yticks(np.arange(0, max(hitting_stats) + 10, 5))



        elif not isINT:
            hitting_stats = [float(x) for x in stats]
            ax.bar(player, hitting_stats, color=colors)

            ax.set_ylabel(f'{whichStat}', color=TEXT)
            ax.set_title(f'{whichStat} by {team} Player ({season}) (Min. of {pa} PA)', color=TEXT)
            ax.set_ylim(0.05, 0.400)
            ax.set_yticks(np.arange(.05, max(hitting_stats) + .100, 0.050))

        if team != "MLB":
            ax.set_xticks(range(len(player)))
            ax.set_xticklabels(player, fontsize=8, color=TEXT)
        else:
            ax.set_xticks(player)
            ax.set_xticklabels(player, fontsize=8, color=TEXT)

        ax.tick_params(axis='x', colors=TEXT)
        ax.tick_params(axis='y', colors=TEXT)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(TEXT)
        ax.spines['bottom'].set_color(TEXT)

        ax.grid(axis='y', color=GRIDLINE, alpha=0.15)
        ax.set_axisbelow(True)

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

    for name, stat_list in playerStats.items():
        names.append(name)
        stat_1.append(float(stat_list[stat1]))
        stat_2.append(float(stat_list[stat2]))

    fig, ax = plt.subplots()
    fig.patch.set_facecolor(PANEL)
    ax.set_facecolor(PANEL)

    colors = [ACCENT_HOT if p == playerName else ACCENT for p in names]
    ax.scatter(stat_1, stat_2, color=colors)

    STAT_INFO = {
        0: {"label": "Batting", "avg": 0.250},
        1: {"label": "OPS", "avg": 0.750},
        2: {"label": "Homeruns", "avg": 20},
        3: {"label": "SLG", "avg": 0.400}
    }

    x_info = STAT_INFO[stat1]
    y_info = STAT_INFO[stat2]

    # lock in the plot's actual data range first - Claude
    x_min, x_max = min(stat_1), max(stat_1)
    y_min, y_max = min(stat_2), max(stat_2)
    x_pad = (x_max - x_min) * 0.08
    y_pad = (y_max - y_min) * 0.08
    ax.set_xlim(x_min - x_pad, x_max + x_pad)
    ax.set_ylim(y_min - y_pad, y_max + y_pad)

    # draw average lines as real data-coordinate lines, spanning the fixed range - Claude
    ax.plot([x_info["avg"], x_info["avg"]], [y_min - y_pad, y_max + y_pad],
             color=ACCENT_HOT, linestyle='--', linewidth=1.5,
             label=f'{x_info["label"]} League Average')
    ax.plot([x_min - x_pad, x_max + x_pad], [y_info["avg"], y_info["avg"]],
             color=TEXT, linestyle='--', linewidth=1.5,
             label=f'{y_info["label"]} League Average')

    # small offset in DATA units instead of pixel "offset points" - Claude
    x_offset = (x_max - x_min) * 0.015
    y_offset = (y_max - y_min) * 0.015

    for i, name in enumerate(names):
        if team == "MLB":
            if name == playerName:
                ax.text(stat_1[i] + x_offset, stat_2[i] + y_offset, name, color=TEXT, fontsize=9)
        else:
            ax.text(stat_1[i] + x_offset, stat_2[i] + y_offset, name, color=TEXT, fontsize=9)

    legend = ax.legend()
    legend.get_frame().set_facecolor(PANEL)
    legend.get_frame().set_edgecolor(TEXT)
    for text in legend.get_texts():
        text.set_color(TEXT)

    ax.tick_params(axis='x', colors=TEXT)
    ax.tick_params(axis='y', colors=TEXT)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(TEXT)
    ax.spines['bottom'].set_color(TEXT)

    ax.grid(True, color=GRIDLINE, alpha=0.15)
    ax.set_axisbelow(True)

    ax.set_xlabel(x_info["label"], color=TEXT)
    ax.set_ylabel(y_info["label"], color=TEXT)
    ax.set_title(f"{team} in {year} (Min. of {pa} PA)", color=TEXT)

    plt.tight_layout()
    graph = mpld3.fig_to_html(fig)
    plt.close()
    return graph