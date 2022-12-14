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

        self.tekst_font = pg.font.SysFont("gabriola", 100)
        self.FPS = 120
        self.clock = pg.time.Clock()

        self.new()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.knight_group = pg.sprite.Group()
        self.sword_group = pg.sprite.Group()
        self.guard_group = pg.sprite.Group()

        self.knight = Player(self)
        self.king = Boss(self)
    

        self.i = 0
        self.start_over = False

        self.last_collision = 0
        self.spawn_1 = True
        self.spawn_2 = True
        self.spawn_3 = True
        self.spawn_4 = True


        self.tekst_hp = self.tekst_font.render("HP: " + str(self.knight.hp), False, self.WHITE)
        self.tekst_boss_hp = self.tekst_font.render("King HP: " + str(self.king.hp), False, self.WHITE)
        
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
            self.screen.blit(self.tekst_boss_hp, (730, 10))



            self.all_sprites.update()

            self.tekst_boss_hp = self.tekst_font.render("King HP: " + str(self.king.hp), False, self.WHITE)

            self.hits = pg.sprite.spritecollide(self.knight, self.enemy_group, False)
            if self.hits:
                if self.last_collision < self.now - 1500: #millisekunder
                    self.knight.immune = False
                
                if not self.knight.immune:
                    self.knight.hp-=200
                    self.knight.immune = True
                    self.last_collision = self.now
                    self.tekst_hp = self.tekst_font.render("HP: " + str(self.knight.hp), False, self.WHITE)
                    if self.knight.hp <=0:
                        self.knight.kill()
                        self.start_over = True
                        playing = False

        
            if self.king.hp == 8000 and self.spawn_1 == True:
                self.black_knight = Guard(self, 1162, 175)
                self.spawn_1 = False

            if self.king.hp == 6000 and self.spawn_2 == True:
                self.black_knight = Guard(self, 1162, 175)
                self.black_knight = Guard(self, 54, 1158)
                self.spawn_2 = False

            if self.king.hp == 4000 and self.spawn_3 == True:
                self.black_knight = Guard(self, 1162, 175)
                self.black_knight = Guard(self, 54, 1158)
                self.black_knight = Guard(self, 54, 175)
                self.spawn_3 = False

            if self.king.hp == 2000 and self.spawn_1700 == True:
                self.black_knight = Guard(self, 1162, 175)
                self.black_knight = Guard(self, 54, 1158)
                self.black_knight = Guard(self, 54, 175)
                self.black_knight = Guard(self, 1162, 1158)
                self.spawn_4 = False

            self.all_sprites.draw(self.screen)
            pg.display.update()

        if self.start_over:
            self.game_over_loop()

    def game_over_loop(self):

        self.game_over=True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text=self.tekst_font.render("GAME                   OVER", False, (self.RED))
            self.game_restart_text=self.tekst_font.render("Press \"Ctrl R\" to restart", False, (self.WHITE))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False

                if event.type == pg.KEYDOWN: 
                   if event.key == pg.K_r and pg.key.get_mods() & pg.KMOD_LCTRL:
                        self.game_over = False

            self.screen.blit(self.game_over_text, (self.WIDTH/2 - self.game_over_text.get_width()/2, 400))
            self.screen.blit(self.game_restart_text, (self.WIDTH/2 - self.game_restart_text.get_width()/2, self.HEIGHT/2))
            pg.display.update()

        self.new()

g = Game()