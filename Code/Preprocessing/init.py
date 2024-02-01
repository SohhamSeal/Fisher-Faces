# Import the necessary libraries

import os  # For file system operations
try:
    import cv2 # OpenCV library for computer vision tasks
except ImportError:
    # OpenCV not installed, installing it
    import subprocess
    subprocess.run(["pip", "install", "opencv-python"])
    # Importing OpenCV after installation
    import cv2
# Now you can use cv2 in your code

location = input("Enter the dataset location: ") # For eg: "Dataset\Celebrity Faces Dataset" (Input)
save_location = input("Enter th edestination to store the cropped images: ") # For eg: "Dataset\Cropped Celebrity Faces Dataset" (Input)