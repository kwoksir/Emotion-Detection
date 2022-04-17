from fer import FER
import cv2
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

detector = FER(mtcnn=True)
font = cv2.FONT_HERSHEY_PLAIN

img = cv2.imread("sample.jpg")
try:
    emotion, score = detector.top_emotion(img)
    print(emotion, score)
except:
    print("No face detected")
