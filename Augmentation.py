import cv2
import numpy as np

# Load image
img = cv2.imread(r'C:\Users\omart\Desktop\testete\1.jpg')

# Define the transformations to apply
flip_code = np.random.choice([-1, 0, 1])
rotation_angle = np.random.randint(-30, 30)
scale_factor = np.random.uniform(0.5, 1.5)
translation_x = np.random.randint(-50, 50)
translation_y = np.random.randint(-50, 50)

# Apply the transformations
img = cv2.flip(img, flip_code)
rows, cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), rotation_angle, scale_factor)
img = cv2.warpAffine(img, M, (cols, rows))
M = np.float32([[1, 0, translation_x], [0, 1, translation_y]])
img = cv2.warpAffine(img, M, (cols, rows))

# Save the augmented image
cv2.imwrite('augmented_image.jpg', img)
