from const import *
from square import Square
from piece import *
from move import Move


class Board:
    def __init__(self):
        # list of 8 zeros for each column
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COL)]
        # print(self.squares) this was used to see that
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        #console
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        #move
        piece.moved = True

        #clear valid moves
        piece.clear_moves()

        #setting the last move
        self.last_move = move


    def valid_move(self, piece, move):
        return move in piece.moves
    def calc_moves(self,piece,row,col):

        def pawn_moves():
            #steps
            steps = 1 if piece.moved else 2


            #vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1+steps))
            for possible_move_row in range(start,end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        move = Move(initial,final)
                        piece.add_move(move)
                    else:
                        break
                else:
                    break


            #Diagonal moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        move =Move(initial, final)

                        piece.add_move(move)
        def knight_moves():
            # so if our Knight is in the center the possible moves it has are '8'
            possible_moves = [
                (row-2, col+1),
                (row-2, col-1),
                (row+2, col+1),
                (row+2, col-1),
                (row-1, col+2),
                (row+1, col+2),
                (row-1, col-2),
                (row+1, col-2),
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col ].isempty_or_rival(piece.color):
                        #Creating Squares of the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row,possible_move_col)  #piece=piece
                        #Creatin new Move
                        move = Move(initial,final)
                        piece.add_move(move) #Appending new Valid Moves

        def straightlines_moves(increments):
            for increment in increments:
                row_increment, col_increment = increment
                possible_move_row = row + row_increment
                possible_move_col = col + col_increment

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)

                        # empty
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # append a new move
                            piece.add_move(move)

                        # has enemy piece
                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            # append a new move
                            piece.add_move(move)
                            break
                        # has team piece
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                    else:
                        break
                    #increments
                    possible_move_row = possible_move_row + row_increment
                    possible_move_col = possible_move_col + col_increment

        def king_moves():
            adjacents = [
                (row - 1, col + 0),
                (row + 1, col + 0),
                (row + 0, col + 1),
                (row + 0, col - 1),
                (row - 1, col - 1),
                (row + 1, col + 1),
                (row - 1, col + 1),
                (row + 1, col - 1),

            ]
            for possible_move in adjacents:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # Creating Squares of the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)  # piece=piece
                        # Creatin new Move
                        move = Move(initial, final)
                        piece.add_move(move)  # Appending new Valid Moves



        #I can also use piece.name == 'Pawn' instead of isinstance
        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straightlines_moves([
                (-1,1), #ur
                (-1,-1),#ul
                (1, -1),#dl
                (1, 1),#dr
            ])

        elif isinstance(piece, Rook):
            straightlines_moves([
                (-1,0),
                (1,0),
                (0,1),
                (0,-1),
            ])

        elif isinstance(piece, Queen):
            straightlines_moves([
                (-1, 1),  # ur
                (-1, -1),  # ul
                (1, -1),  # dl
                (1, 1),  # dr
                (-1, 0),
                (1, 0),
                (0, 1),
                (0, -1),
            ])

        elif isinstance(piece, King):
            king_moves()

    '''
    ->these methods will just be called in our Board class
    ->the reason for using _brfore them is to just show that these are private methods
    '''
    def _create(self):
        for row in range(ROW):
            for col in range(COL):
                self.squares[row][col] = Square(row,col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1,0)
        # if color == 'white':
        #     row_pawn,row_other = (6,7)
        # else:
        #     row_pawn, row_other = (1, 0)

        #Pawns
        for col in range(COL):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
            #self.squares[5][1] = Square(5,1, Pawn(color))

        #Knights
        self.squares[row_other][1] = Square(row_other,1,Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        #self.squares[4][4]= Square(4,4,Knight(color))

        #Bishops
        self.squares[row_other][2] = Square(row_other,2,Bishop(color))
        self.squares[row_other][5] = Square(row_other,5,Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        #self.squares[4][4] = Square(4, 4, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        #self.squares[5][4] = Square(5, 4, Queen(color))


        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))





#instances for calling the finction
#b = Board()
#b._create()

'''
Asthetic Method

if i create an instance of Square class 

s = square()
#Now with s i can call has_piece
s.has_piece

#Now a Asthetic Method let me call method inside of that class without an "object"
I just need the class itself So, I can do 
Square.in_range() And i can call @staticmethod
                                    def in_range(*args):
                                        for arg in args:
                                            if arg < 0 or arg > 7:
                                                return False
                                        return True
without creating any object or without any need of object
'''
