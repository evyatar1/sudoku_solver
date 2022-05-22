# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


board = [
    [0, 2, 0, 3, 0, 0, 0, 0, 0],
    [6, 0, 8, 0, 0, 0, 5, 1, 3],
    [0, 0, 5, 0, 1, 0, 2, 0, 6],
    [3, 8, 9, 5, 7, 1, 6, 2, 4],
    [4, 1, 6, 8, 9, 2, 7, 3, 5],
    [0, 0, 2, 6, 3, 4, 0, 8, 0],
    [0, 0, 0, 2, 6, 0, 0, 5, 0],
    [2, 0, 3, 1, 4, 0, 0, 0, 7],
    [0, 6, 4, 7, 8, 0, 0, 0, 2]
]


def solver(board):
    find = find_empty_element(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solver(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, position):
    # check for row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # check for column
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # check box in the board
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != position:
                return False

    return True


def print_board():
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("----------------------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


def find_empty_element(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

    return None


if __name__ == '__main__':
    print_board()
    print()
    solver(board)
    print()
    print_board()
