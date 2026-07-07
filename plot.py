import numpy as np
import matplotlib.pyplot as plt


def generatePlot(player, battingAverage):
    INTbattingAverage = [float(x) for x in battingAverage]
    fig, ax = plt.subplots()
    colors = ['red' if player == 'Alvarez' else 'steelblue' for player in player]
    ax.bar(player, INTbattingAverage, color=colors)
    ax.axhline(y=0.300, color='red', linestyle='--', linewidth=1.5, label='League Average (.300)')

    ax.set_ylabel('Batting Average')
    ax.set_title('Batting Averages by Player')
    ax.set_ylim(0.0, 0.400)
    ax.set_yticks(np.arange(.0, 0.400, 0.030))# batting avg realistically caps under .400

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()