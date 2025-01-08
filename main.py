import cv2
from Object_detection import load_detection_model, detect_objects
from my_utils import setup_video_capture, draw_detections


def main():
    # Load the object detection model
    model = load_detection_model()

    # Set up video capture (use 0 for webcam, or provide path to a video file)
    cap = setup_video_capture(
        r"C:\Users\Kishan Singh\OneDrive\Desktop\SEM 6\GRAD PARTNERS\5834617-uhd_3840_2160_24fps.mp4")  # Replace with video path or '0' for webcam

    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    # Create a window and resize it
    cv2.namedWindow("Forward Collision Warning", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Forward Collision Warning", 640, 480)  # Resize to desired width and height

    while cap.isOpened():
        # Read the next frame from the video capture
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame or end of video.")
            break

        # Perform object detection on the frame
        detections = detect_objects(frame, model)

        # Draw the detections on the frame (bounding boxes and labels)
        frame = draw_detections(frame, detections)

        # Simulate vehicle speed (in real systems, this would come from the vehicle data)
        vehicle_speed = 15

        # Check if collision warning is needed and show warning sign
        danger_zone_detected = detect_and_warn(frame, detections, vehicle_speed)

        # Resize the frame before displaying it (optional)
        frame_resized = cv2.resize(frame, (640, 480))  # Resize to desired width and height

        # Display the resized frame with object detections and possible warnings
        cv2.imshow("Forward Collision Warning", frame_resized)

        # Check if 'q' key is pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting due to user request.")
            break

    # Release video capture and close any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


def detect_and_warn(frame, detections, speed, detection_range=50, warning_distance=5):
    warning_triggered = False  # Initialize flag to check if warning is needed

    for (x1, y1, x2, y2, confidence, cls) in detections:
        # Calculate object distance based on bounding box size
        object_distance = calculate_distance(x1, y1, x2, y2)

        # Draw distance above the bounding box in blue with increased font size and thickness
        label = f"Dist: {object_distance:.2f}m"
        cv2.putText(frame, label, (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)  # Blue text, larger font, thicker

        # Check if object is in danger zone (within warning distance)
        if object_distance < warning_distance:
            warning_triggered = True  # Set flag to true if any object is too close

    # If any object is detected in the danger zone, display the warning sign
    if warning_triggered:
        display_warning_sign(frame, "Warning! Collision Imminent!")


def calculate_distance(x1, y1, x2, y2):
    # Use bounding box height as a rough proxy for distance (you may need to adjust this factor)
    box_height = abs(y2 - y1)

    # Set a constant to simulate realistic distances. You may adjust this based on camera calibration.
    scaling_factor = 500  # Adjust this factor for calibration

    # Calculate the distance; a larger bounding box height indicates closer proximity
    distance = scaling_factor / box_height if box_height > 0 else 50  # Prevent division by zero

    return max(0, distance)  # Ensure distance is not negative


def display_warning_sign(frame, message):
    # Set font scale and thickness for larger, bolder text
    font_scale = 3  # Increased for larger text
    thickness = 8  # Increased for thicker text

    # Calculate text size and position
    text_size = cv2.getTextSize(message, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
    text_x = (frame.shape[1] - text_size[0]) // 2
    text_y = (frame.shape[0] + text_size[1]) // 2

    # Display the warning message in red
    cv2.putText(frame, message, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 255), thickness)


if __name__ == "__main__":
    main()
