import cv2
import _thread as thread
import time
import keyboard
import os
import uuid

cap = cv2.VideoCapture(1)
labels = ['green', 'black', 'blue', 'white']
number_imgs = 15
IMAGES_PATH = os.path.join('images')

def savePictures(a):
   for label in labels:
      if labels.index(label) == 0:
        input("First Set is {} Press Enter to Start".format(label))

      for imgnum in range(number_imgs):
         print('Collecting image {}'.format(imgnum + 1))
         ret, frame = cap.read()
         imgname = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(imgnum + 1)))
         cv2.imwrite(imgname, frame[50:180, 100:300])
         time.sleep(30)

         if cv2.waitKey(1) & 0xFF == ord('q'):
            break

      if(labels.index(label) + 1 == len(labels)):
         print("Done!")
         break

      input("Next Set is {} Press Enter to Continue".format(labels[labels.index(label) + 1]))

keyboard.on_press_key("p", savePictures)

while True:
   a, frame = cap.read()
   cv2.imshow('frame', frame[50:180, 100:300])

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break




