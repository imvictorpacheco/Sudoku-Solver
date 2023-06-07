from functions import *

# open_sudoku()
# base_matrix = get_main_matrix()
base_matrix = [
[0, 0, 5, 4, 7, 6, 0, 0, 3],
[0, 0, 0, 0, 1, 8, 6, 4, 7],
[0, 0, 7, 2, 0, 1, 0, 8, 0],
[0, 0, 9, 3, 0, 2, 0, 0, 0],
[8, 7, 3, 0, 0, 0, 1, 2, 0],
[2, 0, 0, 7, 0, 4, 0, 0, 9],
[0, 0, 0, 0, 2, 0, 4, 9, 1],
[1, 0, 4, 8, 9, 7, 5, 3, 0],
[5, 0, 2, 1, 4, 0, 7, 6, 0]
]
draft_matrix = matrix_generator(9, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print_matrix(base_matrix)
print('------------------')
base_matrix = solve_matrix(base_matrix, draft_matrix)
print_matrix(base_matrix)