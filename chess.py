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
        self.createarray()
    def createarray(self):
        for column in range(self.dim[0]):
            self.array.append([])
            for row in range(self.dim[1]):
                self.array[column].append(' ')
    def printboard(self):
        for column in range(len(self.array)):
            columnstr = ''
            for i in range(len(self.array[column])):
                columnstr += ' '  + self.array[column][i]
            print(str(self.dim[0] - column) + ' ' + columnstr)
        rangelist = ''
        for i in range(1, len(self.array[0]) + 1):
            rangelist += ' ' + str(i)
        print('X ' + rangelist)
