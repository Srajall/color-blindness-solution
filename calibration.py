import cv2
import numpy as np

# Global variables for calibration
click_coords = None
calibration_state = "idle"
current_color = None
color_patches = {
    "red": (0, 0, 255),
    "green": (0, 255, 0),
    "blue": (255, 0, 0),
    "yellow": (0, 255, 255),
    "cyan": (255, 255, 0),
    "magenta": (255, 0, 255)
}
adjustments = {}

def on_mouse_click(event, x, y, flags, param):
    """
    Callback function to handle mouse click events.
    """
    global click_coords
    if event == cv2.EVENT_LBUTTONDOWN:  # Left mouse button clicked
        click_coords = (x, y)

def start_calibration():
    """
    Start the calibration process.
    """
    global calibration_state, current_color, adjustments
    calibration_state = "calibrating"
    current_color = iter(color_patches.keys())
    adjustments = {}
    print("Starting calibration...")
    print("Click on the color patch that matches the color you see.")

def wait_for_click():
    """
    Wait for the user to click on the patch.
    """
    global click_coords
    click_coords = None
    while click_coords is None:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Allow quitting with 'q'
            return False
    return True

def update_calibration(frame):
    """
    Update the calibration process based on user input.
    :param frame: The current frame from the camera.
    :return: The updated frame with the calibration patch.
    """
    global calibration_state, current_color, click_coords

    if calibration_state != "calibrating":
        return frame

    try:
        color_name = next(current_color)  # Get the next color
        color_bgr = color_patches[color_name]

        # Create a blank image with the color patch
        patch = np.zeros((200, 200, 3), dtype=np.uint8)
        patch[:, :] = color_bgr

        # Display instructions
        instructions = f"Click on the {color_name} patch."
        cv2.putText(patch, instructions, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Overlay the patch on the frame
        frame[10:210, 10:210] = patch

        # Display the frame with the patch
        cv2.imshow('Adjusted Frame', frame)

        # Wait for the user to click on the patch
        print(f"Please click on the {color_name} patch.")
        if not wait_for_click():
            return frame  # Quit if the user presses 'q'

        # Check if the click is within the patch area
        x, y = click_coords
        if 10 <= x <= 210 and 10 <= y <= 210:  # Check if click is within the patch
            print(f"You clicked on the {color_name} patch.")
            adjustments[color_name] = color_name  # No adjustments needed for now
        else:
            print("Please click on the patch.")
            return frame  # Do not move to the next color
    except StopIteration:
        # Calibration complete
        calibration_state = "complete"
        print("Calibration complete!")
        print("Calibration results:", adjustments)

    return frame