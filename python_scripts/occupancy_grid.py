import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((10, 10))

#obstacles
grid[3][3] = 1
grid[3][4] = 1
grid[4][3] = 1
grid[7][8] = 1
grid[6][8] = 1

plt.imshow(grid, cmap='gray_r')
plt.title("Occupancy Grid Map")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.colorbar(label = "Obstacle")
plt.show()