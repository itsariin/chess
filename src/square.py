
class Square:

    #now not every square gonna have piece its either 0 or 1 i.e, piece or no piece
    def __init__(self, row, col, piece=None):
        self.col=col
        self.row = row
        self.piece = piece

    def has_piece(self):
        return self.piece !=None