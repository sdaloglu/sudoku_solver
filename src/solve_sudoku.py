"""
    This code solves a sudoku puzzle using backtracking algorithm.

    Explain how it works step by step

    Backtracking algorithm is a brute force method which tries
    all possible values for the empty boxed until it finds the correct one.

    The algorithm reverts back to the previous configuration of the sudoku
    table as soon as a contradiction is found with the current configuration.




    Written by Sabahattin Mert Daloglu: smd89@cam.ac.uk
"""


# Load Modules:
import sys
from Sudoku import backtracking as bt
from Sudoku import board as bd


# Extracting the input and the output file from the command line
input_file = sys.argv[1]


# Trapping files that can not be opened

try:
    f = open(input_file, "r")
except IOError:
    print("File could not be opened")
else:
    print("Input file opened successfully")

    # Read the text file into a string
    data = f.read()


# output_file = sys.argv[2]


# Reading the input txt file and converting it to a 9x9 numpy array
sudoku_array = bd.board_to_array(data)


def solve_sudoku(sudoku_array):
    if bt.find_empty(sudoku_array) is None:
        return True

    else:
        empty_box = bt.find_empty(sudoku_array)

    for guess in range(1, 10):
        valid = bt.check_validity(sudoku_array, guess, empty_box)
        if valid:
            sudoku_array[empty_box[0], empty_box[1]] = guess

            # Recursive call to solve_sudoku function
            if solve_sudoku(sudoku_array):
                return True

            # Sequence of guesses is not valid, revert back
            sudoku_array[empty_box[0], empty_box[1]] = 0

    return False


f.close()

print(solve_sudoku(sudoku_array))
print(sudoku_array)
