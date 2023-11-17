import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0 :
    ret,frame = cap.read()
    cv2.imshow("Camera", frame)

cap.release()
cv2.destroyAllWindows()