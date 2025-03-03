from imports import *

# Load the Image
image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Create a copy of the image
imageLine = image.copy() 

# Adding Line in Image
cv2.line(imageLine, (654, 100), (654, 530), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA) 

# Display the image
cv2.imshow("Line", imageLine)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show the image
plt.imshow(imageLine[:, :, ::-1])