from controller import Robot

robot = Robot()
TIME_STEP = 64

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

left_motor.setVelocity(3.0)
right_motor.setVelocity(3.0)

sensor_names = [ #The robot's "eyes".
    'ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7'
]
sensors = []

for name in sensor_names:
    sensor = robot.getDevice(name)
    sensor.enable(TIME_STEP)
    sensors.append(sensor)

while robot.step(TIME_STEP) != -1:
    values = [sensor.getValue() for sensor in sensors]

    obstacle_detected = (
        values[0] > 500 or
        values[1] > 500 or
        values[6] > 500 or
        values[7] > 500
    )

    if obstacle_detected:
        print("WALL DETECTED")
        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
    else:
        print("MOVING FORWARD")
        left_motor.setVelocity(3.0)
        right_motor.setVelocity(3.0)