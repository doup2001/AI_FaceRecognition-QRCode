import sys
import cv2

image_file = sys.argv[1]
image = cv2.imread(image_file)

h,w,c = image.shape
print(h, w, c)

cv2.imshow("Image",image)
cv2.waitKey()
cv2.destroyAllWindows()