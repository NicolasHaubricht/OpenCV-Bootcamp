from imports import *

# Load the image
image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Create a copy of the image
imageRectangle = image.copy()

# Adding Rectangle in Image
cv2.rectangle(imageRectangle, (500, 100), (700, 600), (255, 0, 0), thickness=5, lineType=cv2.LINE_8)

# Display the image
cv2.imshow("Rectangle", imageRectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()