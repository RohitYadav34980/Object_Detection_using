import cv2

# Load model and classes
thres = 0.5  # Threshold to detect object
cap = cv2.VideoCapture(0)  # Use default webcam (index 0)
cap.set(3, 640)
cap.set(4, 480)

classNames = []
classFile = "coco.names"
with open("C:\\Users\\muska\\Desktop\\objectdetection\\object\\coco.names", 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = "C:\\Users\\muska\\Desktop\\objectdetection\\object\\ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "C:\\Users\\muska\\Desktop\\objectdetection\\object\\frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success, img = cap.read()

    if not success:
        print("Failed to read frame")
        break

    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    print(classIds, bbox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, classNames[classId - 1].upper(), (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 200, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()