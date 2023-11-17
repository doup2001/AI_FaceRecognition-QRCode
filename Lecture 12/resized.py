import cv2

image = cv2.imread('/Users/eedo_y/OpenSource/Lecture 12/image/lunar_eclipse.jpg')

resized = cv2.resize(image, dsize=(0,0), fx = 0.25 , fy =1.0 , interpolation = cv2.INTER_AREA)

cv2.imshow("Image",image)
cv2.imshow("Resized",resized)

cv2.waitKey()
cv2.destroyAllWindows()