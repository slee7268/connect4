import numpy as np
import random
import itertools

class Piece:

    def __init__(self, color):
        self.color = color
        self.position = None
        self.neighbor = None
        self.edge = None
    def placePiece(self, board, loc):
        #loc is the column that you want to place it in.
        board.addPiece(loc, self)
        return


class Board:
    def __init__(self):
        self.board = np.empty(shape=(6, 7), dtype=object)
        for i in range(0,6):
            for j in range(0,7):
                piece = Piece("null")
                self.board[i,j] = piece

        #add neighbors
        for i in range(0,6):
            for j in range(0,7):
                #corner case
                if(((i==0) & (j==0))
                self.board[i,j].neighbor =

    def displayBoard(self):
        print(self.board)
    def addPiece(self, loc, piece):
        i = 5
        while (self.board[i,loc].color!="null"):
            i = i-1
        self.board[i,loc] = piece
        return
    def returnPiece(self, x, y):
        return self.board[x, y]

class Game:
    def __init__(self, board):
        self.board = board
    def playMove(self, player):
        if(player=="0"):
            piece = Piece("red")
        else:
            piece = Piece("black")
        return piece

    def playRando(self):
        winner = False
        iterator = itertools.cycle(range(2))
        while(winner == False):
            player = next(iterator)
            piece = self.playMove(player)
            pos = random.randint(0, 6)
            self.board.addPiece(pos, piece)
            winner=self.checkWin()
        return
    def checkWin(self):

        return

board = Board()
#board.displayBoard()
piece = Piece("red")

piece.placePiece(board, 0)
#board.displayBoard()
print(board.returnPiece(5,0).color)

game = Game(board)
#print(game.playRando())

test = np.zeros((6, 7))

#things to do. Figure out a way to prettify the board when displaying
#add neighbors to the initialized pieces