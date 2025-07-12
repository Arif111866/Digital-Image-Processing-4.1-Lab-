🎨 Digital Image Processing Laboratory 4.1 🚀

Welcome to my Digital Image Processing Lab 4.1 repository! This repo contains solutions to various image processing tasks as part of my lab exercises. Below are the questions and a brief overview of my approach to solving them. 🌟

📋 Lab Questions and Solutions

1. Grayscale Image of Size 512x512





Tasks: Decrease its spatial resolution by half, observe changes, convert to binary format, and analyze histogram.



Approach: Used Python with OpenCV to resize the image, applied thresholding for binary conversion, and plotted histograms using Matplotlib. 📉

2. Grayscale Image Enhancement





Tasks: Perform brightness enhancement, power law, and logarithmic transforms.



Approach: Implemented enhancement functions in OpenCV, applied different gamma values for power law, and compared results visually. ✨

3. Grayscale Image with Salt & Pepper Noise





Tasks: Apply median and spatial filters (5x5 mask) with varying sizes (3x3, 5x5, 7x7) and compare PSNR.



Approach: Added noise using NumPy, applied filters with OpenCV, and calculated PSNR for performance evaluation. 🔍

4. Grayscale Image with Gaussian Noise





Tasks: Apply 4th order Butterworth and Gaussian low-pass filters, perform edge detection.



Approach: Used SciPy for filter design, applied filters, and implemented edge detection with Canny edge detector. 🛠️

5. Grayscale Image Edge Detection





Tasks: Compare edge detection algorithms, segment using gray level, and demonstrate adaptive thresholding.



Approach: Implemented Sobel and Canny edge detectors, used Otsu’s method for segmentation, and applied adaptive thresholding. 🎯

6. Binary Image with Structuring Element





Tasks: Perform erosion, dilation, opening, closing, boundary extraction, and region filling.



Approach: Utilized morphological operations in OpenCV with custom structuring elements for each task. 🖌️

🌐 Usage

Clone the repo and run the Python scripts with the required dependencies (OpenCV, NumPy, Matplotlib, SciPy). Ensure you have the input images in the working directory. 📂

📚 Dependencies





OpenCV



NumPy



Matplotlib



SciPy

Install them using: pip install opencv-python numpy matplotlib scipy

🚀 Contribution

Feel free to fork, improve, or suggest enhancements! Open an issue or pull request. 🙌

🎉 Acknowledgments

Thanks to my lab instructor and online resources for guidance! 🌐
