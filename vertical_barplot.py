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

def valuelabel_v(barheights, barlabels):
    """Add valuelabels for vertical barplots"""
    for i in range(len(barheights)):
        plt.text(i-0.03, barheights[i]+0.3, barlabels[i], ha = 'center', size = 8, **text_font)

def make_barplot_v(barheights, barnames, barcolors):
    """Make vertical barplot"""
    fig, ax = plt.subplots()
    ax.bar(barnames, barheights, 0.65, color = barcolors, label = barlabels)
    valuelabel_v(barheights, barlabels)
    plt.xticks(**text_font, size = 8, rotation = 45)
    plt.box(False)
    plt.yticks([])
    plt.tick_params(bottom=False)

