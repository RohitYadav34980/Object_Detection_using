import tkinter as tk
from tkinter import filedialog
import cv2
from customtkinter import *
import numpy as np

# Load model and classes
thres = 0.5  # Threshold to detect object

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

def detect_objects(image_path):
    root.destroy()
    img = cv2.imread(image_path)
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
    cv2.waitKey(0)  # Wait until any key is pressed
    cv2.destroyAllWindows()

def browse_file():
    file_path = filedialog.askopenfilename()
    detect_objects(file_path)

root = CTk()
root.title("Object Detection GUI")
root.geometry("500x300")

upload_button = CTkButton(master=root, text="Upload Image", command=browse_file)
upload_button.pack(pady=20)

root.mainloop()
