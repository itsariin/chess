import pygame

from const import *


class Game:

    def __init__(self):
        pass


    def show_bg(self, surface):
        #pass
        for row in range(ROW):
            for col in range(COL):
                if(row+col) % 2 ==0:
                    color = (234, 235, 200)#dark green

                else:
                    color = (119,154, 88)#light green


                rect = (row*Sqsize,col*Sqsize,Sqsize,Sqsize)

                pygame.draw.rect(surface, color, rect)