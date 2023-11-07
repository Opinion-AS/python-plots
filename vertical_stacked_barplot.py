import matplotlib.pyplot as plt
import numpy as np

### primary colors
## Orange, warm black
primary_colors = ["#f26649", "#302026"]

### secondary colors
## Dk. grey, red, yellow, blue, aqua, lt. yellow
secondary_colors = ["#525350", "#f15f5b", "#fce164", "#1c7ca1", "#71c3b4", "#fcf7ba"]

title_font = {"fontname": "Century Gothic"}
text_font = {"fontname": "Arial"}

def make_stacked_barplot_v(barlists, barlabels, save_path, chart_title):
    """Make vertical stacked barplot"""
    fig, ax = plt.subplots()
    width = 0.8 / len(barlists)
    bottom = [0] * len(barlists[0])
    for i, subbar in enumerate(barlists):
        ax.bar(range(len(subbar)), subbar, width, bottom=bottom, color=secondary_colors[i])
        bottom = [a + b for a, b in zip(bottom, subbar)]
    barx = list(range(len(barlists[0])))
    plt.yticks(**text_font, size=8)
    plt.xticks(barx, barlabels, **text_font, size=8, rotation=90)
    plt.box(False)
    plt.tick_params(left=False)
    plt.tick_params(bottom=False)
    ax.set_axisbelow(True)
    plt.grid(axis="y", linewidth=0.2)
    plt.savefig(f"{save_path}/{chart_title}.svg")
