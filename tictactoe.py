import pygame
import sys
import time
import random
from constants import *

pygame.init()

winWidth, winHeight = 1020, 1020
WIN = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("TicTacToe")

font = pygame.font.SysFont('Sans', 25)

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

TOPLEFT = pygame.Rect(100, 100, 200, 200)
TOPMID = pygame.Rect(310, 100, 300, 200)
TOPRIGHT = pygame.Rect(310, 100, 200, 200)

MIDLEFT = pygame.Rect(310, 310, 200, 200)
MIDMID = pygame.Rect(310, 310, 200, 200)
MIDRIGHT = pygame.Rect(310, 310, 200, 200)

BOTLEFT = pygame.Rect(310, 310, 200, 200)
BOTMID = pygame.Rect(310, 310, 200, 200)
BOTRIGHT = pygame.Rect(310, 310, 200, 200)

boardRects = [
    [TOPLEFT, TOPMID, TOPRIGHT],
    [MIDLEFT, MIDMID, MIDRIGHT],
    [BOTLEFT, BOTMID, BOTRIGHT]
]
def drawGrid():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(300, 100, 10, 900))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(610, 100, 10, 900))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(100, 300, 900, 10))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(100, 610, 900, 10))

def drawColors():

    for row in range(len(board)):
        for square in range(len(board[row])):
            if board[row][square] == 1:
                pygame.draw.rect(WIN, RED, boardRects[row][square])

def draw():

    WIN.fill(WHITE)
    drawGrid()
    drawColors()
    pygame.display.update()

def main():

    clock = pygame.time.Clock()
    clock.tick(FPS)

    gameOver = False

    while gameOver == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseCoords = pygame.mouse.get_pos()
                xClick = 0
                yClick = 0
                print("MouseX: {0}, MouseY: {1}".format(mouseCoords[0], mouseCoords[1]))

                if mouseCoords[0] < 300:
                    xClick = 0
                elif mouseCoords[0] > 600:
                    xClick = 2
                elif 300 < mouseCoords[0] < 600:
                    xClick = 1

                if mouseCoords[1] < 300:
                    yClick = 0
                elif mouseCoords[1] > 600:
                    yClick = 2
                elif 300 < mouseCoords[1] < 600:
                    yClick = 1

                board[yClick][xClick] = 1

                print(board)

        draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

main()
