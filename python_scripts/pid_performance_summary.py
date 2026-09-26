#remarks for the report

import matplotlib.pyplot as plt

desired_position = 10
current_position = 0

kp = 0.3

positions = []
errors = []

for step in range(20):
    error = desired_position - current_position

    control_signal = kp * error

    current_position += control_signal

    positions.append(current_position)
    errors.append(error)

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].set_title("Position Response")
ax[0].plot(positions, marker='o')
ax[0].set_xlabel("Time Step")
ax[0].set_ylabel("Position")
ax[0].grid(True)

ax[1].set_title("Error Reduction")
ax[1].plot(errors, marker='o')
ax[1].set_xlabel("Time Step")
ax[1].set_ylabel("Error")
ax[1].grid(True)

plt.tight_layout()
plt.show()