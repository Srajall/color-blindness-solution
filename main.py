import cv2
from calibration import start_calibration, update_calibration, on_mouse_click
from color_adjustment import adjust_hue

def main():
    # Start calibration
    start_calibration()

    # Open the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Create a resizable window
    cv2.namedWindow("Adjusted Frame", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Adjusted Frame", on_mouse_click)  # Set mouse callback

    # Main loop
    hue_shift = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Update calibration process
        frame = update_calibration(frame)

        # Apply hue shift to EVERY frame
        adjusted_frame = adjust_hue(frame, hue_shift)

        # Display the adjusted frame
        cv2.imshow('Adjusted Frame', adjusted_frame)

        # Handle key inputs
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('+'):
            hue_shift += 5
            print(f"Hue shift increased to: {hue_shift}")
        elif key == ord('-'):
            hue_shift -= 5
            print(f"Hue shift decreased to: {hue_shift}")

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()