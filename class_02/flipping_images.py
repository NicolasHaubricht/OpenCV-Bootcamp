from imports import *

img = cv2.imread('class_02/assets/New_Zealand_Boat.jpg', 1) # Load the image with color mode
img = img[:,  :,  :: - 1 ] # Swap the color channels

img_flipped_horz = cv2.flip(img, 1) # Flip the image horizontally
img_flipped_vert = cv2.flip(img, 0) # Flip the image vertically
img_flipped_both = cv2.flip(img, -1) # Flip the image both horizontally and vertically

plt.figure(figsize=(18, 5)) # Create a new figure
plt.subplot(141);plt.imshow(img_flipped_horz);plt.title("Horizontal Flip") # Render the image horizontally and add a title
plt.subplot(142);plt.imshow(img_flipped_vert);plt.title("Vertical Flip") # Render the image vertically and add a title
plt.subplot(143);plt.imshow(img_flipped_both);plt.title("Both Flipped") # Render the image both horizontally and vertically and add a title
plt.subplot(144);plt.imshow(img);plt.title("Original"); # Render the original image and add a title
plt.show() # Show the plot