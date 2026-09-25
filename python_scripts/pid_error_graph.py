import matplotlib.pyplot as plt

desired_position = 10
current_position = 0

kp = 0.5

errors = []

for step in range(20):
    error = desired_position - current_position
    control_signal = kp * error
    current_position += control_signal
    errors.append(error)

plt.title("PID Error vs Time")
plt.plot(errors, marker='o')
plt.xlabel("Time Stop")
plt.ylabel("Error")
plt.grid(True)
plt.show()