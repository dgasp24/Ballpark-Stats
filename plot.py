import numpy as np
import matplotlib.pyplot as plt


def generatePlot(player, hitting_stat, isINT):

    try:
        if isINT:
            fig, ax = plt.subplots()
            colors = ['red' if player == 'Alvarez' else 'steelblue' for player in player]
            ax.axhline(y=20, color='red', linestyle='--', linewidth=1.5, label='League Average (.300)')
            batting_average = [int(x) for x in hitting_stat]
            ax.bar(player, batting_average, color=colors)

            ax.set_ylabel('Home Runs')
            ax.set_title('Home Runs by Player')
            ax.set_ylim(0, max(batting_average)+10)
            ax.set_yticks(np.arange(0, max(batting_average)+10, 5))# batting avg realistically caps under .400

            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
        elif not isINT:
            fig, ax = plt.subplots()
            hitting_stats = [float(x) for x in hitting_stat]
            colors = ['red' if player == 'Alvarez' else 'steelblue' for player in player]
            ax.bar(player, hitting_stats, color=colors)
            ax.axhline(y=0.600, color='red', linestyle='--', linewidth=1.5, label='League Average (.300)')

            ax.set_ylabel('Batting Average')
            ax.set_title('Batting Averages by Player')
            ax.set_ylim(0.0, 0.400)
            ax.set_yticks(np.arange(.0, 0.400, 0.030))  # batting avg realistically caps under .400

            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.show()
    except:
        print("Error, failed to generate chart")