# creating 25 images for awake and drowsy
import os
import time
import cv2


labels = ['Awake', 'Drowsy']  # yawing
number_imgs = 50
cap = cv2.VideoCapture(0)
for label in labels:
    IMAGES_PATH = os.path.join('synthetic_data', label)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    for img_num in range(number_imgs):
        print('Collecting images for {}, image number {}'.format(label, img_num))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, str(img_num) + '.jpg')
        cv2.imwrite(imgname, frame)
        cv2.imshow('Image Collection', frame)
        time.sleep(2)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()