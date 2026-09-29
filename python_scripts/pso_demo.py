import matplotlib.pyplot as plt

particle_positions = [10,50,80]
target_position = 30

history = []

for iteration in range(10):
    history.append(particle_positions.copy())

    for i in range(len(particle_positions)):
        particle_positions[i] += (target_position - particle_positions[i]) * 0.3


for particle in range(3):
    particle_history = []

    for step in history:
        particle_history.append(step[particle])

    plt.plot(particle_history,marker="o", label=f"Particle {particle + 1}")

plt.title("Particle Swarm Optimization Convergence")
plt.axhline(y=target_position, linestyle="--", label="Target Position", color='red')
plt.xlabel("Iteration")
plt.ylabel("Particle Position")
plt.legend()
plt.grid(True)
plt.show()