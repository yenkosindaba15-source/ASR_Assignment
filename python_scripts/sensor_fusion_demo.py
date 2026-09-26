import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Distance sensor obstacle detection
distance_sensor_obstacle = 1

# Camera obstacle detection
camera_obstacle = 1

# Simple sensor fusion
fused_obstacle = max(distance_sensor_obstacle, camera_obstacle)

# Environment map
grid = np.zeros((10, 10))

if fused_obstacle:
    grid[5][5] = 1

plt.imshow(grid, cmap="gray_r")

plt.title("Fused Environment Obstacle Map")
plt.xlabel("Horizontal Grid Position")
plt.ylabel("Vertical Grid Position")

legend_elements = [
    Patch(facecolor='white', edgecolor='black', label='Free Space'),
    Patch(facecolor='black', edgecolor='black', label='Obstacle')
]
plt.legend(handles = legend_elements, loc = 'upper right')

plt.show()

