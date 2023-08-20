# Set the path to the directory containing your labeled data and annotations
data_dir = 'datapreprocessing/Dataset/'
annotation_labels_dir = 'datapreprocessing/Labels/'

train_dir = 'preprocessed_data/train/'
validate_dir = 'preprocessed_data/validate/'

train_ratio = 0.7
validate_ratio = 0.3

# Iterate through each subfolder (label)
for label in os.listdir(data_dir):
    image_dir = os.path.join(data_dir, label)
    annotation_label_dir = os.path.join(annotation_labels_dir, label)
    if os.path.isdir(image_dir) and os.path.isdir(annotation_label_dir):

        image_files = [f for f in os.listdir(image_dir) if f.lower().endswith('.jpg')]

        total_images = len(image_files)

        random.shuffle(image_files)

        train_split = int(total_images * train_ratio)
        validate_split = total_images - train_split

        train_images = image_files[:train_split]
        validate_images = image_files[train_split:]

        for split, split_dir in [(train_images, train_dir), (validate_images, validate_dir)]:

            new_image_dir = os.path.join(split_dir, 'images')
            new_label_dir = os.path.join(split_dir, 'labels')

            os.makedirs(new_image_dir, exist_ok=True)
            os.makedirs(new_label_dir, exist_ok=True)

            for image_file in split:
                print("image_file:", image_file)
                # Move images to the split directory
                image_source_path = os.path.join(image_dir, image_file)
                image_destination_path = os.path.join(new_image_dir, image_file)
                shutil.copy2(image_source_path, image_destination_path)
                print(f'Copied image : {image_file}')

                # copy annotation
                label_source_path = os.path.join(annotation_label_dir, f'{os.path.splitext(image_file)[0]}.txt')
                label_destination_path = os.path.join(new_label_dir, f'{os.path.splitext(image_file)[0]}.txt')

                print("label_source_path:", label_source_path, label_destination_path)
                shutil.copy2(label_source_path, label_destination_path)
                print(f'Copied label : {image_file}')

#         label_source_path = os.path.join(annotation_label_dir, f'{os.path.splitext(image_file)[0]}.txt')
#         label_destination_path = os.path.join(new_label_subdir, f'{os.path.splitext(image_file)[0]}.txt')

#         shutil.copy2(label_source_path, label_destination_path)
#         print(f'Copied label : {os.path.splitext(image_file)[0]}.txt')
