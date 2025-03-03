from imports import *

img_NZ_bgr = cv2.imread("class_02/assets/New_Zealand_Boat.jpg", 1) # Load the image with color mode
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB) # Convert the image to RGB

plt.imshow(img_NZ_rgb) # Select the image to show
plt.show() # Show the image

cropped_region = img_NZ_rgb[200:400, 300:600] # Crop the image
plt.imshow(cropped_region) # Select the image to show
plt.show() # Show the image