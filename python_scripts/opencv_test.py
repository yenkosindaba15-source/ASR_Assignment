import cv2
import numpy as np

# Create a simple test image
image = np.zeros((300, 300, 3), dtype=np.uint8)

# Draw a white rectangle
cv2.rectangle(image, (100, 100), (200, 200), (255, 255, 255), -1)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Edge detection
edges = cv2.Canny(gray, 50, 150)

cv2.imshow("Original Image", image)
cv2.imshow("Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()