import pygame
from const import *

class Dragger:

    def __init__(self):
        self.mouseX=0
        self.mouseY=0

    def updatemouse(self,pos):
        #we'll gonna assign mouseX as x coordinate and similarly for y
        self.mouseX, self.mouseY = pos #kindaa (x,y)

