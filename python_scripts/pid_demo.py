import matplotlib.pyplot as plt

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

    print(f"Step {step}:\n Position = {current_position:.2f} \n Error = {error:.2f} \n")

plt.title("P Controller Position Response")
plt.plot(positions)
plt.xlabel("Time Step")
plt.ylabel("Position")
plt.grid(True)
plt.show()