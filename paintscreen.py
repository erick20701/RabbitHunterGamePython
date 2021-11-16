import pygame
from pygame.locals import *
import math
import random
from bullet import  bullet
from getImage import imageMh

from rabbit import rabbit

class ScreenMh:
    
    def __init__(self,n):
        pygame.init()
        self.width, self.height = 640, 480
        self.keys = [False, False, False, False]
        self.acc=[0,0]
        self.badtimer=100
        self.badtimer1=0
        self.badguys=[[640,100]]
        self.healthvalue=194
        self.timeSt = 30000 + pygame.time.get_ticks()
        
        self.img = imageMh()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Rabbit Hunter')
        self.rab = n
        self.bul = bullet()
        
    checkPause=False

    def pauseGame(self):
        if self.checkPause:
            timePause = pygame.time.get_ticks()
            imgCo = self.img.getImgConti()
            self.screen.blit(imgCo,(0,0))
            pygame.display.update()
            while self.checkPause:
                
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit() 
                        exit(0) 
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        self.checkPause=False
                        timeResume = pygame.time.get_ticks()
                
            self.timeSt+=timeResume-timePause
            
                    


    def blit(self,m,n):
        self.screen.blit(m, n)

    def defBadTime(self):
        self.badtimer-=1

    def paintGrass(self):
        for x in range(self.width//self.img.getGrass().get_width()+1):
            for y in range(self.height//self.img.getGrass().get_height()+1):
                self.screen.blit(self.img.getGrass(),(x*100,y*100))

    def paintRabbit(self):
        self.rab.ss()
        self.screen.blit(self.rab.getPr(), self.rab.getPp())
    
    def rabbitUpdate(self):
        self.rab.update(self.keys)        
    
    def fill(self):
        self.screen.fill(0)
    
    def paintCastel(self):
        self.screen.blit(self.img.getCastle(),(0,30))
        self.screen.blit(self.img.getCastle(),(0,135))
        self.screen.blit(self.img.getCastle(),(0,240))
        self.screen.blit(self.img.getCastle(),(0,345 ))
       
    def paintBullet(self):
         for bullet in self.bul.getArrows():
            index=0
            bullet[1]+=math.cos(bullet[0])*10
            bullet[2]+=math.sin(bullet[0])*10
            if self.bul.ktra(bullet):
                self.bul.popArrows(index)
            index+=1
            for projectile in self.bul.getArrows():
                arrow1 = pygame.transform.rotate(self.img.getArrow(), 360-projectile[0]*57.29)
                self.screen.blit(arrow1, (projectile[1], projectile[2])) 
    

    def paintBadguy(self):
        if self.badtimer==0:
            self.badguys.append([640, random.randint(50,430)])
            self.badtimer=100-(self.badtimer1*2)
            if self.badtimer1>=35:
                self.badtimer1=35
            else:
                self.badtimer1+=5
        index=0
        for badguy in self.badguys:
            if badguy[0]<-64:
                self.badguys.pop(index)
        
            badguy[0]-=2 # 2 là tốc độ con lửng
        # Tấn công lâu đài 
            badrect=pygame.Rect(self.img.getBg1().get_rect())
            badrect.top=badguy[1]
            badrect.left=badguy[0]
            if badrect.left<64:
                self.healthvalue -= random.randint(5,20)
                self.badguys.pop(index)
        # Kiểm tra va chạm 
            index1=0
            for bullet in self.bul.getArrows():
                bullrect=pygame.Rect(self.img.getArrow().get_rect())
                bullrect.left=bullet[1]
                bullrect.top=bullet[2]
                if badrect.colliderect(bullrect):
                    self.acc[0]+=1
                    self.badguys.pop(index)
                    self.bul.popArrows(index1)
                index1+=1
        # Kẻ xấu tiếp theo 
            index+=1
        for badguy in self.badguys:
            self.screen.blit(self.img.getBg1(), badguy)      
        
    def paintClockAndKill(self):
        font = pygame.font.Font(None, 24)
        killtext = font.render(f"Kill point: {self.acc[0]} ", True, (0,0,0))
        survivedtext = font.render(str((self.timeSt-pygame.time.get_ticks())//60000)+":"+str((self.timeSt-pygame.time.get_ticks())//1000%60).zfill(2), True, (0,0,0))
        self.screen.blit(survivedtext, (580,10))
        self.screen.blit(killtext, (280,10))

    def paintHp(self):
        self.screen.blit(self.img.getHealthBar(), (5,5))
        for health1 in range(self.healthvalue):
            self.screen.blit(self.img.getHealth(), (health1+8,8))

    def update(self):
        pygame.display.flip()  

    def checkEven(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit() 
                exit(0) 
            if event.type == pygame.KEYDOWN:
                if event.key==K_w:
                    self.keys[0]=True
                elif event.key==K_a:
                    self.keys[1]=True
                elif event.key==K_s:
                    self.keys[2]=True
                elif event.key==K_d:
                    self.keys[3]=True
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    self.keys[0]=False
                elif event.key==pygame.K_a:
                    self.keys[1]=False
                elif event.key==pygame.K_s:
                    self.keys[2]=False
                elif event.key==pygame.K_d:
                    self.keys[3]=False
                elif event.key==pygame.K_p:
                    self.checkPause=True
            if event.type==pygame.MOUSEBUTTONDOWN:
                position=pygame.mouse.get_pos()
                self.acc[1]+=1
                self.bul.apArrows([math.atan2(position[1]-(self.rab.getPlp()[1]+32),position[0]-(self.rab.getPlp()[0]+26)),self.rab.getPlp()[0]+32,self.rab.getPlp()[1]+32])    

    def checkTime(self):
        if self.timeSt-pygame.time.get_ticks()<10:
            return True
        else:
            return False
    
    
    def checkHp(self):
        if self.healthvalue<=0:
            return True
        else:
            return False
    
    def getAcc(self):
        return self.acc

    def showWL(self,exitcode,accuracy):
       
        if exitcode==0:
            pygame.font.init()
            font = pygame.font.Font(None, 24)
            text = font.render(f"Accuracy: {accuracy:.2f}%", True, (255,0,0))
            textRect = text.get_rect()
            textRect.centerx = self.screen.get_rect().centerx
            textRect.centery = self.screen.get_rect().centery+24
            self.screen.blit(self.img.getGOver(), (0,0))
            self.screen.blit(text, textRect)
        else:
            pygame.font.init()
            font = pygame.font.Font(None, 24)
            text = font.render(f"Accuracy: {accuracy:.2f}%", True, (0,255,0))
            textRect = text.get_rect()
            textRect.centerx = self.screen.get_rect().centerx
            textRect.centery = self.screen.get_rect().centery+24
            self.screen.blit(self.img.getGWin(), (0,0))
            self.screen.blit(text, textRect)
       