import matplotlib.pyplot as plt

#PSO:
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

#Consensus:
leader_value = 10
worker1_value = 20
worker2_value = 30

history_leader = []
history_worker1 = []
history_worker2 = []

for iteration in range(10):
    average = (leader_value + worker1_value + worker2_value) / 3

    leader_value = average
    worker1_value = average
    worker2_value = average

    history_leader.append(leader_value)
    history_worker1.append(worker1_value)
    history_worker2.append(worker2_value)

plt.title("Consensus Convergence")
plt.plot(history_leader, marker="o", label="Leader")
plt.plot(history_worker1, marker="s",label="Worker 1")
plt.plot(history_worker2,marker="*",label="Worker 2")
plt.xlabel("Consensus Iteration")
plt.ylabel("Shared Decision Value")
plt.legend()
plt.grid(True)
plt.show()