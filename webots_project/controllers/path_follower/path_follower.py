from controller import Robot
import math
import csv

robot = Robot()

TIME_STEP = 64

WHEEL_RADIUS = 0.0205
AXLE_LENGTH = 0.052

MAX_SPEED = 6.28
FORWARD_SPEED = 2.5

KP = 3.0
KI = 0.01
KD = 0.25

WAYPOINT_TOLERANCE = 0.025
OBSTACLE_THRESHOLD = 100

# Get the wheel motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Get the wheel encoders
left_encoder = robot.getDevice("left wheel sensor")
right_encoder = robot.getDevice("right wheel sensor")

left_encoder.enable(TIME_STEP)
right_encoder.enable(TIME_STEP)

# Get the distance sensors
sensor_names = ["ps0","ps1","ps2","ps3","ps4","ps5","ps6","ps7"]

distance_sensors = []

for sensor_name in sensor_names:
    sensor = robot.getDevice(sensor_name)
    sensor.enable(TIME_STEP)
    distance_sensors.append(sensor)

# Get the camera
camera = robot.getDevice("camera")
camera.enable(TIME_STEP)

# Planned waypoints in metres
waypoints = [
    (0.00, 0.00),
    (0.15, 0.00),
    (0.15, 0.15),
    (0.30, 0.15)
]

# Estimated robot position
x_position = 0.0
y_position = 0.0
heading = 0.0

# Previous encoder readings
previous_left_position = 0.0
previous_right_position = 0.0

# Start from the second waypoint
# The first waypoint represents the robot's starting position
current_waypoint = 1

# PID values
previous_error = 0.0
integral_error = 0.0

# Store the actual path followed by the robot
actual_path = []

start_time = robot.getTime()

def keep_angle_in_range(angle):
    while angle > math.pi:
        angle -= 2 * math.pi

    while angle < -math.pi:
        angle += 2 * math.pi

    return angle


def limit_speed(speed):
    return max(-MAX_SPEED, min(MAX_SPEED, speed))

def update_odometry():
    global x_position
    global y_position
    global heading
    global previous_left_position
    global previous_right_position

    current_left_position = left_encoder.getValue()
    current_right_position = right_encoder.getValue()

    left_rotation = (current_left_position - previous_left_position)
    right_rotation = (current_right_position - previous_right_position)

    previous_left_position = current_left_position
    previous_right_position = current_right_position

    left_distance = left_rotation * WHEEL_RADIUS
    right_distance = right_rotation * WHEEL_RADIUS

    centre_distance = (left_distance + right_distance) / 2

    heading_change = (right_distance - left_distance) / AXLE_LENGTH

    heading = keep_angle_in_range(heading + heading_change)

    x_position += (centre_distance * math.cos(heading))
    y_position += (centre_distance * math.sin(heading))

def obstacle_in_front():
    sensor_values = []

    for sensor in distance_sensors:
        sensor_values.append(sensor.getValue())

    front_values = [
        sensor_values[0],
        sensor_values[1],
        sensor_values[6],
        sensor_values[7]
    ]

    return max(front_values) > OBSTACLE_THRESHOLD

def save_actual_path():
    with open("actual_path.csv", "w", newline="") as path_file:
        writer = csv.writer(path_file)
        writer.writerow(["x_position", "y_position"])
        writer.writerows(actual_path)


# Allow the encoders to produce their first readings
robot.step(TIME_STEP)

previous_left_position = left_encoder.getValue()
previous_right_position = right_encoder.getValue()


print("PATH FOLLOWING STARTED")
print("----------------------")


while robot.step(TIME_STEP) != -1:
    update_odometry()

    actual_path.append((x_position, y_position))

    # Capture the current camera image
    camera_image = camera.getImage()

    # Check whether all waypoints have been completed
    if current_waypoint >= len(waypoints):
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)

        travel_time = robot.getTime() - start_time

        save_actual_path()

        print("----------------------")
        print("GOAL REACHED")
        print(f"Travel time: {travel_time:.2f} seconds")
        print(f"Final X position: {x_position:.3f} m")
        print(f"Final Y position: {y_position:.3f} m")
        print("Actual path saved to actual_path.csv")

        break

    target_x, target_y = waypoints[current_waypoint]

    x_error = target_x - x_position
    y_error = target_y - y_position

    distance_to_waypoint = math.sqrt(x_error ** 2 + y_error ** 2)

    desired_heading = math.atan2(y_error, x_error)

    heading_error = keep_angle_in_range(desired_heading - heading)

    # moves to the next waypoint when close enough
    if distance_to_waypoint < WAYPOINT_TOLERANCE:
        print(f"Waypoint {current_waypoint} reached: ({target_x:.2f}, {target_y:.2f})")

        current_waypoint += 1

        integral_error = 0.0
        previous_error = 0.0

        continue

    # Use the front sensors for obstacle detection
    if obstacle_in_front():
        print("Obstacle detected: avoidance turn")

        left_speed = -1.5
        right_speed = 1.5

    else:
        time_seconds = TIME_STEP / 1000

        integral_error += (heading_error * time_seconds)
        derivative_error = (heading_error - previous_error) / time_seconds
        correction = (KP * heading_error + KI * integral_error + KD * derivative_error)

        previous_error = heading_error

        # Slow down while making a large turn
        if abs(heading_error) > 0.35:
            forward_speed = 0.5
        else:
            forward_speed = FORWARD_SPEED

        left_speed = (forward_speed - correction)
        right_speed = (forward_speed + correction)

        left_motor.setVelocity(limit_speed(left_speed))
        right_motor.setVelocity(limit_speed(right_speed))

        print(f"Waypoint {current_waypoint} | Position: ({x_position:.3f}, {y_position:.3f}) | Distance: {distance_to_waypoint:.3f} m | Heading error: {heading_error:.3f} rad")