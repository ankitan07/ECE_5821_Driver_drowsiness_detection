import os
from threading import Thread
import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/train_without_test/weights/last.pt',
                       force_reload=True)

def alarm(msg):
    global alarm_status
    global alarm_status2
    global saying

    while alarm_status:
        print('call')
        s = 'espeak "' + msg + '"'
        os.system(s)

    if alarm_status2:
        print('call')
        saying = True
        s = 'espeak "' + msg + '"'
        os.system(s)
        saying = False


# Initialize variables for drowsiness detection
closed_eyes_frames, closed_eyes_threshold = 0, 5
yawning_frames, yawning_threshold = 0, 2
yawn_flag, yawn_time_frame_count, yawn_total_time_frame = False, 0, 10

alarm_status = False
alarm_status2 = False
saying = False

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from the webcam

    if not ret:
        break

    # Perform inference using the YOLOv5 model
    results = model(frame)

    # Process the results and draw bounding boxes on the frame
    annotated_frame = results.render()[0]

    # Extract labels and draw bounding boxes
    for det in results.pred[0]:
        x1, y1, x2, y2, conf, cls = det.tolist()
        label = model.names[int(cls)]  # Extract the label using the class index

        print("label", label)

        if label == "Drowsy":
            closed_eyes_frames += 1
            if closed_eyes_frames >= closed_eyes_threshold:
                print("Closed eyes detected for 10 seconds! Triggering alarm...")
                if alarm_status == False:
                    alarm_status = True
                    t = Thread(target=alarm, args=('wake up, you are drowsy',))
                    t.deamon = True
                    t.start()

                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # Implement alarm logic here
        else:
            closed_eyes_frames = 0
            COUNTER = 0
            alarm_status = False

        # alarm if yawn 3 time in 10 sec
        if yawn_flag:
            yawn_time_frame_count += 1
            if yawn_time_frame_count >= yawn_total_time_frame:
                yawn_flag = False
                yawn_time_frame_count = 0
                yawning_frames = 0
                alarm_status2 = False

        if label == "Yawn":
            if not yawn_flag:
                yawn_flag = True

            yawning_frames += 1
            if yawning_frames >= yawning_threshold:
                print("Yawning detected! Triggering alarm...")
                if alarm_status2 == False and saying == False:
                    alarm_status2 = True
                    t = Thread(target=alarm, args=('take some fresh air,You are yawning a lot',))
                    t.deamon = True
                    t.start()
                # Implement alarm logic here

    # Display the annotated frame
    cv2.imshow('YOLOv5 Object Detection', annotated_frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
