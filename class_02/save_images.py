from imports import *
from resizing_images import *

resized_cropped_region_2x = resized_cropped_region_2x[:,  :,  :: - 1] # Reverse the color channels
cv2.imwrite ("resized_cropped_region_2x.png", resized_cropped_region_2x) # Save resized image to disk