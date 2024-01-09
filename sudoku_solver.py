"""
This program will solve a sudoku puzzle utilizing backtracking 
"""



board = [[0, 3, 0, 0, 0, 0, 0, 0, 1],
         [9, 0, 7, 0, 8, 0, 0, 3, 0],
         [0, 8, 0, 2, 0, 4, 6, 0, 0],
         [4, 0, 0, 6, 0, 7, 3, 1, 0],
         [8, 7, 0, 0, 2, 0, 0, 0, 9],
         [0, 0, 3, 1, 0, 0, 0, 4, 2],
         [0, 1, 0, 0, 0, 0, 0, 8, 0],
         [5, 0, 2, 0, 6, 0, 0, 7, 0],
         [0, 0, 0, 3, 0, 5, 4, 0, 6]]

solved_board = [[2, 3, 4, 9, 7, 6, 8, 5, 1],
                [9, 6, 7, 5, 8, 1, 2, 3, 4],
                [1, 8, 5, 2, 3, 4, 6, 9, 7],
                [4, 2, 9, 6, 5, 7, 3, 1, 8],
                [8, 7, 1, 4, 2, 3, 5, 6, 9],
                [6, 5, 3, 1, 9, 8, 7, 4, 2],
                [3, 1, 6, 7, 4, 2, 9, 8, 5],
                [5, 4, 2, 8, 6, 9, 1, 7, 3],
                [7, 9, 8, 3, 1, 5, 4, 2, 6]]

def print_board(board):
    
    # Prints horizontal lines that seperate rows into sets of 3
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-- --   -- --   -- --")
        
        # Prints vertical lines that seperate columns into sets of 3
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
                
            # Prints out the numbers at the position
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")
       
                
# Finds a position in the board that is empty, denoted by 0
def find_empty(board):
    
    for k in range(len(board)):
        for l in range(len(board[0])):
            if board[k][l] == 0:
                
                # Returns the location of the empty position (row, column)
                return (k, l)
            
def check_valid(board, number, position):
    
    k, l = position
    
    # Check row
    for m in range(len(board[0])):
        if board[k][m] == number and k != m:
            return False
    
    # Check column
    for n in range(len(board)):
        if board[m][l] == number and l != n:
            return False
        
    # Check box
    
    
    