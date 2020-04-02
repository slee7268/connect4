from connect4 import *
import itertools
import math

class Node:
    def __init__(self, state, visit, pos=None, parent=None, child=None):
        self.state = state
        self.visit = visit
        self.wins = 0
        self.losses = 0
        self.pos = pos
        self.parent = parent
        self.child = child

    def backprop(self):
        #redW, blackW, redL, blackL = 0, 0, 0, 0
        self.visit = self.visit + 1
        startNode = self
        newBoard = Board()
        newGame = Game(newBoard)
        while startNode.parent !=None:
            startNode.state = newGame
            startNode.visit = startNode.visit+1
            startNode.wins =startNode.wins+1
            startNode = startNode.parent
        startNode.state = newGame

        print("new game")
        #print(startNode.state.board.displayBoard())
        return startNode

    def isterminal(self):
        if self.child is None:
            return True
        else:
            return False

    def calcucb(self):

        exploration_term = (math.sqrt(2.0)
                            * math.sqrt(math.log(self.parent.visit) / self.visit))
        return

class MCTS:
    def __init__(self, node):
        #initialize the root
        self.root = node
        childList = []
        for i in node.state.board.getLegalMoves():
            childNode = Node(game, 0, pos=i, parent=self.root)
            childList.append(childNode)
        self.root.child = childList

    def initialize_visit(self, runs):
        node = self.root
        for i in range(0, runs):
            legal = node.state.board.getLegalMoves()
            pos = random.randint(0, len(legal)-1)
            move = legal[pos]
            if node.state.turn == 0:
                piece = Piece("red")
            else:
                piece = Piece("black")
            node = node.child[move]
            node.state.board.addPiece(move, piece)
            if node.state.turn == 0:
                node.state.turn = 1
            else:
                node.state.turn = 0
            #newParent.visit = newParent + 1
            if node.state.checkWin() == True:
                print(node.state.board.displayBoard())
                node = node.backprop()
            #print(node.visit)
            childList = []
            for j in node.state.board.getLegalMoves():
                childNode = Node(node.state, 0, pos=j, parent=node)
                childList.append(childNode)
            node.child = childList
        return


    def best_action(self, sim):
        #number of sims
        return



board = Board()
game = Game(board)

root = Node(game, 0)
mcts = MCTS(root)
mcts.initialize_visit(50)

