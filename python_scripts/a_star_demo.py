import numpy as np
import heapq
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import ListedColormap
import time

grid = np.zeros((10, 10))

# Obstacles
grid[3][3] = 1
grid[3][4] = 1
grid[4][3] = 1

start = (0, 0)
goal = (9, 9)

rows, cols = grid.shape

directions = [
    (-1, 0),(1, 0),
    (0, -1),(0, 1)
]

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def a_star(grid, start, goal):
    open_nodes = [(0, start)]

    cost_so_far = {start: 0}
    parent_nodes = {}
    nodes_explored = 0

    while open_nodes:
        nodes_explored += 1
        _, current = heapq.heappop(open_nodes)

        if current == goal:
            break

        for dx, dy in directions:
            next_node = (
                current[0] + dx,
                current[1] + dy
            )
            x, y = next_node

            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0:
                new_cost = cost_so_far[current] + 1

                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost

                    priority = new_cost + heuristic(next_node, goal)
                    heapq.heappush(open_nodes, (priority, next_node))
                    parent_nodes[next_node] = current

    path = []
    current = goal

    while current in parent_nodes:
        path.append(current)
        current = parent_nodes[current]

    path.append(start)
    path.reverse()

    return path, nodes_explored

start_time = time.perf_counter()
path, nodes_explored = a_star(grid, start, goal)
end_time = time.perf_counter()
runtime = end_time - start_time

print("Path Length:", len(path))
print("Nodes Explored: ", nodes_explored) #96
print("Runtime:", runtime)

for x, y in path:
    grid[x][y] = 2

custom_map = ListedColormap(["White", "Black", "Limegreen"])
plt.imshow(grid, cmap=custom_map)

legend_elements = [
    Patch(facecolor='White', label='Free Space'),
    Patch(facecolor='Black', label='Obstacle'),
    Patch(facecolor='Limegreen', label='A* Path')
]

plt.legend(handles=legend_elements)

plt.title("A* Path")
plt.xlabel("X Position")
plt.ylabel("Y Position")

plt.show()