import numpy as np
import cv2
import os

# Function to apply brightness and contrast adjustments
def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    # Code for brightness and contrast adjustment
    # ...
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf



# Input and output directories
input_folder = 'C:/Users/iamge/Desktop/VEGF/DR 2 REPLICATE'  # Folder path where input images are stored
output_folder = 'C:/Users/iamge/Desktop/VEGF/Contrast Enhancement/DR 2 REPLICATE'  # Folder path to save the processed images

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (optional)
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read the image
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        # Resize the image
        img = cv2.resize(img, (800, 800), 0, 0, cv2.INTER_AREA)

        # Apply brightness and contrast adjustments
        enhanced_img = apply_brightness_contrast(img, brightness=0, contrast=64)

        # Save the processed image to the output folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, enhanced_img)

        print(f"Processed and saved: {output_path}")
