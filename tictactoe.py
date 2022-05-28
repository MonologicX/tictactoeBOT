import pygame
import sys
import time
import random
from constants import *
global turn, gameOver, winner
pygame.init()

WIN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption("TicTacToe")
font = pygame.font.SysFont('Sans', 25)
pygame.font.init()

turn = 1
gameOver = False
winner = 0

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

boardRects = [
    [TOPLEFT, TOPMID, TOPRIGHT],
    [MIDLEFT, MIDMID, MIDRIGHT],
    [BOTLEFT, BOTMID, BOTRIGHT]
]

def drawGrid():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(250, 50, 10, 620))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(460, 50, 10, 620))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(50, 250, 620, 10))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(50, 460, 620, 10))

def drawSquares():

    for row in range(len(board)):
        for square in range(len(board[row])):
            if board[row][square] == 1:
                pygame.draw.rect(WIN, RED, boardRects[row][square])
            elif board[row][square] == -1:
                pygame.draw.rect(WIN, BLUE, boardRects[row][square])

def draw():

    WIN.fill(WHITE)
    drawGrid()
    drawSquares()
    pygame.display.update()

def clickBox(row, column, currentTurn):

    if board[row][column] == 0:

        #Place Square
        board[row][column] = currentTurn

        #Change Turns
        if currentTurn == 1:
            currentTurn = -1
        elif currentTurn == -1:
            currentTurn = 1

    return currentTurn

def main():

    clock = pygame.time.Clock()
    clock.tick(FPS)

    gameOver = False

    turn = 1

    while gameOver == False:

        if turn == -1:
            turn = botTurn(turn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseCoords = pygame.mouse.get_pos()
                xClick = 0
                yClick = 0
                print("MouseX: {0}, MouseY: {1}".format(mouseCoords[0], mouseCoords[1]))

                if mouseCoords[0] < 250:
                    xClick = 0
                elif mouseCoords[0] > 460:
                    xClick = 2
                elif 250 < mouseCoords[0] < 460:
                    xClick = 1

                if mouseCoords[1] < 250:
                    yClick = 0
                elif mouseCoords[1] > 460:
                    yClick = 2
                elif 250 < mouseCoords[1] < 460:
                    yClick = 1

                turn = clickBox(yClick, xClick, turn)

        draw()
    while gameOver == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
        WIN.fill(WHITE)

        if winner == 1:
            winMessage = font.render("You Won", True, BLACK)
        elif winner == -1:
            winMessage = font.render("The Bot Won", True, BLACK)
        elif winner == 0:
            winMessage = font.render("DRAW", True, BLACK)

        winMessage.center(WINWIDTH / 2, WINHEIGHT / 2)
        WIN.blit(winMessage, winMessage.get_rect())


        pygame.display.update()

def checkForWin(turn):
    for i in range(3):
        rowSum = board[i][0] + board[i][1] + board[i][2]
        if abs(rowSum) == 3:
            winner = turn
            gameOver = True
        columnSum = board[0][i] + board[1][i] + board[2][i]
        if abs(columnSum) == 3:
            winner = turn
            gameOver = True


def botTurn(turn):

    botRow = 0
    botColumn = 0

    for i in range(3):
        rowSum = board[i][0] + board[i][1] + board[i][2]
        if abs(rowSum) == 2:
            for j in range(3):
                if board[i][j] == 0:
                    botRow = i
                    botColumn = j
                    return clickBox(botRow, botColumn, turn)
        else:
            print("Rand R")
            botRow = random.randint(0, 2)
            botColumn = random.randint(0, 2)

    for i in range(3):
        columnSum = board[0][i] + board[1][i] + board[2][i]
        if abs(columnSum) == 3:
            winner = turn
            gameOver = True
        if abs(columnSum) == 2:
            for j in range(3):
                print(j)
                if board[j][i] == 0:
                    botRow = j
                    botColumn = i
                    return clickBox(botRow, botColumn, turn)
        else:
            print("Rand C")
            botRow = random.randint(0, 2)
            botColumn = random.randint(0, 2)

    gameFinished = True
    for row in board:
        for square in row:
            if square == 0:
                gameFinished = False
    gameOver = gameFinished


    print("Row: {0}, Column: {1}".format(botRow, botColumn))
    newTurn = clickBox(botRow, botColumn, turn)
    checkForWin(turn)
    return newTurn

main()
