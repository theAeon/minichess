class Piece(object):
    ''' base class'''
    def __init__(self, color):
        self.color = color
        self.name = 'lul'
        self.candouble = False
class Pawn(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        if self.color == 'White':
            self.validmoves = [(1, 0)]
            self.validcaptures = ((1, 1), (1,-1))
        else:
            self.validmoves = [(-1, 0)]
            self.validcaptures = ((-1,-1), (-1, 1))
        self.candouble = True
        self.movecount = 2
        self.name = 'Pawn'
class Knight(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.movecount = 1
        self.validmoves = ((2, 1), (1, 2), (-1, 2), (1, -2))
        self.validcaptures = self.validmoves
class Bishop(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.movecount = -1
        self.validmoves = ((1, 1), (-1, 1), (1, -1), (-1, -1))
        self.validcaptures = self.validmoves
class Rook(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.cancastle = True
        self.movecount = -1
        self.validmoves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        self.validcaptures = self.validmoves
class Queen(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.movecount = -1
        self.validmoves = ((1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1))
        self.validcaptures = self.validmoves

class King(Piece):
    def __init__(self, color):
        Piece.__init__(self, color)
        self.incheck = False
        self.cancastle = True
        self.movecount = 1
        self.validmoves = ((1, 0), (0, 1), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (-1, 0))
        self.validcaptures = self.validmoves

class Board(object):
    '''defines state of play'''
    def __init__(self, dim1, dim2):
        self.dim = (dim1, dim2)
        self.array = []
        self.readablearray = []
        self.createarray()
    def createarray(self):
        '''creates array of colums x rows'''
        for column in range(self.dim[0]):
            self.array.append([])
            for i in range(self.dim[1]):
                self.array[column].append(' ')
    def printboard(self):
        '''prints game state'''
        inverse = self.readablearray[::-1]
        for column in range(len(inverse)):
            columnstr = ''
            for i in range(len(inverse[column])):
                columnstr += ' '  + inverse[column][i]
            print(str(self.dim[0] - column - 1) + ' ' + columnstr)
        rangelist = ''
        for i in range(0, len(inverse[0])):
            rangelist += ' ' + str(i)
        print('X ' + rangelist)

class Game(object):
    def __init__(self):
        '''defines initial game state'''
        self.piecedict= {' ' : ' ', 'K' : King('White'), 'N' : Knight('White'), 'P': Pawn('White'), 'Q': Queen('White'), 'R' : Rook('White'), 'B': Bishop('White'), 'k' : King('Black'), 'n' : Knight('Black'), 'p': Pawn('Black'), 'q': Queen('Black'), 'r' : Rook('Black'), 'b': Bishop('Black')}
        self.initpos = ([])
        self.board = Board(1, 1)
    def populate(self):
        '''copies initial state to board'''
        self.board.readablearray = self.initpos
        for i in range(len(self.board.array)):
            for j in range(len(self.board.array[i])):
                self.board.array[i][j] = self.piecedict[self.initpos[i][j]]
    def movepiece(self, start, end):
        '''moves a piece to a location if allowed'''
        piece = self.board.array[start[0]][start[1]]
        loc = self.board.array[end[0]][end[1]]
        if piece == ' ':
            return False
        if self.reachable(piece, start, end, piece.validmoves, piece.validcaptures, piece.movecount, piece.name, start):
            self.board.array[end[0]][end[1]] = piece
            self.board.array[start[0]][start[1]] = ' '
            self.board.readablearray[end[0]][end[1]] = self.board.readablearray[start[0]][start[1]]
            self.board.readablearray[start[0]][start[1]] = ' '
            if self.board.array[end[0]][end[1]].candouble == True:
                self.board.array[end[0]][end[1]].candouble == False
                self.board.array[end[0]][end[1]].movecount -= 1
            if self.board.array[end[0]][end[1]].name == 'Pawn':
                if end[0] == max(range(len(self.board.array))) or end[0] == 0:
                    a = input("Promote Piece (Q, N, B, R) ")
                    if a == 'Q':
                        self.board.array[end[0]][end[1]] = Queen(self.board.array[end[0]][end[1]].color)
                        if self.board.array[end[0]][end[1]].color == 'White':
                            self.board.readablearray[end[0]][end[1]] = 'Q'
                        else:
                            self.board.readablearray[end[0]][end[1]] = 'q'
                    if a == 'N':
                        self.board.array[end[0]][end[1]] = Knight(self.board.array[end[0]][end[1]].color)
                        if self.board.array[end[0]][end[1]].color == 'White':
                            self.board.readablearray[end[0]][end[1]] = 'N'
                        else:
                            self.board.readablearray[end[0]][end[1]] = 'n'
                    if a == 'R':
                        self.board.array[end[0]][end[1]] = Rook(self.board.array[end[0]][end[1]].color)
                        self.board.array[end[0]][end[1]].cancastle = False
                        if self.board.array[end[0]][end[1]].color == 'White':
                            self.board.readablearray[end[0]][end[1]] = 'R'
                        else:
                            self.board.readablearray[end[0]][end[1]] = 'r'
                    if a == 'B':
                        self.board.array[end[0]][end[1]] = Bishop(self.board.array[end[0]][end[1]].color)
                        if self.board.array[end[0]][end[1]].color == 'White':
                            self.board.readablearray[end[0]][end[1]] = 'B'
                        else:
                            self.board.readablearray[end[0]][end[1]] = 'b'

            return True
        else:
            return False

    def reachable(self, piece, location, target, validmoves, validcaptures, movecount, name, origloc):
        try:
                
            if location == target:
                if self.board.array[location[0]][location[1]] == ' ':
                    return True
                if self.board.array[location[0]][location[1]].color != piece.color and piece.name != 'Pawn':
                    return True
                if name == 'notapawn':
                    return True
            for i in validmoves:
                newloc = ((location[0] + i[0], location[1] + i[1]))
                if self.board.array[newloc[0]][newloc[1]] == ' ' or self.board.array[newloc[0]][newloc[1]].color != piece.color:
                    return self.reachable(piece, newloc, target, validmoves, validcaptures, movecount - 1, name, origloc)
            if piece.name == 'Pawn':
                for i in validcaptures:
                    newloc = (origloc[0] + i[0], origloc[1] + i[1])
                    if newloc == target and self.board.array[newloc[0]][newloc[1]] != ' ' and self.board.array[newloc[0]][newloc[1]].color != piece.color:
                        return True
            else:
                return False
        except IndexError:
            return self.reachable(piece, location, target, validmoves[1:], validcaptures, movecount, name, origloc)
    def has_won(self):
        return False
class MicroChess(Game):
    def __init__(self):
        Game.__init__(self)
        self.board = Board(5,4)
        self.initpos = (['R', 'N', 'B', 'K'], [' ', ' ', ' ', 'P'], [' ', ' ', ' ', ' '],['p', ' ', ' ', ' '], ['k', 'b', 'n', 'r'])
def askmove(chess, color):
    chess.board.printboard()
    print(color + " to move")
    start = input("Piece to move (column,row): ")
    end = input("Location (column,row): ")
    start = list(start)
    end = list(end)
    del start[1]
    del end[1]
    start = [int(x) for x in start]
    end = [int(x) for x in end]
    return (tuple(start), tuple(end))

def human_v_human(game, color='White'):
    ''' game logic'''
    chess = game()
    chess.populate()
    while chess.has_won() == False:
        tup = askmove(chess, color)
        start = tup[0]
        end = tup[1]
        if chess.movepiece(start, end) == False:
            continue
        if color == 'White':
            color ='Black'
        else:         
            color = 'White'
human_v_human(MicroChess)