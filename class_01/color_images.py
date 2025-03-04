from imports import *

logo_coca_cola = cv2.imread("class_01/assets/coca-cola-logo.png", 1) # Load the image with color mode
logo_coca_cola_reverse = cv2.cvtColor(logo_coca_cola, cv2.COLOR_BGR2RGB) # Reverse the color channels

plt.imshow(logo_coca_cola_reverse) # Display the image using matplotlib
plt.show() # Show the image