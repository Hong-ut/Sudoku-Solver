from typing import List

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0

    return False

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

class SudokuSolver:
    board1: List[List[int]] = []
    board2: List[List[int]] = []
    board: List[List[int]] = []
    def __init__(self, twoDigitBoard: List[List[int]]):
        for row in twoDigitBoard:
            board1Row = []
            board2Row = []

            for col in row:
                #assume the board contains valid 2 digit ints and 0 reps unfilled space
                num1: int = int(col / 10)
                num2: int = col % 10

                board1Row.append(num1)
                board2Row.append(num2)
                
            self.board1.append(board1Row)
            self.board2.append(board2Row)

    def solveBoard(self):
        solve(self.board1)
        solve(self.board2)

    def getBoard1(self):
        return self.board1
        

    def getBoard2(self):
        return self.board2
    

# print_board(board)
# solve(board1)
# solve(board2)
# print("\n\n\n")

# for row in range(len(board)):
#     for col in range(len(board[row])):
#         board[row][col] = (board1[row][col] * 10) + board2[row][col]


# print_board(board)
