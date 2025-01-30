import cv2
import numpy as np

def adjust_hue(frame, shift=0):
    """
    Adjust the hue of the frame by shifting the hue channel in HSV space.
    :param frame: Input frame (BGR format).
    :param shift: Amount to shift the hue (0-180 in OpenCV).
    :return: Adjusted frame.
    """
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Convert the hue channel to int32 to avoid overflow
    hue_channel = hsv_frame[:, :, 0].astype(np.int32)
    
    # Apply shift and modulo 180
    hue_channel = (hue_channel + shift) % 180
    
    # Convert back to uint8
    hsv_frame[:, :, 0] = hue_channel.astype(np.uint8)
    
    return cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)