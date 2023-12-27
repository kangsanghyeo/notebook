import pygame as pg
import random
from PLAY_settings import *
from PLAYER import *

run = True

GAME_STATE = 0
GAME_INIT = 0
GAME_PLAY = 1
GAME_CLEAR = 2
GAME_OVER = 3

class Game:
    GAME_INIT = 0
    GAME_PLAY = 1
    GAME_CLEAR = 2
    GAME_OVER = 3
    def __init__(self):
        pg.init()
        self.game_state = GAME_INIT
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self): 
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.blockforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        for block in BLOCKFORM_LIST:
            b = Blockform(*block)
            self.all_sprites.add(b)
            self.blockforms.add(b)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()     

    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 0.1
                self.player.vel.y = 0

        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.blockforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top - 100
                self.player.vel.y = -29
        
        if self.player.rect.top <= HEIGHT/4 :
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        while len (self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)
                    
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for block in self.blockforms:
                block.rect.y += abs(self.player.vel.y)
                if block.rect.top >= HEIGHT:
                    block.kill()

        while len(self.blockforms) < 2:
            width = random.randrange(50, 100)
            b = Blockform(random.randrange(0, WIDTH - width), 
                      random.randrange(-75, -30),
                      width, 20)
            self.blockforms.add(b)
            self.all_sprites.add(b)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if self.game_state == GAME_INIT:
                        self.game_state = GAME_PLAY
        
                    self.player.jumping()

                  

    def draw(self):
        self.screen.fill((150, 150, 150))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
                        
    

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
