# object_detection.py

import torch


def load_detection_model():
    """
    Load the YOLOv5 model from the Ultralytics repository.
    :return: Loaded YOLOv5 model.
    """
    print("Loading YOLOv5 model...")
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load YOLOv5 small model
    model.eval()  # Set the model to evaluation mode
    print("Model loaded successfully.")
    return model


def detect_objects(frame, model):
    """
    Perform object detection on a single frame using the loaded YOLOv5 model.
    :param frame: The input image frame on which to perform detection.
    :param model: The YOLOv5 model loaded via torch hub.
    :return: List of detections in the format (x1, y1, x2, y2, confidence, class_name).
    """
    print("Running object detection...")
    results = model(frame)
    detections = []

    # Map class IDs to human-readable labels (e.g., 'car', 'person')
    class_labels = model.names

    for detection in results.xyxy[0]:  # Iterate over detected objects
        x1, y1, x2, y2, confidence, cls = detection[:6]  # Bounding box coordinates, confidence, class ID
        class_id = int(cls)

        # Filter detections by class (example: 2 is "car," 0 is "person")
        if class_id in [2, 0]:  # Class 2 (car) and 0 (person) as per COCO dataset
            class_name = class_labels[class_id]
            detections.append((x1.item(), y1.item(), x2.item(), y2.item(), confidence.item(), class_name))

    print(f"Detections: {detections}")
    return detections


if __name__ == "__main__":
    # Example usage
    import cv2

    # Load model
    model = load_detection_model()

    # Load an example frame (replace 'test_image.jpg' with the path to your test image)
    frame = cv2.imread(r'C:\Users\Kishan Singh\OneDrive\Desktop\SEM 6\GRAD PARTNERS\test_image.jpeg')
    if frame is None:
        print("Error: Could not load the image.")
    else:
        # Perform detection
        detections = detect_objects(frame, model)

        # Print each detected object's details
        for det in detections:
            x1, y1, x2, y2, conf, cls_name = det
            print(f"Detected {cls_name} with confidence {conf:.2f} at [{x1}, {y1}, {x2}, {y2}]")
