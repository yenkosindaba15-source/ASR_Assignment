import matplotlib.pyplot as plt

planned_path = [0,1,2,3,4,5]
actual_path = [0,0.9,1.8,3.1,4.2,5]

tracking_error = []

for planned, actual in zip(planned_path, actual_path):
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