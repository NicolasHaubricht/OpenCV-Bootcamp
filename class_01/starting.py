from imports import *

image = cv2.imread("assets/checkerboard_84x84.jpg" , 0 ) # First argument is the image path, second argument is the color mode (0 for grayscale, 1 for color)

print(image) # Image as a matrix
print(image.shape) # Shape of the image (rows, columns)
print(image.dtype) # Type of the image

plt.imshow(image, cmap='gray') # Display the image using matplotlib and set the color map to grayscale
plt.show() # Show the image