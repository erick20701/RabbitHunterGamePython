import pygame

class imageMh:
    def __init__(self):
        #game play
        self.player1 = pygame.image.load("resources/images/dude.png")
        self.player2 = pygame.image.load("resources/images/dude2.png")
        self.grass = pygame.image.load("resources/images/grass.png")
        self.castle = pygame.image.load("resources/images/castle.png")
        self.arrow = pygame.image.load("resources/images/bullet.png")
        self.badguyimg1 = pygame.image.load("resources/images/badguy.png")
        self.badguyimg=pygame.image.load("resources/images/badguy2.png")
        self.healthbar = pygame.image.load("resources/images/healthbar.png")
        self.health = pygame.image.load("resources/images/health.png")
        self.gameover = pygame.image.load("resources/images/gameover.png")
        self.continiue = pygame.image.load("resources/images/continue.png")
        self.youwin = pygame.image.load("resources/images/youwin.png")
        #Menu
        self.play_img = pygame.image.load('resources/images/play.png')
        self.hd = pygame.image.load('resources/images/huongdan.png')
        self.hdshow = pygame.image.load('resources/images/hdshow.png')
        self.quit_img = pygame.image.load('resources/images/quit.png')
        self.BtHome = pygame.image.load('resources/images/buttonH.png')
        self.BtBack = pygame.image.load('resources/images/buttonBack.png')
        self.BtAg = pygame.image.load('resources/images/buttonAg.png')
    
    def  getImgConti(self):
        return self.continiue

    def  getButtonAg(self):
        return self.BtAg

    def  getButtonBack(self):
        return self.BtBack

    def  getButtonHome(self):
        return self.BtHome
    
    def  getHdShowButton(self):
        return self.hdshow

    def  getHdButton(self):
        return self.hd
    
    def  getPlayButton(self):
        return self.play_img

    def  getQuitButton(self):
        return self.quit_img

    def  getPlayer1(self):
        return self.player1
    
    def  getPlayer2(self):
        return self.player2

    def  getGrass(self):
        return self.grass

    def  getCastle(self):
        return self.castle

    def  getArrow(self):
        return self.arrow

    def  getBg1(self):
        return self.badguyimg

    def  getHealth(self):
        return self.health

    def  getHealthBar(self):
        return self.healthbar

    def  getGOver(self):
        return self.gameover

    def  getGWin(self):
        return self.youwin
 
