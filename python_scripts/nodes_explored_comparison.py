import matplotlib.pyplot as plt
from fontTools.diff import color

algorithms = ["Dijkstra", "A*"]
nodes_explored = [97,96]

plt.title("Nodes Explored Comparison")
plt.bar(algorithms, nodes_explored, color="limegreen", width=0.3)
plt.xlabel("Algorithms")
plt.ylabel("Nodes Explored")

for i, value in enumerate(nodes_explored):
    plt.text(i, value + 0.2, str(value), ha='center')

plt.show()