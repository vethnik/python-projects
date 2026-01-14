import cv2
img=cv2.imread("bmw.jpg")
resize=cv2.resize(img,(1800,1200))
cv2.imwrite("resized.jpg",resize)

cv2.imshow("Resized image",resize)
cv2.waitKey()
cv2.destroyALLWindows()