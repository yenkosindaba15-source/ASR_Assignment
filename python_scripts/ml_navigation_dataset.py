import numpy as np
import pandas as pd

np.random.seed(42)

samples = 1200

dataset_rows = []

for sample_number in range(samples):
    left_sensor = np.random.randint(0, 1001)
    front_left_sensor = np.random.randint(0, 1001)
    front_right_sensor = np.random.randint(0, 1001)
    right_sensor = np.random.randint(0, 1001)

    front_obstacle = max(front_left_sensor,front_right_sensor)

    if front_obstacle < 400:
        action = "MOVE_FORWARD"

    elif left_sensor < right_sensor:
        action = "TURN_LEFT"

    else:
        action = "TURN_RIGHT"

    dataset_rows.append([left_sensor, front_left_sensor, front_right_sensor, right_sensor, action])


column_names = ["left_sensor", "front_left_sensor", "front_right_sensor", "right_sensor", "action"]


navigation_dataset = pd.DataFrame(dataset_rows, columns=column_names)
navigation_dataset.to_csv("../data/navigation_dataset.csv",index=False)

print("\nNAVIGATION DATASET")

print(f"Number of samples: {len(navigation_dataset)}")

print("\nFirst five rows:")
print(navigation_dataset.head())

print("\nAction distribution:")
print(navigation_dataset["action"].value_counts())