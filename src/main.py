#main file from where i'll gonna call everything



#imported some files needed for displayig the board
import pygame
import sys

#attributes from the files i created
from const import *
from game import Game



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
        game=self.game
        screen=self.screen
        board=self.game.board
        #reference for dragger
        dragger=self.game.dragger

        while True:#kind of infinite loop
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():

                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.updatemouse(event.pos)
                    #print(event.pos)

                    #now we want to check if the position has a piece
                    #mouse Y coz rows are affected by Y coordinate
                    clicked_row=dragger.mouseY // Sqsize
                    clicked_col = dragger.mouseX // Sqsize

                    #if clicked square has a piece just asking
                    if board.squares[clicked_row][clicked_col].has_piece():#remeber we created this has_piece method already in the square class
                        pass
                #dragging/movingthecursor
                elif event.type == pygame.MOUSEMOTION:
                    pass
                #releasing the button
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
                #Qutting the application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




            pygame.display.update()
        #print('world')
    
#calling the main
main = Main()
main.mainloop()