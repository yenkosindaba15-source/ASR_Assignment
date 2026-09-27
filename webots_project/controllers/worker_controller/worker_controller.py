from controller import Robot

robot = Robot()

TIME_STEP = 64

receiver = robot.getDevice("receiver")
receiver.enable(TIME_STEP)

print("WORKER ROBOT ACTIVE")

while robot.step(TIME_STEP) != -1:
    while receiver.getQueueLength() > 0:
        message = receiver.getString()

        print("Worker received:", message)

        receiver.nextPacket()