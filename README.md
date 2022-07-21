# Sudoku
Sudoku.py contains a sudoku game with the option to solve it automatically.

## Usage
python sudoku.py

Shows the sudoku on terminal. The player can complete it manually or leave it to the script to solve it.

Upon completing the board manually, the script checks if the sudoku was solved successfully and prints a messege on terminal with the result.

## Input
To insert a number on the board the player must first indicate where by selecting a row and a column number, each going from 1 to 9.
If the coordinates are valid the user must then declare a number from 1 to 9 to place it on the indicated space, or 0 to erase the previous number on that space.

## Logic
A recursive backtracking algorithm is used to solve the puzzle.
The function the script uses to solve it identifies the next empty space on the board and iterates through all numbers from 1 to 9 until it finds a valid option to fill the space, according to the rules of sudoku, to then use recursion to do the same with the next empty space. If the script is not able to find a valid number it backtracks to the last step of the recursion, where it tries the next number.
This continiues until there are no empty spaces left on the board, to then return True if the sudoku could be solved, or False the given board has no actual solution.

### SudokuBoards
Module that contains a dictionary with unsolved sudoku boards, the main script generates a random number to pick a board from it.
