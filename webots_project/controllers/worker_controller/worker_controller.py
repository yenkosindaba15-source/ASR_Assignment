from controller import Robot

robot = Robot()

TIME_STEP = 64

receiver = robot.getDevice("receiver")
receiver.enable(TIME_STEP)

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

left_motor.setVelocity(0)
left_motor.setVelocity(0)

print("WORKER ROBOT ACTIVE")

while robot.step(TIME_STEP) != -1:
    while receiver.getQueueLength() > 0:
        message = receiver.getString()

        print("Worker received:", message)

        if message == "MOVE_FORWARD":
            left_motor.setVelocity(3.0)
            right_motor.setVelocity(3.0)

        receiver.nextPacket()