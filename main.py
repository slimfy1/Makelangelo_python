import cv2
import datetime
import os
from photo import make
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if cap.isOpened() == False:
    print("Error opening video stream or file")

print("This is preview mode \nTo make photo press 's' button on your keybord \nTo close app press 'q'")

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.rectangle(frame,(220,120),(460,360),(0,255,0),3)
        frame = cv2.medianBlur(frame, 3)
        cv2.imshow('image', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(2) & 0xFF == ord('s'):
            currentDT = datetime.datetime.now()
            make(currentDT.strftime("%Y%m%d%H%M%S"), frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()