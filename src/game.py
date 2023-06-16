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


                rect = (col * Sqsize, row * Sqsize, Sqsize, Sqsize)
                pygame.draw.rect(surface, color, rect)

    # print(dragger.mouseY,clicked_row)
    # print(dragger.mouseX, clicked_col)

    # difference between clicked_row/col and mouseX and mouseY
    # so if i click on the left most rook i will get 0 and 0
    # when i click on the right most rook i will get 7 and 7 THESE ARE CLICKED_ROW/COL
    # And dragger.mouseX/Y are some different coordinates
    def show_pieces(self,surface):
        for row in range(ROW):
            for col in range(COL):
                #check if there is a piece i.e, piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # so if you see we are blitting all piece but we have to blit all except
                    # the one which we are dragging

                    #All piece except the dragger piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)# I actually didn't need to send this size as we have already set it default I just want ot be explicit
                        img = pygame.image.load(piece.texture)
                        img_center = col * Sqsize + Sqsize // 2, row * Sqsize + Sqsize // 2
                        piece.texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, piece.texture_rect)



    def show_moves(self,surface):
        if self.dragger.dragging:
            piece = self.dragger.piece

            #loop all valid moves
            for move in piece.moves:
                #color
                color = (180, 180, 180) if (move.final.row + move.final.col) % 2 ==0 else (90, 90, 180)
                #rect
                rect = (move.final.col * Sqsize, move.final.row * Sqsize, Sqsize, Sqsize )
                #blit
                pygame.draw.rect(surface, color, rect)
