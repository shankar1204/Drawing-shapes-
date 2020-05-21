import cv2

img = cv2.imread ('image.jpeg', 1)

img = cv2.rectangle(img, (480,380),(50,40), (225,0,0), 10, 5)
img = cv2.circle(img, (290,190), 50, (0,0,225), 8)
img = cv2.line(img, (100,370), (90,40), (0,225,0), 2)

cv2.imshow('Resulting Frame', img)
cv2.waitKey(5000)
cv2.destroyAllWindows()