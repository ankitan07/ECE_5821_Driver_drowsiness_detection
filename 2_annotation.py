# Path to the directory containing your labeled data

import os
import cv2

data_dir = 'datapreprocessing/Dataset/'
annotation_labels_dir = 'datapreprocessing/Labels/'
annotation_images_dir = 'datapreprocessing/Annotation_images/'
multiple_dir = 'datapreprocessing/multiple/'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
class_index = 0

for label in os.listdir(data_dir):
    '''------------------------------------------------------
        Labelling the image according to the folder they are in
    ------------------------------------------------------'''
    if label == "Awake":
        class_index = 0
    elif label == "Drowsy":
        class_index = 1
    else:  # yawn
        class_index = 2

    total_image, no_face, multiple_face = 0, 0, 0
    label_dir = os.path.join(data_dir, label)
    if os.path.isdir(label_dir):
        annotation_label_dir = os.path.join(annotation_labels_dir, label)
        os.makedirs(annotation_label_dir, exist_ok=True)
        annotation_image_dir = os.path.join(annotation_images_dir, label)
        os.makedirs(annotation_image_dir, exist_ok=True)

        for image_file in os.listdir(label_dir):
            if image_file.lower().endswith('.jpg'):
                total_image += 1
                image_path = os.path.join(label_dir, image_file)

                '''------------------------------------------------------
                annotating the data and image and saving them using cv2
                ------------------------------------------------------'''

                image = cv2.imread(image_path)
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=6, minSize=(300, 300))

                if len(faces) == 1:  # Limit to one face detection per image
                    x, y, w, h = faces[0]

                    annotation_path = os.path.join(annotation_label_dir,
                                                   f'{label}_{os.path.splitext(image_file)[0]}.txt')
                    with open(annotation_path, 'w') as annotation_file:
                        img_height, img_width, _ = image.shape
                        x_center = (x + w / 2) / img_width
                        y_center = (y + h / 2) / img_height
                        width = w / img_width
                        height = h / img_height
                        annotation_file.write(f'{class_index} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n')

                    # Save annotated image
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    new_image_name = f'{label}_{image_file}'
                    new_image_path = os.path.join(annotation_image_dir, new_image_name)
                    cv2.imwrite(new_image_path, image)

                elif len(faces) == 0:
                    no_face += 1
                else:
                    multiple_face += 1
                    x, y, w, h = faces[0]
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    new_image_name = f'{label}_{image_file}'
                    new_image_path = os.path.join(multiple_dir, new_image_name)
                    cv2.imwrite(new_image_path, image)

                '''------------------------------------------------------
                renaming images with label name and deleteing rest of the image 
                ------------------------------------------------------'''
                if len(faces) == 1:
                    new_image_name = f'{label}_{image_file}'
                    new_image_path = os.path.join(label_dir, new_image_name)
                    os.rename(image_path, new_image_path)
                else:
                    os.remove(image_path)

        print(label, "total_image", total_image, (total_image - no_face - multiple_face) / total_image, "no_face",
              no_face, no_face / total_image, "\nmultiple_face", multiple_face, multiple_face / total_image)
