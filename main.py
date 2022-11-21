import pygame as pg
from sprites import *

pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (77,168,25)
MINT = (150,200,175)
PURPLE = (175,150,225)
WIDTH = 1216
HEIGHT = 1238

all_sprites = pg.sprite.Group()
boss_group = pg.sprite.Group()
knight_group = pg.sprite.Group()

Knight = Player()
Black_Knight = Boss()
all_sprites.add(Knight, Black_Knight)
boss_group.add(Black_Knight)
knight_group.add(Knight)


screen = pg.display.set_mode((WIDTH,HEIGHT))
bg=pg.image.load("floor 1.png").convert_alpha()

bg=pg.transform.scale(bg, (WIDTH, HEIGHT))


FPS = 120
clock = pg.time.Clock()

i=0

playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    screen.blit(bg, (i,0))
    screen.blit(bg,(WIDTH+i,0))


    hits = pg.sprite.spritecollide(Black_Knight, knight_group, True)

    if len(knight_group) < 1:
        Black_Knight = Boss()

    all_sprites.update()

    all_sprites.draw(screen)

    pg.display.update()