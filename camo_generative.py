import numpy as np
import matplotlib.pyplot as plt
import random

# Function for camo colors
def army_color():
    army_colors = [
        (34/255, 139/255, 34/255),    # Forest Green
        (210/255, 180/255, 140/255),  # Desert Tan
        (133/255, 94/255, 66/255)     # Dark Earth
    ]
    return army_colors[np.random.randint(len(army_colors))]


# Set up the figure dimensions and background color
width, height = 800, 800
fig = plt.figure(figsize=(width/80, height/80), dpi=80)
ax = plt.axes(xlim=(0, width), ylim=(0, height))
ax.set_facecolor((0, 0, 0))

# Draw random lines
for _ in range(50):
    x1, y1 = random.randint(3, width), random.randint(0, height)
    x2, y2 = random.randint(3, width), random.randint(0, height)
    ax.scatter([x1, x2], [y1, y2], color=army_color(), linewidth=10)

# Draw random circles
for _ in range(50):
    x, y = random.randint(3, width), random.randint(0, height)
    radius = random.randint(10, 50)
    circle = plt.Circle((x, y), radius, linewidth=0, color=army_color())
    ax.add_patch(circle)

# Draw random squares
for _ in range(50):
    x, y = random.randint(3, width), random.randint(0, height)
    w, h = random.randint(10, 50), random.randint(10, 50)
    rect = plt.Rectangle((x, y), w, h, linewidth=0, color=army_color())
    ax.add_patch(rect)


# Remove axis labels
ax.set_xticks([])
ax.set_yticks([])

# Show
plt.show()