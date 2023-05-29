import pygame
import sys

from const import *
from game import Game


class Main:
    
    def __init__(self):
        #pass
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game() #new attribute reference from our main class to our game class
        #print('hello')
    
    
    def mainloop(self):
        #pass

        while True:#kind of infinite loop
            self.game.show_bg(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



            pygame.display.update()
        #print('world')
    

main = Main()
main.mainloop()