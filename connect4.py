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
        # loc is the column that you want to place it in.
        board.addPiece(loc, self)
        return


class Board:
    def __init__(self):
        self.board = np.empty(shape=(6, 7), dtype=object)
        for i in range(0, 6):
            for j in range(0, 7):
                piece = Piece("null")
                piece.pos = [i, j]
                self.board[i, j] = piece

        # add neighbors
        corners = [[0, 0], [5, 0], [5, 6], [0, 6]]
        ledge = [[1, 0], [2, 0], [3, 0], [4, 0]]
        tedge = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
        bedge = [[5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]
        redge = [[1, 6], [2, 6], [3, 6], [4, 6]]

        for i in range(0, 6):
            for j in range(0, 7):
                # corner case
                if self.board[i, j].pos in corners:
                    if self.board[i, j].pos == [0, 0]:
                        pieceList = [self.board[i + 1, j], self.board[i, j + 1], self.board[i + 1, j + 1]]
                        self.board[i, j].addNeighbor(pieceList)
                    elif self.board[i, j].pos == [5, 0]:
                        pieceList = [self.board[i - 1, j], self.board[i, j + 1], self.board[i - 1, j + 1]]
                        self.board[i, j].addNeighbor(pieceList)
                    elif self.board[i, j].pos == [5, 6]:
                        pieceList = [self.board[i - 1, j], self.board[i, j - 1], self.board[i - 1, j - 1]]
                        self.board[i, j].addNeighbor(pieceList)
                    else:
                        pieceList = [self.board[i + 1, j], self.board[i, j - 1], self.board[i + 1, j - 1]]
                        self.board[i, j].addNeighbor(pieceList)

                elif self.board[i, j].pos in ledge:
                    pieceList = [self.board[i - 1, j], self.board[i, j + 1], self.board[i - 1, j + 1],
                                 self.board[i + 1, j], self.board[i + 1, j + 1]]
                    self.board[i, j].addNeighbor(pieceList)
                elif self.board[i, j].pos in tedge:
                    pieceList = [self.board[i, j + 1], self.board[i + 1, j], self.board[i + 1, j + 1],
                                 self.board[i + 1, j - 1], self.board[i, j - 1]]
                    self.board[i, j].addNeighbor(pieceList)
                elif self.board[i, j].pos in bedge:
                    pieceList = [self.board[i, j - 1], self.board[i, j + 1], self.board[i - 1, j],
                                 self.board[i - 1, j + 1], self.board[i - 1, j - 1]]
                    self.board[i, j].addNeighbor(pieceList)
                elif self.board[i, j].pos in redge:
                    pieceList = [self.board[i - 1, j], self.board[i, j - 1], self.board[i - 1, j - 1],
                                 self.board[i + 1, j], self.board[i + 1, j - 1]]
                    self.board[i, j].addNeighbor(pieceList)
                else:
                    # centers
                    pieceList = [self.board[i + 1, j], self.board[i, j + 1], self.board[i + 1, j + 1],
                                 self.board[i - 1, j], self.board[i, j - 1], self.board[i - 1, j - 1],
                                 self.board[i + 1, j - 1], self.board[i - 1, j + 1]]
                    self.board[i, j].addNeighbor(pieceList)

    def displayBoard(self):
        # maybe make new numpy array of the same size, but with 0, 1, 2 to designate if a piece is there
        display = np.empty(shape=(6, 7), dtype=object)
        for i in range(0, 6):
            for j in range(0, 7):
                display[i, j] = self.board[i, j].color
        return display
    def getLegalMoves(self):
        legalMoves = []
        for i in range(0, 7):
            if self.checkFull(i)==False:
                legalMoves.append(i)
        return legalMoves

    def checkFull(self, col):
        # check to see if column is full
        pieceCounter = 0
        for i in range(0, 6):
            if self.board[i, col].color!= "null":
                pieceCounter = pieceCounter + 1

        if pieceCounter == 6:
            return True
        else:
            return False
    def checkFullBoard(self):

        for i in range(0, 6):
            for j in range(0, 7):
                if self.board[i, j].color=="null":
                    return False
        return True

    def addPiece(self, col, piece):
        i = 5
        while self.board[i, col].color != "null":
            i = i - 1
        piece.neighbor = self.board[i, col].neighbor
        self.board[i, col] = piece


        return

    def returnPiece(self, x, y):
        return self.board[x, y]


class Game:
    def __init__(self, board, turn=0):
        self.board = board
        self.turn = turn
    def playMove(self, player, pos):
        if player == 0:
            piece = Piece("red")
        else:
            piece = Piece("black")
        return piece, pos

    def playRandomMove(self, player):
        #print(player)
        if player == 0:
            piece = Piece("red")
            pos = random.randint(0, 6)
        else:
            piece = Piece("black")
            pos = random.randint(0, 6)
        return piece, pos

    def playRando(self):
        winner = False
        iterator = itertools.cycle(range(2))
        moves = 0
        while not winner:
            player = next(iterator)
            piece, pos = self.playRandomMove(player)
            if(self.board.checkFullBoard()):
                print("it's a draw")
                return
            while(self.board.checkFull(pos) == True):
                print("whups that column is already full. Try again")
                piece, pos = self.playRandomMove(player)

            self.board.addPiece(pos, piece)
            if self.turn ==0:
                self.turn = 1
            else:
                self.turn = 0
            print(self.board.displayBoard())
            moves = moves + 1
            winner = self.checkWin()
        print("Number of moves: " + str(moves))
        return self.board

    def playGame(self):
        print("Let's play Connect4!!")
        player1 = input("Player 1, Enter your name: ")
        player2 = input("Player 2, Enter your name: ")
        winner = False
        iterator = itertools.cycle(range(2))
        moves = 0
        while not winner:
            player = next(iterator)
            if player==0:
                print("Player 1, It is your turn!")
                col = input("Player 1, Please enter the column number (0 based indexing) that you'd like to play: ")
                piece = Piece("red")
                col = int(col)
                if self.board.checkFullBoard()==True:
                    print("it's a draw")
                    return
                while self.board.checkFull(col) == True:
                    col = input("Sorry, that was an invalid move. Try again: ")
                    col = int(col)
                self.board.addPiece(col, piece)
                moves = moves +1
                if self.turn == 0:
                    self.turn = 1
                else:
                    self.turn = 0
                print(self.board.displayBoard())
                winner = self.checkWin()
            elif player ==1:
                print("Player 2, It is your turn!")
                col = input("Player 2, Please enter the column number (0 based indexing) that you'd like to play: ")
                piece = Piece("black")
                col = int(col)
                while self.board.checkFull(col) == True:
                    col = input("Sorry that was an invalid move. Try again: ")
                    col = int(col)
                if self.turn == 0:
                    self.turn = 1
                else:
                    self.turn = 0
                self.board.addPiece(col, piece)
                moves = moves + 1
                print(self.board.displayBoard())
                winner = self.checkWin()
        return

    def checkWin(self):
        display = self.board.displayBoard()
        rowRed, rowBlack, colRed, colBlack, diagRed, diagBlack = 0, 0, 0, 0, 0, 0
        #count consecutively by row and then by column
        for i in range(0, 6):
            rowRed = 0
            rowBlack =0
            for j in range(0, 7):
                if display[i, j]== "red":
                    rowBlack = 0
                    rowRed = rowRed + 1
                    if rowRed == 4:
                        print("Player Red wins by row")
                        return True
                elif display[i, j]== "black":
                    rowRed = 0
                    rowBlack = rowBlack + 1
                    if rowBlack == 4:
                        print("Player Black wins by row")
                        return True
                else:
                    rowRed = 0
                    rowBlack = 0
        for k in range(0, 7):
            colBlack = 0
            colRed = 0
            for l in range(0, 6):
                if display[l, k] == "red":
                    colBlack = 0
                    colRed = colRed + 1
                    if colRed == 4:
                        print("player Red wins by col")
                        return True
                elif display[l, k] =="black":
                    colRed = 0
                    colBlack = colBlack + 1
                    if colBlack == 4:
                        print("Player Black wins by col")
                        return True
                else:
                    colRed =0
                    colBlack =0

        diagList = [[[3, 0], [2, 1], [1, 2], [0, 3]],
                    [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]],
                    [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0,5]],
                    [[0, 6], [1,5], [2, 4], [3, 3], [4, 2], [5, 1]],
                    [[5, 2], [4, 3], [3, 4], [2, 5], [1, 6]],
                    [[5, 3], [4, 4], [3, 5], [2, 6]]]
        for diag in diagList:
            diagRed, diagBlack = 0, 0
            for index in diag:
                if display[index[0], index[1]] == "red":
                    diagRed = diagRed + 1
                    diagBlack = 0
                    if diagRed == 4:
                        print("Player Red wins by diag")
                        return True
                elif display[index[0], index[1]] == "black":
                    diagBlack =diagBlack + 1
                    diagRed = 0
                    if diagBlack == 4:
                        print("Player Black wins by diag")
                        return True
                else:
                    diagRed = 0
                    diagBlack = 0
        return False

def test():

    board = Board()
    # board.displayBoard()

    game = Game(board)
    game.playRando()
    return

def test2():
    newBoard = Board()
    game2 = Game(newBoard)
    game2.playGame()
    # print(game.playRando())

#test2()
#testDisplay = game.board.displayBoard()

# things to do. Figure out a way to prettify the board when displaying
