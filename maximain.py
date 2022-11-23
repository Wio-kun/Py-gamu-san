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

        self.WIDTH = 1216
        self.HEIGHT = 1238

        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.bg=pg.image.load("floor 1.png").convert_alpha()

        self.bg=pg.transform.scale(self.bg, (self.WIDTH, self.HEIGHT))

        self.times_new_roman30 = pg.font.SysFont("Times New Roman", 100)
        self.FPS = 120
        self.clock = pg.time.Clock()

        self.new()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.boss_group = pg.sprite.Group()
        self.knight_group = pg.sprite.Group()

        self.Knight = Player()
        self.Black_Knight = Boss()
        self.all_sprites.add(self.Knight, self.Black_Knight)
        self.boss_group.add(self.Black_Knight)
        self.knight_group.add(self.Knight)

        self.i = 0

        self.Knight.hp = 1000

        self.tekst_hp = self.times_new_roman30.render("hp: " + str(self.Knight.hp), False, self.BLACK)

        self.run()

    def run(self):
        playing = True
        while playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False

            self.screen.blit(self.bg, (self.i,0))
            self.screen.blit(self.bg,(self.WIDTH+self.i,0))


            self.hits = pg.sprite.spritecollide(self.Black_Knight, self.knight_group, True)

            if len(self.knight_group) < 1:
                self.Black_Knight = Boss()

            self.all_sprites.update()

            self.all_sprites.draw(self.screen)

            pg.display.update()

g= Game()
