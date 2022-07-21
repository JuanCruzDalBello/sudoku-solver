# Sudoku solver
# Juan Cruz Dal Bello - Portfolio Project

import copy
import random
import os

import SudokuBoards


def print_instructions():
    print('1. Enter row and colum, separated by a space(r c)\n')
    print('2. Enter the number you want to put on the board (1 - 9)')
    print('\ta. Enter 0 if you want to erase a previously entered number on those coordinates.\n')
    print('If any input is non valid, the program will skip that turn.\n')
    print('If you want the program to auto solve the sudoku press "Enter" without any other input on step 1.')
    print()


def clear_console():
    os.system('cls')


def print_board(board):
    """
    Prints board on console.
    """
    for index_r, row in enumerate(board):
        if index_r % 3 == 0 and index_r != 0:
            print('-------+--------+------')

        for index_n, num in enumerate(row):
            if index_n % 3 == 0 and index_n != 0:
                print(' | ', end='')

            if num != 0:
                print(num, end=' ')
            else:      
                print('·', end=' ')

        print()
    
    print('\n')


def next_empty(board):
    """
    Searches for a 0 in the board and returns its coordinates (row, col). Returns None if it does not find a 0.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    
    return None


def valid(board, n, position):      # position must be a tuple
    """
    Returns True if a number does not repeat on the same row, column or cube as n, returns False other ways
    """
    # Check the same row
    row = board[position[0]]
    for index, num in enumerate(row):
        if num == n and index != position[1]:
            return False

    # Check the same column
    for i in range(len(board[0])):
        if board[i][position[1]] == n and i != position[0]:
            return False
  
    # Check the 3x3 cube
    cube_row = (position[0] // 3) * 3           # First check which cube to check
    cube_col = (position[1] // 3 ) * 3
    
    for i in range(cube_row, cube_row + 3):     # Iterate over that cube
        for j in range(cube_col, cube_col + 3):
            if board[i][j] == n and (i, j) != position:
                return False            
    
    return True


def solve_board(board):
    """
     Checks the row and column of the next empty space on the board.
     Tries every number from 1 to 9 on the coordinates and if any of them
    is valid changes that space's value to that number, then uses recursion
    to complete the next empty space.
     If there is no valid number it leaves the space blank and goes back to
    the last iteration, to try another number.
     If there are no more empty spaces on the board, it returns True,
    as the puzzle is solved.
    """
    found = next_empty(board)
    if not found:
        return True
    else:
        row, col = found
    
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i
        
            if solve_board(board):
                return True

            # TODO: checkear si esto requiere un tabulado menos, para quedar afuera del if
            board[row][col] = 0
    
    return False


def valid_coordinates(coordinates):
    """
    Checks if a set of coordinates is valid.
    """
    # Valid coordinates should be a tuple with 2 integers between 1 and 9 inclusive.
    if type(coordinates) != tuple:
        return False

    if len(coordinates) != 2:
        return False

    try:
        if int(coordinates[0]) in range(1, 10) and int(coordinates[1]) in range(1, 10):
            return True
        return False
    except ValueError:
        return False


def valid_number(num):
    """
    Checks if a number is valid to use on the board.
    """
    # Only numbers between 0 and 9 inclusive are valid.
    try:
        if int(num) in range(10):
            return True
        return False
    except ValueError:
        return False


def solved_correctly(original_board, player_board):
    """
    Returns True if a board was solved successfully, comparing it to the correctly solved original board, returns False otherwise.
    """
    if player_board == solve_board(original_board):
        return True
    
    return False


def show_solved_board(board):
    """
    Prints solved board, or a messege saying it was completed incorrectly.
    """
    if not solve_board(board):
        print('\n--------- NO SOLUTION FOR THIS BOARD ---------\n')
        return
    else:
        print('\n--------- SOLVED BOARD ---------\n')
        print_board(board)
        return


def main():
    board = SudokuBoards.boards[str(random.randint(1, len(SudokuBoards.boards)))]       # Original board, remains unchanged until the end of the program, where it is solved
    
    player_board = copy.deepcopy(board)     # Copy the origianl board to have that as a reference to solve it

    while True:
        # Check if there are still empty spaces on the board
        # if not empty_spaces_left(player_board):
        if next_empty(player_board) == None:
            solve_board(board)
            if player_board == board:
                print('\n---------- CONGRATULATIONS, PUZZLE SOLVED CORRECTLY ---------\n')
                break
            else:               
                print('\n---------- INCORRECT SOLUTION, TRY AGAIN ---------\n')
                break

        clear_console()

        # Print instructions and board
        print_instructions()
        print_board(player_board)

        # Checking if the coordinates are valid
        user_input = tuple(input('Enter row, column (from 1 to 9): ').split(' '))
        if valid_coordinates(user_input):
            # Checking if number is valid
            number = input('Enter number (1 - 9): ')
            if valid_number(number):
                player_board[int(user_input[0]) - 1][int(user_input[1]) - 1] = int(number)
        else:
            # Ask if autosolve 
            if user_input[0] == '':
                # Solve the board
                solve_request = input('Solve sudoku automatically? (Y/n): ').upper()
                if solve_request == 'Y':
                    player_board = copy.deepcopy(board)
                    show_solved_board(player_board)
                    break                  


if __name__ == '__main__':
    main()
