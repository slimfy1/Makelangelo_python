import cv2
import numpy as np
import datetime
import os

def make(numb, name):
    print("\nThis is save mode \nTo make photo press 'o' button on your keybord \nor if you want to make photo again press 'r' ")
    in_name = "img/source/th{}.png".format(numb)
    cv2.imwrite(in_name, name)
    img = cv2.imread(in_name, 0)
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 11, 2)
    imS = cv2.resize(th3, (1024, 768))  # Resize image
    cropped = imS[240:580, 360:720]
    cv2.imshow("cropped", cropped)

    for x in range(0, 99999):

        if cv2.waitKey(2) & 0xFF == ord('o'):
            cv2.waitKey(100)
            out_name = "img/th{}.png".format(numb)
            cv2.imwrite(out_name, cropped)
            cv2.destroyWindow('cropped')
            os.remove(in_name)
            cv2.waitKey(1)
            print("make")
            break
        if cv2.waitKey(2) & 0xFF == ord('r'):
            cv2.waitKey(100)
            out_name = "img/th{}.png".format(numb)
            os.remove(in_name)
            print("remake")
            cv2.destroyWindow('cropped')
            break