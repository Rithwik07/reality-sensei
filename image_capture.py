import cv2 # Imports the OpenCV library for computer vision tasks
from PIL import Image # Imports the Pillow library for image processing

def capture_image(file_path="scene.jpg"):
    """
    Captures a single image from the webcam and saves it.
    
    This function uses OpenCV's `VideoCapture` to access the computer's
    webcam (camera index 0). It reads a single frame, saves it as a JPEG
    file, and then returns a Pillow Image object for further processing.
    This is an essential first step for any application that needs to
    analyze a real-time visual scene.
    """
    cap = cv2.VideoCapture(0) # 'cap' is a VideoCapture object for the default camera (0).
    if not cap.isOpened(): # Checks if the camera was successfully opened.
        print("Error: Could not open video device.")
        return None
    ret, frame = cap.read() # Reads a single frame from the camera. `ret` is a boolean, `frame` is the image data.
    if ret: # Checks if the frame was read successfully.
        cv2.imwrite(file_path, frame) # Saves the frame to a file on the disk.
        print(f"Image captured and saved to {file_path}")
    else:
        print("Error: Could not read frame from camera.")
        return None
    cap.release() # Releases the camera so other applications can use it.
    return Image.open(file_path) # Loads the saved image file into a Pillow object.