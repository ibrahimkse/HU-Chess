import sys

f = open(sys.argv[1], "r")
commands = [line.split() for line in f.readlines()]
f.close()
white = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "r1", "n1", "b1", "qu", "b2", "n2", "r2"]
black = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "R1", "N1", "B1", "QU", "B2", "N2", "R2"]
white_pawn = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
black_pawn = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"]
white_rook = ["r1", "r2"]
black_rook = ["R1", "R2"]
white_knight = ["n1", "n2"]
black_knight = ["N1", "N2"]
white_bishop = ["b1", "b2"]
black_bishop = ["B1", "B2"]
possible_moves = []
a = 0
b = 0
index_range = False
chess_board = [["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"],
               ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
               ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
               ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
               ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]]
chess_board1 = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
                ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
                ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
                ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
                ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
                ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
                ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
                ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]


def index_finder(x):
    global a, b
    for z in chess_board:
        if x in z:
            a = chess_board.index(z)
            b = z.index(x)


def index_controller(x, y):
    global index_range
    index_range = False
    if 7 >= x >= 0 and 7 >= y >= 0:
        index_range = True
    return index_range


def move(x, y):
    global chess_board, a, b
    index_finder(x)
    chess_board[a][b] = "  "
    for t in chess_board1:
        if y in t:
            a = chess_board1.index(t)
            b = t.index(y)
    chess_board[a][b] = x


