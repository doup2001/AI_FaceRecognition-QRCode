import cv2

video_file = '/Users/eedo_y/OpenSource/Lecture 12/video/sample.mp4'
cap = cv2.VideoCapture(video_file)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret :
        cv2.imshow('Video',frame)
        #press q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()