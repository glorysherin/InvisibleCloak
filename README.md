# 🧙 InvisibleCloak

This project recreates the famous **invisibility cloak effect from Harry Potter** using **Python** and **OpenCV**.  
By detecting a specific color (default: red) and replacing it with the pre-captured background, the cloak appears invisible, giving the illusion of transparency. 🪄

---

## ✨ Features
- Real-time invisibility cloak effect using webcam
- Detects cloak color in **HSV color space**
- Smooth masking with morphological operations
- Customizable cloak color range
- Lightweight and beginner-friendly

---

## 🚀 How It Works
1. Captures the static background for a few seconds at the start.
2. Detects pixels of the cloak color in each video frame.
3. Replaces the detected cloak pixels with the saved background.
4. Combines cloak-masked background with the original frame → giving the cloak invisibility.

---

## 🛠 Requirements
- Python 3.x
- OpenCV
- NumPy

Install dependencies:
```bash
pip install opencv-python numpy
