import math
import cv2

src = cv2.imread("/Users/eedo_y/OpenSource/Lecture 12/image/mountain.jpg")

if src is None:
    print('Image open failed!')
    sys.exit()

dst = src.copy()

# 원 그리기
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT, 1, 50,
                            param1=328, param2=10, minRadius=90, maxRadius=96)

for circle in circles[0]:
    x,y,r = int(circle[0]), int(circle[1]),int(circle[2])
    cv2.circle(dst,(x,y),r ,(255,255,255),5)

# 라인 그리기

canny = cv2.Canny(gray,5500,2000,apertureSize=5, L2gradient = True)
lines = cv2.HoughLinesP(canny, 0.8, math.pi / 180 , 90 , minLineLength = 10 , maxLineGap = 100)

print("Number of detected lines =", len(lines))

for i in lines :
    cv2.line(dst, (int(i[0][0]), int(i[0][1])) ,(int(i[0][2]) ,int(i[0][3])), (0,0,255), 2 )


cv2.imshow("Detected Circles", dst)
cv2.waitKey()
cv2.destroyAllWindows()