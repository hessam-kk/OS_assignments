import threading
import random
import time
from os import system


def check_row(sudoku_1: list, result: dict):
    for row in sudoku_1:
        tt = sorted(row)
        if tt != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result['valid'] = False
            return


def check_col(sudoku_1: list, result: dict):
    for i in range(9):
        temp = []
        for row in sudoku_1:
            temp.append(row[i])
        if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            result['valid'] = False


def check_square(square: list, result: dict):
    square.sort()
    if square != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        result['valid'] = False
        return


result = {'valid': True}
sudoku_1 = [[6, 2, 4, 5, 3, 9, 1, 8, 7],
            [5, 1, 9, 7, 2, 8, 6, 3, 4],
            [8, 3, 7, 6, 1, 4, 2, 9, 5],
            [1, 4, 3, 8, 6, 5, 7, 2, 9],
            [9, 5, 8, 2, 4, 7, 3, 6, 1],
            [7, 6, 2, 3, 9, 1, 4, 5, 8],
            [3, 7, 1, 9, 5, 6, 8, 4, 2],
            [4, 9, 6, 1, 8, 2, 5, 7, 3],
            [2, 8, 5, 4, 7, 3, 9, 1, 6]]

system('cls')

# Checking Rows Validation
x1 = threading.Thread(target=check_row, args=(sudoku_1, result,))
x1.start()

# Checking Columns Validation
if result['valid']:
    x2 = threading.Thread(target=check_col, args=(sudoku_1, result,))
    x2.start()

if result['valid']:
    # initializing square for the rest 9 threads
    sq1 = [sudoku_1[0][0], sudoku_1[0][1], sudoku_1[0][2],
           sudoku_1[1][0], sudoku_1[1][1], sudoku_1[1][2],
           sudoku_1[2][0], sudoku_1[2][1], sudoku_1[2][2]]

    sq2 = [sudoku_1[0][3], sudoku_1[0][4], sudoku_1[0][5],
           sudoku_1[1][3], sudoku_1[1][4], sudoku_1[1][5],
           sudoku_1[2][3], sudoku_1[2][4], sudoku_1[2][5]]

    sq3 = [sudoku_1[0][6], sudoku_1[0][7], sudoku_1[0][8],
           sudoku_1[1][6], sudoku_1[1][7], sudoku_1[1][8],
           sudoku_1[2][6], sudoku_1[2][7], sudoku_1[2][8]]

    sq4 = [sudoku_1[3][0], sudoku_1[3][1], sudoku_1[3][2],
           sudoku_1[4][0], sudoku_1[4][1], sudoku_1[4][2],
           sudoku_1[5][0], sudoku_1[5][1], sudoku_1[5][2]]

    sq5 = [sudoku_1[3][3], sudoku_1[3][4], sudoku_1[3][5],
           sudoku_1[4][3], sudoku_1[4][4], sudoku_1[4][5],
           sudoku_1[5][3], sudoku_1[5][4], sudoku_1[5][5]]

    sq6 = [sudoku_1[3][6], sudoku_1[3][7], sudoku_1[3][8],
           sudoku_1[4][6], sudoku_1[4][7], sudoku_1[4][8],
           sudoku_1[5][6], sudoku_1[5][7], sudoku_1[5][8]]

    sq7 = [sudoku_1[6][0], sudoku_1[6][1], sudoku_1[6][2],
           sudoku_1[7][0], sudoku_1[7][1], sudoku_1[7][2],
           sudoku_1[8][0], sudoku_1[8][1], sudoku_1[8][2]]

    sq8 = [sudoku_1[6][3], sudoku_1[6][4], sudoku_1[6][5],
           sudoku_1[7][3], sudoku_1[7][4], sudoku_1[7][5],
           sudoku_1[8][3], sudoku_1[8][4], sudoku_1[8][5]]

    sq9 = [sudoku_1[6][6], sudoku_1[6][7], sudoku_1[6][8],
           sudoku_1[7][6], sudoku_1[7][7], sudoku_1[7][8],
           sudoku_1[8][6], sudoku_1[8][7], sudoku_1[8][8]]

    # starting square threads
    x3 = threading.Thread(target=check_square, args=(sq1, result,))
    x3.start()
    x4 = threading.Thread(target=check_square, args=(sq2, result,))
    x4.start()
    x5 = threading.Thread(target=check_square, args=(sq3, result,))
    x5.start()
    x6 = threading.Thread(target=check_square, args=(sq4, result,))
    x6.start()
    x7 = threading.Thread(target=check_square, args=(sq5, result,))
    x7.start()
    x8 = threading.Thread(target=check_square, args=(sq6, result,))
    x8.start()
    x9 = threading.Thread(target=check_square, args=(sq7, result,))
    x9.start()
    x10 = threading.Thread(target=check_square, args=(sq8, result,))
    x10.start()
    x11 = threading.Thread(target=check_square, args=(sq9, result,))
    x11.start()

    # make them wait
    x1.join()
    x2.join()
    x3.join()
    x4.join()
    x5.join()
    x6.join()
    x7.join()
    x8.join()
    x9.join()
    x10.join()
    x11.join()

print(result)
