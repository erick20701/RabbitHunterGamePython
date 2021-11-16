from rabbit import rabbit
from paintscreen import ScreenMh
import pygame
from paintbutton import Button 
from getImage import imageMh

class game(object):
    img = imageMh()
    def __init__(self):
         # background
        self.screen_width = 640
        self.screen_height = 480
        self.screen_size = (640, 480)
        self.background_color = "#00A49A"
        #font
        self.font_Ra = pygame.font.SysFont("Ravie", 55)
        self.font_Hu = pygame.font.SysFont("Ravie", 75)
        self.font_Se = pygame.font.SysFont("Ravie", 35)
        self.ButtonAg = Button(360, 300, self.img.getButtonAg(), 1)
        self.ButtonHome = Button(240, 300, self.img.getButtonHome(), 1)
   
    def BuyTime(self,n):
        tam = rabbit(n)
        screen = ScreenMh(tam)
        running = 1
        exitcode = 0
        while running:
            screen.defBadTime()
            # Check xem có đang pause game hay không
            screen.pauseGame()
            # xóa màn hình trước khi vẽ lại 
            
            screen.fill()
            # vẽ các phần tử màn hình 
            
            screen.paintGrass()
            screen.paintCastel()
            # Đặt vị trí người chơi và xoay 
            screen.paintRabbit()
            # Vẽ mũi tên 
            screen.paintBullet()
            # Vẽ con lửng 
            screen.paintBadguy()
            screen.paintRabbit()
            # Vẽ đồng hồ 
            screen.paintClockAndKill()
            # Vẽ thanh máu
            screen.paintHp()
            # cập nhật màn hình 
            screen.update()
            # lặp lại các sự kiện 
            screen.checkEven()      
            # Di chuyển 
            screen.rabbitUpdate()
            # Kiểm tra thắng / thua 
            if screen.checkTime():
                running=0
                exitcode=1
            if screen.checkHp():
                running=0
                exitcode=0
            if screen.getAcc()[1]!=0:
                accuracy=screen.getAcc()[0]*1.0/screen.getAcc()[1]*100
            else:
                accuracy=0
        # Hiển thị thắng / thua 
        screen.showWL(exitcode,accuracy)      
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            
                if self.ButtonAg.draw(screen):
                    self.BuyTime(n)
                if self.ButtonHome.draw(screen):
                    return
                pygame.display.flip()
