import pygame as pg
import math
from pygame.color import Color
from const import *
from PLATFORM_LIST import *
from stone import Stone
from animation import Animation

class Alien (Animation):
    def __init__(self):
        self.sprite_image = 'alien.png'
        self.sprite_width = 32
        self.sprite_height = 32
        self.sprite_columns = 3
        self.sprite_vel = 5
        self.fps = 10
        self.init_animation()
    def forward(self):
        if self.rect.x < 660:
            self.rect.x += 1
            self.rect.y += 0
    def backward(self):
        if self.rect.x > 200:
            self.rect.x -= 1
            self.rect.y += 0
    
    def update(self):
        self.calc_next_frame()
        rect = (self.sprite_width*self.current_frame, 0,
                self.sprite_width, self.sprite_height)
        self.image.blit(self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))

class Explosion(Animation):
    def __init__(self):
        self.sprite_image = 'explosionsprite.png'
        self.sprite_width = 100
        self.sprite_height = 100
        self.sprite_columns = 25
        self.fps = 16
        self.init_animation()
    def update(self):
        self.calc_next_frame()
        if self.current_frame == self.sprite_columns:
            self.current_frame = 0
            self.kill()
        rect = (self.sprite_width*self.current_frame, 0,
                self.sprite_width, self.sprite_height)
        self.image.blit(self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))

class Catapult(Animation):
    def __init__(self, stone):
        self.sprite_image = 'catapult.png'
        self.sprite_width = 32
        self.sprite_height = 32
        self.sprite_columns = 5
        self.fps = 30
        self.stone = stone
        self.state = CATAPULT_READY
        self.init_animation()

    def update(self):
        if self.state == CATAPULT_FIRE:
            self.calc_next_frame()

            if self.current_frame == self.sprite_columns:
                self.current_frame = 0
                self.state = CATAPULT_READY
                self.stone.setup(
                    (self.rect.x, self.rect.y),
                    self.power, self.direction)
        else:
            self.current_frame = 0

        rect = (self.sprite_width*self.current_frame, 0,
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))

    def forward(self):
        if self.rect.x < 100:
            self.rect.x += 1

    def backward(self):
        if self.rect.x > 0:
            self.rect.x -= 1

    def fire(self, power, direction):
        self.state = CATAPULT_FIRE
        self.power = power
        self.direction = direction
        
class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg .sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
