from imports import *

# Load the image
image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR) 

# Create a copy of the image
imageText = image.copy()

# Add text
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

# Add text to the image
cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA) # Add text to the image

# Display the image
cv2.imshow("Image With Text", imageText) # Display the image
cv2.waitKey(0) # Wait for a key press
cv2.destroyAllWindows() # Close all windows
