from modules.solve import *
from modules.detect_number import *
from modules.clicker import *

# solve puzzle
solve_sudoku(matrix)

# activate clicker
click_sudoku_cells(matrix)

# Ensure solve.py runs
if find_empty(matrix) is None:
    print("\nSolved Sudoku Board:")
else:
    print("No solution exists for puzzle.")

print(matrix)
