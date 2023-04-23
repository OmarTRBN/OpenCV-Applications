import cv2
import os

# in txt : [class, center_x, center_y, width, height]
# for drawing function : (img, top_left_coor, bottom_right_coor, color, thickness) 

# directory with labels and images
directory = r'C:\Users\omart\Desktop\yolov3-new'

def show_bbox(image_path, file_path):

    image = cv2.imread(image_path)
    txt_file = open(file_path)

    coors = [float(i)*640.0 for i in txt_file.readlines()[0].split(' ')]
    xC, yC, h, w = int(coors[1]), int(coors[2]), int(coors[3]), int(coors[4])

    top_left = [xC-int(h/2), yC-int(w/2)]
    bottom_right = [xC+int(h/2), yC+int(w/2)]

    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 6)
    cv2.imshow('win', image)
    cv2.waitKey(100)

for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
        image_path = r'{}\{}'.format(directory,filename)
        file_path = r'{}\{}.txt'.format(directory,filename[:-4])
        show_bbox(image_path, file_path)
    else:
        pass


