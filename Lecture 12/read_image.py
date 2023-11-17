import cv2

image = cv2.imread('/Users/eedo_y/OpenSource/Lecture 12/image/lunar_eclipse.jpg')

h,w,c = image.shape
print(h,w,c)

cv2.imshow("Image",image)
cv2.waitKey()
cv2.destroyAllWindows()

# python -u "/Users/eedo_y/OpenSource/Lecture 12/read_image_arg.py" '/Users/eedo_y/OpenSource/Lecture 12/image/lunar_eclipse.jpg'

