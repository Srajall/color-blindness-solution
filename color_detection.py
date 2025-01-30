import cv2
import numpy as np

def detect_dominant_color_kmeans(frame, k=3):
    """
    Detect the dominant color using k-means clustering.
    :param frame: Input frame (BGR format).
    :param k: Number of clusters.
    :return: Dominant color in BGR format.
    """
    pixels = frame.reshape(-1, 3).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    dominant_label = np.argmax(np.bincount(labels.flatten()))
    dominant_color = centers[dominant_label].astype(int)
    return dominant_color