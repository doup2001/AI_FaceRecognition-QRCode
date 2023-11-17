import cv2

image = cv2.imread('/Users/eedo_y/OpenSource/Lecture 12/image/lunar_eclipse.jpg')

image = cv2.line(image, (100,100) , (1200,500), (255,0,0) , 5)
image = cv2.rectangle(image, (500,200) , (1000,400) , (0,0,255), 5)
image = cv2.circle(image, (300,300), 50 ,(0,255,0),3)
image = cv2.putText(image, "Lunar Eclipse", (500,100),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))

cv2.imwrite('/Users/eedo_y/OpenSource/Lecture 12/image/lunar_eclipse.jpg',image)

cv2.imshow("Image",image)
cv2.waitKey()
cv2.destroyAllWindows