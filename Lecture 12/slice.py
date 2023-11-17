import cv2

image = cv2.imread('/Users/eedo_y/OpenSource/Lecture 12/image/lunar_eclipse.jpg')
sliced = image[400:800, 800:1200].copy() #가로 , 세로

h, w, c = image.shape
print(h,w,c)

cv2.imshow("Image",image)
cv2.imshow("Sliced",image)

cv2.waitKey()
cv2.destroyAllWindows()