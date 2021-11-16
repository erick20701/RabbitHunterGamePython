import pygame
import math
from getImage import imageMh
class rabbit:
    img = imageMh()
    
    def __init__(self,n):
        self.playerpos=[100,230]
        if (n==1):
            self.player = self.img.getPlayer1()
        else:
            self.player = self.img.getPlayer2()
       
    def ss(self): 
        
        self.position = pygame.mouse.get_pos()
        self.angle = math.atan2(self.position[1]-(self.playerpos[1]+32),self.position[0]-(self.playerpos[0]+26))
        self.playerrot = pygame.transform.rotate(self.player, 360-self.angle*57.29)
        self.playerpos1 = (self.playerpos[0]-self.playerrot.get_rect().width/2, self.playerpos[1]-self.playerrot.get_rect().height/2)
    

    def getPr(self):
        return self.playerrot

    def getPp(self):
        return self.playerpos1

    def update(self, keys): 
        if keys[0]:
            if (self.playerpos[1]>2):
                self.playerpos[1]-=2
        elif keys[2]:
            if (self.playerpos[1]<478):
                self.playerpos[1]+=2
        if keys[1]: 
            if (self.playerpos[0]>2):
                self.playerpos[0]-=2
        elif keys[3]:
            if (self.playerpos[0]<638):
                self.playerpos[0]+=2
    
    def getPlp(self):
        return self.playerpos1