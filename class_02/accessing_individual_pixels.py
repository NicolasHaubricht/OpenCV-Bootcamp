from imports import *

cb_img = cv2.imread("class_02/assets/checkerboard_18x18.png", 0) # Load the image with color mode

cb_img_copy = cb_img.copy() # Create a copy of the image
cb_img_copy[2:4, 2:4] = 200 # Change the pixel value at row 2, column 2 to 200

plt.imshow(cb_img_copy, cmap="gray") # Display the image
plt.show() # Show the image
print(cb_img_copy) # Print the image array
