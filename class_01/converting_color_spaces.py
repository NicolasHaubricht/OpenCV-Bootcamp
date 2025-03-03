from imports import *

img = cv2.imread("class_01/assets/coca-cola-logo.png", 1) # Load the image with color mode
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert the color mode from BGR to RGB

plt.imshow(img) # Display the image
plt.show() # Show the image