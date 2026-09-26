import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

grid = np.zeros((10, 10))

#obstacles
grid[3][3] = 1
grid[3][4] = 1
grid[4][3] = 1
grid[7][8] = 1
grid[6][8] = 1

plt.imshow(grid, cmap='gray_r')
plt.title("Occupancy Grid Environment Map")
plt.xlabel("Horizontal Grid Position")
plt.ylabel("Vertical Grid Position")

#Key
legend_elements = [
    Patch(facecolor='white', edgecolor='black', label='Free Space'),
    Patch(facecolor='black', edgecolor='black', label='Obstacle')
]
plt.legend(handles = legend_elements, loc = 'upper right')
plt.show()