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

### 1️⃣ Loading and Displaying Images  
- Reading grayscale (`cv2.IMREAD_GRAYSCALE`) and color (`cv2.IMREAD_COLOR`) images  
- Displaying images using `matplotlib` with proper RGB conversion  

### 2️⃣ Working with Color Images  
- Understanding BGR vs. RGB color formats  
- Converting between color spaces using `cv2.cvtColor()`  

### 3️⃣ Splitting and Merging Color Channels  
- Extracting R, G, B channels with `cv2.split()`  
- Reconstructing images with `cv2.merge()`  
- Visualizing individual color channels  

### 4️⃣ Converting Color Spaces  
- HSV and LAB color space conversions  
- Practical applications of different color spaces  

### 5️⃣ Cropping Images  
- Array slicing techniques for region extraction  
- Selective pixel manipulation  

## 📂 Repository Structure  
```bash
opencv-course/
├── class/
├   ├── script.py
├── imports.py
├── main.py
└── README.md
