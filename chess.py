import string
class Piece(object):
    def __init__(self, color):
        self.passthrough = False
        self.color = color

class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self,color)
        self.candouble = True
class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.passthrough = True
class Bishop(Piece):
    None

class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.cancastle = True

class Queen(Piece):
    None

class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.incheck = False
        self.cancastle = True

class Board(object):
    def __init__(self, dim1,dim2):
        self.dim = (dim1,dim2)
        self.array = []
        self.readablearray = []
        self.createarray()
    def createarray(self):
        for column in range(self.dim[0]):
            self.array.append([])
            for row in range(self.dim[1]):
                self.array[column].append(' ')
    def printboard(self):
        for column in range(len(self.readablearray)):
            columnstr = ''
            for i in range(len(self.readablearray[column])):
                columnstr += ' '  + self.readablearray[column][i]
            print(str(self.dim[0] - column) + ' ' + columnstr)
        rangelist = ''
        for i in range(1, len(self.readablearray[0]) + 1):
            rangelist += ' ' + str(i)
        print('X ' + rangelist)

class Game(object):
    def __init__(self):
        self.piecedict= {' ': ' ', 'K' : King('White'), 'N' : Knight('White'), 'P': Pawn('White'), 'Q': Queen('White'), 'R' : Rook('White'), 'B': Bishop('White'),'k' : King('Black'), 'n' : Knight('Black'), 'p': Pawn('Black'), 'q': Queen('Black'), 'r' : Rook('Black'), 'b': Bishop('Black')}
        self.initpos = ([])
    def populate(self):
        self.board.readablearray = self.initpos
        for i in range(len(self.board.array)):
            for j in range(len(self.board.array[i])):
                self.board.array[i][j] = self.piecedict[self.initpos[i][j]]
class MicroChess(Game):
    def __init__(self):
        Game.__init__(self)
        self.board = Board(5,4)
        self.initpos = (['k', 'b', 'n', 'r'], ['p', ' ', ' ', ' '], [' ', ' ', ' ', ' '],[' ', ' ', ' ', 'P'], ['R', 'N', 'B', 'K'])
