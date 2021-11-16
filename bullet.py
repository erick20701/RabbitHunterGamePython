import pygame
import math
from getImage import imageMh
class bullet:
    img = imageMh()
    def __init__(self):
        self.arrows=[]
    
    def getArrows(self):
        return self.arrows

    def popArrows(self,n):
        self.arrows.pop(n)
    
    def apArrows(self,n):
        self.arrows.append(n)

    def ktra(self,bullet):
        return bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480
        