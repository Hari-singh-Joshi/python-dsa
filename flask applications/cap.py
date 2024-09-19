import cv2


import time
import os

# Create a directory to save images if it doesn't exist
output_dir = 'dataset'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get user input for name and college ID
name = input("Enter your name: ")
college_id = input("Enter your college ID: ")

# Initialize the camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Start capturing images
start_time = time.time()
image_count = 0

print("Capturing images for 10 seconds. Press 'q' to stop early.")

while time.time() - start_time < 7:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame (optional)
    cv2.imshow('Capturing Images', frame)

    # Save the frame with a unique filename
    image_filename = os.path.join(output_dir, f'{name}_{college_id}_{image_count}.jpg')
    cv2.imwrite(image_filename, frame)

    # Increment the image count
    image_count += 1

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

print(f"Captured {image_count} images and saved to '{output_dir}'.")

# Save the metadata to a text file
metadata_filename = os.path.join(output_dir, f'{name}_{college_id}_metadata.txt')
with open(metadata_filename, 'w') as f:
    f.write(f"Name: {name}\n")
    f.write(f"College ID: {college_id}\n")
    f.write(f"Number of Images Captured: {image_count}\n")

print(f"Metadata saved to '{metadata_filename}'.")
