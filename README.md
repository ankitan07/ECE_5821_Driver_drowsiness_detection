# Drivers Drowsiness Detection

This project aims to develop a facial feature detection and drowsiness detection for driver monitoring.
The goal is to accurately detect facial landmarks and track the driver's eye movements to understand their attention and distraction levels while driving.

## Files
* [1_synthetic_data.py](https://github.com/ankitan07/ECE_5821_Driver_drowsiness_detection/blob/master/1_synthetic_data.py)
  * **Creating** images of type Awake, Yawn  
* [2_annotation.py](https://github.com/ankitan07/ECE_5821_Driver_drowsiness_detection/blob/master/2_annotation.py)
  * **Labelling** images into Awake, Yawn and Drowsy and Creating **annotation** in YOLO format for pre-divided data. (only considering iamges with 1 bounding ox for further analysis)
* [3_split.py](https://github.com/ankitan07/ECE_5821_Driver_drowsiness_detection/blob/master/3_split.py)
  * Splitting the images and their corresponding annotation into train, validate and test data set
* [4_train.py](https://github.com/ankitan07/ECE_5821_Driver_drowsiness_detection/blob/master/4_train.py)
  * **Train** the model on image dataset
* [5_testing.py](https://github.com/ankitan07/ECE_5821_Driver_drowsiness_detection/blob/master/5_testing.py)
  * **Testing** the model on image dataset
* [6_realtime_testing_with_alarm.py](https://github.com/ankitan07/ECE_5821_Driver_drowsiness_detection/blob/master/6_realtime_testing_with_alarm.py)
  * **Real time testing** of the model with alarm
* [ECE_5821_Final_Project_report.pdf](https://github.com/ankitan07/ECE_5821_Driver_drowsiness_detection/blob/master/ECE_5821_Final_Project_report.pdf)
  * **Real time testing** of the model with alarm 
