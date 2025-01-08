# 🚗 Forward Collision Warning System 🚗

## Overview

This project implements a **Forward Collision Warning (FCW) System** that leverages real-time video processing to detect vehicles, calculate their distances, and issue collision warnings to prevent accidents. By using **YOLOv5** for object detection and **OpenCV** for video analysis, the system dynamically warns drivers when collision risks are detected based on proximity and speed.

### ⚡ **Key Features:**
- **Real-Time Object Detection**: Detects vehicles, pedestrians, and other objects in video streams using YOLOv5.
- **Collision Risk Analysis**: Calculates distances and triggers warnings for collision risks based on speed and proximity.
- **Dynamic Warning System**: Issues warnings when objects are within 50 meters and moving at speeds above 10 m/s.
- **Visual Overlays**: Displays bounding boxes with IDs, distances, and warnings for detected objects.
- **Flexible Integration**: Can be integrated into **ADAS** systems or used as an aftermarket solution for fleets.

---

## 🚀 **Getting Started**

### **Clone the repository**

Start by cloning this repo to your local machine:
```bash
git clone https://github.com/your-username/forward-collision-warning.git
cd forward-collision-warning
```

### ⚡ **Install dependencies**

Set up your environment and install the necessary libraries:
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## 🎥 **How It Works**

- **Input**: The system processes video files (e.g., MP4) or live video streams.
- **Detection**: It uses YOLOv5 to detect vehicles and other objects in real-time.
- **Distance Calculation**: Measures the distance between detected objects using bounding box dimensions.
- **Collision Risk Prediction**: If an object is within 50 meters and moving faster than 10 m/s, a collision warning is triggered.
- **Output**: Bounding boxes, distances, and warnings are overlaid on the video in real time.

## 📁 **Project Structure**

forward-collision-warning/
│
├── main.py                 # Main script to run the FCW system
├── fcw_code.cpp            # C++ module for real-time video processing
├── object_detection.py     # YOLOv5-based object detection
├── my_utils.py             # Utility functions for distance calculations
├── compliance_checker.py   # Monitors compliance with safety distance
├── code_generator.py       # Generates e-challans or reports
├── test_case_generator.py  # Generates test cases for system validation
├── requirements.txt        # Python dependencies
├── test_video.mp4          # Sample video for testing
└── README.md               # This file

## 🛠️ **Technology Used**

- **Python**: For main logic and scripting.
- **YOLOv5**: Real-time object detection for vehicles and pedestrians.
- **OpenCV**: For video processing and object tracking.
- **C++**: For real-time video processing in the fcw_code.cpp module.
- **NumPy**: For handling numerical operations.
- **Tesseract OCR**: For license plate recognition (if implemented).
- **Matplotlib/Plotly**: For visualizing results.

## 🚀 **Future Improvements**

- **Integration with ADAS**: Seamless integration into advanced driver-assistance systems.
- **Custom Object Detection**: Enhance YOLOv5 with custom training for detecting a wider range of road objects.
- **Fleet Monitoring**: Real-time monitoring of fleet vehicles and driver behavior.
- **Collision Prediction**: More accurate collision predictions using machine learning algorithms.

## 📜 **License**

This project is licensed under the MIT License - see the LICENSE file for details.
