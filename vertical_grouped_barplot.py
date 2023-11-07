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

def make_grouped_barplot_v(barlists, barlabels, save_path, chart_title):
    """Make vertical grouped barplot"""
    fig, ax = plt.subplots()
    width = (1 / len(barlists) / 1.6)
    for i, subbar in enumerate(barlists):
        x_coords = [j + i*width - width*2 for j in range(len(subbar))]
        ax.bar(x_coords, subbar, width, color = secondary_colors[i])
    barx = list(range(len(subbar)))
    plt.yticks(**text_font, size = 8)
    plt.xticks(barx, barlabels, **text_font, size = 8, rotation = 90)
    plt.box(False)
    plt.tick_params(left=False)
    plt.tick_params(bottom=False)
    ax.set_axisbelow(True)
    plt.grid(axis="y", linewidth = 0.2)
    plt.savefig(f"{save_path}/{chart_title}.svg")
