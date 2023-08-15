# annotation.py :Define the class index for faces (can be 0)
import os

class_index = 0

# Split.py file :Define the split ratios (e.g., 70% train, 15% test, 15% validate)
train_ratio = 0.7
test_ratio = 0.15
validate_ratio = 0.15

script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the data directory
data_dir = os.path.join(script_dir, '../datapreprocessing/Dataset/')
annotation_labels_dir = os.path.join(script_dir, '../datapreprocessing/Labels/')
annotation_images_dir = os.path.join(script_dir,'../datapreprocessing/Annotation_images/')
multiple_dir = os.path.join(script_dir,'../datapreprocessing/multiple/')

# Set the paths for train, test, and validate directories
train_dir = os.path.join(script_dir, '../preprocessed_data/train/')
test_dir = os.path.join(script_dir, '../preprocessed_data/test/')
validate_dir = os.path.join(script_dir, '../preprocessed_data/validate/')



