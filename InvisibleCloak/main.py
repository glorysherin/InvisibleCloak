import cv2
import numpy as np
import time

# Start video capture
cap = cv2.VideoCapture(0)
time.sleep(3)  # wait for camera to adjust

# Capture the background (without cloak)
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)  # mirror the frame

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red cloak range (tweak if using different color)
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])
    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Refine mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    # Inverse mask for the rest of the scene
    mask_inv = cv2.bitwise_not(mask)

    # Segment out cloak area from background and frame
    res1 = cv2.bitwise_and(background, background, mask=mask)      # cloak → background
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)           # rest → live frame
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
