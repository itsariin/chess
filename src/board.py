from const import *
from square import Square
from piece import *
from move import Move


class Board:
    def __init__(self):
        # list of 8 zeros for each column
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COL)]
        # print(self.squares) this was used to see that
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self,piece,row,col):

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




        #I can also use piece.name == 'Pawn' instead of isinstance
        if isinstance(piece, Pawn):
            pass

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            pass

        elif isinstance(piece, Rook):
            pass

        elif isinstance(piece, Queen):
            pass

        elif isinstance(piece, King):
            pass

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

        #Knights
        self.squares[row_other][1] = Square(row_other,1,Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        #Bishops
        self.squares[row_other][2] = Square(row_other,2,Bishop(color))
        self.squares[row_other][5] = Square(row_other,5,Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))


        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))





#instances for calling the finction
#b = Board()
#b._create()

