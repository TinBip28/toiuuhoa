import numpy as np


def valid_queen_moves(coord):
    """
    Tính toán các ô mà quân hậu có thể di chuyển tới từ tọa độ coord.

    Args:
        coord (tuple): Tọa độ của quân hậu (dạng (row, col)).

    Returns:
        list: Danh sách các tọa độ mà quân hậu có thể di chuyển tới.
    """
    row, col = coord
    valid_moves = []

    # Di chuyển theo hàng ngang và hàng dọc
    for i in range(8):
        if i != col:
            valid_moves.append((row, i))  # Di chuyển theo hàng ngang
        if i != row:
            valid_moves.append((i, col))  # Di chuyển theo hàng dọc

    # Di chuyển theo đường chéo
    for i in range(1, 8):
        if 0 <= row + i < 8 and 0 <= col + i < 8:
            valid_moves.append((row + i, col + i))  # Đường chéo phải trên
        if 0 <= row - i < 8 and 0 <= col + i < 8:
            valid_moves.append((row - i, col + i))  # Đường chéo phải dưới
        if 0 <= row + i < 8 and 0 <= col - i < 8:
            valid_moves.append((row + i, col - i))  # Đường chéo trái trên
        if 0 <= row - i < 8 and 0 <= col - i < 8:
            valid_moves.append((row - i, col - i))  # Đường chéo trái dưới

    return valid_moves


# Ví dụ: Tính toán các nước đi hợp lệ cho quân hậu tại tọa độ (3, 4)
queen_coord = (3, 4)
valid_moves = valid_queen_moves(queen_coord)
# print("Các ô mà quân hậu có thể di chuyển tới:", valid_moves)

cols = "abcdefgh"
rows = range(1, 9, 1)


def getAllCells(arr1, arr2):
    board = []
    for i in arr1:
        row = []
        for j in arr2:
            row.append(f"{i}{j}")
        board.append(row)
    return board


# print(chess)


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


a = queenMoves("a1")
