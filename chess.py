import string
'''class Piece(object):
    def __init__(self, pos, color):
        self.passthrough = False
        self.position = pos
        self.captured = False
        self.color = color
    def setpos(location):
        self.position = location

class Pawn(Piece):
    def move(location):
    
    def capture(location):
    
    def promote(location):

class Knight(Piece):
    def __init__(self, pos, color):
        Piece.init(self, pos, color)
        self.passthrough = True
    def move(location):

class Bishop(Piece):
    def move(location):

class Rook(Piece):
    def __init__(self, pos, color):
        Piece.init(self, pos, color)
        self.cancastle = True
    def move(location):
    
    def castle(location):

class Queen(Piece):
    def move(location):

class King(Piece):
    def __init__(self, pos, color):
        Piece.__init__(self, pos, color)
        self.incheck = False
        self.cancastle = True
    def move(location):

    def castle(location):
    
'''
class Board(object):
    def __init__(self, dim1,dim2):
        self.dim = (dim1,dim2)
        self.array = []
    def createarray(self):
        for row in range(self.dim[0]):
            self.array.append([])
            for column in range(self.dim[1]):
                self.array[row].append(None)
    def printboard(self):
        for row in board:
            print(self.array)