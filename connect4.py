import numpy as np
import random
import itertools

class Piece:

    def __init__(self, color):
        self.color = color
        self.position = None
        self.neighbor = None
        self.edge = None
        self.pos = None

    def addNeighbor(self, pieces):
        self.neighbor = pieces
        return

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
                piece.pos = [i, j]
                self.board[i, j] = piece

        #add neighbors
        corners = [[0, 0], [5, 0], [5, 6], [0, 6]]
        ledge =[[1, 0], [2, 0], [3, 0], [4, 0]]
        tedge = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
        bedge = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
        redge = [[1, 6], [2, 6], [3, 6], [4, 6]]

        for i in range(0,6):
            for j in range(0,7):
                #corner case
                if self.board[i, j].pos in corners:
                    if self.board[i, j].pos == [0, 0]:
                        pieceList =[self.board[i+1, j], self.board[i, j + 1], self.board[i + 1, j + 1]]
                        self.board[i, j].addNeighbor(pieceList)
                    elif self.board[i, j].pos == [5, 0]:
                        pieceList =[self.board[i - 1, j], self.board[i, j + 1], self.board[i - 1, j + 1]]
                        self.board[i, j].addNeighbor(pieceList)
                    elif self.board[i, j].pos == [5, 6]:
                        pieceList = [self.board[i - 1, j], self.board[i, j - 1], self.board[i - 1, j - 1]]
                        self.board[i, j].addNeighbor(pieceList)
                    else:
                        pieceList = [self.board[i + 1, j], self.board[i, j - 1], self.board[i + 1, j - 1]]
                        self.board[i, j].addNeighbor(pieceList)

                elif self.board[i, j].pos in ledge:
                    pieceList = [self.board[i-1, j], self.board[i, j+1], self.board[i-1, j+1],
                                 self.board[i+1, j], self.board[i+1, j+1]]
                    self.board[i, j].addNeighbor(pieceList)
                elif self.board[i, j].pos in tedge:
                    pieceList = [self.board[i, j+1], self.board[i+1, j], self.board[i+1, j+1],
                                 self.board[i + 1, j - 1], self.board[i, j - 1]]
                    self.board[i, j].addNeighbor(pieceList)
                elif self.board[i, j].pos in bedge:
                    pieceList = [self.board[i, j - 1], self.board[i, j+1], self.board[i-1, j],
                                 self.board[i-1, j +1], self.board[i-1, j - 1]]
                    self.board[i, j].addNeighbor(pieceList)
                elif self.board[i, j].pos in redge:
                    pieceList = [self.board[i - 1, j], self.board[i, j-1], self.board[i - 1, j - 1],
                                 self.board[i + 1, j], self.board[i + 1, j - 1]]
                    self.board[i, j].addNeighbor(pieceList)
                else:
                    #centers
                    pieceList = [self.board[i+1, j], self.board[i, j+1], self.board[i+1, j+1],
                                 self.board[i-1, j], self.board[i, j - 1], self.board[i-1, j-1],
                                 self.board[i+1, j-1], self.board[i-1, j+1]]
                    self.board[i, j].addNeighbor(pieceList)




    def displayBoard(self):
        #maybe make new numpy array of the same size, but with 0, 1, 2 to designate if a piece is there
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
        if player == "0":
            piece = Piece("red")
        else:
            piece = Piece("black")
        return piece

    def playRando(self):
        winner = False
        iterator = itertools.cycle(range(2))
        while winner == False:
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

game = Game(board)
#print(game.playRando())

print(game.board.returnPiece(5, 0).pos)

test = np.zeros((6, 7))

#things to do. Figure out a way to prettify the board when displaying
#add neighbors to the initialized pieces