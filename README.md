# OpenCV Course

[![OpenCV](https://img.shields.io/badge/OpenCV-5.0-%235C3EE8?logo=opencv)](https://opencv.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)

This repository contains Python scripts for basic image processing using OpenCV. The scripts were developed as part of a free OpenCV course, and the repository will be updated as I progress through the modules.  

## 🛠 Technologies Used  
- **Python 3.8+** - Core programming language
- **OpenCV (cv2)** - Computer vision operations
- **NumPy** - Array manipulations and mathematical operations
- **Matplotlib** - Image visualization and plotting

## 📌 Topics Covered  

The `main.py` file is organized into sections, each focusing on a specific OpenCV concept I studied. Below is an overview of the topics:

1. **Basic Image Loading and Display**
   - Loading grayscale and color images using `cv2.imread()`.
   - Inspecting image properties (shape, data type) with NumPy.
   - Displaying images using Matplotlib with proper color mapping.

2. **Working with Color Images**
   - Handling BGR vs. RGB color formats and converting between them.
   - Reversing color channels for proper visualization.

3. **Splitting and Merging Color Channels**
   - Splitting an image into its Red, Green, and Blue channels using `cv2.split()`.
   - Merging channels back into a full-color image with `cv2.merge()`.

4. **Converting Color Spaces**
   - Exploring grayscale and binary image manipulation.
   - Modifying pixel values and visualizing changes.

5. **Cropping Images**
   - Extracting regions of interest (ROI) from images using array slicing.

6. **Resizing Images**
   - Scaling images with different methods:
     - Using scaling factors (`fx`, `fy`) with `cv2.resize()`.
     - Specifying exact dimensions (with potential aspect ratio issues).
     - Maintaining aspect ratio for better quality.

7. **Saving Images**
   - Writing processed images to disk using `cv2.imwrite()`.

8. **Flipping Images**
   - Applying horizontal, vertical, and combined flips with `cv2.flip()`.

9. **Drawing Shapes**
   - Drawing lines with `cv2.line()`.
   - Drawing circles with `cv2.circle()`.
   - Drawing rectangles with `cv2.rectangle()`.

10. **Adding Text**
    - Overlaying text on images using `cv2.putText()` with customizable fonts, sizes, and colors.

11. **Combining Shapes and Text**
    - Integrating rectangles and text for annotations on images.


## 📂 Repository Structure  
```bash
opencv-course/
├── class/
├   ├── script.py
├── imports.py
├── main.py
└── README.md
