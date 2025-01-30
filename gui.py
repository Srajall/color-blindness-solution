import tkinter as tk
from tkinter import ttk

def create_gui():
    """
    Create a simple GUI for the color adjustment tool.
    """
    root = tk.Tk()
    root.title("Color Adjustment Tool")

    # Hue shift slider
    hue_shift_label = ttk.Label(root, text="Hue Shift:")
    hue_shift_label.pack()
    hue_shift_slider = ttk.Scale(root, from_=0, to=180, orient="horizontal")
    hue_shift_slider.pack()

    # Brightness slider
    brightness_label = ttk.Label(root, text="Brightness:")
    brightness_label.pack()
    brightness_slider = ttk.Scale(root, from_=-100, to=100, orient="horizontal")
    brightness_slider.pack()

    # Calibration button
    calibration_button = ttk.Button(root, text="Calibrate", command=calibration)
    calibration_button.pack()

    root.mainloop()