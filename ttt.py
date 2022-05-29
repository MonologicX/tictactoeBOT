import sys
import random

class TTT:
    def __init__(self, XPlayer=None, OPlayer=None):

        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.turn = 1
        self.gameOver = False
        self.XPlayer = XPlayer
        self.OPlayer = OPlayer

    def start(self):

        while self.gameOver == False:

            if self.turn == 1:

                if self.XPlayer == None:
                    self.playerMove()
                else:
                    print(type(self.XPlayer))
                    i = self.XPlayer.move(self.board)

                    if self.board[int(i)]  == 0:
                        self.board[int(i)] = self.turn
                        self.checkBoard()
                        self.display()

            if self.turn == -1:

                if self.OPlayer == None:
                    self.playerMove()
                else:
                    print(type(self.OPlayer))
                    i = self.OPlayer.move(self.board)

                    if self.board[int(i)]  == 0:
                        self.board[int(i)] = self.turn
                        self.checkBoard()
                        self.display()

        while self.gameOver == True:

            i = input("Press E to EXIT:")

            if i == "e":
                sys.exit()

    def playerMove(self):
        i = input("Player X, enter Square Number (0 - 8):")

        if i == "e":
            sys.exit()

        if self.board[int(i)]  == 0:
            self.board[int(i)] = self.turn
            self.checkBoard()
            self.display()

    def display(self):

        displayBoard = []
        for square in self.board:
            if square  == 0:
                displayBoard.append('*')
            elif square  == 1:
                displayBoard.append('X')
            elif square  == -1:
                displayBoard.append('0')

        print("{0}|{1}|{2}".format(displayBoard[0], displayBoard[1], displayBoard[2]))
        print("------")
        print("{0}|{1}|{2}".format(displayBoard[3], displayBoard[4], displayBoard[5]))
        print("------")
        print("{0}|{1}|{2}".format(displayBoard[6], displayBoard[7], displayBoard[8]))

    def checkBoard(self):

        endGame = False

        boardFull = True
        for square in self.board:
            if square  == 0:
                boardFull = False
        endGame = boardFull

        for j in range(3):
            #Rows
            if abs(self.board[(j * 3)]  + self.board[(j * 3) + 1]  + self.board[(j * 3) + 2] ) == 3:
                endGame = True
            #Columns
            if abs(self.board[j]  + self.board[j + 3]  + self.board[j + 6] ) == 3:
                endGame = True
        #Diagonals
        if (abs(self.board[0]  + self.board[4]  + self.board[8] ) == 3) or (abs(self.board[2]  + self.board[4]  + self.board[6] ) == 3):
            endGame = True

        if endGame:
            self.gameOver = True
        else:
            self.turn *= -1

class BOT():
    def __init__(self):
        pass
    def move(self, boardState):
        return random.randint(0, 8)

ttt = TTT(OPlayer = BOT())
ttt.start()
