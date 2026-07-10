import numpy as np
import matplotlib.pyplot as plt


def generatePlot(playerStats, isINT, season, team):
    player = list(playerStats.keys())
    stats = list(playerStats.values())

    try:
        if isINT:
            fig, ax = plt.subplots()
            colors = ['red' if player == 'Alvarez' else 'steelblue' for player in player]
            ax.axhline(y=20, color='red', linestyle='--', linewidth=1.5, label='League Average (.300)')
            hitting_stats = [int(x) for x in stats]
            ax.bar(player, hitting_stats, color=colors)

            ax.set_ylabel('Home Runs')
            ax.set_title(f'Home Runs by {team} Player ({season})')
            ax.set_ylim(0, max(hitting_stats)+10)
            ax.set_yticks(np.arange(0, max(hitting_stats)+10, 5))# batting avg realistically caps under .400

            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
        elif not isINT:
            fig, ax = plt.subplots()
            hitting_stats = [float(x) for x in stats]
            colors = ['red' if player == 'Alvarez' else 'steelblue' for player in player]
            ax.bar(player, hitting_stats, color=colors)
            ax.axhline(y=0.600, color='red', linestyle='--', linewidth=1.5, label='League Average (.300)')

            ax.set_ylabel('Batting Average')
            ax.set_title(f'Batting Averages by {team} Player ({season})')
            ax.set_ylim(0.05, 0.400)
            ax.set_yticks(np.arange(.05, max(hitting_stats)+.100, 0.050))  # batting avg realistically caps under .400

            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
    except:
        print("Error, failed to generate chart")