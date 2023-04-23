import cv2
import os

# Define a function to display the bounding box on an image
# Parameters:
# - image_path: the path to the image file
# - file_path: the path to the corresponding label file (in txt format)
# The directory should have images and the corresponding annonations in YOLO format

def show_bbox(image_path, file_path):

    # Read the image and label file
    image = cv2.imread(image_path)
    txt_file = open(file_path)

    # Extract the bounding box coordinates from the label file
    coors = [float(i)*640.0 for i in txt_file.readlines()[0].split(' ')]
    xC, yC, h, w = int(coors[1]), int(coors[2]), int(coors[3]), int(coors[4])

    # Calculate the top left and bottom right coordinates of the bounding box
    top_left = [xC-int(h/2), yC-int(w/2)]
    bottom_right = [xC+int(h/2), yC+int(w/2)]

    # Draw the bounding box on the image
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 6)
    cv2.imshow('win', image)
    cv2.waitKey(100)


# Define the directory containing the images and labels
directory = r'directory'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the file is an image
    if filename.endswith('.jpg'):
        # Construct the paths to the image and label files
        image_path = r'{}\{}'.format(directory, filename)
        file_path = r'{}\{}.txt'.format(directory, filename[:-4])
        # Call the show_bbox function to display the bounding box on the image
        show_bbox(image_path, file_path)
    else:
        pass
