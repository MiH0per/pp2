#Imports
import pygame as pg
import sys, os
from pygame.locals import *
import random, time
 
#Initialzing 
pg.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pg.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
 
#Setting up Fonts
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pg.image.load("AnimatedStreet.png")
 
#Create a white screen 
surface = pg.display.set_mode((400,600))
surface.fill(WHITE)
pg.display.set_caption("Game")
 
class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
 
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pg.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


#Add coins  class
class coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("coin.png"), (40,40))       
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COINS
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = coin()
 
#Creating Sprites Groups
enemies = pg.sprite.Group()
enemies.add(E1)
all_sprites = pg.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

coins = pg.sprite.Group()
coins.add(C1)
 
#Adding a new User event 
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 1000)


# Adding new Spawn Coin Event that is called every 3s
SPAWN_COIN = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_COIN, 3000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pg.event.get():
        if event.type == SPAWN_COIN:
            new_coin = coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pg.quit()
            sys.exit()
 
    surface.blit(background, (0,0))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    surface.blit(scores, (10,10))
    scores_coin = font_small.render("Coins:" + str(COINS), True, BLACK)
    surface.blit(scores_coin, (300,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()

    if pg.sprite.spritecollideany(P1, coins):
        COINS += 1
        for entity in coins:
            entity.kill()

    if pg.sprite.spritecollideany(E1,coins):
        for entity in coins:
            entity.kill()
 
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(P1, enemies):
          pg.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          surface.fill(RED)
          surface.blit(game_over, (30,250))
           
          pg.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pg.quit()
          sys.exit()        
         
    pg.display.update()
    FramePerSec.tick(FPS)