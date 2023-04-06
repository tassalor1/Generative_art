import numpy as np
import matplotlib.pyplot as plt

def colors():
    blue_group = [
        (0/255, 132/255, 160/255) # Lagoon Blue
    ]
    return blue_group[0]

width, height = 900, 900
fig = plt.figure(figsize=(width/90, height/80), dpi=90)
ax = plt.axes(xlim=(0, width), ylim=(0, height))

# Create the pixelated background
pixel_size = width // 20 # Amount of pixel squares
for i in range(0, width, pixel_size):
    for j in range(0, height, pixel_size):
        rect = plt.Rectangle((i, j), pixel_size, pixel_size, linewidth=0, color=(252/255,218/255,139/255 ))
        ax.add_patch(rect)

# Draw grid lines
for i in range(0, width, pixel_size):
    ax.vlines(i, 0, height, colors='black', linewidth=3.0)
for j in range(0, height, pixel_size):
    ax.hlines(j, 0, width, colors='black', linewidth=3.0)

ax.set_xticks([])
ax.set_yticks([])

plt.show()
