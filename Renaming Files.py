import os

folder_path = '/path/to/folder'
counter = 1

for filename in os.listdir(folder_path):
    # check if file is an image (JPEG or PNG) and has a valid filename format
    if filename.endswith('.jpg') or filename.endswith('.png') and filename.startswith('IMG_'):
        new_filename = 'image_' + str(counter) + os.path.splitext(filename)[1]
        # rename file with new filename
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        counter += 1
