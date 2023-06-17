

class Move:
    def __init__(self, initial, final):
        self.initial=initial
        self.final=final

        # print(Square.in_range(4,2,5,4))

        # Basically we can call the method with the class not with an instance
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