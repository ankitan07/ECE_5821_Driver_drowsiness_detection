# creating 25 images for awake and drwosy
labels = ['Awake', 'Drowsy']  # yawing
number_imgs = 50
# collect iamge from video
cap = cv2.VideoCapture(0)  # camera index 0
# Loop through labels
for label in labels:
    IMAGES_PATH = os.path.join('synthetic_data', label)
    print('Collecting images for {}'.format(label))
    time.sleep(5)

    # Loop through image range
    for img_num in range(number_imgs):
        print('Collecting images for {}, image number {}'.format(label, img_num))

        # Webcam feed
        ret, frame = cap.read()

        # Naming out image path
        imgname = os.path.join(IMAGES_PATH, str(img_num) + '.jpg')

        # Writes out image to file 
        cv2.imwrite(imgname, frame)

        # Render to the screen
        cv2.imshow('Image Collection', frame)

        # 2 second delay between captures
        time.sleep(2)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()