from controller import Robot

robot = Robot()

TIME_STEP = 64
MAX_SPEED = 6.28

emitter = robot.getDevice("emitter")
receiver = robot.getDevice("receiver")

receiver.enable(TIME_STEP)

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)


sensor_names = ["ps0", "ps1", "ps2", "ps3", "ps4", "ps5", "ps6", "ps7"]

distance_sensors = []

for sensor_name in sensor_names:
    sensor = robot.getDevice(sensor_name)
    sensor.enable(TIME_STEP)
    distance_sensors.append(sensor)


robot_name = robot.getName()

# Each robot starts with a different preferred speed
if robot_name == "leader":
    consensus_value = 1.0

elif robot_name == "worker1":
    consensus_value = 3.0

else:
    consensus_value = 5.0

iteration = 0
broadcast_counter = 0
received_values = []

def limit_speed(speed):
    return max(-MAX_SPEED, min(MAX_SPEED, speed))

def obstacle_detected():
    sensor_values = []

    for sensor in distance_sensors:
        sensor_values.append(sensor.getValue())

    front_sensor_values = [
        sensor_values[0],
        sensor_values[1],
        sensor_values[6],
        sensor_values[7]
    ]

    return max(front_sensor_values) > 600

print(f"{robot_name} started with consensus value {consensus_value:.2f}")

while robot.step(TIME_STEP) != -1:
    broadcast_counter += 1

    # Broadcasting this robot's current state
    if broadcast_counter >= 10:
        message = (f"{robot_name}: {consensus_value}")

        emitter.send(message.encode("utf-8"))

        broadcast_counter = 0

    # Receiving states broadcast by other robots
    while receiver.getQueueLength() > 0:
        received_message = receiver.getString()
        message_parts = received_message.split(":")

        if len(message_parts) == 2:
            sender_name = message_parts[0]
            sender_value = float(message_parts[1])

            if sender_name != robot_name:
                received_values.append(sender_value)

        receiver.nextPacket()

    # Applying the local average-consensus rule
    if len(received_values) > 0:
        total_value = consensus_value

        for value in received_values:
            total_value += value

        local_average = total_value / (len(received_values) + 1)
        consensus_value += 0.3 * (local_average - consensus_value)

        received_values.clear()

        iteration += 1

        print(f"{robot_name} | Iteration {iteration} | Consensus value: {consensus_value:.3f}")

    movement_speed = limit_speed(consensus_value)

    # Every robot applies the same local movement rules
    if obstacle_detected():
        left_motor.setVelocity(-1.5)
        right_motor.setVelocity(1.5)

    else:
        left_motor.setVelocity(movement_speed)
        right_motor.setVelocity(movement_speed)