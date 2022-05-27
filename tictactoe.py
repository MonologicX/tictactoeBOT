import pygame
import sys
import time
import random
from constants import *

pygame.init()

winWidth, winHeight = 720, 720
WIN = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("TicTacToe")

font = pygame.font.SysFont('Sans', 25)

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

def main():

    clock = pygame.time.Clock()
    clock.tick(FPS)

    gameOver = False
    turn = 1

    while gameOver == False:

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

                #Place Square
                board[yClick][xClick] = turn

                #Change Turns
                if turn == 1:
                    turn = -1
                elif turn == -1:
                    turn = 1

                print(board)

        draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

main()
