class Piece(object):
    def __init__(self, color):
        self.passthrough = False
        self.color = color
class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.candouble = True
        self.movecount = 2
        self.validmoves = ((1, 0))
        self.validcaptures = ((1, 1))
class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.passthrough = True
        self.movecount = 1
        self.validmoves = ((2, 1), (1, 2), (-1, 2), (1, -2))
        self.validcaptures = self.validmoves
class Bishop(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.movecount = '-1'
        self.validmoves = ((1, 1), (-1, 1), (1, -1), (-1, -1))
        self.validcaptures = self.validmoves
class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.cancastle = True
        self.movecount = '-1'
        self.validmoves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        self.validcaptures = self.validmoves
class Queen(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.movecount = '-1'
        self.validmoves = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1))
        self.validcaptures = self.validmoves

class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.incheck = False
        self.cancastle = True
        self.movecount = '1'
        self.validmoves = ((1, 0), (0, 1), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (-1, 0))
        self.validcaptures = self.validmoves

class Board(object):
    def __init__(self, dim1, dim2):
        self.dim = (dim1, dim2)
        self.array = []
        self.readablearray = []
        self.createarray()
    def createarray(self):
        for column in range(self.dim[0]):
            self.array.append([])
            for i in range(self.dim[1]):
                self.array[column].append(' ')
    def printboard(self):
        for column in range(len(self.readablearray)):
            columnstr = ''
            for i in range(len(self.readablearray[column])):
                columnstr += ' '  + self.readablearray[column][i]
            print(str(self.dim[0] - column - 1) + ' ' + columnstr)
        rangelist = ''
        for i in range(0, len(self.readablearray[0])):
            rangelist += ' ' + str(i)
        print('X ' + rangelist)

class Game(object):
    def __init__(self):
        self.piecedict= {' ' : ' ', 'K' : King('White'), 'N' : Knight('White'), 'P': Pawn('White'), 'Q': Queen('White'), 'R' : Rook('White'), 'B': Bishop('White'), 'k' : King('Black'), 'n' : Knight('Black'), 'p': Pawn('Black'), 'q': Queen('Black'), 'r' : Rook('Black'), 'b': Bishop('Black')}
        self.initpos = ([])
        self.board = Board(1, 1)
    def populate(self):
        self.board.readablearray = self.initpos
        for i in range(len(self.board.array)):
            for j in range(len(self.board.array[i])):
                self.board.array[i][j] = self.piecedict[self.initpos[i][j]]
    def movepiece(self, start, end):
        piece = self.board.array[start[0]][start[1]]
        loc = self.board.array[end[0]][end[1]]
        if piece == ' ':
            return False
        if loc != ' ':
            if piece.color != loc.color:
                if self.reachable(piece, start, end, piece.validmoves, piece.validcaptures, piece.movecount):
                    self.board.array[end[0]][end[1]] = piece
                    self.board.readablearray[end[0]][end[1]] = self.board.readablearray[start[0]][start[1]]
        if loc == ' ':
            if self.reachable(piece, start, end, piece.validmoves, piece.validcaptures, piece.movecount):
                self.board.array[end[0]][end[1]] = piece
                self.board.readablearray[end[0]][end[1]] = self.board.readablearray[start[0]][start[1]]
        else:
            return False

    def reachable(self, piece, location, target, validmoves, validcaptures, movecount):
        try:
            if location == target:
                return True
            if movecount == 0:
                return False
            if validmoves == validcaptures:
                for i in validmoves:
                    newloc = (location[0] + i[0], location[1] + i[1])
                    if self.board.readablearray[newloc[0], newloc[1]] == ' ' and piece.passthrough == False:
                        return self.reachable(piece, newloc, target, i, i, movecount - 1)
                    if piece.passthrough == True:
                        return self.reachable(piece, newloc, target, i, i, movecount - 1)
            if validmoves != validcaptures:
                for i in validcaptures:
                    if self.board.readablearray[location[0] + i[0]][location[1] + i[1]] == True:
                        return True
            
                for i in validmoves:
                    newloc = (location[0] + i[0], location[1] + i[1])
                    return self.reachable(piece, newloc, target, i, 'nope', movecount - 1)
        except IndexError:
            return False
class MicroChess(Game):
    def __init__(self):
        Game.__init__(self)
        self.board = Board(5,4)
        self.initpos = (['k', 'b', 'n', 'r'], ['p', ' ', ' ', ' '], [' ', ' ', ' ', ' '],[' ', ' ', ' ', 'P'], ['R', 'N', 'B', 'K'])
