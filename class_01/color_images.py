from imports import *

logo_coca_cola = cv2.imread("assets/coca-cola-logo.png", 1) # Load the image with color mode
logo_coca_cola_reverse = logo_coca_cola[:,  :,  :: - 1 ] # Reverse the color channels

plt.imshow(logo_coca_cola_reverse) # Display the image using matplotlib
plt.show() # Show the image