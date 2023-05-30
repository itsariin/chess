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

        while True:#kind of infinite loop
            game.show_bg(screen)
            game.show_pieces(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()




            pygame.display.update()
        #print('world')
    
#calling the main
main = Main()
main.mainloop()