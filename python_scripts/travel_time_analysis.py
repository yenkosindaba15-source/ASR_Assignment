import matplotlib.pyplot as plt

navigation_stages = ['Planning', 'Movement', 'Obstacle Avoidance', 'Goal Reached']
travel_times = [0.5,3.2,1.1,0.2]

plt.title("Robot Navigation Travel Time Analysis")
plt.bar(navigation_stages, travel_times)
plt.xlabel("Navigation Stages")
plt.ylabel("Time (seconds)")

for i, value in enumerate(travel_times):
    plt.text(i, value + 0.05, str(value), ha='center')

plt.show()