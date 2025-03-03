from imports import *

# Method 1: Specifying Scaling Factor using fx and fy
img_NZ_bgr = cv2.imread("class_02/assets/New_Zealand_Boat.jpg", 1) # Load the image with color mode
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB) # Convert the image to RGB
cropped_region = img_NZ_rgb[200:400, 300:600] # Crop the image
resized_cropped_region_2x = cv2.resize(cropped_region, None, fx=2, fy=2)  # Resize the image
plt.imshow(resized_cropped_region_2x) # Display the image
plt.show() # Show the image

# Method 2: Specifying exact size of the output image (Problem with aspect ratio)
desired_width = 100 # Define the width
desired_height = 200 # Define the height
dim = (desired_width, desired_height) # Define the desired dimensions
resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA) # Resize background image to sae size as logo image 
plt.imshow(resized_cropped_region) # Display the image
plt.show() # Show the image

# Method 3: Resize while maintaining aspect ratio | Maintaining aspect ratio (Problem with quality) 
desired_width = 100 # Define the width
aspect_ratio = desired_width / cropped_region.shape[1] # Calculate the aspect ratio
desired_height = int(cropped_region.shape[0] * aspect_ratio) # Calculate the height
dim = (desired_width, desired_height) # Define the desired dimensions
resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA) # Resize background image to sae size as logo image
plt.imshow(resized_cropped_region) # Display the image
plt.show() # Show the image

