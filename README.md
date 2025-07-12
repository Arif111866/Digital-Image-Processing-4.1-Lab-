# 🖼️ Digital Image Processing Laboratory - CSE 4.1

This repository contains the implementation of fundamental Digital Image Processing (DIP) techniques using Python (OpenCV, NumPy, Matplotlib). Each task corresponds to a specific lab experiment. The main focus is on image enhancement, restoration, segmentation, filtering, and morphological operations.

📁 Repository Structure:
- `Lab1/` to `Lab6/`: Contains respective experiments, code files, outputs, and image resources.
- Each folder includes clean and well-documented Python notebooks or scripts.

---

## ✅ Lab 1: Image Resolution & Histogram-Based Segmentation
**Dataset**: Grayscale image of size `512x512`

- 🔹 (a) **Spatial Resolution Reduction**: Reduced image resolution by half (subsampling).
- 🔹 (b) **Display Analysis**: Displayed low-resolution image in original window to observe scaling effect.
- 🔹 (c) **Intensity Resolution Decrease**: Reduced bit-depth from 8-bit to 1-bit, observing gradual degradation.
- 🔹 (d) **Histogram & Thresholding**: Plotted image histogram and applied global threshold-based segmentation.

📂 `Lab1/` → [`lab1.ipynb`](./Lab1/lab1.ipynb)

---

## ✅ Lab 2: Brightness, Power Transform & Bit-Plane Analysis

- 🔹 (a) **Brightness Enhancement**: Enhanced brightness for specific gray levels using piecewise transformation.
- 🔹 (b) **Power vs Inverse Log Transform**: Compared effects of gamma correction (power law) vs. inverse log scaling.
- 🔹 (c) **Bit-plane Slicing**: Reconstructed image using MSBs and calculated the difference with the original image.

📂 `Lab2/` → [`lab2.ipynb`](./Lab2/lab2.ipynb)

---

## ✅ Lab 3: Noise Removal using Spatial Filtering

- 🔹 (a) **Salt & Pepper Noise Removal**: Applied 5×5 average and median filters and evaluated PSNR.
- 🔹 (b) **Mask Size Variation**: Tested average filter with 3×3, 5×5, and 7×7 masks, compared PSNR.
- 🔹 (c) **Mean Filters**: Applied harmonic and geometric mean filters and compared with previous methods.

📂 `Lab3/` → [`lab3.ipynb`](./Lab3/lab3.ipynb)

---

## ✅ Lab 4: Frequency Domain Filtering & Edge Detection

- 🔹 (a) **Gaussian vs Butterworth LPF**: Added Gaussian noise and applied both filters; analyzed performance quantitatively.
- 🔹 (b) **Ideal LPF & Ringing**: Demonstrated ringing effect with varying cutoff frequencies (D₀).
- 🔹 (c) **HPF Edge Detection**: Performed edge detection using ideal and Gaussian HPFs on both clean and noisy images.

📂 `Lab4/` → [`lab4.ipynb`](./Lab4/lab4.ipynb)

---

## ✅ Lab 5: Segmentation & Edge Detection

- 🔹 (a) **Spatial Edge Detection**: Compared Sobel, Prewitt, Roberts, and Canny edge detectors.
- 🔹 (b) **Gray Level Segmentation**: Illustrated segmentation based on histogram peaks.
- 🔹 (c) **Global Thresholding**: Applied basic thresholding using Otsu's method.
- 🔹 (d) **Adaptive Thresholding**: Demonstrated segmentation using adaptive techniques (mean & Gaussian).

📂 `Lab5/` → [`lab5.ipynb`](./Lab5/lab5.ipynb)

---

## ✅ Lab 6: Morphological Operations

- 🔹 (a) **Erosion & Dilation**: Applied basic morphological shrinking and expanding.
- 🔹 (b) **Opening & Closing**: Used for noise removal and small object bridging.
- 🔹 (c) **Boundary Extraction**: Extracted image boundaries using morphological gradient.
- 🔹 (d) **Region Filling**: Implemented morphological filling for binary regions.

📂 `Lab6/` → [`lab6.ipynb`](./Lab6/lab6.ipynb)

---

## 🔧 Technologies Used
- Python 3.8+
- OpenCV
- NumPy
- Matplotlib
- Jupyter Notebook

---

## 📸 Sample Visuals
<p float="left">
  <img src="Lab1/output1.png" width="30%" />
  <img src="Lab3/median_vs_avg.png" width="30%" />
  <img src="Lab5/segmentation.png" width="30%" />
</p>

---

## 🧠 Author
**Ariful Islam**  
🎓 CSE, Rajshahi University  
🔗 [GitHub Profile](https://github.com/Arif111866)  
📌 [Portfolio Site](https://arif111866.github.io)

---

## 📜 License
This repository is open-sourced under the MIT License.
