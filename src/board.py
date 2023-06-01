from const import *
from square import Square
from piece import *


class Board:
    def __init__(self):
        # list of 8 zeros for each column
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COL)]
        # print(self.squares) this was used to see that
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    #these methods will just be called in our Board class
    #the reason for using _brfore them is to just show that these are private methods
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
        self.squares[row_other][3] = Square(row_other, 3, Bishop(color))


        # King
        self.squares[row_other][4] = Square(row_other, 4, Bishop(color))





#instances for calling the finction
#b = Board()
#b._create()


#difference between clicked_row/col and mouseX and mouseY
                         #print(dragger.mouseY,clicked_row)
                         #print(dragger.mouseX, clicked_col)
                    # so if i click on the left most rook i will get 0 and 0
                    # when i click on the right most rook i will get 7 and 7 THESE ARE CLICKED_ROW/COL
                    # And dragger.mouseX/Y are some different coordinates