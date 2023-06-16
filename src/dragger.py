import pygame
from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0


        #BLIT METHOD

        #if you see this we are somewhat doing the same thing we did in the game.py file inside show_piece folder
    def update_blit(self, surface):
        #so just updating the texture when we are clicking the piece i.e, increasing the size
        self.piece.set_texture(size=128)#Changing the size is for the image that is we have two folders 80 and 128
        texture = self.piece.texture

        #image
        img = pygame.image.load(texture)

        #rectangle
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center=img_center)

        #blit
        surface.blit(img, self.piece.texture_rect)

        #OTHER METHODS
    def updatemouse(self,pos):
        #we'll gonna assign mouseX as x coordinate and similarly for y
        self.mouseX, self.mouseY = pos #kindaa (x,y)

    def save_initial(self,pos):
        self.initial_row = pos[1] // Sqsize
        self.initial_col = pos[0] // Sqsize

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False


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