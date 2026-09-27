from controller import Robot

robot = Robot()

TIME_STEP = 64

emitter = robot.getDevice("emitter")

commands = ["MOVE_FORWARD", "TURN_LEFT"]

command_index = 0
counter = 0

print("LEADER ROBOT ACTIVE")

while robot.step(TIME_STEP) != -1:
    counter += 1
    if counter % 50 == 0:
        message = commands[command_index]
        emitter.send(message.encode("utf-8"))

        print("Leader sent:", message)

        command_index = (command_index + 1) % len(commands)