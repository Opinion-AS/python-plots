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

def make_donutplot(data, colors):
    """Make donutplot w. labeled pieces"""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(data, wedgeprops = {'width':0.5}, startangle = 90, colors = colors)
    if sum(data) > 100:
        raise Exception("Data must not exceed 100 %.")
    if len(data) != len(colors):
        raise Exception("data and colors must be of same length!")

def valuelabel_pie(sizes, labels):
    """Add valuelabels for circular pie chart"""
    cumulative_sizes = np.cumsum(sizes)
    angles = [360 * size / sum(sizes) for size in cumulative_sizes]
    
    for i, j in enumerate(sizes):
        angle = angles[i]
        radian = angle * np.pi / 180
        x = 0.8 * np.cos(radian)
        y = 0.8 * np.sin(radian)
        plt.text(x, y, labels[i], ha='center', va='center', size = 10, **text_font)
