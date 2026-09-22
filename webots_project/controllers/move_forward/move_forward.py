from controller import Robot

robot = Robot()

TIME_STEP = 64

camera = robot.getDevice("camera")
camera.enable(TIME_STEP)

while robot.step(TIME_STEP) != -1:

    width = camera.getWidth()
    height = camera.getHeight()

    print(f"Camera Active: {width} x {height}")