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
