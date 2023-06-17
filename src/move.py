

class Move:
    def __init__(self, initial, final):
        self.initial=initial
        self.final=final

        # print(Square.in_range(4,2,5,4))

        # Basically we can call the method with the class not with an instance
    # def __str__(self):
    #     s = ''
    #     s+= f'({self.initial.col}, {self.initial.row})'
    #     s += f'->({self.final.col}, {self.final.row})'
    #     return s

        #dunder method these are just some special methods that python has

    # def __eq__(self, other):
    #     return self.initial == other.initial and self.final == other.final
    def __str__(self):
        s = ''
        s += f'({self.initial.col}, {self.initial.row})'
        s += f' -> ({self.final.col}, {self.final.row})'
        return s

    def __eq__(self, other):
        return self.initial == other.initial and self.final == other.final