
class Square:

    #now not every square gonna have piece its either 0 or 1 i.e, piece or no piece
    def __init__(self, row, col, piece=None):
        self.col=col
        self.row = row
        self.piece = piece

    def has_piece(self):
        return self.piece !=None

    def isempty(self):
        return not self.has_piece()

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_team_piece(self,color):
        return self.has_piece() and self.piece.color ==color

    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color !=color
    def isempty_or_rival(self, color):
        return self.isempty() or self.has_rival_piece(color)

    # so we have to check is the possible moves is on the board
    @staticmethod
    def in_range(*args):#this *args basicallt telling python u can have as many parameters as many you want
                        #so we need to loop these arguments
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True




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
#print(Square.in_range(4,2,5,4))

#Basically we can call the method with the class not with an instance