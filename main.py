from functions import *

open_sudoku()
base_matrix = get_main_matrix()
draft_matrix = matrix_generator(9, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print_matrix(base_matrix)
print('------------------')
base_matrix = solve_matrix(base_matrix, draft_matrix)
print_matrix(base_matrix)