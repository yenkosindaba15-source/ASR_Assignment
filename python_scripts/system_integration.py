import pandas as pd
import matplotlib.pyplot as plt

#Planned vs Actual Path:
planned_x = [0,1,2,3,4,5]
planned_y = [0,1,2,3,4,5]

actual_x = [0,1,1.8,3.1,4.2,5]
actual_y = [0,0.9,2.1,3.2,4.1,5]

plt.title("Planned Navigation Path vs Actual Robot Path")
plt.plot(planned_x, planned_y, marker='o',linewidth=2, label="Planned Path")
plt.plot(actual_x, actual_y, marker='*',linewidth=2, label="Actual Path")
plt.xlabel("Horizontal Grid Position")
plt.ylabel("Vertical Grid Position")
plt.legend()
plt.grid(True)
plt.show()


#Tracking Error:
actual_path = [0,0.9,1.8,3.1,4.2,5]

tracking_error = []

for planned, actual in zip(planned_x, actual_path):
    error = abs(planned - actual)
    tracking_error.append(error)

print("Tracking Errors:")

for i, error in enumerate(tracking_error):
    print(f"Point {i}: {error:.2f}")

plt.title("Tracking Error")
plt.plot(tracking_error, marker='o', linewidth=2)
plt.xlabel("Navigation Path Point")
plt.ylabel("Tracking Error (Position units)")
plt.grid(True)
plt.show()


#Travel Time Analysis:
navigation_stages = ['Planning', 'Movement', 'Obstacle Avoidance', 'Goal Reached']
travel_times = [0.5,3.2,1.1,0.2]

plt.title("Robot Navigation Travel Time Analysis")
plt.bar(navigation_stages, travel_times)
plt.xlabel("Navigation Stages")
plt.ylabel("Time (seconds)")

for i, value in enumerate(travel_times):
    plt.text(i, value + 0.05, str(value), ha='center')

plt.show()


#System Evaluation:
evaluation_data = {
    'Metric': ['Path Length', 'Dijkstra Runtime', 'A* Runtime', 'Dijkstra Nodes Explored', 'A* Nodes Explored'],
    'Values': [19, 0.0014338999753817916, 0.0009506999631412327, 97, 96]
}

results = pd.DataFrame(evaluation_data)

print("\nSYSTEM PERFORMANCE EVALUATION\n")
print(results.to_string(index=False))

#An entire summary of sensors, perception, occupancy grid, Dijkstra/A*, and PID control