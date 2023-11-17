import cv2

image = cv2.imread('/Users/eedo_y/OpenSource/Lecture 12/image/lunar_eclipse.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(image,100,200)

cv2.imshow("Image",image)
cv2.imshow("Gray",gray)
cv2.imshow("Canny",canny)

cv2.waitKey()
cv2.destroyAllWindows()