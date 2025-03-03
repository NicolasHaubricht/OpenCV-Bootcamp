from imports import *

img_lake = cv2.imread("assets/New_Zealand_Lake.jpg", 1) # Load the image with color mode
b, g, r = cv2.split(img_lake) # Split the image into blue, green, and red channels

plt.figure(figsize=(20, 5)) # Set the figure size

plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel") # Display the red channel
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel") # Display the green channel
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel") # Display the blue channel

imgMerged = cv2.merge((b, g, r)) # Merge the channels back into an image

plt.subplot(144) # Create a new subplot
plt.imshow(imgMerged[:, :, ::-1]) # Display the image using matplotlib
plt.title("Merged Output") # Set the title
plt.show() # Show the image