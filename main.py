# ================================ Imports ================================ #

import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

# ================================ Starting ================================ #

image = cv2.imread("class_01/assets/checkerboard_84x84.jpg" , 0 ) 
print(image)
print(image.shape)
print(image.dtype)
plt.imshow(image, cmap='gray')
plt.show()

# ================================ Color Images  ================================ #

logo_coca_cola = cv2.imread("class_01/assets/coca-cola-logo.png", 1)
logo_coca_cola_reverse = logo_coca_cola[:,  :,  :: - 1 ]
plt.imshow(logo_coca_cola_reverse)
plt.show()

# ================================ Splitting and Merging Color Channels  ================================ #

img_lake = cv2.imread("class_01/assets/New_Zealand_Lake.jpg", 1)
b, g, r = cv2.split(img_lake)
plt.figure(figsize=(20, 5))
plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")
imgMerged = cv2.merge((b, g, r))
plt.subplot(144)
plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged Output")
plt.show()

# ================================ Converting to different Color Spaces  ================================ #

cb_img = cv2.imread("class_02/assets/checkerboard_18x18.png", 0)
cb_img_copy = cb_img.copy()
cb_img_copy[2:4, 2:4] = 200 
print(cb_img_copy)
plt.imshow(cb_img_copy, cmap="gray")
plt.show()

# ================================ Cropping Images  ================================ #

img_NZ_bgr = cv2.imread("class_02/assets/New_Zealand_Boat.jpg", 1) # Load the image with color mode
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB) # Convert the image to RGB

plt.imshow(img_NZ_rgb) # Select the image to show
plt.show() # Show the image

cropped_region = img_NZ_rgb[200:400, 300:600] # Crop the image
plt.imshow(cropped_region) # Select the image to show
plt.show() # Show the image