import matplotlib.pyplot as plt

desired_position = 10

kp_values = [0.1, 0.3, 0.8]

for kp in kp_values:
    current_position = 0

    positions = []

    for step in range(20):
        error = desired_position - current_position

        control_signal = kp * error

        current_position += control_signal

        positions.append(current_position)

plt.title("Kp Tuning Comparison")
plt.plot(positions, marker='o', linewidth=2, label= f"Kp = {kp}")
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.legend()
plt.grid(True)
plt.show()