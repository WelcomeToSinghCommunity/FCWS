# my_utils.py
import cv2

def setup_video_capture(video_path=0):
    return cv2.VideoCapture(video_path)

def draw_detections(frame, detections):
    for (x1, y1, x2, y2, confidence, cls) in detections:
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f"{cls} {confidence:.2f}", (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
