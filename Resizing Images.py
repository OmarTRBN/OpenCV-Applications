import os
import cv2

# Set the directory where the images are located
directory = r"C:\Users\omart\Desktop\new-data"

# Set the desired size for the images
width = 640
height = 640

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read the image
        im = cv2.imread(os.path.join(directory, filename))
        # Resize the image
        im = cv2.resize(im, (width, height), interpolation=cv2.INTER_AREA)
        # Save the resized image
        cv2.imwrite(os.path.join(directory, filename), im)
