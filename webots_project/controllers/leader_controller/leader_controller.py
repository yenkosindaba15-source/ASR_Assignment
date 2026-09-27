from controller import Robot

robot = Robot()

TIME_STEP = 64

emitter = robot.getDevice("emitter")

print("LEADER ROBOT ACTIVE")

while robot.step(TIME_STEP) != -1:
    message = "MOVE FORWARD"
    emitter.send(message.encode("utf-8"))

    print("Leader sent:", message)