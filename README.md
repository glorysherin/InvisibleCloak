# 🧙‍♂️ Invisible Cloak

A Python implementation of Harry Potter's invisibility cloak using OpenCV. Detects a colored cloth and replaces it with the background to create an invisibility effect.

## Features
- Real-time invisibility effect via webcam
- Customizable cloak colors
- Simple and lightweight

## Installation
```bash
pip install opencv-python numpy
```

## Usage
1. Run the program:
```bash
python main.py
```

2. **Important**: Move out of camera view for the first 3 seconds (background capture)
3. Return with a red cloth/cloak to see the invisibility effect
4. Press 'q' to quit

## Customize Cloak Color

### Blue Cloak
Replace the HSV ranges in `main.py`:
```python
# Replace red ranges with:
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
```

### Green Cloak
```python
lower_green = np.array([40, 150, 0])
upper_green = np.array([80, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)
```

### Common HSV Ranges
| Color | Lower HSV | Upper HSV |
|-------|-----------|-----------|
| Red | `[0, 120, 70]` | `[10, 255, 255]` |
| Blue | `[100, 150, 0]` | `[140, 255, 255]` |
| Green | `[40, 150, 0]` | `[80, 255, 255]` |

## Tips
- Use solid-colored cloth
- Ensure good lighting
- Keep background static during initial capture

---
⭐ Star this repo if you found it helpful!
