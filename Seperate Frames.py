import cv2

filepath = r"C:\Users\omart\Desktop\IKA\Videos\20221111_151217.mp4"

# Open the video file
video = cv2.VideoCapture(filepath)

# Set the frame skip interval
frame_skip = 10

# Initialize frame counter
frame_counter = 0

# Loop through the frames of the video
while True:
  # Grab the next frame
  success, frame = video.read()

  if not success:
    break

  frame = cv2.flip(frame,-1)
  frame = cv2.resize(frame,(900,900))

  # If there are no more frames left, break out of the loop

  # If the frame skip counter is zero, save the current frame
  if frame_counter % 10 == 0:
    cv2.imwrite(r"C:\Users\omart\Desktop\New folder\frame_{}.jpg".format(frame_counter), frame)

  # Increment the frame counter and reset it to zero if it has reached the frame skip interval
  frame_counter = frame_counter + 1