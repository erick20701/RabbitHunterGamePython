import time
from rabbit import rabbit
import pygame
from getImage import imageMh
from paintscreen import ScreenMh
from gamemode import game 
from paintbutton import Button 



class Menu:
    img = imageMh()
    def __init__(self, surf):
        pygame.init()
        self.surf = surf
   
        self.runG = game()
        # tạo các nút 
        self.play_button = Button(130, 350, self.img.getPlayButton(), 1)
        self.hd_button = Button(590, 10, self.img.getHdButton(), 1)
        self.quit_button = Button(390, 350, self.img.getQuitButton(), 1)
        self.ButtonHome = Button(10, 10, self.img.getButtonHome(), 1)
        self.ButtonBack = Button(10, 10, self.img.getButtonBack(), 1)
        self.menu_run(surf)

    def run(self, surf):
        
        surf.fill(self.runG.background_color)
        textRa = self.runG.font_Ra.render("Rabbit", 1, (22, 14, 5))
        textHu = self.runG.font_Hu.render("Hunter", 1, (22, 14, 5))
        surf.blit(textRa, (195, 165))
        surf.blit(textHu, (155, 225))
        if self.play_button.draw(surf):
            time.sleep(0.2)
            self.sec_player(surf)
        if self.quit_button.draw(surf):
            time.sleep(0.2)
            pygame.quit()
                
    def sec_player(self,surf):
        while True:
            surf.fill(self.runG.background_color)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

            player1 = Button(200, 210, self.img.getPlayer1(), 1)
            player2 = Button(360, 207, self.img.getPlayer2(), 1)
            textSe = self.runG.font_Se.render("Player selection ", 1, (22, 14, 5))
            surf.blit(textSe, (135, 100))
            if self.ButtonBack.draw(surf):
                time.sleep(0.2)
                self.menu_run(surf)
            if player1.draw(surf):
                time.sleep(0.5)
                self.runG.BuyTime(1)
                self.menu_run(surf)
            if player2.draw(surf):
                time.sleep(0.5)
                self.runG.BuyTime(2)
                self.menu_run(surf)
            pygame.display.update()
        
        

    def menu_run(self,surf):
        clicked_hd = False

        while True:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
            if clicked_hd == False:
                self.run(surf)

            if self.hd_button.draw(surf):
                time.sleep(0.2)
                clicked_hd = True

            if clicked_hd:
                self.surf.blit(self.img.getHdShowButton(), (0, 0))
                if self.ButtonHome.draw(surf):
                    time.sleep(0.2)
                    clicked_hd = False

            pygame.display.update()