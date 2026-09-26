from controller import Robot

robot = Robot()

TIME_STEP = 64

print("\nAVAILABE ROBOT DEVICES")
print('-------------------------------------------')

for index in range(robot.getNumberOfDevices()):
    device = robot.getDeviceByIndex(index)
    print(f"{index}: {device.getName()}")

print('-------------------------------------------')

while robot.step(TIME_STEP) != -1:
    pass