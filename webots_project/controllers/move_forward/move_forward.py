from controller import Robot

robot = Robot()

TIME_STEP = 64

camera = robot.getDevice("camera")
camera.enable(TIME_STEP)

count = 0

while robot.step(TIME_STEP) != -1:
    image = camera.getImage()

    if image is not None:
        count += 1

        if count % 50 == 0:
            print("Image Captured Successfully.")