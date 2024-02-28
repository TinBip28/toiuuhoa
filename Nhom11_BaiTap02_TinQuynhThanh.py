"""
Thông tin nhóm
Lê Quang Tín, 22001643, K67KHMT&TT
Trần Giao Quỳnh, 22001635, K67KHMT&TT
Trần Viết Thành, 220016, K67KHMT&TT

Danh sách bài tập
- Bài 1. getAllCells(), printWhitePos() ,printChessBoard()
- Bài 2. getRandomElement() 
- Bài 3. filterElement()
- Bài 4. queenMoves()
- Bài 5. display()
"""

import random as rd

cols = "abcdefgh"
rows = range(8, 0, -1)


# Bài 1
def getAllCells(arr1, arr2):
    board = []
    for i in arr1:
        row = []
        for j in arr2:
            row.append(f"{i}{j}")
        board.append(row)
    return board


chess = getAllCells(cols, rows)
# print(chess)


def printWhitePos(colums, rows):
    whiteChess = []
    for row in rows:
        for col in colums:
            if row % 2 == ord(col) % 2:
                whiteChess.append(f"{col}{row}")
    return whiteChess


# print(printWhitePos(cols, rows))


def printChessBoard(colums, rows):
    for row in rows:
        print()
        for col in colums:
            print(f"{col}{row}", end="  ")


printChessBoard(cols, rows)


# Bài 2
rdList = ["a", "b", "c", "d", "e", "f", "g", "h"]


def getRandomElement(list):
    n = len(list)
    if n == 0:
        return None
    else:
        i = rd.randrange(0, n)
        return list[i]


randomEle = getRandomElement(rdList)
print(randomEle)


# Bài 3
listA = [1, 2, 3, 4, 5]
listB = [4, 5, 6, 7, 8]


def filterElement(listA, listB):
    listC = []
    if len(listA) == 0:
        return None
    else:
        for i in listA:
            if i not in listB:
                listC.append(i)
        return listC


filter = filterElement(listA, listB)

print(filter)


# Bài 4
def queenMoves(coord):
    x = coord[0]
    y = coord[1]
    moves = []
    for i in cols:
        if i != x:
            moves.append(f"{i}{y}")
    for j in rows:
        if j != int(y):
            moves.append(f"{x}{j}")
    for k in range(1, 9):
        if 97 <= ord(x) + k < 106 and 1 <= int(y) + k < 9:
            moves.append(f"{chr(ord(x) + k)}{int(y) + k}")
        if 97 <= ord(x) - k < 106 and 1 <= int(y) + k < 9:
            moves.append(f"{chr(ord(x) - k)}{int(y) + k}")
        if 97 <= ord(x) + k < 106 and 1 <= int(y) - k < 9:
            moves.append(f"{chr(k + ord(x))}{int(y) - k}")
        if 97 <= ord(x) - k < 106 and 1 <= int(y) - k < 9:
            moves.append(f"{chr(ord(x) - k)}{int(y) - k}")
    return moves


coordinate = queenMoves("a1")
print(coordinate)


# Bài 5
import chess


def display(fen):
    board = chess.Board(fen)
    print(board)


fen = "r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4"

display(fen)
