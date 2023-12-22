import os
import cv2
import numpy as np
import pyautogui
import time
from modules.cell_locations import cell_locations_dict, center_coordinates_dict, number_pad_dict

# Create an empty 9x9 array
matrix = np.zeros((9, 9), dtype=int)

def find_template(template, screenshot):
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val

# Folder containing template images
template_folder = "C:\\Users\\John\\PycharmProjects\\sudokuBot\\images"

# initial delay before game
time.sleep(3)

# Loop through every entry in the cell_locations_dict
for cell_name, coordinates in cell_locations_dict.items():
    x1, y1, x2, y2 = coordinates

    # Take a screenshot using pyautogui
    screenshot = pyautogui.screenshot()
    screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Define the region coordinates for cropping
    cropped_region = screenshot_np[y1:y2, x1:x2]

    # Loop through every image in the folder
    for filename in os.listdir(template_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            template_path = os.path.join(template_folder, filename)

            # Load the template image
            template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)

            # Find the template in the cropped region
            match_value = find_template(template, cropped_region)

            # Set a threshold for matching, adjust as needed
            threshold = 0.85

            # Extract the first number from the filename
            number = int(str(filename)[0])

            to_add = False

            # Update the matrix based on the match result
            if match_value >= threshold:
                print("found: " + filename + " " + str(number) + " " + str(cell_name) + " " + str(coordinates))
                matrix[int(cell_name.split('_')[0])][int(cell_name.split('_')[1])] = number
                break
            else:
                print("not found: " + filename + " " + str(number) + " " + str(cell_name) + " " + str(coordinates))
                # Leave the matrix entry as blank if no match is found
                matrix[int(cell_name.split('_')[0])][int(cell_name.split('_')[1])] = 0
