import numpy as np
import heapq
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import ListedColormap

from python_scripts.occupancy_grid import legend_elements

grid = np.zeros((10, 10))

# Obstacles
grid[3][3] = 1
grid[3][4] = 1
grid[4][3] = 1

start = (0, 0)
goal = (9, 9)

rows, cols = grid.shape

directions = [
    (-1, 0), (1, 0),
    (0, -1), (0, 1)
]


def dijkstra(grid, start, goal):

    queue = [(0, start)]

    distances = {start: 0}
    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == goal:
            break

        for dx, dy in directions:
            neighbor = (
                current_node[0] + dx,
                current_node[1] + dy
            )

            x, y = neighbor

            if (0 <= x < rows and 0 <= y < cols and grid[x][y] == 0):
                new_distance = current_distance + 1

                if (neighbor not in distances or new_distance < distances[neighbor]):
                    distances[neighbor] = new_distance
                    previous[neighbor] = current_node

                    heapq.heappush(queue,(new_distance, neighbor))
    path = []
    current = goal

    while current in previous:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return path

path = dijkstra(grid, start, goal)

for x, y in path:
    grid[x][y] = 2

#Matplotlib
plt.title("Dijkstra Path")

custom_map = ListedColormap(["White", "Black", "Green"])
plt.imshow(grid, cmap=custom_map)

legend_elements = [
    Patch(facecolor='white', label='Free Space'),
    Patch(facecolor='black', label='Obstacle'),
    Patch(facecolor='green', label='Dijkstra Path')
]
plt.legend(handles=legend_elements, loc='upper right')

plt.xlabel('X Position')
plt.ylabel('Y Position')

plt.show()