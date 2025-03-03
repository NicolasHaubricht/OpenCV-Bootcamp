from imports import *

# Load the image
image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Create a copy of the image
imageRectangle = image.copy()

# Adding Rectangle in Image
cv2.rectangle(imageRectangle, (500, 100), (700, 600), (0, 255, 0), thickness=5, lineType=cv2.LINE_8)

# Adding Text in Image Rectangle
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

# Create a copy of the image
imageRectangleText = imageRectangle.copy()

# Adding Text in Image Rectangle
cv2.putText(imageRectangleText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)

# Display the image
cv2.imshow("Rectangle With Text", imageRectangleText)
cv2.waitKey(0)
cv2.destroyAllWindows()

