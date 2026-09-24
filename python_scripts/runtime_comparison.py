import matplotlib.pyplot as plt

algorithms = ["Dijkstra", "A*"]
runtimes = [0.0014338999753817916, 0.0009506999631412327]


plt.title("Runtime Comparison")
plt.bar(algorithms, runtimes, color="green")
plt.xlabel("Algorithms")
plt.ylabel("Execution Time (seconds)")


for i, value in enumerate(runtimes):
    plt.text(i, value + 0.00005, f"{value:.6f}", ha="center")

plt.show()