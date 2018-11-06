#made by Benthan Vu, sprite classes for game
#sources: goo.gl/2KMivS
import pygame as pg
import random
from pygame.sprite import Sprite
from settings import *

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
    def update(self):
        self.vx = 0
        self.vy = 0
        #checks if a button is pressed
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -5
        if keys[pg.K_RIGHT]:
            self.vx = 5        
        if keys[pg.K_UP]:
            self.vy = -5
        if keys[pg.K_DOWN]:
            self.vy = 5
        

        self.rect.x += self.vx
        self.rect.y += self.vy

class Enemy(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((30,40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.vx = 0
        self.vy = 0
    def update(self):
        self.vx = 0
        self.vy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -5
        if keys[pg.K_RIGHT]:
            self.vx = 5        
        if keys[pg.K_UP]:
            self.vy = -5
        if keys[pg.K_DOWN]:
            self.vy = 5
        

        self.rect.x += self.vx
        self.rect.y += self.vy