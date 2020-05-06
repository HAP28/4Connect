import numpy
import pygame as py
import sys
import math

SquareSize = 100
Column = 7
Row = 6
Radius = int (SquareSize / 2.2)
py.init ( )
py.display.set_caption("4Connect")
font = py.font.Font ("freesansbold.ttf", 75)


def create_board():
    board = numpy.zeros ((Row, Column))
    return board


def DropPiece(board, row, col, piece):
    board[row][col] = piece


def isValidLocation(board, col):
    return board[Row - 1][col] == 0


def getNextOpenRow(board, col):
    for r in range (Row):
        if board[r][col] == 0:
            return r


def winning(board, piece):
    # horizontal check
    for c in range (Column - 3):
        for r in range (Row):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Vertical check
    for c in range (Column):
        for r in range (Row - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # cross check
    for c in range (Column - 3):
        for r in range (Row - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    for c in range (Column):
        for r in range (3, Row):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


def drawBoard(board):
    for c in range (Column):
        for r in range (Row):
            py.draw.rect (screen, (0, 0, 255), (c * SquareSize, r * SquareSize + SquareSize, SquareSize, SquareSize))
            py.draw.circle (screen, (0, 0, 0),
                            (int (c * SquareSize + SquareSize / 2), int (r * SquareSize + SquareSize + SquareSize / 2)),
                            Radius)

    for c in range (Column):
        for r in range (Row):
            if board[r][c] == 1:
                py.draw.circle (screen, (255, 0, 0),
                                (int (c * SquareSize + SquareSize / 2),
                                 height - int (r * SquareSize + SquareSize / 2)),
                                Radius)
            elif board[r][c] == 2:
                py.draw.circle (screen, (255, 255, 0),
                                (int (c * SquareSize + SquareSize / 2),
                                 height - int (r * SquareSize + SquareSize / 2)),
                                Radius)


def Won(turn):
    py.draw.rect (screen, (0, 0, 0), (0, 0, width, SquareSize))
    label = font.render ("Player " + str (turn) + " Wins!", 0, (255, 0, 0))
    screen.blit (label, (75, 10))



board = create_board ( )
GameOver = False
turn = 0

width = Column * SquareSize
height = (Row + 1) * SquareSize

screen = py.display.set_mode ((width, height))
drawBoard (board)


while not GameOver:

    for event in py.event.get ( ):
        if event.type == py.QUIT:
            sys.exit ( )

        if event.type == py.MOUSEMOTION:
            py.draw.rect (screen, (0, 0, 0), (0, 0, width, SquareSize))
            positionx = event.pos[0]
            if turn == 0:
                py.draw.circle (screen, (255, 0, 0), (positionx, int (SquareSize / 2)), Radius)
            else:
                py.draw.circle (screen, (255, 255, 0), (positionx, int (SquareSize / 2)), Radius)

        if event.type == py.MOUSEBUTTONDOWN:

            if turn == 0:
                posx = event.pos[0]
                col = int (math.floor (posx / SquareSize))

                if isValidLocation (board, col):
                    row = getNextOpenRow (board, col)
                    DropPiece (board, row, col, 1)

                    if winning (board, 1):
                        Won (1)
                        GameOver = True


            else:
                posx = event.pos[0]
                col = int (math.floor (posx / SquareSize))

                if isValidLocation (board, col):
                    row = getNextOpenRow (board, col)
                    DropPiece (board, row, col, 2)

                    if winning (board, 2):
                        Won (2)
                        GameOver = True

            drawBoard (board)
            turn += 1
            turn %= 2


    py.display.update ( )

    if GameOver:
        py.time.wait(3000)