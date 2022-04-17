from fer import FER
import cv2
import os

cap = cv2.VideoCapture()
cap.open(0, cv2.CAP_DSHOW)
detector = FER()
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, img = cap.read()
    try:
        emotion, score = detector.top_emotion(img)
        if len(emotion) > 0:
            cv2.putText(img, emotion, (10,50), font, 2, (0,255,0),2)
    except:
        pass

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()


