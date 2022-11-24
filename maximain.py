import pygame as pg
from sprites import *

class Game():
    def __init__(self):
        pg.init()
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.GREEN = (77,168,25)
        self.MINT = (150,200,175)
        self.PURPLE = (175,150,225)
        self.RED = (255,0,0)

        self.WIDTH = 1216
        self.HEIGHT = 1238

        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.bg=pg.image.load("floor 1.png").convert_alpha()
        self.bg=pg.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))

        self.tekst_font = pg.font.SysFont("ebrima", 100)
        self.FPS = 120
        self.clock = pg.time.Clock()

        self.new()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.boss_group = pg.sprite.Group()
        self.knight_group = pg.sprite.Group()

        self.knight = Player()
        self.black_knight = Boss(self)
        self.all_sprites.add(self.knight, self.black_knight)
        self.boss_group.add(self.black_knight)
        self.knight_group.add(self.knight)

        self.i = 0

        self.knight.hp = 1000

        self.last_collision = 0

        self.tekst_hp = self.tekst_font.render("HP: " + str(self.knight.hp), False, self.WHITE)

        self.run()

    def run(self):
        playing = True
        while playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False


            self.now = pg.time.get_ticks()

            self.screen.blit(self.bg, (self.i,0))
            self.screen.blit(self.bg, (self.WIDTH+self.i,0))
            self.screen.blit(self.tekst_hp, (10, 10))

            self.all_sprites.update()

            self.hits = pg.sprite.spritecollide(self.knight, self.boss_group, False)
            if self.hits:
                if self.last_collision < self.now - 1500:
                    self.knight.immune = False
                
                if not self.knight.immune:
                    self.knight.hp-=200
                    self.knight.immune = True
                    self.last_collision = self.now
                    self.tekst_hp = self.tekst_font.render("HP: " + str(self.knight.hp), False, self.WHITE)
                    print(self.knight.hp)
                    if self.knight.hp <=0:
                        self.knight.kill()

            self.all_sprites.draw(self.screen)
            pg.display.update()

g = Game()
 