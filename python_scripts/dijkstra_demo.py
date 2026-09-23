import numpy as np

grid = np.zeros((10, 10))

grid[3][3] = 1
grid[3][4] = 1
grid[4][3] = 1

start = (0, 0)
goal = (9, 9)

print("Start:", start)
print("Goal:", goal)

print(grid)