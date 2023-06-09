#main file from where i'll gonna call everything

#imported some files needed for displayig the board
import pygame
import sys

#attributes from the files i created
from const import *
from game import Game
from square import Square
from move import Move

class Main:
    
    def __init__(self):
        #pass
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
        #new attribute reference from our main class to our game class
        #print('hello')
    
    
    def mainloop(self):
        #now I don't have to self.game/screen simply call screen and game
        screen = self.screen
        game=self.game
        board=self.game.board
        #reference for dragger
        dragger=self.game.dragger

        while True:#kind of infinite loop
            #show methods
            game.show_bg(screen)
            game.show_last_moves(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            game.show_hover(screen)

            #for the fluency
            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                #click
                #in this we update the mouse
                # then check if the square we clicked has a piece or not
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.updatemouse(event.pos)#so we are sending this (pos) information to the update mouse in dragger.py
                          #print(event.pos)

                    #now we want to check if the position has a piece
                    #mouse Y coz rows are affected by Y coordinate


                    clicked_row=dragger.mouseY // Sqsize
                    clicked_col = dragger.mouseX // Sqsize

                    #difference between clicked_row/col and mouseX and mouseY
                         #print(dragger.mouseY,clicked_row)
                         #print(dragger.mouseX, clicked_col)
                    # so if i click on the left most rook i will get 0 and 0
                    # when i click on the right most rook i will get 7 and 7 THESE ARE CLICKED_ROW/COL
                    # And dragger.mouseX/Y are some different coordinates

                    #if clicked square has a piece just asking
                    if board.squares[clicked_row][clicked_col].has_piece():#remeber we created this has_piece method already in the square class
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece color
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)  # in case we did a bad move so we have to comeback to the original position
                            dragger.drag_piece(piece)
                            # Show Methods
                            game.show_bg(screen)
                            game.show_last_moves(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                #dragging/movingthecursor MOUSE MOTION
                # we are checking if we are actually dragging a piece
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // Sqsize
                    motion_col = event.pos[0] // Sqsize

                    game.set_hover(motion_row, motion_col)
                    if dragger.dragging:
                        dragger.updatemouse(event.pos)
                        #show methods
                        game.show_bg(screen)
                        game.show_last_moves(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                #releasing the button
                elif event.type == pygame.MOUSEBUTTONUP:

                    if dragger.dragging:
                        dragger.updatemouse(event.pos)
                        released_row = dragger.mouseY // Sqsize
                        released_col = dragger.mouseX // Sqsize
                        #create valid/possible move
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial,final)
                        #valid ?
                        if board.valid_move(dragger.piece,move):
                            board.move(dragger.piece, move)
                            #draw show methods
                            game.show_bg(screen)
                            game.show_last_moves(screen)
                            game.show_pieces(screen)
                            game.next_turn()
                    dragger.undrag_piece()
                #Qutting the application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
        #print('world')
    
#calling the main
main = Main()
main.mainloop()




