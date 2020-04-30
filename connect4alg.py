from connect4 import *
import itertools
import math
import copy

class Node:
    def __init__(self, state, visit, pos=None, parent=None, child=None):
        if child is None:
            child = []
        self.state = state
        self.visit = visit
        self.wins = 0
        self.games = 0
        self.pos = pos
        self.parent = parent
        self.child = child

    def select(self):

        startNode = self
        if len(startNode.child) == 0 and startNode.parent == None:
            legal = startNode.state.board.getLegalMoves()
            for pos in legal:
                newGame = startNode.genGameState()
                childNode = Node(newGame, 0, pos=pos, parent=startNode)
                piece = Piece("red")
                childNode.state.board.addPiece(pos, piece)
                childNode.state.board.turn=1
                startNode.child.append(childNode)

        while len(startNode.child) > 0:
            ucbList = []
            for child in startNode.child:
                ucb = child.calcucb()
                ucbList.append(ucb)
            maxpos = ucbList.index(max(ucbList))
            print(ucbList)
            node = startNode.child[maxpos]
            startNode = node
        return startNode

    def genGameState(self):
        newBoard=copy.deepcopy(self.state.board)
        newGame = Game(newBoard)
        return newGame

    def expand(self):
        node = self
        legal = node.state.board.getLegalMoves()
        while len(legal) > 0:
            randpos = random.randint(0, len(legal)-1)
            pos = legal[randpos]
            legal.pop(randpos)
            newGame=self.genGameState()
            childNode = Node(newGame, 0, pos=pos, parent=self)
            if childNode.state.board.turn == 0:
                piece = Piece("red")
                childNode.state.board.turn = 1
            else:
                piece = Piece("black")
                childNode.state.board.turn = 0
            childNode.state.board.addPiece(pos, piece)
            self.child.append(childNode)
            #print("sim")
            terminalNode = childNode.sim()
            #print("backprop")
            # print(terminalNode.state.board.displayBoard())
            terminalNode.backprop(childNode)
        return

    def sim(self):
        node = self
        iterator = itertools.cycle(range(2))
        while node.state.checkWin() is not True:
            player = next(iterator)
            legal = node.state.board.getLegalMoves()
            if len(legal) == 0:
                print("twas a draw")
                newGame = node.genGameState()
                drawNode = Node(newGame, 0)
                return drawNode
            randpos = random.randint(0, len(legal)-1)
            newGame = node.genGameState()
            pos = legal[randpos]
            if newGame.board.turn == 0:
                piece = Piece("red")
                newGame.board.turn = 1
            else:
                piece = Piece("black")
                newGame.board.turn = 0
            newGame.board.addPiece(pos, piece)
            newNode = Node(newGame, 0, pos)
            #print(newNode.state.board.turn)
            node = newNode
            #print(node.state.board.displayBoard())
        #print(node.state.board.displayBoard())
        return node

    def backprop(self, node):
        #redW, blackW, redL, blackL = 0, 0, 0, 0
        if self.state.board.checkFullBoard():
            while node.parent is not None:
                node.visit = node.visit + 1
                node.games = node.games + 1
                node = node.parent
        win = self.state.board.turn
        while node.parent is not None:
            #print("hi")
            if node.state.board.turn == win:
                node.wins = node.wins+1
            node.visit = node.visit + 1
            node.games = node.games + 1
            #print("hi")
            """
            print("turn")
            print(win)
            print(node.state.board.turn)
            print(self.state.board.displayBoard())
            print("games")
            print(node.games)
            print("wins")
            print(node.wins)
            """
            node = node.parent

        #print("new game")
        #print(startNode.state.board.displayBoard())
        node.visit = node.visit + 1
        node.games = node.games + 1
        return node

    def calcucb(self):
        if self.visit == 0:
            return 100000000
        exploration_term = (math.sqrt(2.0)
                            * math.sqrt(math.log(self.parent.visit) / self.visit))
        exploit = self.wins/self.games
        return exploit + exploration_term

class MCTS:
    def __init__(self, node):
        #initialize the root
        self.root = node
            #self.root.child = self.root.child.append(childNode)
    def simulate(self, runs):

        loop = 0
        while loop < runs:
            #print('root')
            print('selecting')
            node = self.root
            #print(node.state.board.displayBoard())
            child = node.select()
            #print("childboard")
            #print(child.state.board.displayBoard())
            #print(child.state.board.displayBoard())
            print("expand")
            childNode = child.expand()
            loop = loop + 1
        return

    def playRandom(self, start):

        board = Board()
        game = Game(board)
        newMCTS = self
        if start == 0:
            #mcts goes first
            while game.checkWin()!=True:
                newMCTS.simulate(500)
                pos = newMCTS.best_action()
                piece = Piece("red")
                game.board.turn = 1
                game.board.addPiece(pos, piece)
                print(game.board.displayBoard())
                if game.checkWin()==True:
                    break
                legal = game.board.getLegalMoves()
                pick = random.randint(0, len(legal)-1)
                piece2 = Piece("black")
                game.board.turn = 0
                game.board.addPiece(pick, piece2)
                print(game.board.displayBoard())
                mctsBoard = copy.deepcopy(game.board)
                newGame = Game(mctsBoard)
                node = Node(newGame, 0)
                newMCTS = MCTS(node)
            print("gg")
            print(game.board.displayBoard())
        return

    def best_action(self):
        #number of sims
        #exploit
        exploit = []
        for child in self.root.child:
            val = child.wins/child.games
            print(child.wins, child.games)
            exploit.append(val)
        maxpos = exploit.index(max(exploit))
        choose = self.root.child[maxpos]

        return choose

    def playMe(self):
        board = Board()
        game = Game(board)
        newMCTS = self
        while game.checkWin() != True:
            newMCTS.simulate(100)
            choose = newMCTS.best_action()
            pos = choose.pos
            piece = Piece("red")
            game.board.turn = 1
            game.board.addPiece(pos, piece)
            print(game.board.displayBoard())
            if game.checkWin() is True:
                break
            col = input("pick where you wanna play the piece")
            piece2 = Piece("black")
            game.board.turn = 0
            game.board.addPiece(int(col), piece2)
            print(game.board.displayBoard())
            mctsBoard = copy.deepcopy(game.board)
            newGame = Game(mctsBoard)
            node = Node(newGame, 0)
            newMCTS = MCTS(node)
        print("gg")
        print(game.board.displayBoard())
        return

board = Board()
game = Game(board)

root = Node(game, 0)
mcts = MCTS(root)
#mcts.simulate(100)
#mcts.playRandom(0)
mcts.playMe()

"""
root = Node(game, 0)
for i in range(0, 7):

    board = Board()
    game = Game(board)
    childNode = Node(game, 0, pos=i, parent=root)
    root.child.append(childNode)

piece=Piece("red")
root.child[0].state.board.addPiece(1, piece)


#print(root.state.board.displayBoard())
newBoard = copy.deepcopy(root.state.board)

#newBoard.addPiece(root.child[0].pos, piece)
newBoard.addPiece(1, piece)
print(root.state.board.displayBoard())
print(newBoard.displayBoard())
newGame = Game(newBoard)
childNode = Node(newGame, 0, pos=3, parent=root)
#self.child.append(childNode)

"""