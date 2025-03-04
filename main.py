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
logo_coca_cola_reverse = cv2.cvtColor(logo_coca_cola, cv2.COLOR_BGR2RGB)
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

img_NZ_bgr = cv2.imread("class_02/assets/New_Zealand_Boat.jpg", 1)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_NZ_rgb)
plt.show()
cropped_region = img_NZ_rgb[200:400, 300:600]
plt.imshow(cropped_region) 
plt.show() 

# ================================ Resizing Images  ================================ #

# Method 1: Specifying Scaling Factor using fx and fy
img_NZ_bgr = cv2.imread("class_02/assets/New_Zealand_Boat.jpg", 1)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB) 
cropped_region = img_NZ_rgb[200:400, 300:600]
resized_cropped_region_2x = cv2.resize(cropped_region, None, fx=2, fy=2) 
plt.imshow(resized_cropped_region_2x) 
plt.show()

# Method 2: Specifying exact size of the output image (Problem with aspect ratio)
desired_width = 100
desired_height = 200
dim = (desired_width, desired_height)
resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA) 
plt.imshow(resized_cropped_region) 
plt.show()

# Method 3: Resize while maintaining aspect ratio | Maintaining aspect ratio (Problem with quality) 
desired_width = 100
aspect_ratio = desired_width / cropped_region.shape[1]
desired_height = int(cropped_region.shape[0] * aspect_ratio)
dim = (desired_width, desired_height)
resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
plt.show()

# ================================ Saving Images  ================================ #

resized_cropped_region_2x = resized_cropped_region_2x[:,  :,  :: - 1]
cv2.imwrite("resized_cropped_region_2x.png", resized_cropped_region_2x)

# ================================ Flipping Images ================================ #

img = cv2.imread('class_02/assets/New_Zealand_Boat.jpg', 1)
img = img[:,  :,  :: - 1 ]
img_flipped_horz = cv2.flip(img, 1)
img_flipped_vert = cv2.flip(img, 0)
img_flipped_both = cv2.flip(img, -1)
plt.figure(figsize=(18, 5))
plt.subplot(141);plt.imshow(img_flipped_horz);plt.title("Horizontal Flip")
plt.subplot(142);plt.imshow(img_flipped_vert);plt.title("Vertical Flip")
plt.subplot(143);plt.imshow(img_flipped_both);plt.title("Both Flipped")
plt.subplot(144);plt.imshow(img);plt.title("Original")
plt.show()

# ================================ Drawing Lines ================================ #

image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
imageLine = image.copy()
cv2.line(imageLine, (654, 100), (654, 530), (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
cv2.imshow("Line", imageLine)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(imageLine[:, :, ::-1])

# ================================ Drawing Circles ================================ #

image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
imageCircle = image.copy()
cv2.circle(imageCircle, (925, 580), 50, (0, 255, 255), thickness=5, lineType=cv2.LINE_AA)
cv2.imshow("Circle", imageCircle)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.imshow(imageCircle[:, :, ::-1])

# ================================ Drawing Rectangles ================================ #

image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (500, 100), (700, 600), (255, 0, 0), thickness=5, lineType=cv2.LINE_8)
cv2.imshow("Rectangle", imageRectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ================================ Adding Text ================================ #

image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
imageText = image.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2
cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
cv2.imshow("Image With Text", imageText)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ================================ Adding Text and Rectangle ================================ #

image = cv2.imread("class_03/assets/Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (500, 100), (700, 600), (0, 255, 0), thickness=5, lineType=cv2.LINE_8)
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2
imageRectangleText = imageRectangle.copy()
cv2.putText(imageRectangleText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
cv2.imshow("Rectangle With Text", imageRectangleText)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ================================ New Topic ================================ #



# ================================ New Topic ================================ #



# ================================ New Topic ================================ #



# ================================ New Topic ================================ #