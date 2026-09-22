import numpy as np

grid = np.zeros((10, 10))

grid[3][3] = 1
grid[3][4] = 1
grid[4][3] = 1

print(grid)