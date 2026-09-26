import matplotlib.pyplot as plt

planned_x = [0,1,2,3,4,5]
planned_y = [0,1,2,3,4,5]

actual_x = [0,1,1.8,3.1,4.2,5]
actual_y = [0,0.9,2.1,3.2,4.1,5]

plt.title("Planned Navigation Path vs Actual Robot Path")
plt.plot(planned_x, planned_y, marker='o',linewidth=2, label="Planned Path")
plt.plot(actual_x, actual_y, marker='*',linewidth=2, label="Actual Path")
plt.xlabel("Horizontal Grid Position")
plt.ylabel("Vertical Grid Position")
plt.legend()
plt.grid(True)
plt.show()