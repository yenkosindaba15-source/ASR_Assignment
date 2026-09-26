import pandas as pd

evaluation_data = {
    'Metric': ['Path Length', 'Dijkstra Runtime', 'A* Runtime', 'Dijkstra Nodes Explored', 'A* Nodes Explored'],
    'Values': [19, 0.0014338999753817916, 0.0009506999631412327, 97, 96]
}

results = pd.DataFrame(evaluation_data)

print("\nSYSTEM PERFORMANCE EVALUATION\n")
print(results.to_string(index=False))

#An entire summary of sensors, perception, occupancy grid, Dijkstra/A*, and PID control