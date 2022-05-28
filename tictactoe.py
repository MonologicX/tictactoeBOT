import pygame
import sys
import time
import random
from constants import *

class TicTacToe:
    def __init__(self, starter=1):
        pygame.init()
        pygame.display.set_caption("TicTacToe")

        self.WIN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
        self.FONT = pygame.font.SysFont('Sans', 25)
        pygame.font.init()

        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.boardRects = [
            [TOPLEFT, TOPMID, TOPRIGHT],
            [MIDLEFT, MIDMID, MIDRIGHT],
            [BOTLEFT, BOTMID, BOTRIGHT]
        ]
        self.turn = starter
        self.gameOver = False
        self.winner = 0
        self.clock = pygame.time.Clock()

    def draw(self, gameOver=False):

        if gameOver:
            if self.winner == 1:
                winMessage = self.FONT.render("You Won", True, GREEN)
            elif self.winner == -1:
                winMessage = self.FONT.render("Bot Won", True, GREEN)
            elif self.winner == 0:
                winMessage = self.FONT.render("DRAW", True, GREEN)

            self.WIN.blit(winMessage, winMessage.get_rect(center=(WINWIDTH / 2, WINHEIGHT / 2)))
        else:
            self.WIN.fill(WHITE)
            self.drawGrid()
            self.drawSquares()

        pygame.display.update()

    def drawGrid(self):
        pygame.draw.rect(self.WIN, BLACK, pygame.Rect(250, 50, 10, 620))
        pygame.draw.rect(self.WIN, BLACK, pygame.Rect(460, 50, 10, 620))
        pygame.draw.rect(self.WIN, BLACK, pygame.Rect(50, 250, 620, 10))
        pygame.draw.rect(self.WIN, BLACK, pygame.Rect(50, 460, 620, 10))

    def drawSquares(self):
        for row in range(len(self.board)):
            for square in range(len(self.board[row])):
                if self.board[row][square] == 1:
                    pygame.draw.rect(self.WIN, RED, self.boardRects[row][square])
                elif self.board[row][square] == -1:
                    pygame.draw.rect(self.WIN, BLUE, self.boardRects[row][square])

    def clickBox(self, box):

        boxIndexes = self.index2D(self.boardRects, box)
        if self.board[boxIndexes[0]][boxIndexes[1]] == 0:

            self.board[boxIndexes[0]][boxIndexes[1]] = self.turn

            if self.checkForWin():
                self.winner = self.turn
                self.gameOver = True
            elif self.checkForDraw():
                self.winner = 0
                self.gameOver = True

            if self.turn == 1:
                self.turn = -1
            elif self.turn == -1:
                self.turn = 1

    def index2D(self, array, value):
        for i in range(len(array)):
            if value in array[i]:
                return i, array[i].index(value)

    def resetBoard(self):

        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def botTurn(self):
        self.clickBox(self.boardRects[random.randint(0, 2)][random.randint(0, 2)])

    def checkForWin(self):
        win = False

        for i in range(3):
            if abs(sum(self.board[i])) == 3:
                win = True
            if abs(self.board[0][i] + self.board[1][i] + self.board[2][i]) == 3:
                win = True

        return win
    def checkForDraw(self):

        spaceAvailiable = False
        for row in self.board:
            for square in row:
                if square == 0:
                    spaceAvailiable = True

        if spaceAvailiable:
            return False
        else:
            return True

    def start(self):

        self.clock.tick(FPS)

        self.gameOver = False
        self.turn = 1
        self.winner = 0
        self.resetBoard()

        while self.gameOver == False:

            if self.turn == -1:
                self.botTurn()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseCoords = pygame.mouse.get_pos()

                    for row in self.boardRects:
                        for square in row:
                            if square.collidepoint(mouseCoords) == True:
                                self.clickBox(square)

            self.draw()

        while self.gameOver == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.start()
            self.draw(gameOver=True)

ttt = TicTacToe()
ttt.start()
