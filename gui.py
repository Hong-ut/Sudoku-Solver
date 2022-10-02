import tkinter as tk
from board import board
from SUDOKU import SudokuSolver

def updateBoard(sudokuGridFrame: tk.Frame, s: SudokuSolver):
    for r in range(9):
        for c in range(9):
            cellText = (s.getBoard1()[r][c] * 10) + s.getBoard2()[r][c]
            
            button = tk.Button(sudokuGridFrame, text=' ' if cellText == 0 else cellText, width=2, height=1, padx=3, pady=3)
            button.grid(row=r, column=c)


s = SudokuSolver(board)

window = tk.Tk()
window.title('Sudoku')
window.geometry('270x330')

sudokuGrid = tk.Frame(window)
sudokuGrid.pack()

updateBoard(sudokuGrid, s)

solveButton = tk.Button(window, text='Click to solve', bg='red', command=lambda : (
    s.solveBoard(),
    updateBoard(sudokuGrid, s)
))

solveButton.pack()

window.mainloop()
