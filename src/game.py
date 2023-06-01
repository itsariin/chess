import pygame

from const import *
from board import Board
from dragger import Dragger


class Game:

    def __init__(self):
        self.board = Board()
        #making a refernce from the game
        self.dragger = Dragger()


    #BLIT METHODS
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


    def show_pieces(self,surface):
        for row in range(ROW):
            for col in range(COL):
                #check if there is a piece i.e, piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    img = pygame.image.load(piece.texture)
                    img_center = col * Sqsize + Sqsize // 2, row * Sqsize + Sqsize // 2
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)


