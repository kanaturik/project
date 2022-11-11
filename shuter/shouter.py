import pygame
import os
import time
import random
pygame.init()

#PATH = os.path.dirname(__file__) + os.sep
path = ''
COLOR_WHITE = (255, 255, 255)

ufoMissed = 0
countUFO = 8
hit = 0




class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imageS ,w, h,  x, y, speed):
        super().__init__()
        self.image = pygame.image.load(imageS)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
      
        self.speed = speed
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        
    #def create(self):
        #self.image = pygame.transform.scale(self.image, (self.w, self.h))
    def show(self):
        wind.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    #def __init__(self, image, w, h, x, y, speed):
        #super(). __init__(image, w, h, x, y, speed)
    def control(self):
        keys = pygame.key.get_pressed()
        #events = pygame.event.ge()
        if keys [pygame.K_LEFT] == True:
            self.x -= 10

        if keys [pygame.K_RIGHT] == True:
            self.x += 10

        if keys [pygame.K_SPACE] == True :
            
            bullets.add(Bullet(PATH+ "bullet.png", 10, 40, self.rect.x+20, self.rect.y-35, 10))
               

        self.rect.x = self.x
        self.rect.y = self.y

        

class UFO(GameSprite):

    def update(self):
        global ufoMissed, text2,  hit
        self.rect.y += self.speed
        if self.rect.y > 700:
            self.rect.y = -50
            self.rect.x = random.randint(0, 900)
            ufoMissed += 1 
            text2 = font.render("Пропущено: "+str(ufoMissed), True, COLOR_WHITE)
            print(ufoMissed)
            hit += 1
            text1 = font.render('Счет:'+ str(hit), True, COLOR_WHITE)


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed


wind = pygame.display.set_mode((1000, 700))
beg = GameSprite(PATH+'galaxy.jpg',  1000,700, 0,0,0)
hero = Hero(PATH+'rocket.png', 50, 50, 400, 500, 0)

font = pygame.font.SysFont('Arial', 40)
text1 = font.render("Счет: ", True, COLOR_WHITE)
text2 = font.render("Пропущено: ", True, COLOR_WHITE)
text3 = font.render('Ты проиграл!', True, COLOR_WHITE)

'''  
UFO_list = [
    UFO(PATH+'ufo.png', 100,50, random.randint(0, 900), -30,1),
    UFO(PATH+'ufo.png', 100,50, random.randint(0, 900), -30,2),
    UFO(PATH+'ufo.png', 100,50, random.randint(0, 900), -30,3),
    UFO(PATH+'ufo.png', 100,50, random.  randint(0, 900), -30,2),
    UFO(PATH+'ufo.png', 100,50, random.randint(0, 900), -30,1),
    UFO(PATH+'ufo.png', 100,50, random.randint(0, 900), -30,3)
]
'''


UFO_list = pygame.sprite.Group()
bullets = pygame.sprite.Group()

i = 0
while i < countUFO:
    UFO_list.add(UFO(PATH + 'ufo.png', 50, 50, random.randint(0, 900), -30, random.randint(2,5)))
    i += 1
game = True



clock = pygame.time.Clock()

while game:


    




    beg.show()

    
    
    
    
    hero.show()
    

    hero.control()

    UFO_list.update()

    bullets.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #
    collides = pygame.sprite.groupcollide(UFO_list,bullets, True,True)




    #
    
    
    
    UFO_list.draw(wind)
    bullets.draw(wind)

    wind.blit(text1, (10,10))
    wind.blit(text2, (10,50))    
    
    clock.tick(30)
    pygame.display.update()

    

    