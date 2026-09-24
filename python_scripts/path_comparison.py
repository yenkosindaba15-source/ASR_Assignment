import matplotlib.pyplot as plt

dijkstra_length = 19
a_star_length = 19

algorithms = ["Dijkstra", "A*"]
path_lengths = [dijkstra_length, a_star_length]

plt.title("Path Length Comparison")
plt.bar(algorithms, path_lengths)
plt.xlabel("Algorithms")
plt.ylabel("Number of Nodes")

for i, value in enumerate(path_lengths):
    plt.text(i, value + 0.2, str(value), ha="center")

plt.show()