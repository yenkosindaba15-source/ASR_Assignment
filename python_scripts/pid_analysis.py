import matplotlib.pyplot as plt

#PID Position Response:
#the controller will try to reach position 10 from position 0
desired_position = 10
current_position = 0

kp = 0.5

positions =[]
errors = []

for step in range(20):
    error = desired_position - current_position
    control_signal = kp * error
    current_position += control_signal
    positions.append(current_position)
    errors.append(error)

    print("\nPID Position Response\n")
    print(f"Step {step}:\n Position = {current_position:.2f} \n Error = {error:.2f} \n")

plt.title("P Controller Position Response")
plt.plot(positions)
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.grid(True)
plt.show()


#Error vs Time Analysis:
current_position = 0
errors = []

for step in range(20):
    error = desired_position - current_position
    control_signal = kp * error
    current_position += control_signal
    errors.append(error)

plt.title("PID Error vs Time")
plt.plot(errors, marker='o')
plt.xlabel("Time Step")
plt.ylabel("Error")
plt.grid(True)
plt.show()


#Desired vs Actual Position:
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


#Performance Summary:
#remarks for the report
current_position = 0
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