def show_moves(x):
    global possible_moves
    possible_moves = []
    if x in white_pawn:
        index_finder(x)
        if index_controller(a - 1, b):
            if chess_board[a-1][b] == "  " or chess_board[a-1][b] in black:
                possible_moves.append(chess_board1[a-1][b])
    if x in black_pawn:
        index_finder(x)
        if index_controller(a + 1, b):
            if chess_board[a+1][b] == "  " or chess_board[a+1][b] in white:
                possible_moves.append(chess_board1[a+1][b])
    if x in white_knight:
        index_finder(x)
        if index_controller(a-1, b-1) and chess_board[a-1][b-1] == "  ":
            possible_moves.append(chess_board1[a-1][b-1])
        if index_controller(a-1, b+1) and chess_board[a-1][b+1] == "  ":
            possible_moves.append(chess_board1[a-1][b+1])
        if index_controller(a+1, b-1) and chess_board[a+1][b-1] == "  ":
            possible_moves.append(chess_board1[a+1][b-1])
        if index_controller(a+1, b+1) and chess_board[a+1][b+1] == "  ":
            possible_moves.append(chess_board1[a+1][b+1])
        if index_controller(a-2, b-1):
            if chess_board[a-2][b-1] == "  " or chess_board[a-2][b-1] in black:
                possible_moves.append(chess_board1[a-2][b-1])
        if index_controller(a-2, b+1):
            if chess_board[a-2][b+1] == "  " or chess_board[a-2][b+1] in black:
                possible_moves.append(chess_board1[a-2][b+1])
        if index_controller(a-1, b-2):
            if chess_board[a-1][b-2] == "  " or chess_board[a-1][b-2] in black:
                possible_moves.append(chess_board1[a-1][b-2])
        if index_controller(a-1, b+2):
            if chess_board[a-1][b+2] == "  " or chess_board[a-1][b+2] in black:
                possible_moves.append(chess_board1[a-1][b+2])
        if index_controller(a+1, b-2):
            if chess_board[a+1][b-2] == "  " or chess_board[a+1][b-2] in black:
                possible_moves.append(chess_board1[a+1][b-2])
        if index_controller(a+1, b+2):
            if chess_board[a+1][b+2] == "  " or chess_board[a+1][b+2] in black:
                possible_moves.append(chess_board1[a+1][b+2])
        if index_controller(a+2, b-1):
            if chess_board[a+2][b-1] == "  " or chess_board[a+2][b-1] in black:
                possible_moves.append(chess_board1[a+2][b-1])
        if index_controller(a+2, b+1):
            if chess_board[a+2][b+1] == "  " or chess_board[a+2][b+1] in black:
                possible_moves.append(chess_board1[a+2][b+1])
    if x in black_knight:
        index_finder(x)
        if index_controller(a - 1, b - 1) and chess_board[a - 1][b - 1] == "  ":
            possible_moves.append(chess_board1[a - 1][b - 1])
        if index_controller(a - 1, b + 1) and chess_board[a - 1][b + 1] == "  ":
            possible_moves.append(chess_board1[a - 1][b + 1])
        if index_controller(a + 1, b - 1) and chess_board[a + 1][b - 1] == "  ":
            possible_moves.append(chess_board1[a + 1][b - 1])
        if index_controller(a + 1, b + 1) and chess_board[a + 1][b + 1] == "  ":
            possible_moves.append(chess_board1[a + 1][b + 1])
        if index_controller(a - 2, b - 1):
            if chess_board[a - 2][b - 1] == "  " or chess_board[a - 2][b - 1] in white:
                possible_moves.append(chess_board1[a - 2][b - 1])
        if index_controller(a - 2, b + 1):
            if chess_board[a - 2][b + 1] == "  " or chess_board[a - 2][b + 1] in white:
                possible_moves.append(chess_board1[a - 2][b + 1])
        if index_controller(a - 1, b - 2):
            if chess_board[a - 1][b - 2] == "  " or chess_board[a - 1][b - 2] in white:
                possible_moves.append(chess_board1[a - 1][b - 2])
        if index_controller(a - 1, b + 2):
            if chess_board[a - 1][b + 2] == "  " or chess_board[a - 1][b + 2] in white:
                possible_moves.append(chess_board1[a - 1][b + 2])
        if index_controller(a + 1, b - 2):
            if chess_board[a + 1][b - 2] == "  " or chess_board[a + 1][b - 2] in white:
                possible_moves.append(chess_board1[a + 1][b - 2])
        if index_controller(a + 1, b + 2):
            if chess_board[a + 1][b + 2] == "  " or chess_board[a + 1][b + 2] in white:
                possible_moves.append(chess_board1[a + 1][b + 2])
        if index_controller(a + 2, b - 1):
            if chess_board[a + 2][b - 1] == "  " or chess_board[a + 2][b - 1] in white:
                possible_moves.append(chess_board1[a + 2][b - 1])
        if index_controller(a + 2, b + 1):
            if chess_board[a + 2][b + 1] == "  " or chess_board[a + 2][b + 1] in white:
                possible_moves.append(chess_board1[a + 2][b + 1])
    if x in white_rook:
        index_finder(x)
        if index_controller(a-1, b):
            if chess_board[a-1][b] == "  " or chess_board[a-1][b] in black:
                possible_moves.append(chess_board1[a-1][b])
        if index_controller(a - 2, b):
            if chess_board[a - 1][b] == "  ":
                if chess_board[a - 2][b] == "  " or chess_board[a - 2][b] in black:
                    possible_moves.append(chess_board1[a - 2][b])
        if index_controller(a - 3, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  ":
                if chess_board[a - 3][b] == "  " or chess_board[a - 3][b] in black:
                    possible_moves.append(chess_board1[a - 3][b])
        if index_controller(a - 4, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  ":
                if chess_board[a - 4][b] == "  " or chess_board[a - 4][b] in black:
                    possible_moves.append(chess_board1[a - 4][b])
        if index_controller(a - 5, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and chess_board[a - 4][b] == "  ":
                if chess_board[a - 5][b] == "  " or chess_board[a - 5][b] in black:
                    possible_moves.append(chess_board1[a - 5][b])
        if index_controller(a - 6, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  ":
                if chess_board[a - 6][b] == "  " or chess_board[a - 6][b] in black:
                    possible_moves.append(chess_board1[a - 6][b])
        if index_controller(a - 7, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  " and chess_board[a - 6][b] == "  ":
                if chess_board[a - 7][b] == "  " or chess_board[a - 7][b] in black:
                    possible_moves.append(chess_board1[a - 7][b])
        if index_controller(a, b+1):
            if chess_board[a][b+1] == "  " or chess_board[a][b+1] in black:
                possible_moves.append(chess_board1[a][b+1])
        if index_controller(a, b+2):
            if chess_board[a][b+1] == "  ":
                if chess_board[a][b+2] == "  " or chess_board[a][b+2] in black:
                    possible_moves.append(chess_board1[a][b+2])
        if index_controller(a, b+3):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  ":
                if chess_board[a][b+3] == "  " or chess_board[a][b+3] in black:
                    possible_moves.append(chess_board1[a][b+3])
        if index_controller(a, b+4):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  ":
                if chess_board[a][b+4] == "  " or chess_board[a][b+4] in black:
                    possible_moves.append(chess_board1[a][b+4])
        if index_controller(a, b+5):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and chess_board[a][b + 4] == "  ":
                if chess_board[a][b+5] == "  " or chess_board[a][b+5] in black:
                    possible_moves.append(chess_board1[a][b+5])
        if index_controller(a, b+6):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and chess_board[a][b + 4] == "  " and chess_board[a][b + 5] == "  ":
                if chess_board[a][b+6] == "  " or chess_board[a][b+6] in black:
                    possible_moves.append(chess_board1[a][b+6])
        if index_controller(a, b+7):
            if chess_board[a][b+1] == "  " and chess_board[a][b+2] == "  " and chess_board[a][b+3] == "  " and chess_board[a][b+4] == "  " and chess_board[a][b+5] == "  " and chess_board[a][b+6] == "  ":
                if chess_board[a][b+7] == "  " or chess_board[a][b+7] in black:
                    possible_moves.append(chess_board1[a][b+7])
        if index_controller(a+1, b):
            if chess_board[a+1][b] == "  " or chess_board[a+1][b] in black:
                possible_moves.append(chess_board1[a+1][b])
        if index_controller(a + 2, b):
            if chess_board[a + 1][b] == "  ":
                if chess_board[a + 2][b] == "  " or chess_board[a + 2][b] in black:
                    possible_moves.append(chess_board1[a + 2][b])
        if index_controller(a + 3, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  ":
                if chess_board[a + 3][b] == "  " or chess_board[a + 3][b] in black:
                    possible_moves.append(chess_board1[a + 3][b])
        if index_controller(a + 4, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  ":
                if chess_board[a + 4][b] == "  " or chess_board[a + 4][b] in black:
                    possible_moves.append(chess_board1[a + 4][b])
        if index_controller(a + 5, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and chess_board[a + 4][b] == "  ":
                if chess_board[a + 5][b] == "  " or chess_board[a + 5][b] in black:
                    possible_moves.append(chess_board1[a + 5][b])
        if index_controller(a + 6, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  ":
                if chess_board[a + 6][b] == "  " or chess_board[a + 6][b] in black:
                    possible_moves.append(chess_board1[a + 6][b])
        if index_controller(a + 7, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  " and chess_board[a + 6][b] == "  ":
                if chess_board[a + 7][b] == "  " or chess_board[a + 7][b] in black:
                    possible_moves.append(chess_board1[a + 7][b])
        if index_controller(a, b-1):
            if chess_board[a][b-1] == "  " or chess_board[a][b-1] in black:
                possible_moves.append(chess_board1[a][b-1])
        if index_controller(a, b-2):
            if chess_board[a][b-1] == "  ":
                if chess_board[a][b-2] == "  " or chess_board[a][b-2] in black:
                    possible_moves.append(chess_board1[a][b-2])
        if index_controller(a, b-3):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  ":
                if chess_board[a][b-3] == "  " or chess_board[a][b-3] in black:
                    possible_moves.append(chess_board1[a][b-3])
        if index_controller(a, b-4):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  ":
                if chess_board[a][b-4] == "  " or chess_board[a][b-4] in black:
                    possible_moves.append(chess_board1[a][b-4])
        if index_controller(a, b-5):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and chess_board[a][b - 4] == "  ":
                if chess_board[a][b-5] == "  " or chess_board[a][b-5] in black:
                    possible_moves.append(chess_board1[a][b-5])
        if index_controller(a, b-6):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and chess_board[a][b - 4] == "  " and chess_board[a][b - 5] == "  ":
                if chess_board[a][b-6] == "  " or chess_board[a][b-6] in black:
                    possible_moves.append(chess_board1[a][b-6])
        if index_controller(a, b-7):
            if chess_board[a][b-1] == "  " and chess_board[a][b-2] == "  " and chess_board[a][b-3] == "  " and chess_board[a][b-4] == "  " and chess_board[a][b-5] == "  " and chess_board[a][b-6] == "  ":
                if chess_board[a][b-7] == "  " or chess_board[a][b-7] in black:
                    possible_moves.append(chess_board1[a][b-7])
    if x in black_rook:
        index_finder(x)
        if index_controller(a - 1, b):
            if chess_board[a - 1][b] == "  " or chess_board[a - 1][b] in white:
                possible_moves.append(chess_board1[a - 1][b])
        if index_controller(a - 2, b):
            if chess_board[a - 1][b] == "  ":
                if chess_board[a - 2][b] == "  " or chess_board[a - 2][b] in white:
                    possible_moves.append(chess_board1[a - 2][b])
        if index_controller(a - 3, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  ":
                if chess_board[a - 3][b] == "  " or chess_board[a - 3][b] in white:
                    possible_moves.append(chess_board1[a - 3][b])
        if index_controller(a - 4, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  ":
                if chess_board[a - 4][b] == "  " or chess_board[a - 4][b] in white:
                    possible_moves.append(chess_board1[a - 4][b])
        if index_controller(a - 5, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and chess_board[a - 4][b] == "  ":
                if chess_board[a - 5][b] == "  " or chess_board[a - 5][b] in white:
                    possible_moves.append(chess_board1[a - 5][b])
        if index_controller(a - 6, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  ":
                if chess_board[a - 6][b] == "  " or chess_board[a - 6][b] in white:
                    possible_moves.append(chess_board1[a - 6][b])
        if index_controller(a - 7, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  " and chess_board[a - 6][b] == "  ":
                if chess_board[a - 7][b] == "  " or chess_board[a - 7][b] in white:
                    possible_moves.append(chess_board1[a - 7][b])
        if index_controller(a, b + 1):
            if chess_board[a][b + 1] == "  " or chess_board[a][b + 1] in white:
                possible_moves.append(chess_board1[a][b + 1])
        if index_controller(a, b + 2):
            if chess_board[a][b + 1] == "  ":
                if chess_board[a][b + 2] == "  " or chess_board[a][b + 2] in white:
                    possible_moves.append(chess_board1[a][b + 2])
        if index_controller(a, b + 3):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  ":
                if chess_board[a][b + 3] == "  " or chess_board[a][b + 3] in white:
                    possible_moves.append(chess_board1[a][b + 3])
        if index_controller(a, b + 4):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  ":
                if chess_board[a][b + 4] == "  " or chess_board[a][b + 4] in white:
                    possible_moves.append(chess_board1[a][b + 4])
        if index_controller(a, b + 5):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and chess_board[a][b + 4] == "  ":
                if chess_board[a][b + 5] == "  " or chess_board[a][b + 5] in white:
                    possible_moves.append(chess_board1[a][b + 5])
        if index_controller(a, b + 6):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and chess_board[a][b + 4] == "  " and chess_board[a][b + 5] == "  ":
                if chess_board[a][b + 6] == "  " or chess_board[a][b + 6] in white:
                    possible_moves.append(chess_board1[a][b + 6])
        if index_controller(a, b + 7):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and chess_board[a][b + 4] == "  " and chess_board[a][b + 5] == "  " and chess_board[a][b + 6] == "  ":
                if chess_board[a][b + 7] == "  " or chess_board[a][b + 7] in white:
                    possible_moves.append(chess_board1[a][b + 7])
        if index_controller(a + 1, b):
            if chess_board[a + 1][b] == "  " or chess_board[a + 1][b] in white:
                possible_moves.append(chess_board1[a + 1][b])
        if index_controller(a + 2, b):
            if chess_board[a + 1][b] == "  ":
                if chess_board[a + 2][b] == "  " or chess_board[a + 2][b] in white:
                    possible_moves.append(chess_board1[a + 2][b])
        if index_controller(a + 3, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  ":
                if chess_board[a + 3][b] == "  " or chess_board[a + 3][b] in white:
                    possible_moves.append(chess_board1[a + 3][b])
        if index_controller(a + 4, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  ":
                if chess_board[a + 4][b] == "  " or chess_board[a + 4][b] in white:
                    possible_moves.append(chess_board1[a + 4][b])
        if index_controller(a + 5, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and chess_board[a + 4][b] == "  ":
                if chess_board[a + 5][b] == "  " or chess_board[a + 5][b] in white:
                    possible_moves.append(chess_board1[a + 5][b])
        if index_controller(a + 6, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  ":
                if chess_board[a + 6][b] == "  " or chess_board[a + 6][b] in white:
                    possible_moves.append(chess_board1[a + 6][b])
        if index_controller(a + 7, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  " and chess_board[a + 6][b] == "  ":
                if chess_board[a + 7][b] == "  " or chess_board[a + 7][b] in white:
                    possible_moves.append(chess_board1[a + 7][b])
        if index_controller(a, b - 1):
            if chess_board[a][b - 1] == "  " or chess_board[a][b - 1] in white:
                possible_moves.append(chess_board1[a][b - 1])
        if index_controller(a, b - 2):
            if chess_board[a][b - 1] == "  ":
                if chess_board[a][b - 2] == "  " or chess_board[a][b - 2] in white:
                    possible_moves.append(chess_board1[a][b - 2])
        if index_controller(a, b - 3):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  ":
                if chess_board[a][b - 3] == "  " or chess_board[a][b - 3] in white:
                    possible_moves.append(chess_board1[a][b - 3])
        if index_controller(a, b - 4):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  ":
                if chess_board[a][b - 4] == "  " or chess_board[a][b - 4] in white:
                    possible_moves.append(chess_board1[a][b - 4])
        if index_controller(a, b - 5):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and chess_board[a][b - 4] == "  ":
                if chess_board[a][b - 5] == "  " or chess_board[a][b - 5] in white:
                    possible_moves.append(chess_board1[a][b - 5])
        if index_controller(a, b - 6):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and chess_board[a][b - 4] == "  " and chess_board[a][b - 5] == "  ":
                if chess_board[a][b - 6] == "  " or chess_board[a][b - 6] in white:
                    possible_moves.append(chess_board1[a][b - 6])
        if index_controller(a, b - 7):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and chess_board[a][b - 4] == "  " and chess_board[a][b - 5] == "  " and chess_board[a][b - 6] == "  ":
                if chess_board[a][b - 7] == "  " or chess_board[a][b - 7] in white:
                    possible_moves.append(chess_board1[a][b - 7])
    if x in white_bishop:
        index_finder(x)
        if index_controller(a - 1, b-1):
            if chess_board[a - 1][b-1] == "  " or chess_board[a - 1][b-1] in black:
                possible_moves.append(chess_board1[a - 1][b-1])
        if index_controller(a - 2, b-2):
            if chess_board[a - 1][b-1] == "  ":
                if chess_board[a - 2][b-2] == "  " or chess_board[a - 2][b-2] in black:
                    possible_moves.append(chess_board1[a - 2][b-2])
        if index_controller(a - 3, b-3):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  ":
                if chess_board[a - 3][b-3] == "  " or chess_board[a - 3][b-3] in black:
                    possible_moves.append(chess_board1[a - 3][b-3])
        if index_controller(a - 4, b-4):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  ":
                if chess_board[a - 4][b-4] == "  " or chess_board[a - 4][b-4] in black:
                    possible_moves.append(chess_board1[a - 4][b-4])
        if index_controller(a - 5, b-5):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  ":
                if chess_board[a - 5][b-5] == "  " or chess_board[a - 5][b-5] in black:
                    possible_moves.append(chess_board1[a - 5][b-5])
        if index_controller(a - 6, b-6):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  " and chess_board[a - 5][b-5] == "  ":
                if chess_board[a - 6][b-6] == "  " or chess_board[a - 6][b-6] in black:
                    possible_moves.append(chess_board1[a - 6][b-6])
        if index_controller(a - 1, b+1):
            if chess_board[a - 1][b+1] == "  " or chess_board[a - 1][b+1] in black:
                possible_moves.append(chess_board1[a - 1][b+1])
        if index_controller(a - 2, b+2):
            if chess_board[a - 1][b+1] == "  ":
                if chess_board[a - 2][b+2] == "  " or chess_board[a - 2][b+2] in black:
                    possible_moves.append(chess_board1[a - 2][b+2])
        if index_controller(a - 3, b+3):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  ":
                if chess_board[a - 3][b+3] == "  " or chess_board[a - 3][b+3] in black:
                    possible_moves.append(chess_board1[a - 3][b+3])
        if index_controller(a - 4, b+4):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  ":
                if chess_board[a - 4][b+4] == "  " or chess_board[a - 4][b+4] in black:
                    possible_moves.append(chess_board1[a - 4][b+4])
        if index_controller(a - 5, b+5):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  ":
                if chess_board[a - 5][b+5] == "  " or chess_board[a - 5][b+5] in black:
                    possible_moves.append(chess_board1[a - 5][b+5])
        if index_controller(a - 6, b+6):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  " and chess_board[a - 5][b+5] == "  ":
                if chess_board[a - 6][b+6] == "  " or chess_board[a - 6][b+6] in black:
                    possible_moves.append(chess_board1[a - 6][b+6])
    if x in black_bishop:
        index_finder(x)
        if index_controller(a + 1, b - 1):
            if chess_board[a + 1][b - 1] == "  " or chess_board[a + 1][b - 1] in white:
                possible_moves.append(chess_board1[a + 1][b - 1])
        if index_controller(a + 2, b - 2):
            if chess_board[a + 1][b - 1] == "  ":
                if chess_board[a + 2][b - 2] == "  " or chess_board[a + 2][b - 2] in white:
                    possible_moves.append(chess_board1[a + 2][b - 2])
        if index_controller(a + 3, b - 3):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  ":
                if chess_board[a + 3][b - 3] == "  " or chess_board[a + 3][b - 3] in white:
                    possible_moves.append(chess_board1[a + 3][b - 3])
        if index_controller(a + 4, b - 4):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  ":
                if chess_board[a + 4][b - 4] == "  " or chess_board[a + 4][b - 4] in white:
                    possible_moves.append(chess_board1[a + 4][b - 4])
        if index_controller(a + 5, b - 5):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  ":
                if chess_board[a + 5][b - 5] == "  " or chess_board[a + 5][b - 5] in white:
                    possible_moves.append(chess_board1[a + 5][b - 5])
        if index_controller(a + 6, b - 6):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  " and chess_board[a + 5][b - 5] == "  ":
                if chess_board[a + 6][b - 6] == "  " or chess_board[a + 6][b - 6] in white:
                    possible_moves.append(chess_board1[a + 6][b - 6])
        if index_controller(a + 1, b + 1):
            if chess_board[a + 1][b + 1] == "  " or chess_board[a + 1][b + 1] in white:
                possible_moves.append(chess_board1[a + 1][b + 1])
        if index_controller(a + 2, b + 2):
            if chess_board[a + 1][b + 1] == "  ":
                if chess_board[a + 2][b + 2] == "  " or chess_board[a + 2][b + 2] in white:
                    possible_moves.append(chess_board1[a + 2][b + 2])
        if index_controller(a + 3, b + 3):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  ":
                if chess_board[a + 3][b + 3] == "  " or chess_board[a + 3][b + 3] in white:
                    possible_moves.append(chess_board1[a + 3][b + 3])
        if index_controller(a + 4, b + 4):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  ":
                if chess_board[a + 4][b + 4] == "  " or chess_board[a + 4][b + 4] in white:
                    possible_moves.append(chess_board1[a + 4][b + 4])
        if index_controller(a + 5, b + 5):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  ":
                if chess_board[a + 5][b + 5] == "  " or chess_board[a + 5][b + 5] in white:
                    possible_moves.append(chess_board1[a + 5][b + 5])
        if index_controller(a + 6, b + 6):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  " and chess_board[a + 5][b + 5] == "  ":
                if chess_board[a + 6][b + 6] == "  " or chess_board[a + 6][b + 6] in white:
                    possible_moves.append(chess_board1[a + 6][b + 6])
    if x == "ki":
        index_finder(x)
        if index_controller(a - 1, b):
            if chess_board[a - 1][b] == "  " or chess_board[a - 1][b] in black:
                possible_moves.append(chess_board1[a - 1][b])
        if index_controller(a + 1, b):
            if chess_board[a + 1][b] == "  " or chess_board[a + 1][b] in black:
                possible_moves.append(chess_board1[a + 1][b])
        if index_controller(a, b-1):
            if chess_board[a][b-1] == "  " or chess_board[a][b-1] in black:
                possible_moves.append(chess_board1[a][b-1])
        if index_controller(a, b+1):
            if chess_board[a][b+1] == "  " or chess_board[a][b+1] in black:
                possible_moves.append(chess_board1[a][b+1])
        if index_controller(a - 1, b-1):
            if chess_board[a - 1][b-1] == "  " or chess_board[a - 1][b-1] in black:
                possible_moves.append(chess_board1[a - 1][b-1])
        if index_controller(a - 1, b+1):
            if chess_board[a - 1][b+1] == "  " or chess_board[a - 1][b+1] in black:
                possible_moves.append(chess_board1[a - 1][b+1])
        if index_controller(a + 1, b-1):
            if chess_board[a + 1][b-1] == "  " or chess_board[a + 1][b-1] in black:
                possible_moves.append(chess_board1[a + 1][b-1])
        if index_controller(a + 1, b+1):
            if chess_board[a + 1][b+1] == "  " or chess_board[a + 1][b+1] in black:
                possible_moves.append(chess_board1[a + 1][b+1])
    if x == "KI":
        index_finder(x)
        if index_controller(a - 1, b):
            if chess_board[a - 1][b] == "  " or chess_board[a - 1][b] in white:
                possible_moves.append(chess_board1[a - 1][b])
        if index_controller(a + 1, b):
            if chess_board[a + 1][b] == "  " or chess_board[a + 1][b] in white:
                possible_moves.append(chess_board1[a + 1][b])
        if index_controller(a, b-1):
            if chess_board[a][b-1] == "  " or chess_board[a][b-1] in white:
                possible_moves.append(chess_board1[a][b-1])
        if index_controller(a, b+1):
            if chess_board[a][b+1] == "  " or chess_board[a][b+1] in white:
                possible_moves.append(chess_board1[a][b+1])
        if index_controller(a - 1, b-1):
            if chess_board[a - 1][b-1] == "  " or chess_board[a - 1][b-1] in white:
                possible_moves.append(chess_board1[a - 1][b-1])
        if index_controller(a - 1, b+1):
            if chess_board[a - 1][b+1] == "  " or chess_board[a - 1][b+1] in white:
                possible_moves.append(chess_board1[a - 1][b+1])
        if index_controller(a + 1, b-1):
            if chess_board[a + 1][b-1] == "  " or chess_board[a + 1][b-1] in white:
                possible_moves.append(chess_board1[a + 1][b-1])
        if index_controller(a + 1, b+1):
            if chess_board[a + 1][b+1] == "  " or chess_board[a + 1][b+1] in white:
                possible_moves.append(chess_board1[a + 1][b+1])
    if x == "qu":
        index_finder(x)
        if index_controller(a - 1, b):
            if chess_board[a - 1][b] == "  " or chess_board[a - 1][b] in black:
                possible_moves.append(chess_board1[a - 1][b])
        if index_controller(a - 2, b):
            if chess_board[a - 1][b] == "  ":
                if chess_board[a - 2][b] == "  " or chess_board[a - 2][b] in black:
                    possible_moves.append(chess_board1[a - 2][b])
        if index_controller(a - 3, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  ":
                if chess_board[a - 3][b] == "  " or chess_board[a - 3][b] in black:
                    possible_moves.append(chess_board1[a - 3][b])
        if index_controller(a - 4, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  ":
                if chess_board[a - 4][b] == "  " or chess_board[a - 4][b] in black:
                    possible_moves.append(chess_board1[a - 4][b])
        if index_controller(a - 5, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and \
                    chess_board[a - 4][b] == "  ":
                if chess_board[a - 5][b] == "  " or chess_board[a - 5][b] in black:
                    possible_moves.append(chess_board1[a - 5][b])
        if index_controller(a - 6, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and \
                    chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  ":
                if chess_board[a - 6][b] == "  " or chess_board[a - 6][b] in black:
                    possible_moves.append(chess_board1[a - 6][b])
        if index_controller(a - 7, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and \
                    chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  " and chess_board[a - 6][b] == "  ":
                if chess_board[a - 7][b] == "  " or chess_board[a - 7][b] in black:
                    possible_moves.append(chess_board1[a - 7][b])
        if index_controller(a, b + 1):
            if chess_board[a][b + 1] == "  " or chess_board[a][b + 1] in black:
                possible_moves.append(chess_board1[a][b + 1])
        if index_controller(a, b + 2):
            if chess_board[a][b + 1] == "  ":
                if chess_board[a][b + 2] == "  " or chess_board[a][b + 2] in black:
                    possible_moves.append(chess_board1[a][b + 2])
        if index_controller(a, b + 3):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  ":
                if chess_board[a][b + 3] == "  " or chess_board[a][b + 3] in black:
                    possible_moves.append(chess_board1[a][b + 3])
        if index_controller(a, b + 4):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  ":
                if chess_board[a][b + 4] == "  " or chess_board[a][b + 4] in black:
                    possible_moves.append(chess_board1[a][b + 4])
        if index_controller(a, b + 5):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and \
                    chess_board[a][b + 4] == "  ":
                if chess_board[a][b + 5] == "  " or chess_board[a][b + 5] in black:
                    possible_moves.append(chess_board1[a][b + 5])
        if index_controller(a, b + 6):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and \
                    chess_board[a][b + 4] == "  " and chess_board[a][b + 5] == "  ":
                if chess_board[a][b + 6] == "  " or chess_board[a][b + 6] in black:
                    possible_moves.append(chess_board1[a][b + 6])
        if index_controller(a, b + 7):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and \
                    chess_board[a][b + 4] == "  " and chess_board[a][b + 5] == "  " and chess_board[a][b + 6] == "  ":
                if chess_board[a][b + 7] == "  " or chess_board[a][b + 7] in black:
                    possible_moves.append(chess_board1[a][b + 7])
        if index_controller(a + 1, b):
            if chess_board[a + 1][b] == "  " or chess_board[a + 1][b] in black:
                possible_moves.append(chess_board1[a + 1][b])
        if index_controller(a + 2, b):
            if chess_board[a + 1][b] == "  ":
                if chess_board[a + 2][b] == "  " or chess_board[a + 2][b] in black:
                    possible_moves.append(chess_board1[a + 2][b])
        if index_controller(a + 3, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  ":
                if chess_board[a + 3][b] == "  " or chess_board[a + 3][b] in black:
                    possible_moves.append(chess_board1[a + 3][b])
        if index_controller(a + 4, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  ":
                if chess_board[a + 4][b] == "  " or chess_board[a + 4][b] in black:
                    possible_moves.append(chess_board1[a + 4][b])
        if index_controller(a + 5, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and \
                    chess_board[a + 4][b] == "  ":
                if chess_board[a + 5][b] == "  " or chess_board[a + 5][b] in black:
                    possible_moves.append(chess_board1[a + 5][b])
        if index_controller(a + 6, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and \
                    chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  ":
                if chess_board[a + 6][b] == "  " or chess_board[a + 6][b] in black:
                    possible_moves.append(chess_board1[a + 6][b])
        if index_controller(a + 7, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and \
                    chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  " and chess_board[a + 6][b] == "  ":
                if chess_board[a + 7][b] == "  " or chess_board[a + 7][b] in black:
                    possible_moves.append(chess_board1[a + 7][b])
        if index_controller(a, b - 1):
            if chess_board[a][b - 1] == "  " or chess_board[a][b - 1] in black:
                possible_moves.append(chess_board1[a][b - 1])
        if index_controller(a, b - 2):
            if chess_board[a][b - 1] == "  ":
                if chess_board[a][b - 2] == "  " or chess_board[a][b - 2] in black:
                    possible_moves.append(chess_board1[a][b - 2])
        if index_controller(a, b - 3):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  ":
                if chess_board[a][b - 3] == "  " or chess_board[a][b - 3] in black:
                    possible_moves.append(chess_board1[a][b - 3])
        if index_controller(a, b - 4):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  ":
                if chess_board[a][b - 4] == "  " or chess_board[a][b - 4] in black:
                    possible_moves.append(chess_board1[a][b - 4])
        if index_controller(a, b - 5):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and \
                    chess_board[a][b - 4] == "  ":
                if chess_board[a][b - 5] == "  " or chess_board[a][b - 5] in black:
                    possible_moves.append(chess_board1[a][b - 5])
        if index_controller(a, b - 6):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and \
                    chess_board[a][b - 4] == "  " and chess_board[a][b - 5] == "  ":
                if chess_board[a][b - 6] == "  " or chess_board[a][b - 6] in black:
                    possible_moves.append(chess_board1[a][b - 6])
        if index_controller(a, b - 7):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and \
                    chess_board[a][b - 4] == "  " and chess_board[a][b - 5] == "  " and chess_board[a][b - 6] == "  ":
                if chess_board[a][b - 7] == "  " or chess_board[a][b - 7] in black:
                    possible_moves.append(chess_board1[a][b - 7])
        if index_controller(a - 1, b-1):
            if chess_board[a - 1][b-1] == "  " or chess_board[a - 1][b-1] in black:
                possible_moves.append(chess_board1[a - 1][b-1])
        if index_controller(a - 2, b-2):
            if chess_board[a - 1][b-1] == "  ":
                if chess_board[a - 2][b-2] == "  " or chess_board[a - 2][b-2] in black:
                    possible_moves.append(chess_board1[a - 2][b-2])
        if index_controller(a - 3, b-3):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  ":
                if chess_board[a - 3][b-3] == "  " or chess_board[a - 3][b-3] in black:
                    possible_moves.append(chess_board1[a - 3][b-3])
        if index_controller(a - 4, b-4):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  ":
                if chess_board[a - 4][b-4] == "  " or chess_board[a - 4][b-4] in black:
                    possible_moves.append(chess_board1[a - 4][b-4])
        if index_controller(a - 5, b-5):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  ":
                if chess_board[a - 5][b-5] == "  " or chess_board[a - 5][b-5] in black:
                    possible_moves.append(chess_board1[a - 5][b-5])
        if index_controller(a - 6, b-6):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  " and chess_board[a - 5][b-5] == "  ":
                if chess_board[a - 6][b-6] == "  " or chess_board[a - 6][b-6] in black:
                    possible_moves.append(chess_board1[a - 6][b-6])
        if index_controller(a - 7, b-7):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  " and chess_board[a - 5][b-5] == "  " and chess_board[a - 6][b-6] == "  ":
                if chess_board[a - 7][b-7] == "  " or chess_board[a - 7][b-7] in black:
                    possible_moves.append(chess_board1[a - 7][b-7])
        if index_controller(a - 1, b+1):
            if chess_board[a - 1][b+1] == "  " or chess_board[a - 1][b+1] in black:
                possible_moves.append(chess_board1[a - 1][b+1])
        if index_controller(a - 2, b+2):
            if chess_board[a - 1][b+1] == "  ":
                if chess_board[a - 2][b+2] == "  " or chess_board[a - 2][b+2] in black:
                    possible_moves.append(chess_board1[a - 2][b+2])
        if index_controller(a - 3, b+3):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  ":
                if chess_board[a - 3][b+3] == "  " or chess_board[a - 3][b+3] in black:
                    possible_moves.append(chess_board1[a - 3][b+3])
        if index_controller(a - 4, b+4):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  ":
                if chess_board[a - 4][b+4] == "  " or chess_board[a - 4][b+4] in black:
                    possible_moves.append(chess_board1[a - 4][b+4])
        if index_controller(a - 5, b+5):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  ":
                if chess_board[a - 5][b+5] == "  " or chess_board[a - 5][b+5] in black:
                    possible_moves.append(chess_board1[a - 5][b+5])
        if index_controller(a - 6, b+6):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  " and chess_board[a - 5][b+5] == "  ":
                if chess_board[a - 6][b+6] == "  " or chess_board[a - 6][b+6] in black:
                    possible_moves.append(chess_board1[a - 6][b+6])
        if index_controller(a - 7, b+7):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  " and chess_board[a - 5][b+5] == "  " and chess_board[a - 6][b+6] == "  ":
                if chess_board[a - 7][b+7] == "  " or chess_board[a - 7][b+7] in black:
                    possible_moves.append(chess_board1[a - 7][b+7])
        if index_controller(a + 1, b - 1):
            if chess_board[a + 1][b - 1] == "  " or chess_board[a + 1][b - 1] in black:
                possible_moves.append(chess_board1[a + 1][b - 1])
        if index_controller(a + 2, b - 2):
            if chess_board[a + 1][b - 1] == "  ":
                if chess_board[a + 2][b - 2] == "  " or chess_board[a + 2][b - 2] in black:
                    possible_moves.append(chess_board1[a + 2][b - 2])
        if index_controller(a + 3, b - 3):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  ":
                if chess_board[a + 3][b - 3] == "  " or chess_board[a + 3][b - 3] in black:
                    possible_moves.append(chess_board1[a + 3][b - 3])
        if index_controller(a + 4, b - 4):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  ":
                if chess_board[a + 4][b - 4] == "  " or chess_board[a + 4][b - 4] in black:
                    possible_moves.append(chess_board1[a + 4][b - 4])
        if index_controller(a + 5, b - 5):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  ":
                if chess_board[a + 5][b - 5] == "  " or chess_board[a + 5][b - 5] in black:
                    possible_moves.append(chess_board1[a + 5][b - 5])
        if index_controller(a + 6, b - 6):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  " and chess_board[a + 5][b - 5] == "  ":
                if chess_board[a + 6][b - 6] == "  " or chess_board[a + 6][b - 6] in black:
                    possible_moves.append(chess_board1[a + 6][b - 6])
        if index_controller(a + 7, b - 7):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  " and chess_board[a + 5][b - 5] == "  " and chess_board[a + 6][b - 6] == "  ":
                if chess_board[a + 7][b - 7] == "  " or chess_board[a + 7][b - 7] in black:
                    possible_moves.append(chess_board1[a + 7][b - 7])
        if index_controller(a + 1, b + 1):
            if chess_board[a + 1][b + 1] == "  " or chess_board[a + 1][b + 1] in black:
                possible_moves.append(chess_board1[a + 1][b + 1])
        if index_controller(a + 2, b + 2):
            if chess_board[a + 1][b + 1] == "  ":
                if chess_board[a + 2][b + 2] == "  " or chess_board[a + 2][b + 2] in black:
                    possible_moves.append(chess_board1[a + 2][b + 2])
        if index_controller(a + 3, b + 3):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  ":
                if chess_board[a + 3][b + 3] == "  " or chess_board[a + 3][b + 3] in black:
                    possible_moves.append(chess_board1[a + 3][b + 3])
        if index_controller(a + 4, b + 4):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  ":
                if chess_board[a + 4][b + 4] == "  " or chess_board[a + 4][b + 4] in black:
                    possible_moves.append(chess_board1[a + 4][b + 4])
        if index_controller(a + 5, b + 5):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  ":
                if chess_board[a + 5][b + 5] == "  " or chess_board[a + 5][b + 5] in black:
                    possible_moves.append(chess_board1[a + 5][b + 5])
        if index_controller(a + 6, b + 6):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  " and chess_board[a + 5][b + 5] == "  ":
                if chess_board[a + 6][b + 6] == "  " or chess_board[a + 6][b + 6] in black:
                    possible_moves.append(chess_board1[a + 6][b + 6])
        if index_controller(a + 7, b + 7):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  " and chess_board[a + 5][b + 5] == "  " and chess_board[a + 6][b + 6] == "  ":
                if chess_board[a + 7][b + 7] == "  " or chess_board[a + 7][b + 7] in black:
                    possible_moves.append(chess_board1[a + 7][b + 7])
    if x == "QU":
        index_finder(x)
        if index_controller(a - 1, b):
            if chess_board[a - 1][b] == "  " or chess_board[a - 1][b] in white:
                possible_moves.append(chess_board1[a - 1][b])
        if index_controller(a - 2, b):
            if chess_board[a - 1][b] == "  ":
                if chess_board[a - 2][b] == "  " or chess_board[a - 2][b] in white:
                    possible_moves.append(chess_board1[a - 2][b])
        if index_controller(a - 3, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  ":
                if chess_board[a - 3][b] == "  " or chess_board[a - 3][b] in white:
                    possible_moves.append(chess_board1[a - 3][b])
        if index_controller(a - 4, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  ":
                if chess_board[a - 4][b] == "  " or chess_board[a - 4][b] in white:
                    possible_moves.append(chess_board1[a - 4][b])
        if index_controller(a - 5, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and \
                    chess_board[a - 4][b] == "  ":
                if chess_board[a - 5][b] == "  " or chess_board[a - 5][b] in white:
                    possible_moves.append(chess_board1[a - 5][b])
        if index_controller(a - 6, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and \
                    chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  ":
                if chess_board[a - 6][b] == "  " or chess_board[a - 6][b] in white:
                    possible_moves.append(chess_board1[a - 6][b])
        if index_controller(a - 7, b):
            if chess_board[a - 1][b] == "  " and chess_board[a - 2][b] == "  " and chess_board[a - 3][b] == "  " and \
                    chess_board[a - 4][b] == "  " and chess_board[a - 5][b] == "  " and chess_board[a - 6][b] == "  ":
                if chess_board[a - 7][b] == "  " or chess_board[a - 7][b] in white:
                    possible_moves.append(chess_board1[a - 7][b])
        if index_controller(a, b + 1):
            if chess_board[a][b + 1] == "  " or chess_board[a][b + 1] in white:
                possible_moves.append(chess_board1[a][b + 1])
        if index_controller(a, b + 2):
            if chess_board[a][b + 1] == "  ":
                if chess_board[a][b + 2] == "  " or chess_board[a][b + 2] in white:
                    possible_moves.append(chess_board1[a][b + 2])
        if index_controller(a, b + 3):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  ":
                if chess_board[a][b + 3] == "  " or chess_board[a][b + 3] in white:
                    possible_moves.append(chess_board1[a][b + 3])
        if index_controller(a, b + 4):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  ":
                if chess_board[a][b + 4] == "  " or chess_board[a][b + 4] in white:
                    possible_moves.append(chess_board1[a][b + 4])
        if index_controller(a, b + 5):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and \
                    chess_board[a][b + 4] == "  ":
                if chess_board[a][b + 5] == "  " or chess_board[a][b + 5] in white:
                    possible_moves.append(chess_board1[a][b + 5])
        if index_controller(a, b + 6):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and \
                    chess_board[a][b + 4] == "  " and chess_board[a][b + 5] == "  ":
                if chess_board[a][b + 6] == "  " or chess_board[a][b + 6] in white:
                    possible_moves.append(chess_board1[a][b + 6])
        if index_controller(a, b + 7):
            if chess_board[a][b + 1] == "  " and chess_board[a][b + 2] == "  " and chess_board[a][b + 3] == "  " and \
                    chess_board[a][b + 4] == "  " and chess_board[a][b + 5] == "  " and chess_board[a][b + 6] == "  ":
                if chess_board[a][b + 7] == "  " or chess_board[a][b + 7] in white:
                    possible_moves.append(chess_board1[a][b + 7])
        if index_controller(a + 1, b):
            if chess_board[a + 1][b] == "  " or chess_board[a + 1][b] in white:
                possible_moves.append(chess_board1[a + 1][b])
        if index_controller(a + 2, b):
            if chess_board[a + 1][b] == "  ":
                if chess_board[a + 2][b] == "  " or chess_board[a + 2][b] in white:
                    possible_moves.append(chess_board1[a + 2][b])
        if index_controller(a + 3, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  ":
                if chess_board[a + 3][b] == "  " or chess_board[a + 3][b] in white:
                    possible_moves.append(chess_board1[a + 3][b])
        if index_controller(a + 4, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  ":
                if chess_board[a + 4][b] == "  " or chess_board[a + 4][b] in white:
                    possible_moves.append(chess_board1[a + 4][b])
        if index_controller(a + 5, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and \
                    chess_board[a + 4][b] == "  ":
                if chess_board[a + 5][b] == "  " or chess_board[a + 5][b] in white:
                    possible_moves.append(chess_board1[a + 5][b])
        if index_controller(a + 6, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and \
                    chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  ":
                if chess_board[a + 6][b] == "  " or chess_board[a + 6][b] in white:
                    possible_moves.append(chess_board1[a + 6][b])
        if index_controller(a + 7, b):
            if chess_board[a + 1][b] == "  " and chess_board[a + 2][b] == "  " and chess_board[a + 3][b] == "  " and \
                    chess_board[a + 4][b] == "  " and chess_board[a + 5][b] == "  " and chess_board[a + 6][b] == "  ":
                if chess_board[a + 7][b] == "  " or chess_board[a + 7][b] in white:
                    possible_moves.append(chess_board1[a + 7][b])
        if index_controller(a, b - 1):
            if chess_board[a][b - 1] == "  " or chess_board[a][b - 1] in white:
                possible_moves.append(chess_board1[a][b - 1])
        if index_controller(a, b - 2):
            if chess_board[a][b - 1] == "  ":
                if chess_board[a][b - 2] == "  " or chess_board[a][b - 2] in white:
                    possible_moves.append(chess_board1[a][b - 2])
        if index_controller(a, b - 3):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  ":
                if chess_board[a][b - 3] == "  " or chess_board[a][b - 3] in white:
                    possible_moves.append(chess_board1[a][b - 3])
        if index_controller(a, b - 4):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  ":
                if chess_board[a][b - 4] == "  " or chess_board[a][b - 4] in white:
                    possible_moves.append(chess_board1[a][b - 4])
        if index_controller(a, b - 5):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and \
                    chess_board[a][b - 4] == "  ":
                if chess_board[a][b - 5] == "  " or chess_board[a][b - 5] in white:
                    possible_moves.append(chess_board1[a][b - 5])
        if index_controller(a, b - 6):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and \
                    chess_board[a][b - 4] == "  " and chess_board[a][b - 5] == "  ":
                if chess_board[a][b - 6] == "  " or chess_board[a][b - 6] in white:
                    possible_moves.append(chess_board1[a][b - 6])
        if index_controller(a, b - 7):
            if chess_board[a][b - 1] == "  " and chess_board[a][b - 2] == "  " and chess_board[a][b - 3] == "  " and \
                    chess_board[a][b - 4] == "  " and chess_board[a][b - 5] == "  " and chess_board[a][b - 6] == "  ":
                if chess_board[a][b - 7] == "  " or chess_board[a][b - 7] in white:
                    possible_moves.append(chess_board1[a][b - 7])
        if index_controller(a - 1, b-1):
            if chess_board[a - 1][b-1] == "  " or chess_board[a - 1][b-1] in white:
                possible_moves.append(chess_board1[a - 1][b-1])
        if index_controller(a - 2, b-2):
            if chess_board[a - 1][b-1] == "  ":
                if chess_board[a - 2][b-2] == "  " or chess_board[a - 2][b-2] in white:
                    possible_moves.append(chess_board1[a - 2][b-2])
        if index_controller(a - 3, b-3):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  ":
                if chess_board[a - 3][b-3] == "  " or chess_board[a - 3][b-3] in white:
                    possible_moves.append(chess_board1[a - 3][b-3])
        if index_controller(a - 4, b-4):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  ":
                if chess_board[a - 4][b-4] == "  " or chess_board[a - 4][b-4] in white:
                    possible_moves.append(chess_board1[a - 4][b-4])
        if index_controller(a - 5, b-5):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  ":
                if chess_board[a - 5][b-5] == "  " or chess_board[a - 5][b-5] in white:
                    possible_moves.append(chess_board1[a - 5][b-5])
        if index_controller(a - 6, b-6):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  " and chess_board[a - 5][b-5] == "  ":
                if chess_board[a - 6][b-6] == "  " or chess_board[a - 6][b-6] in white:
                    possible_moves.append(chess_board1[a - 6][b-6])
        if index_controller(a - 7, b-7):
            if chess_board[a - 1][b-1] == "  " and chess_board[a - 2][b-2] == "  " and chess_board[a - 3][b-3] == "  " and chess_board[a - 4][b-4] == "  " and chess_board[a - 5][b-5] == "  " and chess_board[a - 6][b-6] == "  ":
                if chess_board[a - 7][b-7] == "  " or chess_board[a - 7][b-7] in white:
                    possible_moves.append(chess_board1[a - 7][b-7])
        if index_controller(a - 1, b+1):
            if chess_board[a - 1][b+1] == "  " or chess_board[a - 1][b+1] in white:
                possible_moves.append(chess_board1[a - 1][b+1])
        if index_controller(a - 2, b+2):
            if chess_board[a - 1][b+1] == "  ":
                if chess_board[a - 2][b+2] == "  " or chess_board[a - 2][b+2] in white:
                    possible_moves.append(chess_board1[a - 2][b+2])
        if index_controller(a - 3, b+3):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  ":
                if chess_board[a - 3][b+3] == "  " or chess_board[a - 3][b+3] in white:
                    possible_moves.append(chess_board1[a - 3][b+3])
        if index_controller(a - 4, b+4):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  ":
                if chess_board[a - 4][b+4] == "  " or chess_board[a - 4][b+4] in white:
                    possible_moves.append(chess_board1[a - 4][b+4])
        if index_controller(a - 5, b+5):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  ":
                if chess_board[a - 5][b+5] == "  " or chess_board[a - 5][b+5] in white:
                    possible_moves.append(chess_board1[a - 5][b+5])
        if index_controller(a - 6, b+6):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  " and chess_board[a - 5][b+5] == "  ":
                if chess_board[a - 6][b+6] == "  " or chess_board[a - 6][b+6] in white:
                    possible_moves.append(chess_board1[a - 6][b+6])
        if index_controller(a - 7, b+7):
            if chess_board[a - 1][b+1] == "  " and chess_board[a - 2][b+2] == "  " and chess_board[a - 3][b+3] == "  " and chess_board[a - 4][b+4] == "  " and chess_board[a - 5][b+5] == "  " and chess_board[a - 6][b+6] == "  ":
                if chess_board[a - 7][b+7] == "  " or chess_board[a - 7][b+7] in white:
                    possible_moves.append(chess_board1[a - 7][b+7])
        if index_controller(a + 1, b - 1):
            if chess_board[a + 1][b - 1] == "  " or chess_board[a + 1][b - 1] in white:
                possible_moves.append(chess_board1[a + 1][b - 1])
        if index_controller(a + 2, b - 2):
            if chess_board[a + 1][b - 1] == "  ":
                if chess_board[a + 2][b - 2] == "  " or chess_board[a + 2][b - 2] in white:
                    possible_moves.append(chess_board1[a + 2][b - 2])
        if index_controller(a + 3, b - 3):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  ":
                if chess_board[a + 3][b - 3] == "  " or chess_board[a + 3][b - 3] in white:
                    possible_moves.append(chess_board1[a + 3][b - 3])
        if index_controller(a + 4, b - 4):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  ":
                if chess_board[a + 4][b - 4] == "  " or chess_board[a + 4][b - 4] in white:
                    possible_moves.append(chess_board1[a + 4][b - 4])
        if index_controller(a + 5, b - 5):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  ":
                if chess_board[a + 5][b - 5] == "  " or chess_board[a + 5][b - 5] in white:
                    possible_moves.append(chess_board1[a + 5][b - 5])
        if index_controller(a + 6, b - 6):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  " and chess_board[a + 5][b - 5] == "  ":
                if chess_board[a + 6][b - 6] == "  " or chess_board[a + 6][b - 6] in white:
                    possible_moves.append(chess_board1[a + 6][b - 6])
        if index_controller(a + 7, b - 7):
            if chess_board[a + 1][b - 1] == "  " and chess_board[a + 2][b - 2] == "  " and chess_board[a + 3][b - 3] == "  " and chess_board[a + 4][b - 4] == "  " and chess_board[a + 5][b - 5] == "  " and chess_board[a + 6][b - 6] == "  ":
                if chess_board[a + 7][b - 7] == "  " or chess_board[a + 7][b - 7] in white:
                    possible_moves.append(chess_board1[a + 7][b - 7])
        if index_controller(a + 1, b + 1):
            if chess_board[a + 1][b + 1] == "  " or chess_board[a + 1][b + 1] in white:
                possible_moves.append(chess_board1[a + 1][b + 1])
        if index_controller(a + 2, b + 2):
            if chess_board[a + 1][b + 1] == "  ":
                if chess_board[a + 2][b + 2] == "  " or chess_board[a + 2][b + 2] in white:
                    possible_moves.append(chess_board1[a + 2][b + 2])
        if index_controller(a + 3, b + 3):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  ":
                if chess_board[a + 3][b + 3] == "  " or chess_board[a + 3][b + 3] in white:
                    possible_moves.append(chess_board1[a + 3][b + 3])
        if index_controller(a + 4, b + 4):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  ":
                if chess_board[a + 4][b + 4] == "  " or chess_board[a + 4][b + 4] in white:
                    possible_moves.append(chess_board1[a + 4][b + 4])
        if index_controller(a + 5, b + 5):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  ":
                if chess_board[a + 5][b + 5] == "  " or chess_board[a + 5][b + 5] in white:
                    possible_moves.append(chess_board1[a + 5][b + 5])
        if index_controller(a + 6, b + 6):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  " and chess_board[a + 5][b + 5] == "  ":
                if chess_board[a + 6][b + 6] == "  " or chess_board[a + 6][b + 6] in white:
                    possible_moves.append(chess_board1[a + 6][b + 6])
        if index_controller(a + 7, b + 7):
            if chess_board[a + 1][b + 1] == "  " and chess_board[a + 2][b + 2] == "  " and chess_board[a + 3][b + 3] == "  " and chess_board[a + 4][b + 4] == "  " and chess_board[a + 5][b + 5] == "  " and chess_board[a + 6][b + 6] == "  ":
                if chess_board[a + 7][b + 7] == "  " or chess_board[a + 7][b + 7] in white:
                    possible_moves.append(chess_board1[a + 7][b + 7])


for i in commands:
    if i[0] == 'move':
        print(">", *i)
        show_moves(i[1])
        if i[2] in possible_moves:
            move(i[1], i[2])
            print("OK")
        else:
            print("FAILED")
    elif i[0] == 'showmoves':
        print(">", *i)
        show_moves(i[1])
        possible_moves.sort()
        if possible_moves == []:
            print("FAILED")
        else:
            print(*possible_moves)
    elif i[0] == 'exit':
        print(">", *i)
        exit()
    elif i[0] == 'print':
        print(">", *i)
        for j in range(0, (len(chess_board))):
            print(*chess_board[j])
    elif i[0] == 'initialize':
        print(">", *i)
        chess_board = [["R1", "N1", "B1", "QU", "KI", "B2", "N2", "R2"],
                       ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8"],
                       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                       ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
                       ["r1", "n1", "b1", "qu", "ki", "b2", "n2", "r2"]]
        for j in range(0, (len(chess_board))):
            print(*chess_board[j])
