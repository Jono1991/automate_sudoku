import pyautogui
import time
from modules.cell_locations import cell_locations_dict, center_coordinates_dict, number_pad_dict

def click_sudoku_cells(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            key = f"{i}_{j}"
            if key in cell_locations_dict:
                center_x, center_y = center_coordinates_dict[key]
                pyautogui.click(center_x, center_y)
                time.sleep(0.1)
                number = matrix[i][j]
                if number in number_pad_dict:
                    number_x, number_y = number_pad_dict[number]
                    pyautogui.click(number_x, number_y)
                time.sleep(0.1)
