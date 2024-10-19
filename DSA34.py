# Sudoku Solver

'''
Write a program to solve a sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:-
1- Each of the digits 1-9 must occur exactly once in each row.
2- Each of the digits 1-9 must occur exactly once in each column.
3- Each of the digits 1-9 must occur exactly once in each f the 9 (3*3) sub-boxes of the grid.
'''





from typing import List
class Solution:
    def solveSudoku(board):
        def isgood(board, row, col, i):
            for j in board[row]:
                if j == str(i):
                    return False
            for j in range(9):
                if board[j][col] == str(i):
                    return False
            temprow = (row // 3) * 3
            tempcol = (col // 3) * 3
            for a in range(temprow, temprow + 3):
                for b in range(tempcol, tempcol + 3):
                    if board[a][b] == str(i):
                        return False
            return True
        dot = 0
        for line in board:
            for i in line:
                if i == ".":
                    dot += 1
        def help(board, row, col):
            if row == 9:
                return True
            nextrow = row
            nextcol = col
            if col == 9:
                return help(board, row + 1, 0)
            if board[row][col] != ".":
                return help(board, row, col + 1)
            for i in range(1, 10):
                if isgood(board, row, col, i):
                    board[row][col] = str(i)
                    if help(board, nextrow, nextcol):
                        return True
                    else:
                        board[row][col] = "."
        help(board, 0, 0)
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution.solveSudoku(board)
print(board)