import numpy as np
import matplotlib.pyplot as plt
import random

# Function for camo colors
def army_color():
    army_colors = [
        (96/255,68/255,57/255), # Brown
        (158/255,154/255,117/255), # Desert Tan
        (65/255,83/255,59/255), # Green
        (85/255,72/255,64/255) # Dark Brown
    ]
    return army_colors[np.random.randint(len(army_colors))]


# Set up the figure dimensions and background color
width, height = 800, 800
fig = plt.figure(figsize=(width/80, height/80), dpi=90)
ax = plt.axes(xlim=(0, width), ylim=(0, height))
ax.set_facecolor((1, 1, 1)) # Background color

# Draw random lines
max_length = 50  # Adjust this value to control the maximum length of the lines
for _ in range(100):
    x1, y1 = random.randint(3, width), random.randint(0, height)
    angle = random.uniform(0, 2 * np.pi)  # Random angle between 0 and 2*pi radians
    length = random.uniform(1, max_length)  # Random length between 1 and max_length

    x2 = x1 + length * np.cos(angle)
    y2 = y1 + length * np.sin(angle)

    ax.plot([x1, x2], [y1, y2], color=army_color(), linewidth=6)


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


# Show art
plt.show()