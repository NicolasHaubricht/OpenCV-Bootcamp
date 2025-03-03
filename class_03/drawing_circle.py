from imports import *

# Load the image
image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Create a copy of the image
imageCircle = image.copy() 

# Adding Circle in Image
cv2.circle(imageCircle, (925, 580), 50, (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)

# Display the image
cv2.imshow("Circle", imageCircle)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# Show the image
plt.imshow(imageCircle[:, :, ::-1]) 