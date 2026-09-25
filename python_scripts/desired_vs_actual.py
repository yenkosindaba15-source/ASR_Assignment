import matplotlib.pyplot as plt

desired_position = 10
current_position = 0

kp = 0.3

actual_positions = []
desired_positions = []

for step in range(20):
    error = desired_position - current_position

    control_signal = kp * error

    current_position += control_signal

    actual_positions.append(current_position)
    desired_positions.append(desired_position)

plt.title("Desired vs Actual Position")
plt.plot(desired_positions, linestyle="--", linewidth=2, label="Desired Position")
plt.plot(actual_positions, linewidth=2, marker="o", label="Actual Position")
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.show()