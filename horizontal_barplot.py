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

def valuelabel_h(barheights, barlabels):
    """Add valuelabels for horizontal barplots"""
    for i in range(len(barheights)):
        plt.text(list(barheights)[i]+0.3, i-0.06, list(barheights)[i], ha = 'left', size = 8, **text_font)

def make_barplot_h(barheights, barlabels, barcolors, save_path, chart_title):
    """Make horizontal barplot"""
    fig, ax = plt.subplots()
    ax.barh(list(barlabels), list(barheights), 0.65, color = barcolors, label = barlabels)
    valuelabel_h(barheights, barlabels)
    plt.yticks(**text_font, size = 8)
    plt.box(False)
    plt.xticks([])
    plt.tick_params(left=False)
    plt.savefig(f"{save_path}/{chart_title}.svg")
