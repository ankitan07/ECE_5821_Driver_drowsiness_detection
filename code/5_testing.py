# testing firs ton an image on best.pt weight
model_1 = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/train_without_test/weights/best.pt',
                         force_reload=True)

data_dir = 'datapreprocessing/Dataset/'
data = {'Label': [], 'Total_Image': [], 'D_Label': [], 'A_Label': [], 'Y_Label': []}

count = 0  # just to show only one pciture detected with 2 frame

for label in os.listdir(data_dir):
    label_dir = os.path.join(data_dir, label)
    total_image, D_label, A_label, Y_label = 0, 0, 0, 0
    if os.path.isdir(label_dir):
        for image_file in os.listdir(label_dir):
            if image_file.lower().endswith('.jpg'):
                total_image += 1
                img = os.path.join(data_dir, label, image_file)
                results = model_1(img)

                results = str(results)

                labels_start = results.find("1 ")  # Find the start of label information
                labels_end = results.find("Speed:")  # Find the end of label information
                labels_info = results[labels_start:labels_end].strip()
                labels_info = sorted(labels_info.split(','))
                labels_info = [label.lower().strip() for label in labels_info]
                D_label += labels_info.count('1 drowsy')
                A_label += labels_info.count('1 awake')
                Y_label += labels_info.count('1 yawn')

                # print if 2 frame detected
                if len(labels_info) > 1 and count == 0:
                    count == 1
                    results = model_1(img)
                    %matplotlib
                    inline
                    plt.imshow(np.squeeze(results.render()))
                    plt.show()

    print(label, ":\n", "total_image: ", total_image, "D_label : ", D_label, "A_label : ", A_label, "Y_label : ",
          Y_label)
    data['Label'].append(label)
    data['Total_Image'].append(total_image)
    data['D_Label'].append(D_label)
    data['A_Label'].append(A_label)
    data['Y_Label'].append(Y_label)

label_best_weigth_mapping_df = pd.DataFrame(data)
label_best_weigth_mapping_df