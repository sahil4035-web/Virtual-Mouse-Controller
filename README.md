# Virtual Mouse Control Using Hand Gestures

## Project Overview

Virtual Mouse Control is a Computer Vision project that allows users to control the computer mouse using hand gestures captured through a webcam. The system uses OpenCV and MediaPipe for real-time hand tracking and PyAutoGUI for mouse automation.

The application eliminates the need for a physical mouse by translating hand movements and gestures into mouse actions such as cursor movement, left click, and right click.

---

## Problem Statement

Develop a Virtual Mouse application using Python, OpenCV, and MediaPipe that allows users to control the computer cursor through real-time hand gestures captured by a webcam.

The application should detect and track hand landmarks to perform mouse operations without using a physical mouse while ensuring smooth cursor movement, accurate tracking, and minimal latency.

---

## Features

* Real-time webcam video capture
* Hand detection and tracking using MediaPipe
* Cursor movement using index finger tracking
* Left-click gesture using thumb and index finger pinch
* Right-click gesture using index and middle finger pinch
* Cursor smoothing to reduce jitter
* Virtual frame for controlled cursor movement
* Hand landmark visualization
* Gesture status display on screen
* Easy application exit using keyboard key

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

---

## Required Libraries

Install the required libraries:

```bash id="4q0f2n"
pip install opencv-python mediapipe pyautogui numpy
```

---

## Project Workflow

1. Capture live video from webcam.
2. Detect hand landmarks using MediaPipe Hands.
3. Track the index fingertip position.
4. Convert camera coordinates into screen coordinates.
5. Move the mouse cursor accordingly.
6. Detect pinch gestures for mouse clicks.
7. Apply smoothing for stable cursor movement.
8. Display landmarks and gesture information.
9. Exit application by pressing the 'Q' key.

---

## Hand Gesture Controls

| Gesture                     | Action           |
| --------------------------- | ---------------- |
| Move Index Finger           | Move Cursor      |
| Thumb + Index Finger Pinch  | Left Click       |
| Index + Middle Finger Pinch | Right Click      |
| Press Q                     | Exit Application |

---

## System Requirements

### Hardware

* Webcam
* Windows/Linux/Mac Computer

### Software

* Python 3.10 or above
* VS Code or Jupyter Notebook

---

## Project Structure

```text
Virtual_Mouse/
│
├── virtual_mouse.py
├── README.md
└── requirements.txt
```

---

## Expected Output

* Hand landmarks displayed on webcam feed.
* Mouse cursor follows index finger movement.
* Left click performed using thumb-index pinch.
* Right click performed using index-middle pinch.
* Smooth and responsive cursor control.
* Real-time gesture recognition.

---

## Learning Outcomes

By completing this project, students will learn:

* OpenCV webcam handling
* Real-time video processing
* Computer Vision fundamentals
* Hand landmark detection using MediaPipe
* Coordinate mapping techniques
* Mouse automation using Python
* Human-Computer Interaction (HCI)
* Gesture-based control systems

---

## Future Enhancements

* Double-click gesture
* Drag and drop support
* Scroll up and scroll down gestures
* Volume control using hand gestures
* Brightness control
* Multi-hand tracking
* Gesture customization
* AI-based gesture recognition

---

## Applications

* Touchless computer interaction
* Smart classrooms
* Accessibility solutions
* Interactive presentations
* Gaming controls
* Human-Computer Interaction research

---

## Conclusion

The Virtual Mouse Control System demonstrates how Computer Vision and Machine Learning techniques can be used to create touchless Human-Computer Interaction systems. By combining OpenCV, MediaPipe, and PyAutoGUI, users can control their computers naturally using hand gestures without requiring a physical mouse.

---

## Author

Siddhesh

Diploma in Electrical Engineering

AI & Machine Learning / Computer Vision Project
